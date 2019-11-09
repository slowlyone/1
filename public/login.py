# import yaml
import time
from common.util import Util
from selenium import webdriver

class Mylogin(object):
    def __init__(self,driver):
        self.driver=driver
        # self.data=Util().operateYaml('../data/pageData/page1.yaml')
        # self.data2=Util().operateYaml('../data/inputData/loginData.yaml')
        self.data= Util().operateYaml("../data/inputData/loginData.yaml")

    def login(self):
        tar1=self.driver.find_element_by_css_selector(self.data['login']['function']['登入'])
        if tar1.is_displayed():
            tar1.click()

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector(self.data['login']['function']['邮箱']).send_keys\
            (self.data['login']['login_data_01']['username'])
        self.driver.find_element_by_css_selector(self.data['login']['function']['密码']).send_keys\
            (self.data['login']['login_data_01']['pwd'])
        tar2= self.driver.find_element_by_css_selector(self.data['login']['function']['立即登录'])
        tar2.click()
        time.sleep(2)

# if __name__ == '__main__':
#     driver =webdriver.Firefox()
#     driver.get("http://47.104.84.186:8080/forum")
#     driver.implicitly_wait(10)
#     # #print(driver.find_element_by_css_selector("input[type='button']").text)
#     a=driver.find_element_by_css_selector("input[type='button']").get_attribute('value')
#     print(a)
#     time.sleep(2)
#     k=Mylogin(driver)
#     k.login()
