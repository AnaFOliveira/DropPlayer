import psycopg2
import sys

class DropMusic_Concerto:
    def addConcert(titulo, data, localizacao):
        """ insert a new album into the album table """
        conn = None

        try:
            sql="""INSERT INTO concerto VALUES(%s,%s,%s, default)"""
            sqlId="""select concertoid from concerto where tour=%s and data=%s and localizacao=%s"""

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (data, titulo, localizacao))
            # commit the changes to the database
            conn.commit()
            cur.execute(sqlId, (titulo, data, localizacao))
            row=cur.fetchone()
            return row[0]
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def addConcertArtista(posicao,idC,idArtista):
        sql = """INSERT INTO numerodeatuacao
             VALUES(%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (posicao,idC, idArtista))
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def getPosition(concerto):
        conn = None

        try:
            sql="""select coalesce(max(posicao)+1,1) from posicaonoconcerto where concerto_concertoid=%s"""

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (concerto))
            # commit the changes to the database
            row=cur.fetchone()
            return row[0]
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
    def addConcertMusic(posicao, idC,idMusica):
        sql = """INSERT INTO posicaonoconcerto
             VALUES(%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (posicao, idC, idMusica))
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()


    def deleteMusica(posicao,idM, concerto):
        sql = """Delete from posicaonoconcerto
             where musica_musica_id=%s and concerto_concertoid=%s"""
        sqlP="""Update posicaonoconcerto SET posicao= posicao-1 where concerto_concertoid=%s and posicao> %s"""
        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (idM, concerto))
            # commit the changes to the database
            conn.commit()
            cur.execute(sqlP, (concerto,posicao))
            # commit the changes to the database
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
