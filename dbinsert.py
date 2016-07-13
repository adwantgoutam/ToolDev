__author__ = 'adwant'
import mysql.connector

print("Into this file")

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)


hand = open('temp','r+')
print("Again Into this file")
try:
    cursor = cnx.cursor()

    cursor.execute(""" select max(test_instance_id) from test_instance """)
    number = cursor.fetchone()
    k = ', '.join(map(str,number))
    k = int(k)+1
    print(k)
    for line in hand:
        line = line.rstrip()
        key, value = line.split(None,1)
        print(key)
        print(value)
        cursor.execute("""
                 insert into test_argument (test_instance_id,arg_name,arg_desc) values (%s,%s,%s)""",
                (k,key,value)
                           )

finally:
        cnx.commit()
        cnx.close()

print("Inserted successfully")






