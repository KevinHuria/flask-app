# models.py
from app import app
from app import db, login_manager
from flask_login import UserMixin




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)

    def get_id(self):
        try:
            return (self.sno)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __repr__(self):
        return 'User(%s , %s)' % (self.uname, self.email)
