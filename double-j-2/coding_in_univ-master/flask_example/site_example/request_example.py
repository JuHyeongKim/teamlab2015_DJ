# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/request')
def request_form():
    return render_template('request_form.html')

@app.route('/response', methods=["GET"])
def respons_for_get():
    if request.method == "GET":

        # For Post Method
        # username = request.form['name']
        # email = request.form['email']
        # id = request.form['id']

        # For Get Method
        username =  request.args.get('name', 'Anonymous')
        email = request.args.get('email', 'Anonymous')
        id = request.args.get('id', 'Anonymous')


        result = "Hello " + username + "<br>"+ "Your Email is "+  email+  "<BR>"+  "Your ID is"+  id

        return result

    return "Error"


if __name__ == '__main__':
    app.run(debug=True)