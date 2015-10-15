__author__ = 'sanjiv'

"""
An email crawler written to crawl Jana (http://www.jana.com) website. This program uses selenium library to crawl and
capture email ids. This crawler is required for those websites that uses external javascript call to load HTML content.
BeautifulSoup is used to parse html pages that have static content and does not depend on external javascript content
to load the contents. Hence this crawler does not uses BS.

How to run from command line:
python email_crawler.py http://jana.com

format of the URL : http://www.abc.com or http://abc.com (Do not give URL in quotes)


Output: List of email ids, printed one by one on screen

Limitation :  --> Google chrome needs to be present for this crawler to run as selenium uses Chrome driver.
              --> Provide the path of chrome driver(chromedriver.exe). Similar driver comes for other browser as well.
"""

from contextlib import closing
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
import re
import sys

# Function to open the given website, wait for the dynamic content to load and then collect all elements by 'body' tag.
# It then parses the html page and returns the fully loaded html page.


def jana_page_source(url):
    with closing(Chrome('C:\Users\sanjiv\Anaconda\Practice ML with Data\chromedriver.exe')) as browser:
        browser.get(url)
        element = browser.find_element_by_tag_name('body')
        WebDriverWait(browser, timeout=10).until(
             lambda x: x.find_element_by_tag_name('body'))
        page_source = browser.page_source
    return page_source


# main crawler function that crawls the Jana website and returns the email list


def email_crawler_jana_specific(url):
    pat_url = '<span ng-click="changeRoute\W+\w+\W+'
    email_pattern = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-z]+'
    emails_list = set()
    page_source = jana_page_source(url)
    url_handles = re.findall(pat_url, page_source, re.I)
    for each in url_handles[1:]:
        suffix_url = each.split("'")[1]
        complete_url = 'http://www.jana.com/' + suffix_url
        page_source = jana_page_source(complete_url).encode('utf-8')
        # capturing emails in text form from HTML pages
        email_in_text_form = re.findall(email_pattern, page_source, re.I)
        # Updating the emails list and removing the unicode value
        emails_list.update(email_in_text_form)
    print "Printing each of the collected email ids......" + "\n"
    return emails_list


print "Crawling", sys.argv[1], "and collecting all the email id's........" + "\n"
emails_set = email_crawler_jana_specific(sys.argv[1])
for each in emails_set:
    print "Email Id: ", each