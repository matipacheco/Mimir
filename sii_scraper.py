import re
import numpy
import scrapy

class BDInserter:
	def __init__(self, matrix):
		self.matrix = matrix
		

class SiiSpider(scrapy.Spider):
	name 				= 'siispider'
	years 			= range(1990,2018)
	start_urls 	= ["http://www.sii.cl/pagina/valores/dolar/dolar1990.htm"]

	# for year in years:
	# 	start_urls.append("http://www.sii.cl/pagina/valores/dolar/dolar" + str(year) +".htm")

	def parse(self, response):
		matrix = numpy.array([])

		regex 	= "<td>(.+?)</td>"
		pattern = re.compile(regex)

		rows = response.xpath('///table[@class="tabla"]/tbody/tr')
		
		for row in rows:
			amounts = row.xpath('./td').extract()

			for amount in amounts:
				parsed_amount = re.findall(pattern, amount)

				if not parsed_amount:
					matrix = numpy.append(matrix, 0)
				else:
					parsed_amount = str(parsed_amount[0])
					parsed_amount = float(parsed_amount.replace(',', '.'))
					matrix 				= numpy.append(matrix, parsed_amount)

		matrix = matrix[:-12]
		matrix = numpy.reshape(matrix,(31, 12))
		matrix = numpy.transpose(matrix)
		
		inserter = BDInserter(matrix)
		# inserter.insert_on_bd()