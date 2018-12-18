import psycopg2
import sys


class DropMusic_Playlist:
    ##############################################################################################################################################################################3333
    def showPlaylistsPerUser(user):

        sql = """select nome, user_username from playlist where user_username=%s or publica=True"""
        shown=False

        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
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
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
                return shown


    def showPlaylists(user):
        sql = """select nome from playlist where user_username=%s"""
        shown=False

        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
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
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
                return shown
##################################################################################################################3
    def getList(user,nome):
        sql = """select posicao, titulo from posicaoplaylist, musica
             where playlist_user_username=%s and playlist_nome=%s and musica_musica_id= musica_id"""
        shown=False

        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (user,nome))
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
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
                return shown

    def getId(posicao, nome, user):
        sql = """select musica_musica_id from posicaoplaylist
             where playlist_user_username=%s and playlist_nome=%s and posicao= %s"""
        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (user,nome,posicao))
            # commit the changes to the database
            row = cur.fetchone()   
            return row[0]
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def createList(user, nome, idM, publica): ##############################diferente sem idM
        sqlCreate = """INSERT INTO playlist
             VALUES(%s,%s,%s)"""
        sqlAdd= ("""INSERT INTO posicaoplaylist
             VALUES(1,%s,%s,%s)""")


        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sqlCreate, (nome,publica, user))
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.execute(sqlAdd, (nome,user, idM))
            conn.commit()

            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
    
    def updateList(user, nome, idM):
        sqlPosicao= """Select coalesce(max(posicao)+1,1) from posicaoplaylist Where playlist_nome=%s and playlist_user_username=%s"""
        sql= """INSERT INTO posicaoplaylist
             VALUES(%s,%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sqlPosicao, (nome,user))
            row = cur.fetchone()   
            cur.execute(sql, (row[0],nome,user, idM))
            conn.commit()

            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
    def deleteMusicaP(posicao, nome,user):
        sql = """Delete from posicaoplaylist
             where playlist_user_username=%s and playlist_nome=%s and posicao= %s"""
        sqlP="""Update posicaoplaylist SET posicao= posicao-1 where playlist_user_username=%s and playlist_nome=%s and posicao> %s"""
        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (user,nome,posicao))
            # commit the changes to the database
            conn.commit()
            cur.execute(sqlP, (user,nome,posicao))
            # commit the changes to the database
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()  
