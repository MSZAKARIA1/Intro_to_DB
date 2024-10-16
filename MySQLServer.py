import mysql.connector

def create_database():
    try:
        # Create a connection to the MySQL server
        conn_object = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="3Obcure@!995"
        )

        # Declare a cursor object and store it in a variable
        cursor_object = conn_object.cursor()

        # Try to create the database
        cursor_object.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Print the error message in case of failure
        print(f"Error: {err}")

    finally:
        # Close the cursor and the connection if they were opened
        if cursor_object:
            cursor_object.close()
        if conn_object:
            conn_object.close()

# Run the function to create the database
if __name__ == "__main__":
    create_database()
