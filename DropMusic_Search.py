import psycopg2
import sys

class search:

    def searchMusicByName(value):
        
        conn = None
        try:
            cmd=""" select * from musica where titulo like '%%' """  
            sql=cmd[:]
                #se não resultar,
                #sql = """ select * from musica where titulo like '%'""" + value + """'%' """
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (value))
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

    def searchMusicById(value):
        
        conn = None
        try:
            sql=""" select * from musica
                    where musica_id = %s"""  ###### COMITS???
                #se não resultar,
                #sql = """ select * from album where titulo like '%'""" + value + """'%' """
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (value))
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
                
    def searchMusicByArtistName(value): #######CHECK SQL
        
        conn = None
        try:
            sql = """ select titulo, musica_id, duracao, papel, artista_artistaid, nome
            from funcao_na_musica, musica, artista
            where funcao_na_musica.musica_musica_id=musica.musica_id AND
            funcao_na_musica.artista_artistaid=artista.artistaid AND
            artista.nome like '%%s%' """      
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (value))
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

    def searchMusicByArtistId(value): #######CHECK SQL
        
        conn = None
        try:
            sql = """ select titulo, musica_id, duracao, papel, artista_artistaid, nome
            from funcao_na_musica, musica, artista
            where funcao_na_musica.musica_musica_id=musica.musica_id AND
            funcao_na_musica.artista_artistaid=artista.artistaid AND
            funcao_na_musica.artistaid = %s """      
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (value))
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
    
    def searchMusicByAlbum(value): #######CHECK SQL, não sei é necessário fazer com join
        
        conn = None
        try:
            sql = """ select musica.titulo, musica_id, duracao, posicao, album_titulo, album_data_lancamento
            from posicao_alb_mus, musica, album
            where posicao_alb_mus.musica_musica_id=musica.musica_id AND
            posicao_alb_mus.album_titulo=album.titulo AND
            posicao_alb_mus.album_data_lancamento=album.data_lancamento AND
            album.titulo like '%%s%' """      
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (value))
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
                
    def searchMusicByGenero(value): #######CHECK SQL, não sei é necessário fazer com join
        
        conn = None
        try:
            sql = """ select titulo, musica_id, duracao, genero_genero
            from musica, genero_musica
            where genero_musica.musica_musica_id=musica.musica_id AND
            genero_musica.genero_genero=genero.genero_genero AND
            genero.genero like '%%s%' """
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (value))
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
                
    def searchMusicByData(value):
        
        conn = None
        try:
            sql=""" select * from musica
                    where data_lancamento like %s"""  ###### COMITS???
                #se não resultar,
                #sql = """ select * from album where titulo like '%'""" + value + """'%' """
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            date=datetime.date(value)
            cur.execute(sql, (date))
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
    
    
    def searchMusicByPontuacao(value): #######CHECK SQL, não sei é necessário fazer com join
        
        conn = None
        try:
            sql = """ select musica.titulo, musica_id, duracao, pontuacao from musica, album x, posicao_alb_mus,critica c
            where posicao_alb_mus.musica_musica_id=musica_id and 
            posicao_alb_mus.album_titulo=x.titulo AND posicao_alb_mus.album_data_lancamento=x.data_lancamento and
            x.titulo=c.album_titulo AND x.data_lancamento=c.album_data_lancamento 
            group by musica_id, pontuacao
            having avg(c.pontuacao) =  %s """      
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (value))
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
    
    def searchMusicByLetra(value): #######CHECK SQL, não sei é necessário fazer com join
        
        conn = None
        try:
            sql = """ select titulo, musica_id, duracao, letra
            from musica
            where letra like '%%s%'"""      
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (value))
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
   
