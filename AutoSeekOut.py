#!/usr/bin/python3
try:
	from selenium import webdriver
	from selenium.webdriver.firefox.service import Service
	from selenium.webdriver.common.by import By
	from selenium.webdriver.common.keys import Keys
	import time
	import pandas as pd
	from os import path
except ModuleNotFoundError as e:
	print(e)

""" Necessary Global Variables """
# Driver Path
DPATH:str = "geckodriver.exe"

# Change URL
URL:str = "https://app.seekout.io/project/cf3ec799-9f29-4069-a29c-6d034b69fe59"

# Page Number parameter for the URL
PAGENUMSTR:str = "?page="

# PageSize -> Data per page; sortBy -> oldest to newest
CTRLSTR:str = "&pageSize=100&sortBy=oldest"

# Seekout LOGIN CREDS
EMAIL:str = "example@mail.com"
PASSWD:str = "password123"

# Change the Starting Page Number
STARTFROM:int = 140

# Change the limit of the Page Iteration. It should be the last page number of the project.
LIMIT:int = 142

# Change Title of the project
TITLE = "Intuit"

# Change File Name. The script will save the data in one CSV. It has to be cleaned and divided.
FILE = "Intuit.csv"

#Main Class
class Scrape:
	#Private Attributes
	__path = None
	__email = None
	__password = None
	__scripts = None
	PAGE = None

	def __init__(self):
		self.__path = DPATH
		self.__email = EMAIL
		self.__password = PASSWD
		self.__scripts = {
			'height':'return document.documentElement.scrollHeight;',
			'scroup':"window.scrollTo(0,0);"
		}
		self.PAGE = STARTFROM # Change here

	def getCreds(self) -> dict:
		return {
			'dvrpath': self.__path,
			'email': self.__email,
			'passwd': self.__password
			}
	
	def __init(self) -> "driver object":
		try:
			driver = Service(self.__path)
			firefox = webdriver.Firefox(service=driver)
			return firefox
		except Exception as err:
			print(err.message)

	def __login(self): #Private Method
		try:
			handler = self.__init()
			handler.get(URL)
			handler.maximize_window()
			time.sleep(15)
			#Selecting and filling the username and password fields
			handler.find_element(By.NAME, "username").send_keys(self.__email)
			handler.find_element(By.NAME,"password").send_keys(self.__password)
			time.sleep(5) #Halt for completing captcha
			#Selecting and clicking the login button
			handler.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[1]/div/form/button").click()
			return handler
		except Exception as err:
			print(err.message)

	def __getDetails(self,name,role,company,location,linkedin):
		print(f"{self.PAGE}")
		print(f"{name}")
		print(f"{role}")
		print(f"{company}")
		print(f"{location}")
		print(f"{linkedin}")
		print("=" * 70)

	#def __scroll(self,handler,height):

	def __writecsv(self,data:list) -> bool:
		try:
			issaved = False
			if path.exists(FILE):
				df = pd.read_csv(FILE, names=['name','linkedin','role','company','location'])
			else:
				df = pd.DataFrame(columns=['name','linkedin','role','company','location'])
			
			if data[1] not in df['linkedin'].values:
				df.loc[-1] = data
				df.index = df.index + 1
				issaved = True
			
			df.to_csv(FILE,mode="w")
			return issaved

		except Exception as error:
			print(error)


	def Scrape(self):
		try:
			handler = self.__login()
			time.sleep(15)
			while(self.PAGE <= LIMIT):
				url = f"{URL}{PAGENUMSTR}{str(self.PAGE)}{CTRLSTR}"
				handler.get(url)
				time.sleep(15)
				if (TITLE in handler.title): # Change here
					#Smooth Scrolling
					height = int(handler.execute_script(self.__scripts['height'])) * 2
					for i in range(1,height,100):
						start = 0
						handler.execute_script(f"window.scrollTo({start},{i});")
						start = i

					time.sleep(2)
					candidates = handler.find_elements(By.CLASS_NAME,"-iui3H")
					total = len(candidates)
					added = 0
					for idx in range(len(candidates)):
						name = candidates[idx].find_element(By.CLASS_NAME,"-wzpkV").text
						rolecomp = candidates[idx].find_element(By.CLASS_NAME,"-ezKRP").text
						lst = rolecomp.split(' at ')
						role = lst[0]
						company = lst[len(lst) - 1]
						locationstr = candidates[idx].find_element(By.CLASS_NAME,"-PhaLH").text
						location = locationstr.split('\n')[0]
						linkedin = candidates[idx].find_element(By.CLASS_NAME,"-v1sSJ").get_attribute('href')
						#print(repr(rolecomp)) #prints raw str
						self.__getDetails(name,linkedin,role,company,location)
						added = added + 1 if (self.__writecsv([name,linkedin,role,company,location]) == True) else added + 0

					print(f"Total Candidates: {total}")
					print(f"Added: {added}")
					self.PAGE += 1
					print("-x-" * 70)
			handler.close()
		except Exception as err:
			print(err.message)
		
if __name__ == "__main__":
	bot = Scrape()
	bot.Scrape()
