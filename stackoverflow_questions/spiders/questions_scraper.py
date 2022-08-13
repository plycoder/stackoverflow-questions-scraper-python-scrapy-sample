import scrapy


class QuestionsScraperSpider(scrapy.Spider):
    name = 'questions_scraper'
    start_urls = ['https://stackoverflow.com/questions']
    host_url = 'https://stackoverflow.com'

    def parse(self, response):
        SET_SELECTOR = '#questions .s-post-summary'
        for stackoverflow_item in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.s-post-summary--content-title a::text'
            URL_SELECTOR = '.s-post-summary--content-title a::attr(href)'
            
            yield {
                'name': stackoverflow_item.css(NAME_SELECTOR).extract_first(),
                'url': self.host_url+stackoverflow_item.css(URL_SELECTOR).extract_first(),
                }
          
        # follow next page links
        NEXT_PAGE_SELECTOR = '#mainbar > div.s-pagination.site1.themed.pager.float-left .s-pagination--item.js-pagination-item::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract()
        next_page_url=self.host_url+next_page[len(next_page)-1]
        if next_page:
            yield scrapy.Request(
                url = next_page_url
            )
        else:
            print()
            print('No Page Left')
            print()  
