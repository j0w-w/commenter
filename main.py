#!/bin/python3
import sys
from bs4 import BeautifulSoup, Comment
import requests
import os

def extract_html_comments(url):
    request = requests.get(url)
    html_text = request.text
    soup = BeautifulSoup(html_text, 'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    unique_comments = list(dict.fromkeys(comment.strip() for comment in comments))
    return unique_comments


def main():
    if sys.argv[1] == "txt":
        for url in sys.stdin:
            try:
                url = url.strip('\n')
                comments = extract_html_comments(url)
                for comment in comments:
                    os.system(f"echo '{url}  :  {comment}'  >> {sys.argv[2]}")
            except:
                pass
    elif sys.argv[2] == "html":
        for url in sys.stdin:
            try:
                url = url.strip('\n')
                comments = extract_html_comments(url)
                for comment in comments:
                    #write to html
                    pass
            except:
                pass
    else:
        print("usage: cat urls | ./main.py html ~/comments.pdf")
        print("usage: cat urls | ./main.py txt ~/comments.txt")


main()