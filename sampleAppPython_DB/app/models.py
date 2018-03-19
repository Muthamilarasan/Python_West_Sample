from sqlalchemy import Column, Integer, String
from db import Base


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name=None):
        self.name = name

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'name': self.name
       }

    # def __repr__(self):
    #     return "{\"Contact\" {\"name\":"%s", \"id\":"%s"}}" % (self.name, self.id)

    # def __repr__(self):
    #     return "<Contact(name='%s', id='%s')>" % (self.name, self.id)



# return "<User(name='%s', fullname='%s', password='%s')>" % (
# ...                             self.name, self.fullname, self.password)

# from app import db
#
# class Contact(db.Model):
#
#     __tablename__ = 'contact'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60), unique=True)
#
#     def __repr__(self):
#         return '<Contact: {}>'.format(self.name)
