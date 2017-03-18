from flask import Flask
import urllib2
import sys
import json
import base64

githubUrl = str(sys.argv[1])
githubUrl = githubUrl.replace('github.com','api.github.com/repos') + '/contents/'
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/<fileName>")
def github1(fileName):
    response = urllib2.urlopen(githubUrl + fileName)
    html = response.read()
    j = json.loads(html)
    return base64.b64decode(j['content'])

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
