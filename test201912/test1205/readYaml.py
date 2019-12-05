import yaml
import os


class ReadYaml:

    def __init__(self, key = None):
        self.key = key
        pwd = os.getcwd()
        self.yamlPath = os.path.join(pwd, 'cfgyaml.yaml')

    def readByKey(self):
        f = open(self.yamlPath, 'r', encoding='utf-8')
        cfg = f.read()
        dic = yaml.load(cfg)  # string->dic
        if self.key:
            return dic[self.key]
        else:
            return dic


if __name__ == '__main__':
    ReadYaml('email').readByKey()
