from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time

from selenium.webdriver.support.select import Select

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

log.info("Start testing")
login_button = driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/a')
login_button.click()
time.sleep(1)
login_input = driver.find_element(By.ID, 'id_username')
password_input = driver.find_element(By.ID, 'id_password')

login_input.send_keys("selenium")
password_input.send_keys("seleniumselenium123")

login_button = driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/form/button')
login_button.click()

time.sleep(1)
log.info("Successful authorization")

category_button = driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[2]/a')
category_button.click()
time.sleep(1)

create_category_button = driver.find_element(By.XPATH, '/html/body/main/div/a')
create_category_button.click()
time.sleep(1)

category_name_input = driver.find_element(By.XPATH, '//*[@id="id_title"]')
category_desc_input = driver.find_element(By.XPATH, '//*[@id="id_description"]')
category_name_input.send_keys("selenium")
category_desc_input.send_keys("selenium desc")
category_button = driver.find_element(By.XPATH, '/html/body/main/div/form/button')
category_button.click()

log.info(f"Successful creation of a category. Category name: {category_name_input}")
time.sleep(1)
category_update_button = driver.find_element(By.XPATH, '/html/body/main/div/div/div/a[1]')
category_update_button.click()
category_desc_input = driver.find_element(By.XPATH, '//*[@id="id_description"]')
category_desc_input.send_keys("123")

save_category_button = driver.find_element(By.XPATH, '/html/body/main/div/form/button')
save_category_button.click()
time.sleep(1)
log.info(f"Successful updating a category")

view_products = driver.find_element(By.XPATH, '/html/body/main/div/div/div/a[3]')
view_products.click()

create_product = driver.find_element(By.XPATH, '/html/body/main/div/a[1]')
create_product.click()

product_name = driver.find_element(By.XPATH, '//*[@id="id_title"]')
product_name.send_keys("selenium product")

product_desc = driver.find_element(By.XPATH, '//*[@id="id_description"]')
product_desc.send_keys("selenium product")
product_price = driver.find_element(By.XPATH, '//*[@id="id_selling_price"]')
product_price.send_keys("100")
product_quantity = driver.find_element(By.XPATH, '//*[@id="id_amount"]')
product_quantity.send_keys("10")
product_measure = driver.find_element(By.XPATH, '//*[@id="id_measure_unit"]')
product_measure.send_keys("штук")

driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(2)
create_product_button = driver.find_element(By.XPATH, '/html/body/main/div/form/button')
create_product_button.click()
time.sleep(1)
log.info("Successfully created product")

all_products_button = driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[3]/a')
all_products_button.click()
time.sleep(1)
log.info("Opened page 'products heap'")

order_button = driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[4]/a')
order_button.click()
time.sleep(1)

create_order_button = driver.find_element(By.XPATH, '/html/body/main/div/a')
create_order_button.click()

buyer_name = driver.find_element(By.XPATH, '//*[@id="id_buyer"]')
buyer_name.send_keys("selenium buyer")
add_product_button = driver.find_element(By.XPATH, '//*[@id="add-product-button"]')
add_product_button.click()

dropdown = driver.find_element(By.XPATH, '//*[@id="products-list"]/div/select')
select = Select(dropdown)
time.sleep(1)
select.select_by_visible_text("selenium product")

amount_input = driver.find_element(By.XPATH, '//*[@id="products-list"]/div/input[2]')
amount_input.send_keys("5")
time.sleep(1)

add_product_button.click()
delete_product_button = driver.find_element(By.XPATH, '//*[@id="products-list"]/div[2]/button')
delete_product_button.click()

time.sleep(1)

create_order_button = driver.find_element(By.XPATH, '//*[@id="order-form"]/button[2]')
create_order_button.click()
time.sleep(1)
log.info("Successfully created order")

delete_order = driver.find_element(By.XPATH, '/html/body/main/div/table/tbody/tr/td[7]/a')
delete_order.click()

delete_order_confirm = driver.find_element(By.XPATH, '/html/body/main/div/form/input[2]')
delete_order_confirm.click()
log.info("Successfully deleted order")

time.sleep(1)

category_button = driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[2]/a')
category_button.click()
time.sleep(1)
delete_category_button = driver.find_element(By.XPATH, '/html/body/main/div/div/div/a[2]')
delete_category_button.click()

time.sleep(1)

delete_category_button_confirm = driver.find_element(By.XPATH, '/html/body/main/div/form/input[2]')
delete_category_button_confirm.click()
time.sleep(1)
log.info("Successfully deleted category")

profile_button = driver.find_element(By.XPATH, '//*[@id="navbarNav"]/div/a')
profile_button.click()
log.info("Open a profile page")
time.sleep(1)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)
name_input = driver.find_element(By.XPATH, '//*[@id="id_first_name"]')
name_input.send_keys("123")
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(1)
save_profile_button = driver.find_element(By.XPATH, '/html/body/main/div/form/button')
save_profile_button.click()
log.info("Successfully saved user data")

logout_button = driver.find_element(By.XPATH, '//*[@id="navbarNav"]/div/form/button')
logout_button.click()
time.sleep(1)
log.info("Logout")

driver.close()
log.info("Testing has been completed successfully")
