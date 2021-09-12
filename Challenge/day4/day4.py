# 수정해야 할 부분:
# url에 '.'이 포함되지 않으면 "is down" 출력하기

import requests


def check_url(url):  # url인지 아닌지 확인
    try:
        req = requests.get(url)
        print(f"{url} is up!")
    except:
        print(f"{url} is not a valid url")


def yes_no():
    answer = input("\nDo you want to start over? y/n ")
    if answer == 'y' or answer == 'n':
        return answer
    else:
        print("That is not a valid answer")
        print(type(answer))
        return yes_no()


while True:
    print("\nWelcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (seperated by comma)")

    sentence = input()

    url_list = sentence.lower().split(',')
    new_list = [i.strip() for i in url_list]  # 공백문자 제거한 list

    for i in range(len(new_list)):  # http존재여부 확인+추가해주기
        url = new_list[i]
        check = url.find("http")
        if check == -1:
            url = "http://"+new_list[i]

        check_url(url)

    y_n = yes_no()
    if y_n == 'y':
        continue
    else:
        break
