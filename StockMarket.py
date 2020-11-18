# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:58:02 2020

@author: darth
"""

import bs4
import requests
import time
from bs4 import BeautifulSoup


def parsePrice():
    r=requests.get('https://au.finance.yahoo.com/quote/GOOG?p=GOOG')    
    soup=bs4.BeautifulSoup(r.text,"lxml")
    price=soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

def parsePrice2():
    r=requests.get('https://au.finance.yahoo.com/quote/TSLA?p=TSLA')    
    soup=bs4.BeautifulSoup(r.text, "lxml")
    price2=soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price2

def parsePrice3():
    r=requests.get('https://au.finance.yahoo.com/quote/AAPL?p=AAPL')    
    soup=bs4.BeautifulSoup(r.text, "lxml")
    price3=soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price3

def parsePrice4():
    r=requests.get('https://au.finance.yahoo.com/quote/CCL.AX?p=CCL.AX')   
    soup=bs4.BeautifulSoup(r.text, "lxml")
    price4=soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price4



while True:

    print('The current price for Alphabet INC (GOOGLE) according to Yahoo Finance is: ' +str(parsePrice()))

    print('The current price for Tesla according to Yahoo Finance is: ' +str(parsePrice2()))

    print('The current price for Apple INC according to Yahoo Finance is: '+str(parsePrice3()))

    print('The current price for Coca Cola Amatil according to Yahoo Finance is: '+str(parsePrice4()))
    time.sleep(1)
