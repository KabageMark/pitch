from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login_manager

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    pass_secure = db.Column(db.String(255),index = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    

    @login_manager.user_loader
    def load_user(self,user_id):
            return User.query.get(int(user_id))


    def __repr__(self):
        return f'User {self.username} '
        
class Pitches(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String)
    category = db.Column(db.String)

    def __repr__(self):
        return f'User {self.pitch} {self.category} '