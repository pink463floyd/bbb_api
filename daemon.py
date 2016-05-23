import psycopg2

conn = psycopg2.connect("dbname='django' user='djangouser' host='127.0.0.1' password='dbpass'")
cur = conn.cursor()
cur.execute("""SELECT * from api_trips""")
rows = cur.fetchall()

for row in rows:
    #print "   ", row[0], row[1], row[2], row[3], row[4]
    print row


cur = conn.cursor()
update="UPDATE api_trips SET delay = 3;"
cur.execute(update)
conn.commit();


cur = conn.cursor()
cur.execute("""SELECT * from api_trips""")
rows = cur.fetchall()

for row in rows:
    #print "   ", row[0], row[1], row[2], row[3], row[4]
    print row

