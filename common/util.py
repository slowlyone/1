import yaml
import random

'''
toolsClass
'''
class Util(object):

    def __init__(self):
        pass

    def operateYaml(self,filename):
        file= open(filename,"r",encoding='utf-8')
        data = yaml.full_load(file)
        file.close()
        return data

    def suijishu(self):
        '''生成随机的数'''
        k=''.join([str(i) for i  in random.sample(range(15),14)])

        return k

# if  __name__=="__main__":
#     k=Util()
#     data=k.operateYaml("../data/pageData/page1.yaml")
#     print(data['page1']['url'])
