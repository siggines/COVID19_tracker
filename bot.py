from selenium import webdriver
from time import sleep
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class Cidrap():
    def __init__(self,stdout = None,stderr = None):
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        self.driver = webdriver.Chrome(options=op)

    def grab(self):
        self.driver.get('http://www.cidrap.umn.edu/')
        title = self.driver.find_element_by_xpath('//*[@id="node-183161"]/div/div/div[2]/div/h3').get_attribute('textContent')
        print(title)
        paragraph = self.driver.find_element_by_xpath('//*[@id="node-183161"]/div/div/div[2]/div/div[2]/div/div').get_attribute('textContent')
        print(paragraph)

bot = Cidrap()
bot.grab()
