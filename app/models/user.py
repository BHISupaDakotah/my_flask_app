from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<User {self.username}>"
