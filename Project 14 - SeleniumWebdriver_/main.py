from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# Bypassing Captcha
captcha = driver.find_element(By.LINK_TEXT, "Try different image")
captcha.click()

# Fetching the price from amazon.com
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.ID, value="twotabsearchtextbox")
print(search_bar.get_attribute("placeholder"))


driver.quit()
# driver.close()

