import os
import yaml

##
# 笔记更新器
# 自动将更新推送到远程仓库
##
curPath = os.path.dirname(os.path.realpath(__file__))
yamlPath = os.path.join(curPath, 'conf.yaml')
confFile = open(yamlPath,'r',encoding='UTF-8')
config = confFile.read()
dist = yaml.load(config, Loader=yaml.BaseLoader)
os.chdir(dist['BlogLocalPath'])
os.system('git status')
os.system('git add .')
os.system('git commit -m "Update"')
os.system('git push')

print('##### Update Over #####')
print('Blog -- http://yankeyon.gitee.io/keyonblog/#/')
os.system("pause")