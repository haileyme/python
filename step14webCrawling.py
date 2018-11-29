# Crawling at Aladin, the online bookstore website

import requests
import lxml.html
import re
import time


def main():
    session = requests.Session()
    response = session.get("https://www.aladin.co.kr/shop/common/wnew.aspx?ViewRowsCount=50&ViewType=Detail&SortOrder=3&page=1&BranchType=1&PublishDay=84")
    urls = scrape_list_page(response)
    
    for url in urls:
        # print(url)
        time.sleep(1)
        response=session.get(url)
        bookInfo=scrape_detail_page(response)
        print(bookInfo)

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.ss_book_list a.bo3'):
        url = a.get('href')
        yield url

def scrape_detail_page(response):
    root = lxml.html.fromstring(response.content)
    bookInfo = {
        'title' : root.cssselect('.pwrap_bgtit a.p_topt01')[0].text_content(),
        'price' : root.cssselect('.p_goodstd02 span.p_new_price_ph')[0].text_content(),
    }
    return bookInfo

if __name__ == "__main__":
    main()
