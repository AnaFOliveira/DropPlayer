import psycopg2
import sys


class interface:

## tlvz ter metodo get conn e adaptar os outro metodos tds para o chamarem
    
    def checkPassword(cred):
        """authenticates login"""
        usern=cred[0]
        passw=cred[1]
        conn = None
        valid=False

        try:

            #connects to data base
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()

            # selects user with the give username
            cur.execute("SELECT password FROM users WHERE username= (%s) ", (usern,))
            row = cur.fetchone()

            #Verifys if the user exists and if the password is correct
            if (row!=None and row[0]==passw): #
                valid=True
            else:
                print('As suas credenciais estão incorretas')
                
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error) #A APAGAR NO FUTURO!!!! ----------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')

        finally:
            if conn is not None:
                conn.close()                                       
                return valid


    def validate(cred):
        """verifys if a new user regist is valid"""

        usern=cred[0]
        passw=cred[1]
        conn = None 
        valid=False

        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            # selects a user with the same username as the input
            cur.execute("SELECT username FROM users WHERE username= (%s) ", (usern,))
            row = cur.fetchone()

            #if such a user exists the regist is not valid
            if row!=None:
                print('já existe um utilizador com esse nome :( ')
            elif usern=='' or passw=='': ### WHAT IF THEY TYPE '  '
                print('A pass e user não podem ser nulos!')
            else: 
                valid=True      
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:

            print(error) #A APAGAR NO FUTURO!!!!-------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')

        finally:
            if conn is not None:
                conn.close()
            return valid



    def insert_user(user):
        """ insert a new user into the users table """

        sql = """INSERT INTO users(username, password, editor)
             VALUES(%s,%s,%s)"""
        usern=user[0]
        passw=user[1]

        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (usern, passw, 'false'))
            # commit the changes to the database
            conn.commit()
            print('ja esta registado!')
            # close communication with the database
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()


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
        sql="""select album.*, round(avg(coalesce(pontuacao)),1) from album, critica c
                where album.data_lancamento=c.album_data_lancamento AND album.titulo=c.album_titulo AND data_lancamento=%s
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
                print( shown) ### UNUSED!!!!!!!!!!!!!!!!!!!!!!!!!

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

##### devemos preocupar nos que o editor salte posicoes nos concertos ou albuns???? OU QUE DATA LANCAMENTO MUSICA < QUE A DO ALBUM?


    def edits(user):
        conn = None
        editor=False
        try:
            sql="""  select editor from users where username= %s """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (user,))   
            row = cur.fetchone()
            editor=row[0]
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                return editor

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
            cmd=""" update album set =%s where data_lancamento=%s and titulo=%s """  ###### COMITS???
            sql= cmd[:18]+op+cmd[18:]
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (new,idA[1],idA[0]))
            print('saved')
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                

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
            cmd=""" update musica set =%s where musica=%s """  ###### COMITS???
            sql= cmd[:14]+op+cmd[14:]
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (new,idM))
            print('saved')
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

    def verifyG(genero):
        conn = None
        try:
            sql="""  select genero
            from genero
            where genero=%s """  
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (genero,))   
            row = cur.fetchone()
            if row is not None:
                return True
                print('this is a genre')
            else:
                return False
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

    def addArtist(nome, bio):
        """ insert a new album into the album table """
        conn = None

        try:
            sql="""INSERT INTO artista VALUES(%s,%s, default)"""
            sqlId="""select artistaid from artista where nome=%s and biografia=%s"""

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (nome, bio))
            # commit the changes to the database
            conn.commit()
            cur.execute(sqlId, (nome, bio))
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


    def addBand(nome,bio, band, idAr):
        """ insert a new album into the album table """
        conn = None

        try:
            sql="""INSERT INTO banda VALUES(%s,%s,%s,%s,%s,%s)"""

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (nome,bio, idAr,band[1], band[0], band[2]))
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
    def addBandArtista(papel, dataE, dataS, idAr, artista):
        """ insert a new album into the album table """
        conn = None

        try:
            sql="""INSERT INTO artista_na_banda VALUES(%s,%s,%s,%s,%s)"""

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (papel, dataE, dataS, idAr, artista))
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

    def addMusico(nome, bio, artista0, artista1, artista2, idAr):
        """ insert a new album into the album table """
        conn = None

        try:
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            
            if artista1=='null':
                sql="""INSERT INTO musico (nome,biografia, data_nascimento, data_obito, local_nascimento, artistaid) VALUES(%s,%s,%s,null,%s,%s)"""
                cur.execute(sql, (nome, bio, artista0, artista2, idAr))

            else:
                sql="""INSERT INTO musico (nome,biografia, data_nascimento, data_obito, local_nascimento, artistaid) VALUES(%s,%s,%s,%s,%s,%s)"""
                cur.execute(sql, (nome, bio, artista0, artista1, artista2, idAr))

           
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
        
    def addAlbumMusica(posicao, titulo,data,musica):
        sql = """INSERT INTO artista_album
             VALUES(%s,%s,%s,%s)"""


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

    def addAMucicGenre(idM,genero):
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


        
##############################################################################################################################################################################3333
    def showPlaylistsPerUser(user):

        sql = """select nome, user_username from playlist where user_username='a' or publica=True"""
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


    def showPlaylists(user):
        sql = """select nome from playlist where user_username='a'"""
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
    def getList(user,nome):
        sql = """select posicao, titulo from posicaoplaylist, musica
             where playlist_user_username=%s and playlist_nome=%s and musica_musica_id= musica_id"""
        shown=False

        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
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
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
                return shown

    def getId(posicao, nome, user):
        sql = """select musica_musica_id from posicaoplaylist
             where playlist_user_username=%s and playlist_nome=%s and posicao= %s"""
        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (user,nome,posicao))
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

                
    def createList(user, nome, idM, publica):
        sqlCreate = """INSERT INTO playlist
             VALUES(%s,%s,%s)"""
        sqlAdd= ("""INSERT INTO posicaoplaylist
             VALUES(1,%s,%s,%s)""")


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
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
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
    
    def updateList(user, nome, idM):
        sqlPosicao= """Select max(posicao)+1 from posicaoplaylist """
        sql= """INSERT INTO posicaoplaylist
             VALUES(%s,%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sqlPosicao, (nome,user))
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

    def setAdmin(user):
        sql= """ Update users SET editor=True WHERE username= %s"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (user,))
            conn.commit()

            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

####    def deleteAlbum(idA):
####        sql= """ Delete from album WHERE titulo=%s AND data_lancamento= %s"""
####
####
####        try:
####
####            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
####            cur = conn.cursor()
####            cur.execute(sql, (idA[0],idA[1]))
####            conn.commit()
####
####            print('as alteracoes foram guardadas com sucesso!')
####            cur.close()
####
####        except (Exception, psycopg2.DatabaseError) as error:
####            print(error)##-------------------------------------------------------------------------------------------
####            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
####        finally:
####            if conn is not None:
####                conn.close()

    def updateMusicAlbum(album,idM):
        sqlPosicao= """Select max(posicao)+1 from posicao_alb_mus """
        sql= """INSERT INTO posicao_alb_mus
             VALUES(%s,%s,%s,%s)"""


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sqlPosicao, (album[0],album[1]))
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
