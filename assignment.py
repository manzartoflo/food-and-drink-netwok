#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:08:21 2019

@author: manzar
"""

import requests
from bs4 import BeautifulSoup

url = "https://foodanddrinknetwork-uk.co.uk/suppliers/char/"

alpha = [chr(alp) for alp in range(65, 91)]
header = 'Company Name, Telephone, Email, Website\n'
file = open('assignment.csv', 'w')
file.write(header)

for data in alpha[:20]:
    req = requests.get(url + str(data))
    soup = BeautifulSoup(req.text, 'lxml')
    divs = soup.findAll('div', {'class': 'organization'})
    for div in divs:
        name = div.h3.span.text
        print(name)
        try:
            no = div.findAll('span', {'class': 'phone-number-block'})
            tel = no[0].span.a.attrs['value']
            #print(tel)
        except:
            tel = 'NaN'
            #print(tel)
            
        try:
            em = div.findAll('span', {'class': 'email-address-block'})
            email = em[0].span.a.attrs['href'].split('mailto:')[1]
            #print(email)
        except:
          email = 'NaN'
          #print(email)
          
        try:
            wb = div.findAll('span', {'class': 'link-block'})
            web = wb[0].span.a.attrs['href']
            #print(web)
        except:
            web = 'NaN'
            #print(web)
        file.write(name.replace(',', '' ) + ', ' + tel + ', ' + email + ', ' + web + '\n')
file.close()