from flask import Flask, render_template

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/<username>")
def contact(username): #함수 이름 달라도 됨
  return f"Hello {username} how are you doing"

app.run(host="0.0.0.0") #repl.it을 위해 있는것. 로컬에선 지워
