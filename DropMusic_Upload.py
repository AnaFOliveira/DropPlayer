import psycopg2
import sys

class uploads:

    def showUploadsDetailsPerUser(user):

            sql = """select nome, user_username, musica_musicaid from upload where user_username=%s"""
            shown=False

            try:

                conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
                # create a new cursor
                cur = conn.cursor()
                # execute the INSERT statement
                cur.execute(sql, (user))
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

    def  addUpload(user, idM, ficheiro='', nome='', tipo_ficheiro=''):
        sql = """INSERT INTO upload
                VALUES (%s,%s,%s,%s,%s)"""
        
        try:
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (ficheiro,nome,tipo_ficheiro, user, idM))
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
                
