
from flask import Flask , render_template, request, redirect
from flaskext.mysql import MySQL
#import mysql.connector
#from flask_mysqldb import MySQL
#import pymysql

app = Flask(__name__)
#app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] ='root'
app.config['MYSQL_DATABASE_DB'] = 'calsoft'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)
mysql = MySQL(app)

#db = app.config("localhost", "root", "root", "calsoft")
#db = sql.connect(host = '',port = 3306,user = 'root',passwd = 'root',database = 'calsoft')

@app.route("/" ,methods=['GET', 'POST'])
def create_table():
   if request.method == 'POST':
      userDetails = request.form

      name = userDetails['name']

      email = userDetails['email']

      #cur = mysql.connection.cursor()
      conn = mysql.connect()
      cursor = conn.cursor()

      cursor.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))

      conn.commit()

      cursor.close()

      return 'success'
   return render_template('index.html')

if __name__ == "__main__":
        app.run(debug=True ,host = '0.0.0.0')

