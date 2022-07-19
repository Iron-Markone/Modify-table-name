#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os


# In[7]:



def src(url):
    # 获取该文件夹所有文件名字
    files = os.listdir(url)
    postfix = input("请输入要保存的文件后缀名,输入0则表示去除后缀")
    for fileName in files:
        # 以文件名字最后一个.为目标进行切割并保存为元祖
        portion = os.path.splitext(fileName)
        # 获取元祖第一个位置并进行赋值
        newName = portion[0]
        # 把旧的文件名与路径进行拼接
        i = os.path.join(r'C:\Users\Administrator\Desktop\AM-FBA订单表-5月' + '\\' + fileName)
        # 把新的文件名与路径进行拼接
#         postfix = input("请输入要保存的文件后缀名,输入0则表示去除后缀")
        if postfix == 0:
            o = os.path.join(r'C:\Users\Administrator\Desktop\AM-FBA订单表-5月' + '\\' + newName)
        else:
            o = os.path.join(r'C:\Users\Administrator\Desktop\AM-FBA订单表-5月' + '\\' + newName + postfix)
        # 把旧的文件名字替换为新的文件名字
        os.rename(i, o)


# In[8]:


way = input("请输入重命名文件夹位置")
src(way)


# In[ ]:




