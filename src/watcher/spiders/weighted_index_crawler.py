import scrapy

class WeightedIndexCrawler(scrapy.Spider):
  # TAIEX index
  name = "taiex"
  
  start_urls = [
    'https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=20220927&_=1664284275215',
  ]
  
  def __start_requests(self):
    urls = [
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)
  
  def parse(self, response, **kwargs):
    page = response.url.split("/")[4].split(".")[0]
    filename = f'{page}.html'
    with open(filename, 'wb') as f:
      f.write(response.body)
    self.log(f'Saved file {filename}')
