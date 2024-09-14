from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    profile_description = db.Column(db.String(500), nullable=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref='posts')

# Many-to-many relationship for connections
connections = db.Table('connections',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('connected_user_id', db.Integer, db.ForeignKey('user.id'))
)
