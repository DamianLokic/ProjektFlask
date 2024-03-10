from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    body = db.Column(db.String(1000))

    def __repr__(self):
        return '<Post {}>'.format(self.title)
