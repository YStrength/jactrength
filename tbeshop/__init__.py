import pymysql
#原来测试django模型的时候使用了另一种db，需要显式切换
pymysql.install_as_MySQLdb()