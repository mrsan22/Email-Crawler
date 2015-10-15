__author__ = 'sanjiv'

"""
A email crawler written in Python to collect valid email ids from the given website. It takes the input URL as command
line argument and prints out the each of the email ids.

How to run from command line:
python email_crawler.py <URL>

format of the <URL> : http://www.abc.com or http://abc.com (Do not give URL in quotes)
Sample websites : http://www.cens.io

Output: List of email ids, printed one by one on screen
"""

from bs4 import BeautifulSoup
from collections import deque
import re
import sys
from urlparse import urlparse
from urlparse import urljoin
import urllib2


# function to check validity of the URL
def valid_url(domain, url, href):
    return ':' not in href and domain in urljoin(url, href)


# Helper function to check whether url contains '#' symbol and return True/False
def contains_pound(absurl):
    return '#' in absurl


# Main function that enables running of a crawler
def email_crawler(url):
    # Regular expression for detecting email id from a given string
    email_pattern = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-z]+'
    # Double ended queue to form the frontier
    urls_queue = deque([url])
    # A set to store the list of visited urls and avoid duplicate urls
    visted_urls = set()
    # A set to contain all the email ids from a given website
    emails_list = set()
    while len(urls_queue):
        parsed_url = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_url)
        url_to_be_processed = urls_queue.pop()
        html_response = urllib2.urlopen(url_to_be_processed)
        # Beautiful Soup object containing the parsed html page
        parsed_html_page = BeautifulSoup(html_response)
        # Adding into visited urls list
        visted_urls.add(url_to_be_processed)
        # getting text from HTML page with the mentioned tags
        parsed_html_page_with_tags = parsed_html_page.find_all({'a': True, 'p': True})
        # capturing emails in text form from HTML pages
        email_in_text_form = re.findall(email_pattern, str(parsed_html_page_with_tags), re.I)
        # Updating the emails list and removing the unicode value
        emails_list.update(email_in_text_form)
        for link in parsed_html_page.find_all('a', href=True):
            if valid_url(domain, url_to_be_processed, link['href']):
                absolute_url = urljoin(url_to_be_processed, link['href'])
                if contains_pound(absolute_url):
                    absolute_url = absolute_url.split('#')[0]
                if absolute_url not in visted_urls and absolute_url not in urls_queue:
                    urls_queue.appendleft(absolute_url)
    print "Printing each of the collected email ids......" + "\n"
    return emails_list

print "Crawling", sys.argv[1], "and collecting all the email id's........" + "\n"
emails_set = email_crawler(sys.argv[1])
for each in emails_set:
    print "Email Id: ", each