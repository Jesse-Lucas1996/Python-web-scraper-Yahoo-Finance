# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:58:02 2020

@author: darth
"""

import bs4
import requests
import time
from bs4 import BeautifulSoup

while True:
    def googlePrice():
        r=requests.get('https://au.finance.yahoo.com/quote/GOOG?p=GOOG')    
        soup=bs4.BeautifulSoup(r.text,"lxml")
        price=soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        return price

    def teslaPrice():
        r=requests.get('https://au.finance.yahoo.com/quote/TSLA?p=TSLA')    
        soup=bs4.BeautifulSoup(r.text, "lxml")
        price2=soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        return price2

    def applePrice():
        r=requests.get('https://au.finance.yahoo.com/quote/AAPL?p=AAPL')    
        soup=bs4.BeautifulSoup(r.text, "lxml")
        price3=soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        return price3

    def cocaColaPrice():
        r=requests.get('https://au.finance.yahoo.com/quote/CCL.AX?p=CCL.AX')   
        soup=bs4.BeautifulSoup(r.text, "lxml")
        price4=soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        return price4

    print('The current price for Alphabet INC (GOOGLE) according to Yahoo Finance is: ' +str(googlePrice()))

    print('The current price for Tesla according to Yahoo Finance is: ' +str(teslaPrice()))

    print('The current price for Apple INC according to Yahoo Finance is: '+str(applePrice()))

    print('The current price for Coca Cola Amatil according to Yahoo Finance is: '+str(cocaColaPrice()))
    time.sleep(1)
