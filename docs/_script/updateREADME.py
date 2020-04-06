import os
import yaml

##
# 笔记链接自动生成器
# 将新的笔记URL根据分类添加进首页README.md
##

# 加载yaml配置文件，获取配置
def getConfig(configFile):
    curPath = os.path.dirname(os.path.realpath(__file__))
    yamlPath = os.path.join(curPath, configFile)
    confFile = open(yamlPath,'r',encoding='UTF-8')
    config = confFile.read()
    dist = yaml.load(config, Loader=yaml.BaseLoader)
    return dist

# 检查配置读取情况
def checkConfig(param, key):
    if(param == ""):
        print("can't read " + key + "from conf.yaml")
        os.system('pause')
        exit()


# 忽略文件名
def ignoreFile(name):
    for ignore in ignoreList:
        if(ignore == name):
            return True
    return False

# 获取file_dir下所有文件夹名
# 忽略文件名单为ignoreList
def getFolderName(file_dir):
    folderNames = []
    for file in os.listdir(file_dir):
        if (ignoreFile(file)):
            continue
        folderNames.append(file)
    return folderNames

# 获取file_dir下所有后缀为suffix的文件
def getFileNames(file_dir, suffix):
    fileNames = []
    for file in os.listdir(file_dir):
        if (file.endswith(suffix)):
            fileNames.append(file)
    return fileNames

# 读MD文件
def readFile(fileDist, file_dir):     
    file = open(file_dir,'rt', encoding='UTF-8')
    for line in file:
        deleteHasURL(fileDist, line)
    file.close()

# 删除字典中已有URL
def deleteHasURL(fileDist, line):
    for urls in fileDist.values():
        for url in urls[:]:
            if(("- "+url+"\n") == line):
                urls.remove(url)

# 转换为MarkDown URL
def trans2URL(dist):
    for key in dist:
        fileNames = getFileNames(root+key,'.md')
        for i in range(len(fileNames)):
            fileNames[i] = '['+ fileNames[i][:-3] +'](' + blog+key+'/'+fileNames[i] + ')'
        dist[key] = fileNames
    return dist

# 将新的URL插入到合适位置
def insertNewUrl(fileDist, fileContext):
    for key,value in fileDist.items():
        if(len(value) == 0):
            continue
        
        for i in range(len(fileContext)):
            if(fileContext[i] == '- '+key+'\n'):
                for j in range(len(value)):
                    value[j] = '- ' + value[j] + '\n'
                    fileContext.insert(i,value[j])
                    print('Insert a new url: ' + value[j])
                break
    return fileContext

# 检查是否需要更新
def checkUpdate(fileDist):
    for value in fileDist.values():
        if(len(value) != 0):
            return True
    return False

# 流程
# 1. 获取文件夹路径，转化为字典格式 fileDist{ 'Web':[ None, ... ], ... }
# 2. 获取每个文件夹文件，拼接成最终可访问URL fileDist{ 'Web':[ '[SSM](yankeyon.gitee.io/keyonblog/#/Web/SSM.md)', ... ], ... }
# 3. 读取README.md，删除字典中已有URL
# 4. 将字典中剩余URL写入README.md

ignoreList = ['.git','_media','_script','.nojekyll','coverpage.md','index.html','navbar.md','README.md','Doc']
fileDist = {}

# Step0 Load & Check Config
configDist = getConfig('conf.yaml')
root = configDist['BlogLocalPath']
checkConfig(root, 'BlogLocalPath')
if(root[-1] != '/'):
    root = root + '/'
blog = configDist['BlogRepoPath']
checkConfig(blog, 'BlogRepoPath')
if(blog[-1] != '/'):
    blog = blog + '/'
ignoreList = configDist['ignoreList']
checkConfig(ignoreList, 'ignoreList')

# Step1
folderNames = getFolderName(root) # [Web,DB,...]
#print("Step1. " + str(folderNames))
fileDist = fileDist.fromkeys(folderNames) # { 'Web':[ None, ... ], ... }
# Step2
fileDist = trans2URL(fileDist)
#print("Step2. " + str(fileDist)))
# Step3
try:
    readFile(fileDist, root+'README.md')
except Exception as e:
    print(e)
#print("Step3. " + str(fileDist)))
if(checkUpdate(fileDist)):
    pass
else:
    print('##### README.md is already up to date #####')
    os.system('pause')
    exit(0)
# Step4
try:
    fileContext = []
    file = open(root+'README.md','rt', encoding='UTF-8')
    fileContext = file.readlines()
    fileContext = insertNewUrl(fileDist, fileContext)
    file.close()
    newFile = open(root+'README.md','w', encoding='UTF-8')
    newFile.writelines(fileContext)
    newFile.close()
except Exception as e:
    print(e)
print('##### Update README.md Success #####')
os.system('pause')