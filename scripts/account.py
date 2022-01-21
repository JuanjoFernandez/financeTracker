import sqlite3
import os
from datetime import date
from datetime import datetime as dt
from stat import SF_APPEND

class Account:
    """
    Expects an array of parameters according to the number of columns in the
    "accounts" database.

    """
    
    # Class variables
    
    def __init__(self, account_info) -> None:
        self.account_info = account_info

    def create(self):
        # Database parameters
        path = os.path.join('databases', 'accounts.db')
        connection = sqlite3.connect(path)
        cursor = connection.cursor()

        # Creates the query
        values_holder = ""
        column_number = 8
        for column in range(column_number):
            values_holder += '?,'
        values_holder = values_holder[:-1]
        query = f"INSERT INTO accounts * VALUES ({values_holder});"

        cursor.execute(query, self.account_info)

        connection.close()

    def modify(self):
        pass

    def update_balance(self, amount):
        pass
        
def get_account_info():
    # Database parameters
    path = os.path.join('databases', 'accounts.db')
    connection = sqlite3.connect(path)
    cursor = connection.cursor()

# Getting the next id
    query = 'SELECT id FROM accounts WHERE id=(SELECT max(id) FROM accounts);'
    cursor.execute(query)
    id_array = cursor.fetchone()
    current_id = id_array[0] + 1

# Getting number and name of columns
    query = "PRAGMA table_info('accounts');"
    cursor.execute(query)
    columns_info = cursor.fetchall()
    column_number = len(columns_info)

# Getting the account information
    account_info = []
    for item in range(column_number):
        
        # Getting the account id automatically
        if columns_info[item][1] == 'id':
            print (f"The id for the new account will be: {current_id}")
            account_info.append(current_id)

        # Getting the date of creation, if blank use current date
        elif columns_info[item][1] == 'dateCreated':
            date_str = input("Please provide the date of account creation (MM/DD/YYYY), leave blank to use today's date:")
            if not date_str:
                print(dt.strftime(date.today(), "%m/%d/%Y"))
    
        else:
            account_info.append\
                (input(f"Please provide account {columns_info[item][1]}, expects a(n) {columns_info[item][2]}: "))

    connection.close

    return account_info

# Create the account and update the database
new_account = Account(get_account_info())






