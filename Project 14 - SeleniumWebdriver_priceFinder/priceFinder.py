from selenium import webdriver
from selenium.webdriver.common.by import By
import fake_useragent

user_agent = fake_useragent.UserAgent()
my_agent = user_agent.random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f'--user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# Fetching the price from amazon.com
product_name = driver.find_element(By.ID, value="productTitle")
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# Printing the fetched product name and price
print("Product: "+str(product_name.text))
print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.ID, value="twotabsearchtextbox")
print(search_bar.get_attribute("placeholder"))


driver.quit()
# driver.close()

