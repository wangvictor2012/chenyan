import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '1a-2b-3c-$!'

#MYSQL_HOST = '172.16.1.181'
#MYSQL_HOST = '172.16.17.23'
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = 'root'
MYSQL_PASS = 'wang123456'
#MYSQL_USER = 'admin'
#MYSQL_PASS = 'fangling'
MYSQL_DB = 'chenyan'

'''
#ImagefileSrc = '/var/www/qrcode/app/static/img/'
ImagefileSrc = 'D:\\Etudiant\\Test\\qrcode\\app\\static\\img\\'
#JsTypecodeIndexSrc = '/var/www/qrcode/app/static/js/TypecodeIndex.js'
JsTypecodeIndexSrc = 'D:\\Etudiant\\Test\\qrcode\\app\\static\\js\\TypecodeIndex.js'
#JsMaterialSerialIndexSrc = '/var/www/qrcode/app/static/js/Material_serial_Index.js'
JsMaterialSerialIndexSrc = 'D:\\Etudiant\\Test\\qrcode\\app\\static\\js\\Material_serial_Index.js'
#ErrorlogSrc = '/var/www/qrcode/tmp/error.log'
ErrorlogSrc = 'D:\\Etudiant\\Test\\qrcode\\tmp\\error.log'
#JsERPinfoSrc = '/var/www/qrcode/app/static/js/ERP_info.js'
JsERPinfoSrc = 'D:\\Etudiant\\Test\\qrcode\\app\\static\\js\\ERP_info.js'

ERPDownloadSrc = 'D:\\Etudiant\\Git_place\\qrcode\\app\\static\\files\\'
'''