from flask import Flask
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify
from flask import flash, request



#app
app = Flask(__name__)
CORS(app)



#config
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = '8KH6ipNhIAbz6dzXDous'
#app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'database-1.catbdoykbe7o.ap-south-1.rds.amazonaws.com'
mysql.init_app(app)
print("connected")
port = 5000



#super-code
@app.route('/')
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("USE Linux;")
        cursor.execute("SELECT name,last from Cp ORDER BY RAND() LIMIT 1")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
