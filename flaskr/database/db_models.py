from database.db_initialization import db

class CounterTable(db.Model):
	__tablename__ = "counter_new"

	id = db.Column(db.Integer, primary_key=True)
	count = db.Column(db.Integer, nullable=True)

	def __repr__(self):
		return f'<Count> {self.count}'
	
# with app.app_context():
#     db.create_all()