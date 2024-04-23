from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    tid = datetime.now()
    return str('Klokka er nå: ' + str(tid)[12:20])

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8081)