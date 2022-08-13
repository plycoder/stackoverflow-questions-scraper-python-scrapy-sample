# stackoverflow-questions-scraper-python-scrapy-sample
Stackoverflow questions sample using Python and Scrapy framework


## Usage

### Start using it

1. To run spider run following command from project root directory using terminal:
```sh
scrapy crawl questions_scraper -o questions.json
```
Above command will write stackoverflow question name & url on questions.json. 

#### The questions scraper scripts should work untill no changes in Stackoverflow dom element