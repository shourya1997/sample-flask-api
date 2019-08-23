import flask
import pymysql as mc
import config

db_name = config.DBNAME
username = config.USERNAME
password = config.PASSWORD
tabel_name = config.TABLE
host = config.HOST

app = flask.Flask(__name__)

def getDBconnection():
    try:
        cnx = mc.connect(host,username,password,db_name)
        return cnx
    except Exception as e:
        print("Error while connecting to DB: {}".format(e))

def insert_query(uid, node_id, api_date, api_time, clid, number):
    cnx = getDBconnection()

    query = "INSERT INTO {table} (uid, node_id, api_date, api_time, clid, input) VALUES('{uid}','{node_id}','{api_date}','{api_time}','{clid}',{number})".format(table=tabel_name,uid=uid, node_id=node_id, api_date=api_date, api_time=api_time, clid=clid, number=number)
    try:
        cursor = cnx.cursor()
        result = cursor.execute(query)
        cnx.commit()
        print("Insetion in DB complete")
    except Exception as e:
        print("Error in insertion:",e)
    finally:
        cnx.close()
        print("DB is closed")


@app.route('/params',methods=['POST'])
def params():
    uid = flask.request.form['uid']
    node_id = flask.request.form['node_id']
    api_date = flask.request.form['date']
    api_time = flask.request.form['time']
    clid = flask.request.form['clid']
    number = flask.request.form['input']

    insert_query(uid,node_id,api_date,api_time,clid,number)

    return 'yo'

if __name__ == "__main__":
    app.run(debug=True)