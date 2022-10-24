from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.config import *

class ProcessMarketDemo:

  def __init__(self):

    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get('https://www.saucedemo.com/')

  def add_item_cart(self):
    # Add to cart
    buttons = self.driver.find_elements(By.TAG_NAME, 'button')
    buttons = [button for button in buttons if button.text == 'ADD TO CART']

    for btn in buttons:
      sleep(1)
      btn.click()
    

  def auth(self):
    for position in data_secret:
      field = self.driver.find_element(By.ID, position)
      field.send_keys(data_secret[position])
      sleep(1)
      button = self.driver.find_element(By.ID, "login-button")
      button.submit()
  
  def process_market(self, process):
    if process == 'shopping_cart_container':
        self.driver.find_element(By.ID, process).click()
        sleep(1)
    elif process == 'continue':
      for field in data:
        field_dt = self.driver.find_element(By.ID, field)
        field_dt.send_keys(data[field])
        sleep(1)
      btnContinue = self.driver.find_element(By.ID, process)
      btnContinue.click()
    elif process == 'finish':
      self.driver.find_element(By.ID, process).click()
      sleep(1)
    else:
      self.driver.find_element(By.ID, process).click()
      sleep(1)
    

  def handle(self):
    for process in processes_market:
      self.process_market(process)
