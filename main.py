import re
import requests
from bs4 import BeautifulSoup


def find_credit_card_numbers(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    card_pattern = r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
    return re.findall(card_pattern, text)

def find_in_file(file_name):
    if not isinstance(file_name, str):
        raise TypeError("file name must be string")
    try:
        with open(file_name,'r',encoding='utf-8') as in_file:
            text=in_file.read()
            return find_credit_card_numbers(text)
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
    return find_credit_card_numbers(inp_text)

def find_in_site(url):
    if not isinstance(url, str):
        raise TypeError("text or url must be string")
    try:
       response = requests.get(url)
       response.raise_for_status()
       html = response.text
       soup = BeautifulSoup(html, 'html.parser')
       text = soup.get_text(strip=True)
       return find_credit_card_numbers(text)
    except requests.RequestException as e:
        print(f"error fetching url: {e}")
        return []

def main():
    print("ku")


if __name__ == '__main__':
    main()