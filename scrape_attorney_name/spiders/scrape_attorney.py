import scrapy, json
# from ..items import ScrapeAttorneyNameItem

class ScrapeAttorneySpider(scrapy.Spider):
    name = 'scrape_attorney'

    page_no = 2
    start_urls = ['https://www.martindale.com/search/attorneys/?term=%2A'
    ]



    def parse(self, response):
        # response.meta.get("type")
        attorney_name = response.css('.detail_title a').css('::text').extract()
        
        yield {
            "name": attorney_name
            }
        # yield {
        #     "name": attorney_name[0]
        # }
        


        url = "https://www.martindale.com/search/attorneys/?term=%2A&page={page_no}".format(page_no = ScrapeAttorneySpider.page_no)
        if ScrapeAttorneySpider.page_no <= 20:
            ScrapeAttorneySpider.page_no += 1
            yield response.follow(url, callback = self.parse)



            # yield scrapy.Request(
            # callback=self.parse,
            # meta={'page': url}
            # meta={"type": "list/attorney"}
            # )
            

                # url="https://www.kaercher.com/api/v1/products/search/shoppableproducts/partial/20035386?page={page}&size=8&isocode=nl-NL".format(page=next_page),



                # item["attorney_name"] = attorney_name
                # item["attorney_location"] = attorney_location





            # attorney_name = response.css('.detail_title a').css('::text').extract()
            # attorney_location = response.css('.detail_location').css('::text').extract()

        
            # attorney_name = attorney_name
            # location = attorney_location
                # yield item

           

        # next_page = response.css("li a.arrow::attr(href)").get()


        # '.next a ::attr(href)