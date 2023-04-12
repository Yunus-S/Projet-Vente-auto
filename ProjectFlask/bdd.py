import uuid
import app
import mysql.connector
import datetime
import crypt


def user_signup():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    uid = str(uuid.uuid4())
    query = "INSERT INTO users VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s )"
    mdpcrypte = crypt.crypt_mdp(app.request.form['motdepasse'])
    region = get_region_number()
    print(mdpcrypte)
    val = (uid, app.request.form['nom'], app.request.form['prenom'], app.request.form['adresse'], app.request.form['telephone'], app.request.form['mail'], app.request.form['status'], region, app.request.form['login'],mdpcrypte)

    cursor.execute(query, val)

    cnx.commit()
    cnx.close()


def get_region_number():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()
    query = "SELECT idregion FROM region WHERE nomregion = %s"
    val = (app.request.form['region'],)
    cursor.execute(query, val)

    result = cursor.fetchall()

    return result[0][0]

    cnx.commit()
    cnx.close()


def user_login():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = ("SELECT password FROM users WHERE login = %s")
    val = (app.request.form['log_user_id'],)
    cursor.execute(query, val)

    result = cursor.fetchall()

    if not result:
        return 0
    else :
        if crypt.match_mdp(app.request.form['log_user_password'], result[0][0])==True :
            return 1
        else :
            return 0


    cnx.commit()
    cnx.close()


def user_exist_check() :
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = ("SELECT login FROM users WHERE login = %s")
    val = (app.request.form['login'],)
    cursor.execute(query, val)

    result = cursor.fetchall()
    print (result)

    if not result :
        return 1
    else :
        return 0

    cnx.commit()
    cnx.close()


def user_director_check(username):
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = ("SELECT status FROM users WHERE login = %s")
    val = (username,)
    cursor.execute(query, val)

    result = cursor.fetchall()

    return result[0][0]

    cnx.commit()
    cnx.close()

def users():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = ("SELECT * FROM users")
    cursor.execute(query)

    result = cursor.fetchall()

    return result

    cnx.commit()
    cnx.close()


def delete_users():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = ("DELETE FROM users WHERE idusers = %s")
    val = (app.request.form['user_id'],)
    cursor.execute(query, val)

    cnx.commit()
    cnx.close()

def savereport():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = "INSERT INTO rapportdevisite VALUES (null, %s ,%s ,%s ,%s ,%s ,%s)"
    date_actuelle = datetime.date.today()
    heure_actuelle = datetime.datetime.now().time()
    heure_formatee = heure_actuelle.strftime("%H:%M")
    id = app.request.form.get('id')
    val = (id, date_actuelle, heure_formatee, app.request.form['frais'], app.request.form['resultat'], app.request.form['observation'])
    cursor.execute(query, val)

    cnx.commit()
    cnx.close()


def visitlist():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = ("SELECT * FROM listvisite")
    cursor.execute(query)

    result = cursor.fetchall()
    return result

    cnx.commit()
    cnx.close()


def visit(id):
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = ("SELECT * FROM visite WHERE idlistvisite = %s")
    val = (id, )
    cursor.execute(query, val)

    result = cursor.fetchall()
    return result

    cnx.commit()
    cnx.close()


def getrapport():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = ("SELECT * FROM rapportdevisite")
    cursor.execute(query, )

    result = cursor.fetchall()
    return result

    cnx.commit()
    cnx.close()
