import psycopg2

def Team(id, first_name, last_name, phone, email):
	conn = psycopg2.connect("dbname=app user=postgresSQL")
	cur = conn.cursor()

	cur.execute("CREATE TABLE person (id int PRIMARY KEY, first_name, last_name, phone, email")
	VALUES ('%s', '%s', '%s', '%s'); %"))" 

	conn.commit()
	cur.close
	conn.close()
