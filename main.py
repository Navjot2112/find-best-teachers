import mysql.connector
from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)
connection = None
cursor = None
try:
    # Establish connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="jandu@2003",
        database="sys"
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # SQL query to retrieve rows of a particular feature
        # sql_query = f"SELECT * FROM sys.yt_teachers WHERE channel_title = '{channel_title}'"
        sql_query = "SELECT DISTINCT channel_title FROM sys.yt_teachers"

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Extract channel title from the rows
        channel_title = list(set(row[0] for row in rows))

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)

finally:
    # Close cursor and connection if they are defined and connected
    if cursor is not None:
        cursor.close()   
    if connection is not None and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")  

@app.route("/")
def hello_world():
    return render_template('jandu.html')



@app.route("/retrieve")
def retrieve():
    data=channel_title
    return render_template('course.html',data=data)
@app.route("/subject")
def subject():
    connection = None
    cursor = None
    rows = []
    title=request.args.get('title')

    try:
        # Establish connection to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jandu@2003",
            database="sys"
        )

        if connection.is_connected():
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # SQL query to retrieve rows with the title "Operating System"
            sql_query = f"SELECT * FROM sys.yt_teachers WHERE channel_title ='{title}'"

            # Execute the SQL query
            cursor.execute(sql_query)

            # Fetch all rows
            rows = cursor.fetchall()

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)

    finally:
        # Close cursor and connection if they are defined and connected
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
        print("Rows:", rows)  # Add this line for debugging 
        for row in rows:
            print(row)
        return render_template('subject.html',row=rows)
@app.route("/online")
def online():
    return render_template('online.html')    

if __name__ == "__main__":
    app.run(debug=True, port=5000)

        
