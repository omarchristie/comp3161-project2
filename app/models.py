from . import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    D_O_B = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    address= db.Column(db.String(255))
    phone = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.user_id)  # python 2 support
        except NameError:
            return str(self.user_id)  # python 3 support

    def __repr__(self):
        return '<Email %r>' % (self.email)
