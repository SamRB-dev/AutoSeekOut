# AutoSeekOut
A simple, cross-platform web scraping *tool/bot* to scrape data from [Seekout](https://seekout.com/).
Purely written in **Python** and **Selenium**. It will generate generate a CSV file 
with all data scraped from *Seekout*. 

## Tested On
#### Linux
1. Debian
  * Parrot OS Release 5.1 (Electro Ara) 64-bit

#### Windows
1. Windows 10 Pro
  * Version: 21H2
  * Build: 19044.1889


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

To activate the environment:
* Linux/MacOS
  - source path/<name of your environment>/bin/activate
* Windows
  - path\to\your\env\Scripts\activate
To deactivate the environment, simply type deactivate

#### Installing Necessary Modules
After you have activated your virtual environment, it's time to install the necessary packages.
To install those packages, just type
* pip3 install -r requirements.txt

## Final Steps
Lastly, to get the script up and running, you need to make few changes in the script itself. On my future updates I'll make sure to reduce these steps to make your life easier. But for subsequent time, make these following changes. 

1. Open the scripts in your preferred IDE or text editor.
2. On line 15, DPATH variable, set the path of your browser driver as string. i.e.
  * DPATH = "path/to/browser/drive.exe"
3. On line 27,28 (EMAIL,PASSWD) variables, set your login credetials as string. i.e.
  * EMAIL = "example@mail.com"
  * PASSWD = "password123"
4. On line 31,34 (STARTFROM,LIMIT) variables, set the starting page number(STARTFROM) and last page number (LIMIT) of the project you want the bot to scrape. i.e.
  * STARTFROM = 1
  * LIMIT = 100
5. On line 37 (TITLE) variable, set the title to the title of the project data page so that the bot can identify the project. i.e If the project title is "Projects/Database - Intuit" then you will set the variable as 
  * TITLE = "Intuit"
6. Lastly, on line 40 (FILE) variable, set the file name as your desired file name.

### Run the script in CMD/terminal
```
python3 AutoSeekOut.py
```
OR,
```
python AutoSeekOut.py
```