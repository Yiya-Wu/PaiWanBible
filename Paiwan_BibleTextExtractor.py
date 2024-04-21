#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

def main():

    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read the contents of the file
        html_contents = file.read()
        print(html_contents)
    
    soup = BeautifulSoup(html_contents, "html.parser")

        # Example: Find all <a> tags with class "some-class"
        # links = soup.find_all("a", class_="some-class")

        # Iterate through the found links and do something with them
        # for link in links:
            # print(link.get("href"))
    return None
    
if __name__ == "__main__":
    file_path = "/Users/yiyawu/Documents/yiya/00.txt"
    main()
