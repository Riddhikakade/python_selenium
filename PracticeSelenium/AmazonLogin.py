from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

webdriver = webdriver.Chrome("C://browserdrivers//chromedriver.exe")
webdriver.get("https://www.amazon.com/")
webdriver.maximize_window()

#for username
login =webdriver.find_element_by_xpath("//a[@class='nav-a nav-a-2   nav-progressive-attribute']").click()
username = webdriver.find_element_by_xpath("//input[@name='email']")
username.click()
username.send_keys("kakaderiddhi2015@gmail.com")

#for continue btn
btn = webdriver.find_element_by_xpath("//input[@type='submit']")
btn.click()

#for password
password = webdriver.find_element_by_xpath("//input[@type='password']")
password.click()
password.send_keys("Riddhi@123")

#for signin button
signin =webdriver.find_element_by_id("signInSubmit")
signin.click()

#for dropdown
select =webdriver.find_element_by_xpath("//select[@aria-describedby='searchDropdownDescription']")
select.click()
drp=Select(select)
time.sleep(3)

#for value selection
drp.select_by_visible_text('Books')

#for search the product
searchBar =webdriver.find_element_by_xpath("//input[@type='text']")
searchBar.send_keys('firebird')
searchBar.submit()

product =webdriver.find_element_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
product.click()

#for product quantity
#quantity = webdriver.find_element_by_xpath("//span[@data-action='a-dropdown-button']")
webdriver.find_element_by_xpath("(//span[@class='a-dropdown-label'])").click()
time.sleep(2)
select = webdriver.find_element_by_xpath("(//a[@href='javascript:void(0)'])[33]")
select.click()

#add to cart
addcart =webdriver.find_element_by_id("add-to-cart-button")
addcart.click()

#searchBar= webdriver.find_element_by_id("twotabsearchtextbox")
#searchBar.click()
time.sleep(3)
webdriver.close()