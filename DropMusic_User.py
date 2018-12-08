class DropMusic_User:
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
