import re
import requests
from bs4 import BeautifulSoup

def find_ways(text):
    if not isinstance(text, str):
        raise TypeError("text must be string")
    return re.findall(r"[A-Z]:\\([a-zA-Z0-9 _.-]+\\)*[a-zA-Z0-9 _.-]*", text)

def find_in_file(file_name):
    if not isinstance(file_name, str):
        raise TypeError("file name must be string")
    try:
        with open(file_name,'r',encoding='utf-8') as in_file:
            text=in_file.read()
            return find_ways(text)
    except FileNotFoundError:
        print("file was not found. Please check the file path")
        return None
    except IsADirectoryError:
        print("specified path is directory not a file")
        return None
    except Exception as e:
        print(f"unexpected error occurred: {e}")
        return None

def find_in_input_text():
    inp_text=input("enter string:" )
    return find_ways(inp_text)

def find_in_site(text, url):
    if not isinstance(text, str) or not isinstance(url, str):
        raise TypeError("text or url must be string")
    response=re

def main():
    print("ku")


if __name__ == '__main__':
    main()