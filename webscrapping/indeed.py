import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/취업?q=python&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")
    # soup: 데이터를 분류해주는 역할

    pagination = soup.find("div", {"class": "pagination"})
    # 페이지 관련 검사를 보면, div class="pagination"이 페이지를 나타낸다
    # 따라서 soup는 html을 가져왔으니까 여기서 find해라 어떤걸? div class pagination을 가진 정보들을 가져온다.

    links = pagination.find_all('a')
    # links는 pagination 변수 에서 find all 'a'를 찾아서 리스트를 만들어준것
    # 'a'는 페이지를 가르키는 html에서 2,3,4,5 페이지를 찾는것
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    # 업무
    jobTitle = html.find("h2", {"class": "jobTitle"})
    title = jobTitle.find("span", title=True).string
    if title == "new":
        title = jobTitle.find_all("span")[1].string

    # 회사
    company = html.find("span", {"class": "companyName"})
    if company is not None:
        company = str(company.string)
    else:
        company = str(company)
    company = company.strip()

    # 장소
    location = html.find("div", {"class": "companyLocation"}).string

    job_id = html["data-jk"]

    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://kr.indeed.com/취업?q=python&limit=50&vjk={job_id}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")  # html
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("a", {"class": "fs-unmask"})  # 모든 일자리 찾기

    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page) 
  return jobs