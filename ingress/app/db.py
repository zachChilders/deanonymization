import os
import datetime
import requests 
import csv
import psycopg2

class DB(object):

  def __init__(self):
    self.connstr = os.environ.get('ingressconnectionstring', None)


  def get_connection(self):
    if self.connstr:
      return psycopg2.connect(self.connstr)
    else:
      return psycopg2.connect(
          dbname='ingress',
          user='cameron',
          password=''
      )


  def insert_rows(self, file_object, table_name):

    conn = None
    copy_statement = """
        COPY %s FROM STDIN WITH
            CSV
            HEADER
            DELIMITER AS ','
        """

    try:
        conn = self.get_connection()
        cur = conn.cursor()

        print("Copying data into", table_name)
        cur.copy_expert(sql=copy_statement % table_name, file=file_object)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


  def execute_sql(self, sql, params=None):
    # print("Executing sql:", sql)
    try:
      conn = self.get_connection()
      cur = conn.cursor()
      sql_args = list(filter(lambda v: v is not None, [sql, params]))
      # print("SQL_ARGS:", sql_args)
      cur.execute(*sql_args)
      conn.commit()
      rows = []
      if cur.description != None:
        rows = cur.fetchall()
      cur.close()
      return rows
    except (Exception, psycopg2.DatabaseError) as error:
      if str(error) != 'no results to fetch':
        print("SQL Error >>", error)
      raise Exception('SQL error {}'.format(error)) 
    finally:
      if conn and conn is not None:
          conn.close()


  def create_table(self, csv_record, columns):
    table_name = '_' + str(datetime.datetime.now())
    
    table_name = table_name.replace('-', '_') \
                            .replace(' ', '_at_') \
                            .replace(':', '_') \
                            .replace('.', '_')

    print("Creating table:", table_name)
    sql = 'create table if not exists ' + table_name + " (" + " VARCHAR(400),".join(columns) + " VARCHAR(400))"
    rows = self.execute_sql(sql)

    return table_name


  def check_url(self, url):
    result = self.execute_sql("""select id from tables_index where csv_url = %s""", [url])
    print("URL Lookup:", result, url)
    if len(result) > 0:
      return False
    else:
      return True


  def get_next_record(self):
    sql = '''
      update tables_index
      set 
        state = 1, parsed_at = '{}'
      where 
        id = (
          select id from tables_index
          where state = 0 
          order by inserted_at asc
          limit 1
        )
      returning id, csv_url, parse_attempts
    '''.format(datetime.datetime.now())

    resp = self.execute_sql(sql)
    if resp:
      return dict( zip(('id', 'csv_url', 'parse_attempts'), resp.pop()))
    else:
      return False


  def parse_failed(self, record):
    print("Parsing failed for:", record)
    sql = '''
      update tables_index
      set 
        state = 3, failed_at = '{}', parse_attempts = {}
      where 
        id = {}
    '''.format(datetime.datetime.now(), record['parse_attempts'] + 1, record['id'])

    self.execute_sql(sql)


  def parse_succeeded(self, record):
    print("Parsing succeeded for:", record)
    sql = '''
      update tables_index
      set 
        state = 2, succeeded_at = '{}', parse_attempts = {}
      where 
        id = {}
    '''.format(datetime.datetime.now(), record['parse_attempts'] + 1, record['id'])

    self.execute_sql(sql)


  def set_table_name(self, record, table_name):
    sql = '''
      update tables_index
      set 
        table_name = '{}'
      where 
        id = {}
    '''.format(table_name, record['id'])

    self.execute_sql(sql)
