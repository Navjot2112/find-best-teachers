import mysql.connector
from mysql.connector import Error

def check_database_connection():
    connection = None
    cursor = None

    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jandu@2003",
            database="sys"  # Update this with your actual database name
        )

        # Check if the connection is successful
        if connection.is_connected():
            print("Successfully connected to the database")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print(f"Connected to database: {db_name[0]}")
            
            # Optionally, list tables
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            print("Tables in the database:", tables)

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        # Close cursor and connection if they are defined and connected
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Run the function to check database connection
check_database_connection()
