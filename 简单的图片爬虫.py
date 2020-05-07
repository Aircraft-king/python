# -*- coding: utf-8 -*-
import codecs
import csv
import requests
from bs4 import  BeautifulSoup

def getHTML(url):
    r=requests.get(url)
    return r.content

#jiexi
def openHTML(html):
    soup=BeautifulSoup(html,'html parser')
    body=soup.body

    company_middle=body.find('div',attrs={'class':'middle'})
    company_list_ct=company_middle.find('div',attrs={'class':'list-ct'})

    company_list=[]

    for company_ul in company_list_ct.find_all('url',attrs={'class':'company-list'}):
        for company_li in company_ul.find_all('li'):
            company_url=company_li.a['href']
            company_info=company_li.get_text()
            company_list.append([company_info.encode('gbk'),company_url.encode('gbk')])

    return company_list

def WriteCSV(file_name,data_list):
    with codecs.open(file_name,'wb') as f:
        writer=csv.writer(f)
        for data in data_list:
            writer.writerow=(data)


url='http://www.cninfo.com.cn/cninfo-new/information/companylist'
html=getHTML(url)
data_list=openHTML(html)
WriteCSV('result.csv',data_list)
