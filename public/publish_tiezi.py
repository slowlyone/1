#下：调试：
# from selenium import webdriver

from common.util import Util
from common.base import BaseCommon

class Publish_tiezi(object):
    def __init__(self,driver):
        self.driver=driver
        # #调试
        # self.driver=webdriver.Firefox()
        self.data_page=Util().operateYaml("../data/pageData/page1.yaml")
        self.basecommon=BaseCommon(self.driver)

    def publish(self):
        self.driver.find_element_by_css_selector("input[type='button']").click()
        self.driver.implicitly_wait(5)
        tar_title=self.driver.find_element_by_css_selector(self.data_page['page1']['function2']['标题'])
        tar_title.click()
        tar_title.send_keys(self.data_page['page1']['function2']['标题内容']+Util().suijishu())
        iframe_bite = self.driver.find_element_by_css_selector(self.data_page['page1']['function2']['iframe'])

        self.driver.switch_to.frame(iframe_bite)

        # iframe_bite.send_keys('AAA')  #即使一个frame 只有 也不能发信息
        article=self.driver.find_element_by_css_selector(self.data_page['page1']['function2']['文本位置'])
        article.send_keys(self.data_page['page1']['function2']['文章内容'])

        #下拉框    , 注意要切回 主frame
        self.driver.switch_to.default_content()

        self.driver.find_element_by_css_selector(self.data_page['page1']['function2']['立即发布']).click()
        self.basecommon.untilTime("CSS_SELECTOR",self.data_page['page1']['personal']['图片上传弹框'])
        tankuang=self.driver.find_element_by_css_selector(self.data_page['page1']['personal']['图片上传弹框'])
        content=tankuang.text
        # print(content)
        return content
        # self.assertEqual(tankuang.text,"发布成功")








