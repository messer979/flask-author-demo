# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app         import db
from flask_login import UserMixin

class User(UserMixin, db.Model):

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))

    def __init__(self, user, email, password):
        self.user       = user
        self.password   = password
        self.email      = email

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 

class Auteur(UserMixin, db.Model):
    pen_name       = db.Column(db.String(50),     primary_key=True)
    last_name     = db.Column(db.String(30),  unique = True)
    first_name    = db.Column(db.String(30), unique = True)
    adress = db.Column(db.String(100))
    phone = db.Column(db.String(10))
    email = db.Column(db.String(50))
    social_number = db.Column(db.String(15))
    withholding_tax = db.Column(db.Boolean)

    def __init__(self, pen_name, last_name, first_name, adress, phone, email, social_number, withholding_tax):
        self.pen_name   = pen_name
        self.last_name  = last_name
        self.first_name = first_name
        self.adress = adress
        self.phone  = phone
        self.email  = email
        self.social_number  = social_number
        self.withholding_tax    = withholding_tax

    # def __repr__(self):
    #     return str(self.id) + ' - ' + str(self.user)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 
