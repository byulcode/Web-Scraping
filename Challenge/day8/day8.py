import os
import csv
import requests
from bs4 import BeautifulSoup

# extract_alba 에서 가져오기가 안됨

os.system("clear")
alba_url = "http://www.alba.co.kr"
#------------ Home page ----------------#
company_list = []
company_request = requests.get(alba_url)
company_soup = BeautifulSoup(company_request.text, "html.parser")

ul = company_soup.find("div", {"id": "MainSuperBrand"}).find(
    "ul", {"class": "goodsBox"}).find_all("a", {"class": "brandHover"})

for i in ul:  # company_list 채우기
    href = i.attrs['href']  # 회사별 상세 사이트
    name = i.find("strong").text.strip()  # 회사 이름
    name = name.replace("/", "_")
    company = {
        'name': name,
        'link': href
    }
    company_list.append(company)

#------------ detail pages ----------------#


def get_last_alba(url):  # 알바 채용공고 개수 반환
    result = requests.get(url)
    page_soup = BeautifulSoup(result.text, "html.parser")

    paging = page_soup.find("p", {"class": "jobCount"})
    max_alba = paging.find("strong").text
    return int(max_alba)


def extract_alba(url):  # 채용공고 정보 리스트 반환
    alba_list = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    table = soup.find("table")
    html = table.find_all("tr")[1:]

    last_alba = get_last_alba(url)  # 알바 개수
    for i in range(last_alba):
        place = html.find("td", {"class": "local"}).text
        place = place.replace(u'\xa0', u' ')
        title = html.select_one("span.company").text
        alba_time = html.select_one("span.time").text
        pay = html.select_one("span.payIcon").text + \
            html.select_one("span.number").text
        enrol_date = html.select_one("td.regDate").text
        alba = {
            'place': place,
            'title': title,
            'time': alba_time,
            'pay': pay,
            'date': enrol_date
        }
        alba_list.append(alba)
    return alba_list


#-----------file save-------------#
def save_to_file(companies):
    for company in companies:
        fname = company['name'] + ".csv"
        file = open(fname, mode="w")
        writer = csv.writer(file)
        writer.writerow(["place", "title", "time", "pay", "date"])
        albas = extract_alba(company['link'])
        for alba in albas:
            print(list(alba.values()))
        return


save_to_file(company_list)
