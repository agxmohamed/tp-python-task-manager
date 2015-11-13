class Comment(db.Model):
	id = db.Column(db.Integer, primary_key = true)
	content = db.Column(db.Unicode)
	date = db.Column(db.DateTime)
	

		
