
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import json

import json



# enable browser logging
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(r'C:\Users\tonin_work\Documents\Repos\test\New folder\chromedriver.exe',desired_capabilities=d,options=chrome_options)
# driver = webdriver.Firefox()


driver.get("https://sym.gg/?game=warzone&page=gunsmith")


wz_data = driver.execute_script(f'''
return WarzoneData
''')


with open('warzone_full_data.json','w') as f:
    json.dump(wz_data, f, ensure_ascii=False, indent=4)