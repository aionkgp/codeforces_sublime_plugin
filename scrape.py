import scrapy
from bs4 import BeautifulSoup as bs
from time import sleep

class WordsSpider(scrapy.Spider):
	name = "cf"
	download_delay = 10
	def start_requests(self):
		urls = ['http://codeforces.com/problemset/problem/1060/D']

		for url_item in urls:
			print(url_item)
			yield scrapy.Request(url=url_item, callback = self.parse)

	def parse(self, response):
		file = open("problem.txt","w")
		file.write(response.css('div.problemindexholder').css('div.problem-statement').css("div.title::text").extract()[0])
		file.write('\n')
		file.write(response.css('div.problemindexholder').css('div.problem-statement').css("div.time-limit::text").extract()[0])
		file.write('\n')
		file.write(response.css('div.problemindexholder').css('div.problem-statement').css("div.memory-limit::text").extract()[0])
		file.write('\n')
		file.write(response.css('div.problemindexholder').css('div.problem-statement').css("div.input-file::text").extract()[0])
		file.write('\n')
		file.write(response.css('div.problemindexholder').css('div.problem-statement').css("div.output-file::text").extract()[0])
		file.write('\n')

		PS = response.css('div.problemindexholder').css('div.problem-statement').css("div.input-specification").xpath('//p').extract()
		for sentence in PS:
			file.write(sentence)
			file.write('\n')
		file.close()
