class DropMusic_artista:

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
