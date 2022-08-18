from flask import Flask
from datetime import datetime
app = Flask(__name__)

team = {
    "india": [
        {
            "name": "Rohit Sharma",
            "description": "Right hand batter and captain",
            "date": datetime.now()
        },
        {
            "name": "Virat Kohli",
            "description": "Right hand batter",
            "date": datetime.now()
        },
        {
            "name": "Suryakumar Yadav",
            "description": "Right hand batter",
            "date": datetime.now()
        },
        {
            "name": "KL Rahul",
            "description": "Right hand batter",
            "date": datetime.now()
        },
        {
            "name": "Hardik Pandya",
            "description": "Allrounder",
            "date": datetime.now()
        },
        {
            "name": "Dinesh Kartik",
            "description": "Right hand batter and wicketkeeper",
            "date": datetime.now()
        },
        {
            "name": "Ravindra Jadeja",
            "description": "Allrounder",
            "date": datetime.now()
        },
        {
            "name": "Bhuvneshwar Kumar",
            "description": "Right arm medium fast bowler",
            "date": datetime.now()
        },
        {
            "name": "Arshdeep Singh",
            "description": "Left arm fast bowler",
            "date": datetime.now()
        },
        {
            "name": "Yuzi Chahal",
            "description": "Right arm leggie",
            "date": datetime.now()
        },
        {
            "name": "Mohammad Shami",
            "description": "Right arm fast bowler",
            "date": datetime.now()
        }
    ]
}

@app.route("/")
def index():
    return "Indian Cricket team for worldcup 2022"

@app.route("/india")
def get_india():
    return team


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)