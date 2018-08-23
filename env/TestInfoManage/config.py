import os
#密钥
SECRET_KEY=os.urandom(24)
DEBUG=True
# DEBUG=False
CMS_USER_ID = 'sessionid'
#数据库配置
DB_USERNAME='root'
DB_PASSWORD='123456'
DB_PORT='3306'
DB_HOST='127.0.0.1'
DB_NAME='testinfomanage'

DB_URI='mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATION=False

