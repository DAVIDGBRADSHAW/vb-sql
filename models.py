from flask_sqlalchemy import SQLAlchemy                         #new: Flask-SQLAlchemy
from sqlalchemy import  Column, Integer, Text, TIMESTAMP
from datetime import datetime

db = SQLAlchemy()

class Booking(db.Model):
    __table_args__ = {"schema": "cd"}
    __tablename__ = 'bookings'
    bookid = db.mapped_column(db.Integer, primary_key=True)
    facid = db.mapped_column(db.Integer, db.ForeignKey('cd.facilities.facid'))
    memid = db.mapped_column(db.Integer, db.ForeignKey('cd.members.memid'))
    starttime = db.mapped_column(db.DateTime, default=datetime.utcnow)
    slots = db.mapped_column(db.Integer, primary_key=False)
    member = db.relationship('Member', back_populates='bookings')
    facility = db.relationship('Facility', back_populates='bookings')    

    def __str__(self):
        return f'"{self.bookid}" at {self.facid} {self.memid} ({self.starttime:%Y-%m-%d}) {self.slots}'

    @staticmetho
    def get_bookings():
       
        sql = text("""select mems.firstname, mems.surname, bks.starttime, bks.slots, bks.bookid 
                        from cd.bookings bks inner join cd.members mems on mems.memid = bks.memid 
                        order by bks.starttime desc""")
        return db.session.execute(sql).all()  # Returns just the integers

   

class Facility(db.Model):
    __table_args__ = {"schema": "cd"}
    __tablename__ = 'facilities'
    facid = db.mapped_column(db.Integer, primary_key=True)
    name = db.mapped_column(db.String(100), nullable=False)
    membercost = db.mapped_column(db.Numeric, nullable=False)
    guestcost = db.mapped_column(db.Numeric, nullable=False)
    initialoutlay = db.mapped_column(db.Numeric, nullable=False)
    monthlymaintenance = db.mapped_column(db.Numeric, nullable=False)
    bookings = db.relationship('Booking', back_populates='facility')

    def __str__(self):
        return f'"{self.memid}", {self.zipcode}, {self.recommendedby}, {self.telephone}, {self.firstname}, {self.surname}, {self.address}, ({self.joindate:%Y-%m-%d}) '




#    @staticmethod
#    def get_post_lengths():
#        # An example of how to use raw SQL inside a model
#        sql = text("SELECT length(title) + length(content) FROM blog_post")
#        return db.session.execute(sql).scalars().all()  # Returns just the integers
class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    emails   = db.relationship('Email', backref='user', cascade="all, delete-orphan",lazy=True)
    
class Email(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    email   = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='CASCADE'),  nullable=False)
















# class User(db.Model):
#     id          = db.Column(db.Integer, primary_key=True)
#     username    = db.Column(db.Text, nullable=False)
#     email       = db.Column(db.Text, unique=True, nullable=False)
# 	##WARNING: SECURITY: Do NOT store a password like this: just for play here
#     password    = db.Column(db.Text, nullable=False)
#     created_at  = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)