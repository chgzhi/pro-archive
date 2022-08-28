# processArchivePic.py
'''
Date: 2022-08-17
Author: Guangzhi Chen
'''

import os
import fitz # 用于将图片拼接。安装方法pip install -i https://pypi.tuna.tsinghua.edu.cn/simple fitz pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyMuPDF
filePath = "./figs" # 输入文件夹目录
outPath = "./outs" 

fileNames = os.listdir(filePath) # 得到文件夹下所有文件的名称

# 用一个字典存储一个序列中的多个编号，方便后来同序列输出一个pdf
seriesDic = {}
for fileName in fileNames:
    key = fileName[:11]
    value = fileName[11:]
    seriesDic.setdefault(key, []).append(value)
    


#Function: 用于拼接
#Params:
#      1. key：为一个字符串，序列名
#      2. value: 为一个列表
def pic2Pdf(key, value):
    seriePdf = fitz.open()
    for i in value:
        imgFile = filePath + '/' + key + i 
        imgDoc = fitz.open(imgFile)
        #print(dir(imgDoc)) # 调试，用于查找方法名
        pdfBytes = imgDoc.convert_to_pdf()
        imgPdf = fitz.open(key + i[:-4] + '.pdf', pdfBytes)
        seriePdf.insert_pdf(imgPdf)
    if not os.path.exists(outPath): # 如果不存在文件夹，则创建
        os.makedirs(outPath)
    seriePdf.save("./outs/" + key + '.pdf')
    seriePdf.close()


## 档案图片的批量合并转成pdf
for k in seriesDic:
    pic2Pdf(k, seriesDic[k])



## 一下代码，用于单元测试
#print(seriesDic)
#pic2Pdf('030-002-001', ['001.JPG'])
#pic2Pdf('030-002-002', ['001.JPG', '002.JPG'])
