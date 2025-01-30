from flask import Flask, jsonify
from datetime import datetime
import pytz
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/", methods=["Get"])
def get_info():
    email = "ebenezerboluwatife14@gmail.com"
    github_url ="https://github.com/softtech2005/hng12_stage0_task.git"

    current_datetime = datetime.now(pytz.utc).isoformat()

    response ={
        "email" : email,
        "current_datetime" : current_datetime,
        "github_url" : github_url
    }


    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
