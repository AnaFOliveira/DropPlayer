
import psycopg2
import sys
class DropMusic_artista:

    def addArtist(nome, bio):
        """ insert a new album into the album table """
        conn = None

        try:
            sql="""INSERT INTO artista VALUES(%s,%s, default)"""
            sqlId="""select artistaid from artista where nome=%s and biografia=%s"""

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (nome, bio))
            conn.commit()
            print('saved')
            cur.execute(sqlId, (nome, bio))
            row=cur.fetchone()
            return row[0]
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def addBand(banda , fim, idAr):
        """ insert a new album into the album table """
        conn = None
        try:            

            conn= psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur= conn.cursor()
            if fim=='null':
                sql="""INSERT INTO banda VALUES(%s,%s,null,%s)"""
                cur.execute(sql, (  banda[1], banda[0],idAr))

            else:
                sql="""INSERT INTO banda VALUES(%s,%s,%s,%s)"""
                cur.execute(sql, ( banda[1], banda[0], banda[2],idAr))

            conn.commit()
            print('saved')
            
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
                              
    def listaArtists(): #Shows list of every artist 

        conn = None
        sql="""SELECT *
                FROM artista """
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
            print('ocorreu um problema :(')

        finally:
            if conn is not None:
                conn.close()
                
    def listaMusico(): 

        conn = None
        sql="""SELECT *
                FROM musico """
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
            print('ocorreu um erro :(')
        finally:
            if conn is not None:
                conn.close()
                
    def listaBandas(): #Shows list of every artist 

        conn = None
        sql="""SELECT *
                FROM banda """
 
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
            print('ocorreu um erro :(')

        finally:
            if conn is not None:
                conn.close()

    def showDetailsArtist(idAr): 
    
        conn = None
        shown=False
        sql="""select artista.* from artista
                where artistaid=%s""" 
    
        try:
    
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idAr))   
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

    def removeArtist(idAr,art):
        conn = None
        try:
            cmd="""delete from artista_na_banda where banda_artista_artistaid=%s and artista_artistaid=%s"""  
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(cmd, (idAr,art))
            conn.commit()
            print('saved')
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
                
    def alterArtistDetails(op,new,idAr):
        conn = None
        try:
            cmd="""update artista set =%s where artistaid=%s """  
            sql= cmd[:19]+op+cmd[19:]
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (new,idAr))
            conn.commit()
            print('saved')
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
    def alterMusicoDetails(op,new,idAr):
        conn = None
        try:
            cmd="""update musico set =%s where artistaid=%s """  
            sql= cmd[:18]+op+cmd[18:]
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (new,idAr))
            conn.commit()
            print('saved')
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()


    def alterBandDetails(op,new,idAr):
        conn = None
        try:
            cmd="""update banda set =%s where artistaid=%s """  
            sql= cmd[:17]+op+cmd[17:]
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (new,idAr))
            conn.commit()
            print('saved')
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
            
                
    def addBandArtista(papel, dataE, dataS, idAr, artista):
        """ insert a new album into the album table """
        conn = None

        try:
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()

            if dataS=='null':
                sql="""INSERT INTO artista_na_banda VALUES(%s,%s,null,%s,%s)"""
                cur.execute(sql, (papel, dataE, idAr, artista))
            else:
                sql="""INSERT INTO artista_na_banda VALUES(%s,%s,%s,%s,%s)"""
                cur.execute(sql, (papel, dataE, dataS, idAr, artista))
            
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def addMusico( artista0, artista1, artista2,idAr):
        conn = None

        try:
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            
            if artista1=='null':
                sql="""INSERT INTO musico ( data_nascimento, data_obito, local_nascimento, artistaid) VALUES(%s,null,%s,%s)"""
                cur.execute(sql, ( artista0, artista2,idAr))

            else:
                sql="""INSERT INTO musico ( data_nascimento, data_obito, local_nascimento, artistaid) VALUES(%s,%s,%s,%s)"""
                cur.execute(sql, ( artista0, artista1, artista2,idAr))

           
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:

            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def verifyA(idA):
        conn = None
        try:
            sql="""  select artistaid
            from artista
            where artistaid=%s """  
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idA,))   
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
    def getType(idAr):
        conn = None
        try:
            sql="""  select artistaid
            from banda
            where artistaid=%s """  
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idAr,))   
            row = cur.fetchone()
            if row is None:
                return False
            else:
                return True
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
    def listMembers(idAr):
        conn = None
        try:
            sql="""  select *
            from artista_na_banda
            where banda_artista_artistaid=%s """  
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql, (idAr,))   
            row = cur.fetchone()
            while row is not None:
                print( row )

                row = cur.fetchone()
            cur.close()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()

    def detailBandas(idAr): #Shows list of every artist 
        """ query data from the artists"""

        conn = None
        sql="""SELECT *
                FROM banda Where artistaid=%s"""
                
        try:
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql,(idAr,))   
            row = cur.fetchone()

            while row is not None:
                print( row )
                row = cur.fetchone()
                
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print('ocorreu um erro')

        finally:
            if conn is not None:
                conn.close()
    def detailMusico(idAr): 

        conn = None
        sql="""SELECT *
                FROM musico Where artistaid=%s"""
                
        try:
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            cur = conn.cursor()
            cur.execute(sql,(idAr,))   
            row = cur.fetchone()

            while row is not None:
                print( row )
                row = cur.fetchone()
                
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print('ocorreu um erro')

        finally:
            if conn is not None:
                conn.close()
