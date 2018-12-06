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

        try:
            sql="""  select user_username, pontuacao, comentario from critica
            WHERE album_data_lancamento=%s AND album_titulo=%s """  
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
            from musica, posicao_alb_mus e where e.musica_musica_id=musica.musica_id AND e.musica_musica_id=%i """  
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
            from genero_musica where musica_musica_id=%i """  
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
                where artistaid=artista_artistaid AND musica_musica_id=%i """  
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
            where concerto_concertoid=concertoid AND musica_musica_id=%i """  
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
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres")
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
            where musica_id=%i """  
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
    def verifyA(idA):
        conn = None
        try:
            sql="""  select musica_id
            from artista
            where artistaid=%i """  
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
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
