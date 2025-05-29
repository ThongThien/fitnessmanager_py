class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/pydb_new'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://thongthien2004:YourPassword@thongthien2004.mysql.pythonanywhere-services.com/thongthien2004$duan_db_py'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
