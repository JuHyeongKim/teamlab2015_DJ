from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/cookie', methods=["GET", "POST"])
def cookie_test():

    if request.method == "POST":
        username = request.form['username']
        id = request.form['userid']

        resp = make_response(render_template('cookie.html',  username=username, userid=id))
        resp.set_cookie('username', value=username)
        resp.set_cookie('userid', value=id)

        return resp


    if 'username' in request.cookies:
        username = request.cookies.get('username')
        id = request.cookies.get('userid')

        return render_template('cookie.html', username=username, userid=id)

    return render_template('cookie.html')


if __name__ == "__main__":
    app.run()
