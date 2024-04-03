from api.model.db_initialization import db

class CounterTable(db.Model):
	__tablename__ = "counter_new"

	id = db.Column(db.Integer, primary_key=True)
	count = db.Column(db.Integer, nullable=True)

	def __repr__(self):
		return f'<Count> {self.count}'
	
class UserAccountTable(db.Model):
	__tablename__ = "user_account_new"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255), nullable=False)
	password = db.Column(db.String(255), nullable=False)

	def __repr__(self):
		return f'<Username> {self.username} <Password> {self.password}'
	
# with app.app_context():
#     db.create_all()