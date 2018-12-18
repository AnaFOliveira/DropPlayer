import psycopg2
import sys

class DropMusic_Genero:
    def addGenero(gen):
        """ insert a new genero into the generos table """

        sql = """INSERT INTO genero
        VALUES(%s)"""
        
        try:

            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (gen,))
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()

    def verifyG(genero):
        conn = None
        try:
            sql="""  select genero
            from genero
            where genero=%s """  
            conn = psycopg2.connect(host="localhost",database="musicabd", user="postgres", password="1234")
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
            print('Passou-se algo de errado! Volte a tentar')
        finally:
            if conn is not None:
                conn.close()
