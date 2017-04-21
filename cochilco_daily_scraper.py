import re
import scrapy

from manager import *

class CochilcoSpider(scrapy.Spider):
	start_urls = ["https://boletin.cochilco.cl/"]
	name       = 'cochilcospider'

	def parse(self, response):
		regex   = "\d+,\d+"
		pattern = re.compile(regex)

		cells       = response.xpath('////div[@class="Table"]/div[@class="Row"]/div[@class="Cell"]/h3')
		copper_cell = cells[1].extract()

		parsed_amount = re.findall(pattern, copper_cell)[0]
		parsed_amount = parsed_amount.replace(',', '.')
		parsed_amount = float(parsed_amount)

		# manager = Manager(None, None)
		# manager.insert_copper_record(parsed_amount)