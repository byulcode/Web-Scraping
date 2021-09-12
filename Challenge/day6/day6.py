import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
from extract_iban import extract_countries


os.system("clear")
print("Welcome to CurrencyConvert PRO 2000\n")

# 나라 리스트 출력
IBAN = "https://www.iban.com/currency-codes"
countries = extract_countries(IBAN)
for i, v in enumerate(countries):
    print('#{} {}'.format(i, v['country']))


def ask():  # 이부분 잘 작동 안함 -> 수정 필요
    global a
    try:
        choice = int(input("# : "))
        if choice >= len(countries) or choice < 0:
            print("Choose a number from the list.")
            ask()
        else:
            a = countries[choice]
            print(a['country'])
            return(a)
    except ValueError:
        print("That wasn't a number")
        ask()


# 국가 코드 입력받기
print("\nWhere are you from? Choose a country by number")
first = ask()
first_code = first['code']
print("\nNow choose another country.")
second = ask()
sec_code = second['code']


def ask_amount():  # 환전할 값 입력받기
    try:
        amount = int(
            input((f"\nHow many {first_code} do you want to  convert to {sec_code}?\n")))
        return amount
    except ValueError:
        print("That wasn't a number")
        ask_amount()


amount = ask_amount()

WISE = f"https://wise.com/gb/currency-converter/{first_code.lower()}-to-{sec_code.lower()}-rate?amount={amount}"
request = requests.get(WISE)
soup = BeautifulSoup(request.text, "html.parser")

result = soup.find("input", {"id": "rate"})

if result:
    result = result['value']

    result = float(result) * float(amount)
    amount = format_currency(amount, first_code, locale="ko_KR")
    result = format_currency(result, sec_code, locale="ko_KR")
    print(f"{amount} is {result}")
