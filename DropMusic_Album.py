import psycopg2
import sys


class DropMusic_Album:

    def listaAlbum():
        """ query data from the album and critica table """

        conn = None
        sql="""SELECT album.titulo, album.data_lancamento, round(avg(coalesce(pontuacao)),1)
                FROM album LEFT JOIN critica c
                ON (album.titulo=c.album_titulo AND album.data_lancamento=c.album_data_lancamento)
                GROUP BY album.titulo, album.data_lancamento""" 
        
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


    def showDetails(idA):
        """query data about the album and its details as well as criticisms"""

        conn = None
        shown=False
        sql="""select album.*, round(avg(coalesce(pontuacao)),1) FROM album LEFT JOIN critica c
                ON ( album.data_lancamento=c.album_data_lancamento AND album.titulo=c.album_titulo) where data_lancamento=%s
                AND titulo=%s group by album.titulo, album.data_lancamento""" 


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idA[1],idA[0]))   
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


    def listMusic(idA):
        """shows musics within an album - returns a boolean that indicates whether the musics are currently being shown"""

        conn = None
        shown=False
        sql=""" select posicao, musica.titulo, duracao from posicao_alb_mus, musica
                where posicao_alb_mus.musica_musica_id=musica_id
                AND album_data_lancamento=%s AND album_titulo=%s """
        try:
 
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idA[1],idA[0]))   
            row = cur.fetchone()         

            while row is not None:
                print( row )
                row = cur.fetchone()
            shown=True
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error) ##--------------------------------------------------------------------------------
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                return shown

    def listComents(idA):
        """lists the coments of a certain album"""

        conn = None
        sql="""  select user_username, pontuacao, comentario from critica
            WHERE album_data_lancamento=%s AND album_titulo=%s """  

        try:   
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idA[1],idA[0]))   
            row = cur.fetchone()

            while row is not None:
                print( row ) ##------------------------------------------------------------------------
                row = cur.fetchone()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')

        finally:
            if conn is not None:
                conn.close()

    def addComent(comment, idA, credentials):
        conn = None                                       ##### por aqui qq coisa para seele ja comentou antes alterar pontuacao ou dar msg de erro

        try:
            sql="""  insert into critica
            Values (%s , %s, %s, %s, %s) """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (comment[0], comment[1], credentials, idA[0], idA[1]) )
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-----------------------------------------------------------------------------------
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()

    def listArtistsInAlbum(idA):
        conn = None
        try:
            sql="""  select artista.nome from artista, artista_album where artista_artistaid=artistaid AND album_titulo=%s AND album_data_lancamento=%s """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idA[0],idA[1]))   
            row = cur.fetchone()
            print('Artistas: \n')
            while row is not None:
                print( row )
                row = cur.fetchone()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()

        
    def alterValue(op,new,idA):
        
        conn = None
        try:
            cmd=""" update album set =%s where data_lancamento=%s and titulo=%s """ 
            sql= cmd[:18]+op+cmd[18:]
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (new,idA[1],idA[0]))
            conn.commit()
            print('saved')
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
    def verifyA(idA):
        conn = None
        try:
            sql="""  select artistaid
            from artista
            where artistaid=%s """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idA,))   
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

    def updateMusicAlbum(album,idM):
        sqlPosicao= """Select max(posicao)+1 from posicao_alb_mus where album_data_lancamento=%s and album_titulo=%s"""
        sql= """INSERT INTO posicao_alb_mus
             VALUES(%s,%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sqlPosicao, (album[1],album[0]))
            row = cur.fetchone()
            if row[0] == 'null':
                cur.execute(sql, (row[0],idM,album[0],album[1]))
            else:
                cur.execute(sql, (1,idM,album[0],album[1]))

            conn.commit()

            print('as alteracoes foram guardadas com sucesso!')
            
                
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def listGenreInAlbum(album):
        sql="""select distinct genero_genero from genero_musica gen, musica, posicao_alb_mus pos
        WHERE gen.musica_musica_id=musica_id and pos.musica_musica_id=musica_id and album_data_lancamento=%s and album_titulo=%s"""
        try:
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (album[1],album[0]))   
            row = cur.fetchone()
            while row is not None:
                print( row )
                row = cur.fetchone()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()

    def addAlbum(titulo, data, estudio, editora):
        """ insert a new album into the album table """
        conn = None

        try:
            sql="""INSERT INTO album VALUES(%s,%s,%s,%s)"""
            
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (titulo, data, estudio, editora))
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

    def addAlbumMusica(posicao, titulo,data,musica):
        sql = """INSERT INTO posicao_alb_mus                     
             VALUES(%s,%s,%s,%s)"""##############################################THIS DOESNT LOOK OK


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (posicao, musica,titulo, data))
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
    def addAlbumArtista(titulo,data,artista):
        sql = """INSERT INTO artista_album
             VALUES(%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (artista,titulo, data))
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


    def removeAlbumArtista(titulo,data,artista):
        sql = """Delete from artista_album
             where artista_artistaid=%s and album_data_lancamento=%s and album_titulo=%s"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (artista, data,titulo))
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
                
    def getIdA( posicao, idA):
        sql = """select musica_musica_id from posicao_alb_mus
             where album_data_lancamento=%s and album_titulo=%s and posicao= %s"""
        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (idA[1],idA[0],posicao))
            # commit the changes to the database
            row = cur.fetchone()   
            return row[0]
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()


    def deleteMusica(posicao, idA):
        sql = """Delete from posicao_alb_mus
             where album_titulo=%s and album_data_lancamento=%s and posicao= %s"""
        sqlP="""Update posicao_alb_mus SET posicao= posicao-1 where album_titulo=%s and album_data_lancamento=%s and posicao> %s"""
        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (idA[0],idA[1],posicao))
            # commit the changes to the database
            conn.commit()
            cur.execute(sqlP, (idA[0],idA[1],posicao))
            # commit the changes to the database
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
