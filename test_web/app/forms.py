# -*- coding: UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, SelectField, TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms.fields.html5 import DateField
from wtforms import ValidationError
import sys

#datachoice = [('100010','Type ABCD'),('100100', 'Type G'),('100110', 'Type H')]

def encodechinese(chinese):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    return chinese.encode('utf-8')

def test():
    #This is just a test for github.    



