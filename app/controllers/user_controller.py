from app.models.user import User
from app import db

class UserController:
    
    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def create_user(data):
        new_user = User(
            username=data['username'],
            email=data['email'],
            age=data['age']
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def update_user(user_id, data):
        user = User.query.get(user_id)
        if user:
            user.username = data['username']
            user.email = data['email']
            user.age = data['age']
            db.session.commit()
            return user
        return None
    
    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
