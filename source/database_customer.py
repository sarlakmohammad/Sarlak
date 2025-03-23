#Copyright (c) 2025 @sarlakmohammad
    #All rights reserved

import sqlite3

class DBCustomer:
    def __init__(self,filename):
        self._db_name = filename
        self.connection = sqlite3.connect(self._db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS db_customer(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company NVARCHAR(50) NOT NULL UNIQUE,
            customer NVARCHAR(50),
            landline VARCHAR(50),
            phone_number VARCHAR(50),
            debt BIGINT(20) DEFAULT 0,
            paid BIGINT(20) DEFAULT 0,
            remain BIGINT(20) DEFAULT 0
        );
        ''')
        self.connection.close()

    def connect_cursor(self):
        self.connection = sqlite3.connect(self._db_name)
        self.cursor = self.connection.cursor()

    def insert_into(self,
                    company:str,
                    customer:str,
                    landline: str,
                    phone_number: str
                    ):
        self.connect_cursor()
        self.cursor.execute('''
            INSERT OR IGNORE INTO db_customer(company,customer,landline,phone_number)
            VALUES(?,?,?,?);
        ''',(company,customer,landline,phone_number))
        self.connection.commit()
        self.connection.close()

    def show_data(self):
        self.connect_cursor()
        self.cursor.execute('''
                    SELECT * FROM db_customer;
                ''')
        _data = self.cursor.fetchall()
        return _data

    def delete_data1(self,customer_id):
        self.connect_cursor()
        self.cursor.execute('''
            DELETE FROM db_customer
            WHERE customer_id = ?;
        ''',(customer_id,))
        self.connection.commit()
        self.connection.close()

    def delete_data2(self,customer):
        self.connect_cursor()
        self.cursor.execute('''
            DELETE FROM db_customer
            WHERE customer = ?;
        ''',(customer,))
        self.connection.commit()
        self.connection.close()

    def delete_data3(self,company):
        self.connect_cursor()
        self.cursor.execute('''
            DELETE FROM db_customer
            WHERE company = ?;
        ''',(company,))
        self.connection.commit()
        self.connection.close()

    def get_data1(self,customer_id):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT * FROM db_customer
            WHERE customer_id = ?;
        ''',(customer_id,))
        _data = self.cursor.fetchone()
        return _data

    def get_data2(self,customer):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT * FROM db_customer
            WHERE customer = ?;
        ''',(customer,))
        _data = self.cursor.fetchone()
        return _data

    def get_data3(self,company):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT * FROM db_customer
            WHERE company = ?;
        ''',(company,))
        _data = self.cursor.fetchone()
        return _data

    def search_data1(self,customer_data):
        self.connect_cursor()
        self.cursor.execute(f'''
            SELECT * FROM db_customer
            WHERE customer LIKE ?;
        ''',(f'%{customer_data}%',))
        _data = self.cursor.fetchall()
        return _data

    def search_data2(self,company_data):
        self.connect_cursor()
        self.cursor.execute(f'''
            SELECT * FROM db_customer
            WHERE company LIKE ?;
        ''',(f'%{company_data}%',))
        _data = self.cursor.fetchall()
        return _data

    def change_data1(self,debt,customer_id):
        self.connect_cursor()
        self.cursor.execute('''
            UPDATE db_customer
            SET debt = debt + ?
            WHERE customer_id = ? AND remain >= 0;
        ''',(debt,customer_id))
        self.cursor.execute('''
            UPDATE db_customer
            SET paid = paid - ?
            WHERE customer_id = ? AND remain < 0 AND ? < paid;
        ''', (debt, customer_id, debt))
        self.cursor.execute('''
            UPDATE db_customer
            SET debt = ? - paid,paid = 0
            WHERE customer_id = ? AND remain < 0 AND ? >= paid;
        ''', (debt, customer_id, debt))
        self.connection.commit()
        self.connection.close()

    def change_data2(self,paid,customer_id):
        self.connect_cursor()
        self.cursor.execute('''
            UPDATE db_customer
            SET paid = paid + ?
            WHERE customer_id = ? AND remain <= 0;
        ''',(paid,customer_id))
        self.cursor.execute('''
            UPDATE db_customer
            SET debt = debt - ?
            WHERE customer_id = ? AND remain > 0 AND ? < debt;
        ''', (paid, customer_id, paid))
        self.cursor.execute('''
            UPDATE db_customer
            SET paid = ? - debt,debt = 0
            WHERE customer_id = ? AND remain > 0 AND ? >= debt;
        ''', (paid, customer_id, paid))
        self.connection.commit()
        self.connection.close()

    def update_data(self,customer_id):
        self.connect_cursor()
        self.cursor.execute('''
            UPDATE db_customer
            SET remain = debt - paid
            WHERE customer_id = ?;
        ''',(customer_id,))
        self.connection.commit()
        self.connection.close()