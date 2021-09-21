#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#By William Baudrand Chaudeyrac


from bs4 import BeautifulSoup
import requests
from csv import *


#----------------------obtaining data----------------------------
def obtdata():#creation of list to contain data for the 4 informations
    dataobt=[]#number of star /5 
    data2=[]#price of the product
    data3=[]#name of the product
    data4=[]#availability
    
    for sub_heading0 in soup.find_all('div',class_="rating-result-ndp"):#
        dataobt.append(sub_heading0.text)#filling with the number of star of each product 
    for sub_heading1 in soup.find_all('div',class_="price-box price-final_price"):#
        data2.append(sub_heading1.text)#filling with the price of each product 
    for sub_heading2 in soup.find_all('a',class_="product-item-link"):#
        data3.append(sub_heading2.text)#filling with the name of each product 
    for sub_heading3 in soup.find_all('div',class_="stock available"):#
        data4.append(sub_heading3.text)#filling with the availability of each product 
    return dataobt,data2,data3,data4


url=["https://www.airsoft-entrepot.fr/all-catalog/approvisionnement-et-maintenance/tests-de-tir/chrony.html?in-stock=1","Chrony"]#page of Chronies
      
page = requests.get(url[0])#allow us to use the url for BeautifulSoup


soup = BeautifulSoup(page.text, 'html.parser')



print("Waiting 4 results ...")

infos,info2,info3,info4=obtdata()#collecting data from the previous function

#print(len(infos))
#print(len(info2))
#print(len(info3))
#print(len(info4))
#print(infos)
#print(info2)
#print(info3)
#print(info4)


#-----------------cleaning data------------------------

for i in range(0,len(info3)):#cleaning the names to make them easier to read(the \n and "                  ")
    test=info3[i]
    test=test.replace("\n","")
    test=test.replace(" ","")
    info3[i]=test
for i in range(0,len(infos)):#cleaning the rating to make them easier to read (the \n)
    test=infos[i]
    test=test.replace("\n","")
    infos[i]=test
for i in range(0,len(info2)):#cleaning the prices to make them easier to read, and to suppress useless caracters
    test=info2[i]
    test=test.replace("\n","")
    test=test.replace("\xa0","")
    info2[i]=test


#print(info3)
#print(infos)
#print(info2)
#--------------------data storing-------------------------

W= open('data.CSV','w',encoding='utf-8')#creating a .csv file to store the data


W.write(str(info3)+'\n')#writing the datas into the .csv file
W.write(str(infos)+'\n')
W.write(str(info2)+'\n')  
W.write(str(info4)+'\n')               
W.close()#never forget to close a file after opening it
