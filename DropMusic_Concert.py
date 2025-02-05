import psycopg2
import sys

class DropMusic_Concerto:

    def addConcert(titulo, data, localizacao):
        conn = None

        try:
            sql="""INSERT INTO concerto VALUES(%s,%s,%s, default)"""
            sqlId="""select concertoid from concerto where tour=%s and data=%s and localizacao=%s"""

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
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
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def addConcertArtista(posicao,idC,idArtista):
        sql = """INSERT INTO numerodeatuacao
             VALUES(%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (posicao,idC, idArtista))
            # commit the changes to the database
            conn.commit()
            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def getPosition(concerto):
        conn = None

        try:
            sql="""select coalesce(max(posicao)+1,1) from posicaonoconcerto where concerto_concertoid=%s"""

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            cur.execute(sql, (concerto))
            # commit the changes to the database
            row=cur.fetchone()
            return row[0]
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
    def addConcertMusic(posicao, idC,idMusica):
        sql = """INSERT INTO posicaonoconcerto
             VALUES(%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (posicao, idC, idMusica))
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()


    def deleteMusica(posicao,idM, concerto):
        sql = """Delete from posicaonoconcerto
             where musica_musica_id=%s and concerto_concertoid=%s"""
        sqlP="""Update posicaonoconcerto SET posicao= posicao-1 where concerto_concertoid=%s and posicao> %s"""
        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the  statement
            cur.execute(sql, (idM, concerto))
            # commit the changes to the database
            conn.commit()
            cur.execute(sqlP, (concerto,posicao))
            # commit the changes to the database
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
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
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idC))   
            row = cur.fetchone()
            if row is not None:
                return True
            else:
                return False
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                
    def listaConcertos(): 
        """ query data from the artists"""

        conn = None
        sql="""SELECT *
                FROM concerto """
                
        try:
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
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
                
    def showDetailsConcerto(idC): 
    
        conn = None
        shown=False
        sql="""select * from concerto
                where concertoid=%s""" 
    
        try:
    
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idC))   
            row = cur.fetchone()
            while row is not None:
                print( row )
                row = cur.fetchone()
            shown=True
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                return shown    
            
    def alterConcertDetails(op,new,idC): 
        conn = None
        try:
            cmd="""update concerto set =%s where concertoid=%s """  
            sql= cmd[:20]+op+cmd[20:]
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (new,idC))
            conn.commit()
            print('saved')
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close() 
    def listArtistsInConcerts(idC):
        
        conn = None
        shown=False
        sql="""select numero_atuacao, nome  from numerodeatuacao, artista
                where artista_artistaid=artistaid and concerto_concertoid=%s""" 
    
        try:
    
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idC))   
            row = cur.fetchone()
            while row is not None:
                print( row )
                row = cur.fetchone()
            shown=True
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                return shown    
    def listMusicsInConcerts(idC):
        
        conn = None
        shown=False
        sql="""select posicao, titulo  from posicaonoconcerto, musica
                where musica_musica_id=musica_id and concerto_concertoid=%s""" 
    
        try:
    
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idC))   
            row = cur.fetchone()
            while row is not None:
                print( row )
                row = cur.fetchone()
            shown=True
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                return shown    



    def addConMusica(idC,idM):

        sqlPosicao= """Select coalesce(max(posicao)+1,1) from posicaonoconcerto where concerto_concertoid=%s and musica_musica_id=%s"""
        sql= """INSERT INTO posicaonoconcerto
             VALUES(%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sqlPosicao, (idC, idM))
            row = cur.fetchone()   
            cur.execute(sql, (row[0],idC, idM))
            conn.commit()

            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def addConArtista(idC,artista):
        sqlPosicao= """Select coalesce(max(numero_atuacao)+1,1) from numerodeatuacao where concerto_concertoid=%s and artista_artistaid=%s"""
        sql= """INSERT INTO numerodeatuacao
             VALUES(%s,%s,%s)"""

        try:
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sqlPosicao, (idC, artista))
            row = cur.fetchone()   
            cur.execute(sql, (row[0],idC, artista))
            conn.commit()

            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()


    def deleteMusicaC(posicao, idC,idM):
        sql = """Delete from posicaonoconcerto
             where concerto_concertoid=%s and musica_musica_id=%s and posicao= %s"""
        sqlP="""Update posicaonoconcerto SET posicao= posicao-1 where concerto_concertoid=%s and musica_musica_id=%s and posicao> %s"""
        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (idC,idM,posicao))
            # commit the changes to the database
            conn.commit()
            cur.execute(sqlP, (idC,idM,posicao))
            # commit the changes to the database
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()  
    def deleteArtistaC(posicao, idC,idA):
        sql = """Delete from numerodeatuacao
             where concerto_concertoid=%s and artista_artistaid=%s and numero_atuacao= %s"""
        sqlP="""Update numerodeatuacao SET numero_atuacao= numero_atuacao-1 where concerto_concertoid=%s and artista_artistaid=%s and numero_atuacao> %s"""
        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (idC,idA,posicao))
            # commit the changes to the database
            conn.commit()
            cur.execute(sqlP, (idC,idA,posicao))
            # commit the changes to the database
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()  
