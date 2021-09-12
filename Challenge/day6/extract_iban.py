import os
import requests
from bs4 import BeautifulSoup
#day5 수정함

os.system("clear")
url = "https://www.iban.com/currency-codes"

def extract_countries(url):
  countries = []
  request = requests.get(url)
  html = request.text
  soup = BeautifulSoup(html, "html.parser")
  trs = soup.select('table>tbody>tr')

  for result in trs:
    name = result.select_one('td:nth-of-type(1)').text.capitalize()
    code = result.select_one('td:nth-of-type(3)').text

    if name and code:
      country = {
        'country' : name,
        'code' : code
      }
      countries.append(country)
  return countries


def find_code():
  try:
    code_num = int(input("# : "))
    if code_num > len(countries) or code_num < 0:
      print("Please choose number a number from the list")
      find_code()
    else:
      country = countries[code_num]
      return country
  except ValueError:
    print("That wasn't a number.")
    find_code()


countries = extract_countries(url)
