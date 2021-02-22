from selenium import webdriver
# 設定facebook登入資訊
url = 'https://www.facebook.com/'
email='ga2006191535@yahoo.com.tw'
password='s60155'
# 建立瀏覽器物件
driver = webdriver.Chrome()
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id('email').send_keys(email) #輸入郵件
driver.find_element_by_id('pass').send_keys(password)#輸入密碼
driver.find_element_by_id('u_0_b').click()    # 按登入鈕