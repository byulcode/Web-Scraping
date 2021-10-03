from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

db = {}


@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)  # db에 있는지 찾기
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs  # 결과 db에 저장
    else:
        return redirect("/")  # home으로 되돌아감
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs
                           )


app.run(host="0.0.0.0")  # repl.it을 위해 있는것. 로컬에선 지워
