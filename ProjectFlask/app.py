from flask import Flask
from flask import abort, redirect, url_for, render_template
from flask import request
import bdd
from flask import session


# https://flask.palletsprojects.com/en/1.1.x/quickstart/


app = Flask(__name__)
app.secret_key = '_5#ax2L"FaQ4z\n\xec]/'

# Page d'accueil du site.
# Par exemple : http://127.0.0.1:5000/


@app.route('/home')
def home():

    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck=='Director' :
            return render_template('homeadm.html')
        return render_template('home.html')
    else:
        return redirect(url_for('index'))


@app.route('/new_user', methods=['POST'])
def newuser():
    exist_check = bdd.user_exist_check()
    if exist_check == 1:
        bdd.user_signup()
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck == 'Director':
            return redirect(url_for('new_user'))
        return redirect(url_for('index'))
    else:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck == 'Director':
            return redirect(url_for('new_user'))
        return redirect(url_for('index'))


@app.route('/login')
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    else :
        return render_template('login.html')


@app.route('/user_login', methods=['GET','POST'])
def user_login():
    log = bdd.user_login()
    if log == 1:
        session['username'] = request.form['log_user_id']
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    return "Vous n'êtes pas connecté. <br><a href = '/login'>" + "Cliquez ici pour vous connecter</a>"


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/visitlist')
def visitlist():
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        list = bdd.visitlist()
        if ck == 'Director':
            return render_template('visitlistadm.html', lists = list)
        return render_template('visitlist.html', lists = list)
    else:
        return redirect(url_for('index'))


@app.route('/detailledlist')
def detailledlist():
    id_list = request.args.get('list_id')
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        list = bdd.visit(id_list)
        if ck == 'Director':
            return render_template('listdetailadm.html', lists = list)
        return render_template('listdetail.html', lists = list)
    else:
        return redirect(url_for('index'))


@app.route('/visitingreport')
def visitingreport():
    id_visit = request.args.get('visit_id')
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck == 'Director':
            return render_template('visitingreportadm.html', id=id_visit)
        return render_template('visitingreport.html', id=id_visit)
    else:
        return redirect(url_for('index'))


@app.route('/reportlist')
def reportlist():
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        rep = bdd.getrapport()
        if ck == 'Director':
            return render_template('lirapportadm.html', report=rep)
        return render_template('lirapport.html', report=rep)
    else:
        return redirect(url_for('index'))


@app.route('/visitingreport', methods=['POST'])
def reportsave():
    bdd.savereport()
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck == 'Director':
            return render_template('visitingreportadm.html')
        return redirect(url_for('visitingreport.html'))
    else:
        return redirect(url_for('index'))

@app.route('/ordering')
def ordering():
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck == 'Director':
            return render_template('orderingadm.html')
        return render_template('ordering.html')
    else:
        return redirect(url_for('index'))


@app.route('/profile')
def profile():
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck == 'Director':
            return render_template('profileadm.html')
        return render_template('profile.html')
    else:
        return redirect(url_for('index'))


@app.route('/administration')
def administration():
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck == 'Director':
            return render_template('administration.html')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/new_user')
def new_user():
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck == 'Director':
            return render_template('new_user.html')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete_user')
def delete_user():
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck == 'Director':
            user = bdd.users()
            return render_template('delete_user.html',users = user)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete_user', methods=['POST'])
def deluser():
    bdd.delete_users()
    us = session.get('username')
    ck = bdd.user_director_check(us)
    if ck == 'Director':
        return redirect(url_for('delete_user'))
    return redirect(url_for('index'))

@app.route('/disable_user')
def disable_user():
    if 'username' in session:
        us = session.get('username')
        ck = bdd.user_director_check(us)
        if ck == 'Director':
            return render_template('disable_user.html')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()