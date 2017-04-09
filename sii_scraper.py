import re
import numpy
import scrapy
from mimir import *

class SiiSpider(scrapy.Spider):
	start_urls  = []
	name 				= 'siispider'
	years 			= [range(1990,2018)[0]]

	for year in years:
		start_urls.append("http://www.sii.cl/pagina/valores/dolar/dolar" + str(year) +".htm")

	def parse(self, response):
		matrix = numpy.array([])

		td_regex 	 = "<td>(.+?)</td>"
		td_pattern = re.compile(td_regex)

		url_regex   = "\d+"
		url_pattern = re.compile(url_regex)
		url_year 		= int(re.findall( url_pattern, response.url)[0])
		
		rows = response.xpath('///table[@class="tabla"]/tbody/tr')
		
		for row in rows:
			amounts = row.xpath('./td').extract()

			for amount in amounts:
				parsed_amount = re.findall(td_pattern, amount)

				if not parsed_amount:
					matrix = numpy.append(matrix, 0)
				else:
					parsed_amount = str(parsed_amount[0])
					parsed_amount = float(parsed_amount.replace(',', '.'))
					matrix 				= numpy.append(matrix, parsed_amount)

		matrix = matrix[:-12]
		matrix = numpy.reshape(matrix,(31, 12))
		matrix = numpy.transpose(matrix)

		mimir = Mimir(matrix, url_year)
		mimir.read()