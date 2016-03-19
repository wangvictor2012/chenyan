# -*- coding: UTF-8 -*-
from flask import render_template, flash, redirect, request, url_for, g, send_from_directory
from flask.ext.login import login_required, login_user, current_user, logout_user, session
from app import app, login_manager, db
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from forms import LoginForm, RegisterForm
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
import MySQLdb

'''
@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
'''
@app.route('/')
def begin():
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    cursor = db.cursor()
    form = LoginForm()
    error_message = []
    if not form.login.data:
        validate_code()
    print session['validate']
    if form.login.data:
        userphone = str(request.form.get('form-userphone'))
        password = str(request.form.get('form-password'))
        validate = str(request.form.get('form-validation'))
        
        if validate.upper() in session['validate'].upper():
            sql = "SELECT * FROM user_info where USERID = '%s' and PASS_WORD = '%s' limit 1" %(userphone, password)
            res = cursor.execute(sql)
            cursor.close()
            if res:
                return redirect(url_for('get_code'))
            else:
                error_message = [u"用户名或密码输入错误，请重新输入。。。"]

        else:
            error_message = [u"验证码输入有误，请重新输入。。。"]

    if form.register.data:
        return redirect(url_for('register'))

    if form.visitor.data:
        return redirect(url_for('visitor'))
        
    return render_template('login.html', form = form, error_message = error_message, validate_code=session['validate'])


@app.route('/get_code', methods = ['GET', 'POST'])
#@login_required
#flag_return: 0:查询按钮提交后结果（未选择产品） 1, 正常程序; 2, 询问是否注册，返回是; 3, 已注册返回标志
def get_code():
    return render_template('get_code.html')


def validate_code():
    lib_code = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',\
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    code = ''
    for t in range(10):
        code+=lib_code[random.randint(0, 35)]
    session['validate'] = code


@app.route('/register', methods = ['GET', 'POST'])
#@login_required
#flag_return: 0:查询按钮提交后结果（未选择产品） 1, 正常程序; 2, 询问是否注册，返回是; 3, 已注册返回标志
def register():
    form = RegisterForm()
    error_message = []
    if not form.register.data:
        validate_code()
    if form.validate_on_submit():
        if form.register.data:
            validate_message = form.Validate.data
            print validate_message, session['validate']
            if validate_message.upper() in session['validate'].upper():
                studentid = form.StudentID.data
                userphoe = form.UserPhone.data
                password = form.PassWord1.data

                print studentid, userphoe, password
            else:
                error_message = [u"验证码输入错误.."]
    else:
        print 'Not validate'
        print form.errors

    return render_template('register.html',form=form, error_message = error_message, validate_code=session['validate'])

@app.route('/vistor', methods = ['GET', 'POST'])
#@login_required
#flag_return: 0:查询按钮提交后结果（未选择产品） 1, 正常程序; 2, 询问是否注册，返回是; 3, 已注册返回标志
def vistor():
    return render_template('vistor.html')



