__author__ = 'adwant'
import re
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='test')

hand = open('mytest.txt','r+')
hand.next()
hand.next()
hand.next()

try:
    cursor = cnx.cursor()

    cursor.execute(""" select max(test_instance_id) from test_instance """)
    number = cursor.fetchone()
    k = ', '.join(map(str, number))
    k = int(k) + 1
    print(k)


    for line in hand:
        line = line.rstrip()
        if re.search('-', line) :
            str = line.strip().strip(' ')
            str = str.split(' ',1)
            print(str)
            key = str[0].strip('-')
            value = str[1].strip(' ')
            cursor.execute("""
                insert into test_argument (test_instance_id,arg_name,arg_desc) values (%s,%s,%s)""",
                           (k,key, value)
                           )
finally:
    cnx.commit()
    cnx.close()

print("Inserted Successfully")
