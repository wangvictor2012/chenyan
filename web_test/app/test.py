# -*- coding: cp936 -*-
'''
import MySQLdb

MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = 'root'
MYSQL_PASS = 'wang123456'
MYSQL_DB = 'chenyan'

db = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER ,passwd=MYSQL_PASS,db=MYSQL_DB,charset='utf8')
cursor = db.cursor()

sql = "SELECT * FROM user_info where USERID = '%s' and PASS_WORD = '%s' limit 1" %('0260', '*Iamlock-221')
res = cursor.execute(sql)
#res= cursor.fetchall()


print res
'''

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('D:\Etudiant\chenyan\web_main\app\static\fonts\ARIALNI.TTF', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg');
