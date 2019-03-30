import csv
import os

import requests

from db import DB


class CSVtoSQL():

  def __init__(self, csv_record):

    self.db = DB()

    try:
      self.parse_csv(csv_record)
      self.db.parse_succeeded(csv_record)
    except Exception as e:
      print("Parsing failed:", e)
      self.db.parse_failed(csv_record)


  def parse_csv(self, csv_record):
    print("\nSearching for", csv_record['csv_url'], "to download...")
    with requests.Session() as s:

      resp = s.get(csv_record['csv_url'], stream=True)

      with open('out.csv', 'w') as f:
        writer = csv.writer(f)
        reader = csv.reader(resp.text.splitlines())

        for idx, row in enumerate(reader):
          # Skip column names
          if idx == 0:
            for column_name in row:
              try:
                int(column_name)
                print("Found a integer in a column name, scrapping data")
                return False
              except ValueError:
                continue

            columns = list(map(lambda x: x.lower().replace(' ', '_').replace('-', '_').replace('(', '_').replace(')', '_'), row))
            continue

          writer.writerow(row)

      table_name = self.db.create_table(csv_record, columns)
      self.db.set_table_name(csv_record, table_name)

      with open('out.csv', 'r') as f:
        self.db.insert_rows(f, table_name)

      os.remove('out.csv')
