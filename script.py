from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Enter your contacts in the list
Contact = ['user1','user2','user3']

driver = webdriver.Chrome(executable_path = "C:\Program Files\Selenium\chromedriver")
driver.get("https://web.whatsapp.com/")
driver.maximize_window()


for i in Contact:
    x_arg = '//*[@id="side"]/div[1]/div/label/input'
    wait = WebDriverWait(driver, 600)
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    group_title.send_keys(i + Keys.ENTER)
    driver.implicitly_wait(20)
    input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    input_box.send_keys('This is automated text sended by saikat to : '+i+"" + Keys.ENTER)





