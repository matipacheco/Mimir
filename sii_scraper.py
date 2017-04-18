import re
import numpy
import scrapy

from manager  import *
from inserter import *
from datetime import date

class SiiSpider(scrapy.Spider):
	start_urls = []
	name       = 'siispider'
	year       = date.today().year

	start_urls.append("http://www.sii.cl/pagina/valores/dolar/dolar" + str(year) +".htm")

	def parse(self, response):
		matrix = numpy.array([])

		td_regex   = "<td(.*)>(.+?)</td>"
		td_pattern = re.compile(td_regex)

		rows = response.xpath('///table[@class="tabla"]/tbody/tr')

		for row in rows:
			amounts = row.xpath('./td').extract()

			for amount in amounts:
				parsed_amount = re.findall(td_pattern, amount)

				try:
					if not parsed_amount:
						parsed_amount = 0
				
					else:
						data, parsed_amount = parsed_amount[0]
						parsed_amount       = str(parsed_amount)
						parsed_amount       = float(parsed_amount.replace(',', '.'))

				except UnicodeEncodeError:
					parsed_amount = 0

				finally:
					matrix = numpy.append(matrix, parsed_amount)

		matrix = matrix[:-12]
		matrix = numpy.reshape(matrix,(31, 12))
		matrix = numpy.transpose(matrix)

		manager = Manager(matrix, self.year)
		manager.insert()