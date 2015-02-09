# -*- coding:utf-8-*-

from flask import Flask, render_template, request, make_response, url_for, session, g, redirect, abort, flash
from flask.ext.mysql import MySQL
from werkzeug.security import check_password_hash, generate_password_hash
import json
# import time
# from datetime import datetime

# configuration
DEBUG = True
SECRET_KEY = 'Teamlab_Double_j_2015'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASK EXAMPLE_SETTINGS', silent=True)

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'YOUR_PASSWORD'
app.config['MYSQL_DATABASE_PASSWORD'] = '198214'
app.config['MYSQL_DATABASE_DB'] = 'double_j'
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
    print 'g.db :', (g.db)

    data = g.db.fetchall()
    print 'data :', data
    rv = [dict((g.db.description[idx][0], value)
               for idx, value in enumerate(row)) for row in data]
    return (rv[0] if rv else None) if one else rv


def get_user_id(UserID):
    """Convenience method to look up the id for a username."""
    return query_db('select UserID from User where UserID = %s', [UserID], one=True)
    print query_db()


@app.before_request
def before_request():
    print ("Start Application")
    db_connect = connect_db()
    db_connect.autocommit(1)

    g.db = db_connect.cursor()
    print type(g.db)
    g.user = None
    if 'user_id' in session:
        g.user = query_db('select * from User where UserID = %s', [session['user_id']], one=True)
    print 'g.user :', g.user
    # print 'user_id :', session['user_id']
    # session['user_id'] = None


@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/')
def index():
    # if not g.user:
    # return redirect(url_for('login'))
    return redirect(url_for('to_main'))


@app.route('/main')
def to_main():
    return render_template('main.html')


@app.route('/register')
def to_register_user():
    return render_template('register.html')

@app.route('/mypage')
def to_mypage():
    return render_template('mypage.html')

@app.route('/findID')
def to_find_id():
    return render_template('find_ID.html')

@app.route('/findPassword')
def to_find_password():
    return render_template('find_password.html')


@app.route('/login')
def to_login():
    return render_template('login.html')

@app.route('/posting')
def to_posting():
    return render_template('posting.html')

@app.route('/registerUser', methods=["POST"])
def insert_new_user():
    if g.user:
        return redirect(url_for('to_main'))
    error=None
    if request.method == 'POST':

        id = request.form['UserID']
        password = generate_password_hash(request.form['UserPassword'])
        email = request.form['UserEmail']
        nickname = request.form['UserNickname']
        password_check_1 = request.form['UserPassword']
        password_check_2 = request.form['UserPassword_2']



        if not id:
            error = 'Please input the ID'

        elif not password:
            error = 'Please input the Password'

        elif password_check_1 != password_check_2:
            error = 'Please input again Password check'

        elif not nickname:
            error = 'Please input the Nickname'

        elif not email or \
                        '@' not in email:
            error = 'Please input the Email'

        elif get_user_id(id) is not None:

            error = 'The ID is already exists. Please input another ID'
        else:
            g.db.execute('''insert into User (
                UserID, UserEmail, UserPassword, UserNickname) values (%s, %s, %s, %s)''',
                         [id, email, password, nickname])
            # flash('Thank you for registration. Now you can login')
            return redirect(url_for('to_main'))

    return render_template('register.html', error=error)

@app.route('/check_login', methods=["POST"])
def login_check():
    if request.method == "POST":

        user = query_db('''select * from User where UserID = %s''', [request.form['UserID']], one=True)
        print 'user :', user

        if user is None:
            error = 'Invalid username'
        elif not check_password_hash(user['UserPassword'], request.form['UserPassword']):
            error = 'Invalid password'
        else:
            session['user_id'] = user['UserID']
            return redirect(url_for('to_main'))

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    print "a"
    """Logs the user out."""
    session.pop('user_id', None)
    return redirect(url_for('to_main'))


@app.route('/serverdata')
def transferdata():
    if not g.user:
        return redirect(url_for('login'))

    json_data = query_db('''select name, servername, serverip, id, email from user''')
    return json.dumps(json_data)

@app.route('/deleteUser', methods=["POST"])
def delete_user_ajax():
    if request.method == "POST":
        email = request.form['email']
        print '''DELETE FROM user WHERE email=%s''', [email]

        g.db.execute('''DELETE FROM user WHERE email=%s''', [email])
    return "Success"


if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)
