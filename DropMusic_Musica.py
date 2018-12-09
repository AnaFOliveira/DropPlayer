import psycopg2
import sys
class DropMusic_Musica:

    def showingMusic(idM):
        conn = None
        shown=False
        try:
            sql="""  select musica.titulo, letra, musica.data_de_lancamento, duracao, album_titulo, album_data_lancamento, posicao 
            from musica, posicao_alb_mus e where e.musica_musica_id=musica.musica_id AND e.musica_musica_id=%s """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idM,))   
            row = cur.fetchone()
            while row is not None:
                print( row )
                row = cur.fetchone()
                shown=True
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                return shown

    def listgenres(idM):
        conn = None
        try:
            sql="""  select genero_genero
            from genero_musica where musica_musica_id=%s """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idM,))   
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


    def listArtistsInMusic(idM):
        conn = None
        try:
            sql="""  select artista.nome, papel 
                from funcao_na_musica, artista
                where artistaid=artista_artistaid AND musica_musica_id=%s """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idM,))   
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


    def listConcertsInMusic(idM):
        conn = None
        try:
            sql="""  select tour, posicao
            from concerto, posicaonoconcerto
            where concerto_concertoid=concertoid AND musica_musica_id=%s """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idM,))   
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

    def alterMusicValue(op,new,idM):
        conn = None
        try:
            cmd="""update musica set =%s where musica_id=%s """  ###### COMITS???
            sql= cmd[:18]+op+cmd[18:]
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (new,idM))
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()

    def verifyM(idM):
        conn = None
        try:
            sql="""  select musica_id
            from musica
            where musica_id=%s """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idM,))   
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


    def addMusic(titulo, data, duracao, letra):
        """ insert a new album into the album table """
        conn = None

        try:
            sql="""INSERT INTO musica VALUES(%s,%s,%s, default, %s)"""
            sqlId="""select musica_id from musica where letra=%s and data_de_lancamento=%s and duracao=%s and titulo=%s"""

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (letra, data, titulo, duracao))
            # commit the changes to the database
            conn.commit()
            cur.execute(sqlId, (letra, data, duracao, titulo))
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

    def addMusicArtista(idM,funcao,artista):
        sql = """INSERT INTO funcao_na_musica
             VALUES(%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (funcao, artista,idM))
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

    def removeMusicArtista(idM, artista):
        sql = """Delete from funcao_na_musica
             where artista_artistaid=%s and musica_musica_id=%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (funcao, artista,idM))
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

    def addAMusicGenre(idM,genero):
        sql = """INSERT INTO genero_musica
             VALUES(%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (genero, idM))
            # commit the changes to the database
            conn.commit()
            print('done')
            # close communication with the database
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def removeMusicGenre(idM,gen):
        sql = """Delete from genero_musica
             VALUES(%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (genero, idM))
            # commit the changes to the database
            conn.commit()
            print('done')
            # close communication with the database
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()


    def listMusic():
        conn = None
        shown=False
        try:
            sql="""  select musica.titulo, duracao, musica_id 
            from musica """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql)   
            row = cur.fetchone()
            while row is not None:
                print( row )
                row = cur.fetchone()
                shown=True
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                return shown


                
