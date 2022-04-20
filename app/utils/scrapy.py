
import scrapy
import json


class ScoreSpider(scrapy.Spider):
    name = 'get_notes'
    data = []

    def start_requests(self):
        urls = ['https://www.bien-dans-ma-ville.fr/classement-ville-global/']
        for i in range(1, 22):
            urls.append(f'https://www.bien-dans-ma-ville.fr/classement-ville-global/?page={i}')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for row in response.xpath('*//tbody/tr'):
            self.data.append({
                'city': row.xpath('td[2]//text()').extract_first().split('(')[0],
                'score': row.xpath('td[3]//text()').extract_first()
            })

        with open('city_score.json', 'w') as f:
            json.dump(self.data, f, ensure_ascii=False)
