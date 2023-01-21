from flask import Flask, render_template, request
from remoteok import extract_remoteok_jobs
from weworkremotely import extract_weworkremotely_jobs

app = Flask("JobScrapper")

OKDB = {}
WWDB = {}


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/result")
def result():
  global OKDB, WWDB
  keyword = request.args.get("keyword")
  if keyword in OKDB:
    remoteokJobList = OKDB[keyword]
  else:
    remoteokJobList = extract_remoteok_jobs(keyword)
    OKDB = remoteokJobList
  if keyword in OKDB:
    weWorkRemotelyJobList = WWDB[keyword]
  else:
    weWorkRemotelyJobList = extract_weworkremotely_jobs(keyword)
    WWDB[keyword] = weWorkRemotelyJobList
  return render_template("result.html",
                         keyword=keyword,
                         OKJobs=remoteokJobList,
                         WWJobs=weWorkRemotelyJobList)


app.run("0.0.0.0")
