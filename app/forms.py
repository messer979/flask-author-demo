# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, DataRequired

class LoginForm(FlaskForm):
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])

class RegisterForm(FlaskForm):
	name        = StringField  (u'Name'      )
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])
	email       = StringField  (u'Email'     , validators=[DataRequired(), Email()])


class AuthorForm(FlaskForm):
	pen_name	= StringField  (u'Pen Name'	 , validators=[DataRequired()])
	first_name	= StringField  (u'First Name'      )
	last_name	= StringField  (u'Last Name'      )
	adress		= StringField  (u'Address'      )
	phone		= StringField  (u'Phone'      )
	email 		= StringField  (u'Email'	, validators=[DataRequired(), Email()])
	social_number = StringField  (u'Social #'      )
	withholding_tax = BooleanField  (u'Witholding'      )