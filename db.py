import mysql.connector

# Database configuration
db_config = {
    'host': '',         # Localhost means your MySQL server is on your local machine
    'port': '',         # MySQL's default port
    'user': '',     # Replace with your MySQL username
    'password': '', # Replace with your MySQL password
    'database': '' # Your specific database name
}

# Function to create a connection to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to display available tables
def display_tables(cursor):
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("\nAvailable Tables:")
    for idx, table in enumerate(tables, 1):
        print(f"{idx}. {table[0]}")

# Function to fetch data from a specific table
def fetch_data_from_table(cursor, table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    results = cursor.fetchall()
    
    print(f"\nDisplaying records from the '{table_name}' table:")
    for row in results:
        print(row)

# Function to display the menu and execute user choice
def menu():
    connection = connect_to_database()
    if connection is None:
        return
    
    cursor = connection.cursor()

    while True:
        print("\n==== Database Menu ====")
        print("1. View Available Tables")
        print("2. Fetch Data from a Table")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            display_tables(cursor)
        elif choice == '2':
            display_tables(cursor)
            table_choice = input("\nEnter the number of the table to fetch data from: ")
            try:
                table_choice = int(table_choice)
                tables = cursor.fetchall()
                if 1 <= table_choice <= len(tables):
                    fetch_data_from_table(cursor, tables[table_choice - 1][0])
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    
    cursor.close()
    connection.close()

# Run the menu
if __name__ == "__main__":
    menu()
