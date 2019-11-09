from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


#调试阶段补全：
# from  selenium import webdriver

class BaseCommon(object):

    def __init__(self,driver):
        '''初始化driver'''
        self.driver=driver
        # 调试:
        # self.driver=webdriver.Firefox()


    def back(self):
        #浏览器后退
        self.driver.back()

    def  forward(self):
        self.driver.forward()

    def  fresh(self):
        self.driver.refresh()

    def openUrl(self,url):
        "打开浏览器的方法"
        self.driver.get(url)

    def title(self):
        return self.driver.current_url



    def maxBroswer(self):
        self.driver.maximize_window()

    def cloeBroswer(self):
        self.driver.close()

    def  quitBroswer(self):
        self.driver.quit()


    def screenShot(self,path):
        #path="D:\\baidu_img.jpg"
        self.driver.get_screenshot_as_file(path)

    def untilTime(self,attrib,attrCont):
        '''WebDri 时间'''
        if attrib == "ID":
            elem = WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_all_elements_located((By.ID,attrCont))
            )

        elif attrib == "CLASS_NAME":
            elem = WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,attrCont))
            )
        elif attrib=="LINK_TEXT":
            elem=WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_all_elements_located((By.LINK_TEXT,attrCont))
            )
        elif attrib=="PARTIAL_LINK_TEXT":
            elem=WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT,attrCont))
            )
        elif attrib=="XPATH":
            elem=WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_all_elements_located((By.XPATH,attrCont))
            )
        elif attrib=="CSS_SELECTOR":
            elem=WebDriverWait(self.driver,5,0.5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR,attrCont))
            )

        return elem

    def move_to_elem(self,element):
        #鼠标移动到某元素

        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self,element):
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self,element):
        ActionChains(self.driver).context_click(element).perform()

    def drag(self,source,destince):
        '''托拽某滑动控件从一个地方滑动到另一个地方'''
        ActionChains(self.driver).drag_and_drop(source,destince).perform()

    '''1多窗口切换'''

    '''2alert'''
    def  alert_accept(self):
        '''正向'''
        self.driver.switch_to.alert.accept()

    def  alert_dismiss(self):
        '''逆向'''
        self.driver.switch_to.alert.dismiss()


    def down_move(self):
        '''下滑底部'''
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.8)")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.7)")

    def  iframe_default(self):
        self.driver.switch_to.default_content()

    def Select(self,posite,index):
        Select(posite).select_by_index(index)

