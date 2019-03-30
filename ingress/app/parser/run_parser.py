import time
import sys
sys.path.insert(0, '..')

from db import DB
from csv_to_sql import CSVtoSQL

class RunParser():

  def __init__(self):

    self.db = DB()

    print("Pulling from database queue")
    while True:

      try:
        csv_record = self.db.get_next_record()

        if csv_record:
          CSVtoSQL(csv_record)
        else:
          print("Nothing found, waiting...")
          time.sleep(5)

      except Exception as e:
        print("Caught exception:", e)

RunParser()
