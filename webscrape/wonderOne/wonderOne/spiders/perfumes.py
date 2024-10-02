import scrapy


class PerfumesSpider(scrapy.Spider):
    name = "perfumes"
    allowed_domains = ["www.essenza.ng"]
    start_urls = ["https://www.essenza.ng/collections/all-fragrance"]

    def parse(self, response):
        for products in response.css('div.product-item.product-item--vertical'):
            yield{
                'name' : products.css('a.product-item__title.text--strong.link::text').get(),
                'link' : products.css('a.product-item__title.text--strong.link').attrib['href'],
                'price' : products.css('span.money::text').get().replace('₦',' '),
            }

        next_page = response.css('a.pagination__next.link').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
