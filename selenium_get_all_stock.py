from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv

stock_url = "https://stockanalysis.com/stocks/"
DRIVER_PATH = "/Users/macbookair/Desktop/FinancialDashbaordLessons/chromedriver"

options = Options()
options.headless = False 

#OPen our web browser
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#go to webpage
driver.get(stock_url)

stock_ticker = dri

time.sleep(1000)

#Quit browser
driver.quit()