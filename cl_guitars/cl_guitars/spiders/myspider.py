import scrapy

class MySpider(scrapy.Spider):
    name = "cl_guitars"
    start_urls = ["https://hudsonvalley.craigslist.org/d/musical-instruments/search/msa"]
    
    def parse(self,response):
        for title in response.xpath("//li[@class = 'result-row']//p"):
            yield {
                'title':title.xpath("a/text()").extract_first()}