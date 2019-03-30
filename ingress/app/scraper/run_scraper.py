import time, sys
sys.path.insert(0, '..')

from scrape import CSVFinder

class RunScraper(object):

	def __init__(self):
		self.scraper = CSVFinder()
			
RunScraper()
