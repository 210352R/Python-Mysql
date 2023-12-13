import mysql.connector

query = " select *  from user;"

try:
    connection = mysql.connector.connect(host='localhost' , database='teacher' , user='root' , password='1234')
    cursor = connection.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    print(result)

    connection.commit()

    print("Methanata wenakm hari ")

    print(result[0][1])

finally:
    if connection.is_connected():
        connection.close()