import mysql.connector

conn = mysql.connector.connect(user='root', password="asdfghjkl;'", database='test', use_unicode=True)
cursor = conn.cursor()

# cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
# cursor.execute('INSERT INTO user (id, name) VALUES (%s, %s)', ['1', 'Michael'])
# print cursor.rowcount;

# conn.commit()
# cursor.close()

cursor = conn.cursor()

cursor.execute('SELECT * FROM user WHERE id = %s' % '1')

values = cursor.fetchall()

print values
cursor.close()
