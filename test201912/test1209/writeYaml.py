import os
from ruamel import yaml


dic = {
    'a': 111,
    'b': 222,
    'c': 333
}

path = os.getcwd()
yamlPath = os.path.join(path, 'test.yaml')
print(yamlPath)

# with open(yamlPath, 'w', encoding='utf-8') as f:
#     yaml.dump(dic, f)

# 写入到yaml文件（写入到yaml后多余{}，不是合法yaml格式，需要添加yaml.RoundTripDumper，故需要安装ruamel
# 使用pip安装即可：pip install ruamel.yaml
with open(yamlPath, 'w', encoding='utf-8') as f:
    yaml.dump(dic, f, Dumper=yaml.RoundTripDumper)

