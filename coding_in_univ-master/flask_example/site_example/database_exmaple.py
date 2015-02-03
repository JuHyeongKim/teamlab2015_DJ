from flask import Flask, render_template, request, make_response, url_for, session, g, redirect
from flask.ext.mysql import MySQL
from werkzeug.security import check_password_hash, generate_password_hash
import json


# configuration
DEBUG = True
SECRET_KEY = 'TeamlabTest2015'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASK EXAMPLE_SETTINGS', silent=True)

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'YOUR_PASSWORD'
app.config['MYSQL_DATABASE_PASSWORD'] = 'gachon2014'
app.config['MYSQL_DATABASE_DB'] = 'flask_example'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



def connect_db():
    return mysql.connect()


def init_db():
    """Creates the database tables."""
    db = connect_db()

    with app.open_resource('schema.sql', mode='r') as f:
        sql_statements = " ".join(f.readlines())
        for sql in sql_statements.split(";"):
            if not sql:
                cursor = db.cursor()
                cursor.execute(sql)
                cursor.close()
    db.close()


def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    g.db.execute(query, args)
    print (g.db)

    data = g.db.fetchall()
    print data
    rv = [dict((g.db.description[idx][0], value)
               for idx, value in enumerate(row)) for row in data]
    return (rv[0] if rv else None) if one else rv


@app.before_request
def before_request():
    print ("Start Application")
    db_connect = connect_db()
    db_connect.autocommit(1)

    g.db = db_connect.cursor()
    print type(g.db)
    g.user = None
    if 'user_id' in session:
        g.user = query_db('select * from user where email = %s',
                          [session['user_id']], one=True)


@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def index():
    if not g.user:
        return redirect(url_for('login'))
    return redirect(url_for('server_list'))


@app.route('/register')
def register_user():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registerUser', methods=["POST"])
def insert_new_user():
    if request.method == "POST":
        name = request.form['username']
        id = request.form['userid']
        email = request.form['useremail']
        password = generate_password_hash(request.form['password'])
        print(password)

        g.db.execute('''insert into user (id, name, email, password) values (%s, %s, %s, %s)''', [id, name, email, password])
        return redirect(url_for('login'))

    return "Error"

@app.route('/check_login', methods=["POST"])
def login_check():
    if request.method == "POST":
        user = query_db('''select * from user where email = %s''', [request.form['email']], one=True)

        if user is None:
            error = 'Invalid username'
        elif not check_password_hash(user['password'], request.form['password']):
            error = 'Invalid password'
        else:
            session['user_id'] = user['email']
            return redirect(url_for('server_list'))

        return  render_template('login.html', error=error)

    return "Error"

@app.route('/serverdata')
def transferdata():
    if not g.user:
        return redirect(url_for('login'))
    
    json_data = query_db('''select name, servername, serverip, id, email from user''')
    return json.dumps(json_data)


@app.route('/serverList')
def server_list():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('serverlist.html')


@app.route('/deleteuser',  methods=["POST"])
def delete_user_ajax():
    if request.method == "POST":
        email = request.form['email']
        print '''DELETE FROM user WHERE email=%s''', [email]

        g.db.execute('''DELETE FROM user WHERE email=%s''', [email])
    return  "Success"



@app.route('/base')
def base_test():
    return render_template('base.html')


if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)
