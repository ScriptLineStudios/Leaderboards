from flask import Flask, request, render_template, abort
from flask_sqlalchemy import SQLAlchemy
import secrets
import random
import time

times = []
calls = []

app = Flask(__name__)
db_name = 'sockmarket.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
db = SQLAlchemy(app)

class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    data = db.Column(db.String(10000))
    api_key = db.Column(db.String(30))
    scores = db.Column(db.String(1000))

    def __repr__(self):
        return f"Leaderboard('{self.name}', '{self.data}', '{self.api_key}', '{self.scores}')"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new_leaderboard', methods=['POST'])
def create_new_leaderboard():
    if request.method == 'POST':
        name = str(request.form["name"])
        led = Leaderboard.query.filter_by(name=name).first()
        if led:
            return "This leaderboard already exists!"
        else:
            api_key = secrets.token_hex(32)
            db.session.add(Leaderboard(id=random.randrange(-100000, 100000), name=name, data="", api_key=str(api_key), scores=""))
            db.session.commit()
            return f"Your api key is {api_key}"


@app.route('/add', methods=["POST"])
def landing_page():
    if request.method == "POST":
        key = request.args['apiKey']
        data = request.args['data']
        scores = request.args['scores']
        leaderboard = Leaderboard.query.filter_by(api_key=key).first()

        try:
            if type(int(scores)) == int or type(float(scores)) == float:        
                leaderboard.data += data
                leaderboard.data += ","

                leaderboard.scores += scores
                leaderboard.scores += ","

                db.session.commit()

                return "<Response [200]>"

        except ValueError:
            abort(400, "Bad request")

def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

@app.route('/leaderboard/<name>')
def leaderboard(name):
    leaderboard = Leaderboard.query.filter_by(name=name).first()

    scores = [float(score) for score in leaderboard.scores.split(",")[:-1]]
    data = leaderboard.data.split(",")[:-1]

    if scores and data != []:
        list1, list2 = zip(*sorted(zip(scores, data)))
        list1, list2 = Reverse(list1),Reverse(list2)
    else:
        list1, list2 = [], []

    return render_template("leaderboard.html", data=list2, scores=list1)



