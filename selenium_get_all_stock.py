from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv

stock_url = "https://stockanalysis.com/stocks/"
DRIVER_PATH = '/Users/macbookair/Desktop/FinancialDashbaordLessons/chromedriver'

opt = Options()
opt.headless = False

#Open our web browser
driver = webdriver.Chrome(options=opt, executable_path=DRIVER_PATH)


#Go to webpage
driver.get(stock_url)

tick_loc = 1
stock_list = list()

while True:
    try:
        stock_ticker = driver.find_element_by_xpath(f"/html/body/div[2]/div/div[2]/main/article/div/div/ul/li[{tick_loc}]/a").get_attribute('innerHTML').split()[0]
        tick_loc = tick_loc + 1
        stock_list.append(stock_ticker)
    except Exception as e:
        print(e)
        break

#Quit browser
driver.quit()


with open('stock_ticker_list.csv', mode='w') as ticker_file:
    ticker_writer = csv.writer(ticker_file)
    for ticker in stock_list:
        print('Saving: ', ticker)
        ticker_writer.writerow([ticker])