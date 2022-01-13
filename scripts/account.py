import sqlite3
import os

class Account:
    """
    Expects an array of parameters according to the number of columns in the
    "accounts" database.

    """
    
    # Class variables
    
    def __init__(self, account_info) -> None:
        self.account_info = account_info

    def create(self):
        
        pass

    def modify(self):
        pass

    def update_balance(self, amount):
        pass
        
path = os.path.join('databases', 'accounts.db')
connection = sqlite3.connect(path)
cursor = connection.cursor()

# Getting the next id
query = 'SELECT id FROM accounts WHERE id=(SELECT max(id) FROM accounts);'
cursor.execute(query)
id_array = cursor.fetchone()
current_id = id_array[0] + 1

# Getting number of columns
query = "PRAGMA table_info('accounts');"
cursor.execute(query)
columns_info = cursor.fetchall()
column_number = len(columns_info)

connection.close