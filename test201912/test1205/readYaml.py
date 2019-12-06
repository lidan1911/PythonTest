import yaml
import os


class ReadYaml:
    '''
    读取yaml的类，实例化该类可以选择是否传递参数key，key即yaml中配置的key，若不传，即返回yaml中所有配置项
    '''

    def __init__(self, key = None):
        self.key = key
        pwd = os.getcwd()
        self.yamlPath = os.path.join(pwd, 'cfgyaml.yaml')

    def readByKey(self):
        '''
        读取yaml的方法封装
        :return: 返回读取到的yaml字典
        '''
        f = open(self.yamlPath, 'r', encoding='utf-8')
        cfg = f.read()
        dic = yaml.load(cfg)  # string->dic
        if self.key:
            return dic[self.key]
        else:
            return dic


if __name__ == '__main__':
    ReadYaml('email').readByKey()
