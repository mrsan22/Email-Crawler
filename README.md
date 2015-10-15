Jana coding-challenge:

Create a command line program that will take an internet domain name (i.e. “jana.com”) and print out a list of the email addresses that were found on that website.

For this exercise , I am submitting 2 python programs:

1) email_crawler.py ||
2) email_crawler_jana.py 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
*******************
1) email_crawler.py
*******************
This python program is a normal email crawler that finds all the email ids from a given website. 

How to run from command line:
python email_crawler.py <URL>

format of the <URL> : http://www.abc.com or http://abc.com (Do not give URL in quotes)
Sample websites : http://www.cens.io

Output: List of email ids, printed one by one on screen

I have Anaconda environement that comes preloaded with all the required libraries.

Libraries required:
from bs4 import BeautifulSoup --> easy_install BeautifulSoup4 ||
from collections import deque --> Inbuilt ||
import re --> Inbuilt ||
import sys --> Inbuilt ||
from urlparse import urlparse --> Inbuilt ||
from urlparse import urljoin --> Inbuilt ||
import urllib2 --> Inbuilt ||

Output:
C:\Users\sanjiv\Google Drive\Workspace\PycharmProjects\Coop\Jana>python email_crawler.py http://cens.io
Crawling the input website and collecting all the email id's........

Printing each of the collected email ids......

Email Id:  jwilliams@scovillepr.com

*****
NOTE:
*****
This email crawler works very well for most of the websites. However some website (http://jana.com) are built with AngularJS and loads content of the website dynamically. This means
that when you hit http://jana.com or any other of it's webpage it's entire content(complete html page with all tags) are not loaded immediately. And hence library such as BeautifulSoup,
that is made to parse the content from static web pages fails to extract content from Jana website. As seen below, there are no 'href' from the webpages, they are ng-click. Also,
class='view-frame' has no element loaded when we parse the page, as seen below class="view-frame" is empty. The content of these tags are loaded dynamically by javascript call.


                <li><span ng-click="changeRoute('home')">Home</span></li>
                <li><span ng-click="changeRoute('product')">Product</span></li>
                <li><span ng-click="changeRoute('about')">About</span></li>
                <li><span ng-click="changeRoute('careers')">Careers</span></li>
                <li><span ng-click="changeRoute('contact')">Contact</span></li>
				
				<div ui-view class="view-frame"></div>
				

So to capture email id's from such websites like http://www.jana.com I made a separate web crawler that uses selenium library to capture the tags. 
*************************
2) email_crawler_jana.py
*************************
This crawler is made specifically for Jana website. As of now, it only runs and collect email ids that are present on the Jana websites. This crawler simulates UI behaviour using 
selenium and hence is able to get all the tags once all the javascript calls has been made and page is loaded completely.

How to run from command line:
python email_crawler.py http://jana.com

format of the URL : http://www.abc.com or http://abc.com (Do not give URL in quotes)


Output: List of email ids, printed one by one on screen

Limitation :  Google chrome needs to be present for this crawler to run as selenium uses Chrome driver.
              Provide the path of chrome driver(chromedriver.exe). Similar driver comes for other browser as well.
			  
Libraries required:
from contextlib import closing ||
from selenium.webdriver import Chrome --> pip install selenium ---> http://selenium-python.readthedocs.org/ ||
from selenium.webdriver.support.ui import WebDriverWait ||
import re ||
import sys ||

Also this crawler assumes that you have Google Chrome browser. You also need to set path for the chromedriver in the program.
Example : 'C:\Users\sanjiv\Anaconda\Practice ML with Data\chromedriver.exe'

Output:
C:\Users\sanjiv\Google Drive\Workspace\PycharmProjects\Coop\Jana>python email_crawler_jana.py http://jana.com
Crawling http://jana.com and collecting all the email id's........

Printing each of the collected email ids......

Email Id:  press@jana.com
Email Id:  info@jana.com
Email Id:  sales@jana.com
