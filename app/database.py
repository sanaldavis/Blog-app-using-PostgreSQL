import psycopg2 as lite
con=None
con=lite.connect(database='chackobhavan')
cur=con.cursor()
cur.execute('''CREATE TABLE blog_database( id serial, author text, post text, day text, time text, comment text)''')
con.commit()
con.close()

