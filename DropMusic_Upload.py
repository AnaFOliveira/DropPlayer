import psycopg2
import sys

class uploads:

    def showUploadsDetailsPerUser(user):

            sql = """select nome, user_username, musica_musicaid from upload where user_username=%s"""
            shown=False

            try:

                conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
                # create a new cursor
                cur = conn.cursor()
                # execute the INSERT statement
                cur.execute(sql, (user))
                # commit the changes to the database
                row = cur.fetchone()
                while row is not None:
                    print( row ) ##------------------------------------------------------------------------
                    row = cur.fetchone()
                    shown=True
    # close communication with the database
                cur.close()

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)##-------------------------------------------------------------------------------------------
                print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
            finally:
                if conn is not None:
                    conn.close()
                    return shown

    def showUploads(user):
        sql = """select nome, musica_musica_id from uploads where user_username=%s"""
        shown=False

        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (user,))
            # commit the changes to the database
            row = cur.fetchone()
            while row is not None:
                print( row ) ##------------------------------------------------------------------------
                row = cur.fetchone()
                shown=True
# close communication with the database
            cur.close()



        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
                return shown
##################################################################################################################3
    def getListUploads(user):
        sql = """select musica_musica_id from upload
             where user_username=%s"""
        shown=False

        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (user,))
            # commit the changes to the database
            row = cur.fetchone()
            shown=True
            while row is not None:
                print( row ) ##------------------------------------------------------------------------
                row = cur.fetchone()
                shown=True
# close communication with the database
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
                return shown

    def shareUpload(user,idM,userIdShare):
        sqlAdd= ("""INSERT INTO user_upload
        VALUES(%s,%s,%s)""")
        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            cur.execute(sqlAdd, (userIdShare,user, idM))
            conn.commit()
            print('foi partilhado com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
                
    def addUpload(user, idM, userIdShare='', tipo_ficheiro='',nome='', ficheiro=''):
        sqlCreate = """INSERT INTO upload
             VALUES(%s,%s,%s,%s,%s)"""
        sqlAdd= ("""INSERT INTO user_upload
             VALUES(%s,%s,%s)""")


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sqlCreate, (ficheiro,nome,tipo_ficheiro,user,idM))
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.execute(sqlAdd, (userIdShare,user, idM))
            conn.commit()

            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
    
    def updateUpload(user, idM):
        sqlPosicao= """update upload set musica_musica_id = %s where user_username = %s """
        sql= """INSERT INTO posicaoplaylist
             VALUES(%s,%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sqlPosicao, (idM,user))
            row = cur.fetchone()   
            cur.execute(sql, (row[0],nome,user, idM))
            conn.commit()

            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
  

