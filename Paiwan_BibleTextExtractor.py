#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

def main(inputSTR):
    soup = BeautifulSoup(inputSTR, "html.parser")
    result = str(soup.get_text())
    print(result, '===')    
    a = result.replace('(暫無內容)', '')
    print(a)
    
if __name__ == "__main__":
    file_path = "/Users/yiyawu/Documents/yiya/Paiwan_marku.txt"
    with open(file_path, 'r') as file:
        html_contents = file.read()
        
        main(html_contents)
