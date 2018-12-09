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
 def verifyC(idC):
        conn = None
        try:
            sql="""  select id
            from concerto
            where concertoid=%s """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idC))   
            row = cur.fetchone()
            if row is not None:
                return True
            else:
                return False
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                
    def listaConcertos(): #Shows list of every details of concerts
        """ query data from the artists"""

        conn = None
        sql="""SELECT *
                FROM concerto """
                ##ON (album.titulo=c.album_titulo AND album.data_lancamento=c.album_data_lancamento)
                ##GROUP BY album.titulo, album.data_lancamento""" 
        try:
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql)   
            row = cur.fetchone()

            while row is not None:
                print( row )
                row = cur.fetchone()
                
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()
                
    def showDetailsConcerto(idC): #Search artist !!!!!!!!!!!!!!!!!!!!!!!!!!!
        """query data about the artist and its details as well as criticisms"""
    
        conn = None
        shown=False
        sql="""select *, from concerto
                where concertoid=%s
                group by concerto.tour""" 
    
        try:
    
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idC))   
            row = cur.fetchone()
            while row is not None:
                print( row )
                row = cur.fetchone()
            shown=True
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##----------------------------------------------------------------------------------
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                return shown    
            
    def alterConcertDetails(op,new,idC): #ver se o . faz o efeito (selecionar aquele atributo)
        conn = None
        try:
            cmd="""update concerto. set =%s where concertoid=%s """  ###### COMITS???
            sql= cmd[:15]+op+cmd[15:]
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (new,idC))
            print('saved')
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close() 
