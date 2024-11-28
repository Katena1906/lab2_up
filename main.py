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
        return []
    except IsADirectoryError:
        print("specified path is directory not a file")
        return []
    except Exception as e:
        print(f"unexpected error occurred: {e}")
        return []

def find_in_input_text():
    inp_text=input("enter string:" )
    return find_ways(inp_text)

def find_in_site(url):
    if not isinstance(url, str):
        raise TypeError("text or url must be string")
    try:
       response = requests.get(url)
       response.raise_for_status()
       html = response.text
       soup = BeautifulSoup(html, 'html.parser')
       text = soup.get_text(strip=True)
       return find_ways(text)
    except requests.RequestException as e:
        print(f"error fetching url: {e}")
        return []

def main():


if __name__ == '__main__':
    main()