import psycopg2

class uploads:

    def showUploadsDetailsPerUser(user):
            #CHECKKKKKKKKKKKKK
            sql = """select nome, user_username, musica_musicaid,titulo 
            from upload, musica
            where user_username=%s
            and musica.musicaid=upload.musica_musicaid"""
            shown=False

            try:

                conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="postgres")
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

#    def showUploads(user):
#        sql = """select nome, musica_musica_id from uploads where user_username=%s"""
#        shown=False
#
#        try:
#
#            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
#            # create a new cursor
#            cur = conn.cursor()
#            # execute the INSERT statement
#            cur.execute(sql, (user,))
#            # commit the changes to the database
#            row = cur.fetchone()
#            while row is not None:
#                print( row ) ##------------------------------------------------------------------------
#                row = cur.fetchone()
#                shown=True
## close communication with the database
#            cur.close()
#
#
#
#        except (Exception, psycopg2.DatabaseError) as error:
#            print(error)##-------------------------------------------------------------------------------------------
#            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
#        finally:
#            if conn is not None:
#                conn.close()
#                return shown
##################################################################################################################3
#    def getMusicUpload(user):
#        sql = """select musica_musica_id, titulo from upload, musica
#             where user_username=%s and upload.musica_musicaid=musica.musicaid"""
#        shown=False
#
#        try:
#
#            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="1234")
#            # create a new cursor
#            cur = conn.cursor()
#            # execute the INSERT statement
#            cur.execute(sql, (user,))
#            # commit the changes to the database
#            row = cur.fetchone()
#            shown=True
#            while row is not None:
#                print( row ) ##------------------------------------------------------------------------
#                row = cur.fetchone()
#                shown=True
## close communication with the database
#            cur.close()
#
#        except (Exception, psycopg2.DatabaseError) as error:
#            print(error)##-------------------------------------------------------------------------------------------
#            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
#        finally:
#            if conn is not None:
#                conn.close()
#                return shown

    def shareUpload(user,idM,userIdShare): 
        sqlAdd= ("""INSERT INTO user_upload
        VALUES(%s,%s,%s)""")
        
        try:
            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="postgres")
            # create a new cursor
            cur = conn.cursor()
            cur.execute(sqlAdd, (userIdShare,user, idM))
            conn.commit()
            print('foi partilhado com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
                
    def addUpload(user, idM, userIdShare='', tipo_ficheiro='',nome='', ficheiro=''):
        sqlCreate = """INSERT INTO upload
             VALUES(%s,%s,%s,%s,%s)"""
        sqlAdd= ("""INSERT INTO user_upload
             VALUES(%s,%s,%s)""")


        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="postgres")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sqlCreate, (ficheiro,nome,tipo_ficheiro,user,idM))
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.execute(sqlAdd, (userIdShare,user, idM))
            conn.commit()

            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()
    
#    def updateUpload(user, idM): ##########ALTERAR
#        sqlMusica= """update upload set musica_musica_id = %s where user_username = %s and"""
#        sql= """INSERT INTO posicaoplaylist
#             VALUES(%s,%s,%s,%s)"""
#
#
#        try:
#
#            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="postgres")
#            cur = conn.cursor()
#            cur.execute(sqlMusica, (idM,user))
#            row = cur.fetchone()   
#            cur.execute(sql, (row[0],nome,user, idM))
#            conn.commit()
#
#            print('as alteracoes foram guardadas com sucesso!')
#            cur.close()
#
#        except (Exception, psycopg2.DatabaseError) as error:
#            print(error)##-------------------------------------------------------------------------------------------
#            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
#        finally:
#            if conn is not None:
#                conn.close()
  
    def listUsersShared(user,idM):
        
        sql = """select user_username from user_upload
        where upload_user_username = %s and upload_music_musica_id"""
        try:

            conn = psycopg2.connect(host="localhost",database="musicas", user="postgres", password="postgres")
            cur = conn.cursor()
            cur.execute(sql, (user, idM))
            conn.commit()

            print('as alteracoes foram guardadas com sucesso!')
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)##-------------------------------------------------------------------------------------------
            print ('Algo correu mal :( /n tentaremos resolver o problema no futuro')
        finally:
            if conn is not None:
                conn.close()