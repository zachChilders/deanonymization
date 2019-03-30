import time
import datetime
from db import DB

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CSVFinder(object):
  
  def __init__(self):
    self.chrome_options = webdriver.ChromeOptions()
    self.chrome_options.add_argument('--headless')
    self.chrome_options.add_argument('--no-sandbox')
    self.chrome_options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Chrome(options=self.chrome_options)
    self.db = DB()

    self.term = ''
    self.base_url = 'https://catalog.data.gov/dataset?q={}'.format(self.term)

    self.driver.get(self.base_url)
    
    time.sleep(1)
    
    self.find_csv_urls()

    next_page = self.has_next_page()
    while next_page:
      next_page.click()
      time.sleep(2)
      self.find_csv_urls()
      next_page = self.has_next_page()


  def has_next_page(self):
    pag = self.find('.pagination.pagination-centered')
    lis = self.findList('li', pag)
    
    next_li = None
    for idx, li in enumerate(lis):
      if 'active' == li.get_attribute('class'):
        next_li = self.find('a', lis[idx+1])
        break

    print("Next found:", next_li)
    return next_li


  def find_csv_urls(self):
    results = self.findList(".label[data-format='csv']")

    for idx, result in enumerate(results):
      url = result.get_attribute('href')
      if self.is_new_url(url) == True:
        self.add_csv_url(url)


  def is_new_url(self, url):
    result = self.db.execute_sql("""select id from tables_index where csv_url = %s""", [url])
    print("URL Lookup:", result, url)
    if len(result) > 0:
      return False
    else:
      return True


  def add_csv_url(self, url):
    print("Adding url to tables_index\n")
    sql = """insert into tables_index (csv_url, state, inserted_at) values ('{}', 0, '{}')""".format(url, datetime.datetime.now())
    self.db.execute_sql(sql)


  def getAction(self):
    return ActionChains(self.driver)


  def find(self, selector, ele=None):
    if ele:
      return ele.find_element_by_css_selector(selector)
    else:
      return self.driver.find_element_by_css_selector(selector)


  def findList(self, selector, ele=None):
    if ele:
      return ele.find_elements_by_css_selector(selector)
    else:
      return self.driver.find_elements_by_css_selector(selector) 