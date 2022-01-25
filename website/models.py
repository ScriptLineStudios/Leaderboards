db_name = 'sockmarket.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
db = SQLAlchemy(app)

class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    data = db.Column(db.String(10000))
    api_key = db.Column(db.String(30), unique=True)
    scores = db.Column(db.String(1000))

    def __repr__(self):
        return f"Leaderboard('{self.name}', '{self.data}', '{self.api_key}', '{self.scores}')"