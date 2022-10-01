# AutoSeekOut
A simple, cross-platform web scraping *tool/bot* to scrape data from [Seekout](https://seekout.com/).
Purely written in **Python** and **Selenium**. It will generate generate a CSV file 
with all data scraped from *Seekout*. 

## Tested On
#### Linux
1. Debian
  * Parrot OS Release 5.1 (Electro Ara) 64-bit



## Installation
#### Browser Driver
No matter which operating system you are using, you need to download the web driver for your prefered browser for Selenium to control your browser. Here's a list of web drivers you can download based on your operating system. 

**[Note]: Always make sure you are downloading the driver based on the version of your browser**
* [Chrome](https://chromedriver.chromium.org/downloads)
* [Firefox](https://github.com/mozilla/geckodriver)
* [Safari](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari)

#### Creating a Virtual Environment
It's always a good idea to run code in a virtual environment. In order to create a python environment install the following package -
* For Python 3.7 or above
  * pip3 install virtualenv

Now to create an environment using virtualenv 
* python3 -m venv <name of your environment> 
or,
* python -m venv <name of your environment>

###### To activate the environment:
* Linux/MacOS
  - source path/<name of your environment>/bin/activate
* Windows
  - path\to\your\env\Scripts\activate
To deactivate the environment, simply type deactivate