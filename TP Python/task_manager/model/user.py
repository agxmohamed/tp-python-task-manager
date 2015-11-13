class User(db.Model):
	id = db.Column(db.Integer, primary_key = true)
	name = db.Column(db.Unicode)
	lastname = db.Column(db.Unicode)
	email = db.Column(db.Unicode)
	password = db.Column(db.Unicode)
	last_connection = db.Column(db.DateTime)
	picture = db.Column(db.Unicode)
	task = db.Column(db.Integer)
