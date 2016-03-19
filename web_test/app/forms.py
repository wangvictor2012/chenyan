# -*- coding: UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField, BooleanField
from wtforms.validators import Required, Length, EqualTo, Regexp
import sys

class LoginForm(Form):
    login = SubmitField(u'登录')
    register = SubmitField(u'注册')
    visitor = SubmitField(u"游客通道")

class RegisterForm(Form):
    StudentID = IntegerField('StudentID', validators = [Required(message=u"学号不能为空..")])
    UserPhone = StringField('UserPhone', validators = [Required(message=u"手机号不能为空.."), Length(11, message=u"请输入11位有效手机号"),Regexp('[0-9]*$',message=u"手机号必须为11位数字")])
    PassWord1 = PasswordField('PassWord', validators = [Required(message=u"密码不能为空.."), EqualTo('PassWord2',message=u'两次输入密码不匹配')])
    PassWord2 = PasswordField('PassWord', validators = [Required(message=u"确认密码不能为空..")])
    Validate = StringField('Validate', validators = [Required(message=u"验证码不能为空..")])
    register = SubmitField(u'注册')

'''
class UserForm(Form):
    submit = SubmitField(encodechinese("登录"))
    username = TextField('username', validators = [Required()])
    password = PasswordField('username', validators = [Required()])
    

class BomForm(Form):
    submit = SubmitField(encodechinese("查询"))
    calculate = SubmitField(encodechinese("物料汇总"))
    download = SubmitField(encodechinese("下载"))
    bomid = TextField('bomid', validators = [Required()])

class BomForm_Edit(Form):
    newbom = SubmitField(encodechinese("新建 BOM"))
    add = SubmitField(encodechinese("增加"))
    delete = SubmitField(encodechinese("删除"))
    commit = SubmitField(encodechinese("提交"))
    
'''