class Priority(db.Model):
	id = db.Column(db.Integer, primary_key = true)
	name = db.Column(db.Unicode)
	description = db.Column(db.Unicode)
	value = db.Column(db.Integer)
	color = db.Column(db.Unicode)
	