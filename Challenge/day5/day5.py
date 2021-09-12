import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

print("Hello! Please select a country by number: ")
url = "https://www.iban.com/currency-codes"


def extract_country(tr):  # country와 code dict형태로 반환
    # country
    country = tr.select_one('td:nth-of-type(1)').text.capitalize()

    # Alpha3-code
    code = tr.select_one('td:nth-of-type(3)').text

    return {
        'country': country,
        'code': code
    }


def find_code():

    try:
        code_num = int(input("# : "))
        if code_num > len(countries) or code_num < 0:
            print("Please choose number a number from the list")
            find_code()
        else:
            country = countries[code_num]
            print(f"You chose {country['country']}")
            print(f"The currency code is {country['code']}")
    except ValueError:
        print("That wasn't a number.")
        find_code()


response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
trs = soup.select('table>tbody>tr')


countries = []
for result in trs:
    country = extract_country(result)
    # 통화 코드 없을경우 리스트에서 제외
    if country['code']:
        countries.append(country)


for i, v in enumerate(countries):
    print('#{} {}'.format(i, v['country']))

find_code()
