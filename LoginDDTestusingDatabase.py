from selenium import webdriver
import time
import cx_Oracle
import os
os.environ['PATH']='C:\\oracle\\instantclient_19_6'
driver=webdriver.Chrome(executable_path="C:\Python\drivers\chromedriver.exe")
driver.get("https://demo.openmrs.org/openmrs/login.htm")
driver.maximize_window()
#create connection
dsn_tns = cx_Oracle.makedsn('localhost', '1523', service_name='orcl3')
conn = cx_Oracle.connect(user='system', password='system', dsn=dsn_tns)
cur=conn.cursor()
query="select * from users2"
cur.execute(query)
for cols in cur:
    driver.find_element_by_name("username").send_keys(cols[0])
    driver.find_element_by_name("password").send_keys(cols[1])
    driver.find_element_by_id("Isolation Ward").click()
    driver.find_element_by_id("loginButton").click()
    time.sleep(5)
    #validation started
    if driver.current_url == "https://demo.openmrs.org/openmrs/referenceapplication/home.page":
        print("Test Passed")
        driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul/li[3]/a").click()
    else:
        print("Test Failed")
    driver.find_element_by_xpath("//*[@id='content']/div[2]/div/header/div/a/img").click()
cur.close()
conn.close()
print("Data driven test completed")
