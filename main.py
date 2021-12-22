import pandas as pd
import time

from selenium.webdriver import Chrome
driver_path = "C:\\Users\\Vrushali\\Desktop\\chromedriver.exe"
driver = Chrome(executable_path=driver_path)
l = ['https://www.veromoda.in/fashion-vm/fashion-accessories-vm/vm-belt',
     'https://www.veromoda.in/fashion-vm/fashion-accessories-vm/fashion-bags-belts-wallets-vm']
links = []
for i in l:
    driver.get(i)

    previous_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == previous_height:
            break
        previous_height = new_height
    a = '//*[@id="ajax-product-list"]/div/div/div[1]/a'
    link_elements = driver.find_elements_by_xpath(a)
    for i in link_elements:
        href = i.get_attribute('href')
        links.append(href)
        print(href)
print(len(links))
#df = pd.DataFrame(links,columns=['Links'])
#print(df)
# df.to_csv('links.csv')

"""
path = '/html/body/header/div/div/div[4]/div/div[2]/div/div/ul/li[2]/div/div/div/div/div/div/div/ul/li/a[@class="main-menu with-submenu"]'
paths = ['/html/body/header/div/div/div[4]/div/div[2]/div/div/ul/li[3]/div/div/div/div/div/div/div/ul/li/a[@class="main-menu with-submenu"]'
         ,'/html/body/header/div/div/div[4]/div/div[2]/div/div/ul/li[4]/div/div/div/div/div/div/div/ul/li/a[@class="main-menu with-submenu"]'
         ,'/html/body/header/div/div/div[4]/div/div[2]/div/div/ul/li[5]/div/div/div/div/div/div/div/ul/li/a[@class="main-menu with-submenu"]',
         '/html/body/header/div/div/div[4]/div/div[2]/div/div/ul/li[6]/div/div/div/div/div/div/div/ul/li/a[@class="main-menu with-submenu"]',
         '/html/body/header/div/div/div[4]/div/div[2]/div/div/ul/li[7]/div/div/div/div/div/div/div/ul/li/a[@class="main-menu with-submenu"]',
         '/html/body/header/div/div/div[4]/div/div[2]/div/div/ul/li[5]/div/div/div/div/div/div/div/ul/li/a[@class="main-menu with-submenu"]']
new_links = []
for j in paths:
    li = driver.find_elements_by_xpath(j)
    print(len(li))
    for i in li:
        href = i.get_attribute("href")
        print(href)
        new_links.append(href)
"""
driver.quit()
