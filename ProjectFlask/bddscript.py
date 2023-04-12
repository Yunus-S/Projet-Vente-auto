import uuid
import app
import mysql.connector
import datetime
import crypt
import random


def getseller():
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = "SELECT idusers FROM users WHERE status != 'Director'"

    cursor.execute(query, )

    result = cursor.fetchall()

    return result

    cnx.commit()
    cnx.close()


def getsellerreg(id):
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = "SELECT idregion FROM users WHERE idusers = %s"
    val = (id,)
    cursor.execute(query, val)

    result = cursor.fetchall()

    return result[0][0]

    cnx.commit()
    cnx.close()


def createlist(id):
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    date = datetime.date.today()
    print(date)
    query = "INSERT INTO listvisite VALUES (%s ,%s ,%s)"
    val=(None,id,date)

    cursor.execute(query, val)

    cnx.commit()
    cnx.close()


def getlist(id):
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()
    datecheck = datetime.date.today()
    query = "SELECT idlistvisite FROM listvisite WHERE date = %s AND iduser = %s"
    val = (datecheck, id)
    cursor.execute(query, val)

    result = cursor.fetchall()
    return result[0][0]

    cnx.commit()
    cnx.close()


def getclient(reg):
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()
    query = "SELECT idclient FROM client WHERE idregion = %s AND status = 'a visiter'"
    val = (reg,)
    cursor.execute(query, val)

    result = cursor.fetchall()
    if result == []:
        return 0

    return result[0][0]

    cnx.commit()
    cnx.close()


def createvisite(idcli,idlist):
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = "INSERT INTO visite VALUES (%s ,%s ,%s, %s, %s, %s)"
    val = (None, idcli, None, None, None, idlist)

    cursor.execute(query, val)

    cnx.commit()
    cnx.close()


def updateclient(idcli):
    cnx = mysql.connector.connect(user='root',
                                  password='merguez',
                                  host='localhost',
                                  database='venteauto')
    cursor = cnx.cursor()

    query = "UPDATE client SET status = 'visite en cours' WHERE idclient = %s"
    val = (idcli, )

    cursor.execute(query, val)

    cnx.commit()
    cnx.close()

#createlist()
#getseller()
