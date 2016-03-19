from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB
import MySQLdb

app = Flask(__name__)
app.config.from_object('config')

db = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER ,passwd=MYSQL_PASS,db=MYSQL_DB,charset='utf8')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

'''
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    #file_handler = RotatingFileHandler('D:/Etudiant/Test/qrcode/tmp/error.log', 'a', 1 * 1024 * 1024, 10)
    file_handler = RotatingFileHandler(ErrorlogSrc, 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.WARNING)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
    app.logger.info('errorlog startup')
'''
from app import views

