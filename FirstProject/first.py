from flask import Flask
from flask import request
import json
app = Flask(__name__)

name = "Roushan"
@app.route("/name")
def hello():
    return json.dumps({"name": name})


if __name__ == "__main__":
    app.run()



