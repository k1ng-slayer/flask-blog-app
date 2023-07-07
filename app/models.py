from app import db
from datetime import datetime



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default="defualt.jpeg")
    password = db.Column(db.String(60), nullable=False)
    # 'posts' has a relationship with 'class Post'
    posts = db.relationship("Post", backref="author", lazy=True) 

    def __repr__(self):
        return (f"User('{self.username}', '{self.email}', '{self.image}')")
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # declaring a foreign key to establish connection between both the tables
    # 'class User' & 'class Post' will be coverted to table 'user' & table 'post' & NOT table 'User' & table 'Post'
    # hence, we use lowercase 'user' in 'user.id'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    

    def __repr__(self):
        return (f"Post('{self.title}', '{self.date_posted}')")