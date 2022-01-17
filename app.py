from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_name = 'sockmarket.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
db = SQLAlchemy(app)

class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    data = db.Column(db.String(10000))
    api_key = db.Column(db.String(30))
    scores = db.Column(db.String(1000))

    def __repr__(self):
        return f"Leaderboard('{self.name}', '{self.data}', '{self.api_key}', '{self.scores}')"

@app.route('/add', methods=['POST'])
def landing_page():
    if request.method == 'POST':
        key = request.args['apiKey']
        data = request.args['data']
        scores = request.args['scores']
        leaderboard = Leaderboard.query.filter_by(api_key=key).first()
        leaderboard.data += data
        leaderboard.data += ","

        leaderboard.scores += scores
        leaderboard.scores += ","

        db.session.commit()
        return "<Response [200]>"

def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

@app.route('/leaderboard/<name>')
def leaderboard(name):
    leaderboard = Leaderboard.query.filter_by(name=name).first()

    scores = [int(score) for score in leaderboard.scores.split(",")[:-1]]
    data = leaderboard.data.split(",")[:-1]

    if scores and data != []:
        list1, list2 = zip(*sorted(zip(scores, data)))
        list1, list2 = Reverse(list1),Reverse(list2)
    else:
        list1, list2 = [], []

    return render_template("leaderboard.html", data=list2, scores=list1)

if __name__ == '__main__':
    app.run(debug=True)

