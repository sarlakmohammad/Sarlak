import sqlite3

class DBContractor:
    def __init__(self,filename):
        self._db_name = filename
        self.connection = sqlite3.connect(self._db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS db_contractor(
            contractor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            contractor NVARCHAR(50) NOT NULL UNIQUE,
            cont_name NVARCHAR(50),
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
                    contractor:str,
                    cont_name:str,
                    landline: str,
                    phone_number: str
                    ):
        self.connect_cursor()
        self.cursor.execute('''
            INSERT OR IGNORE INTO db_contractor(contractor,cont_name,landline,phone_number)
            VALUES(?,?,?,?);
        ''',(contractor,cont_name,landline,phone_number))
        self.connection.commit()
        self.connection.close()

    def show_data(self):
        self.connect_cursor()
        self.cursor.execute('''
                    SELECT * FROM db_contractor;
                ''')
        _data = self.cursor.fetchall()
        return _data

    def delete_data1(self,contractor_id):
        self.connect_cursor()
        self.cursor.execute('''
            DELETE FROM db_contractor
            WHERE contractor_id = ?;
        ''',(contractor_id,))
        self.connection.commit()
        self.connection.close()

    def delete_data2(self,cont_name):
        self.connect_cursor()
        self.cursor.execute('''
            DELETE FROM db_contractor
            WHERE cont_name = ?;
        ''',(cont_name,))
        self.connection.commit()
        self.connection.close()

    def delete_data3(self,contractor):
        self.connect_cursor()
        self.cursor.execute('''
            DELETE FROM db_contractor
            WHERE contractor = ?;
        ''',(contractor,))
        self.connection.commit()
        self.connection.close()

    def get_data1(self,contractor_id):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT * FROM db_contractor
            WHERE contractor_id = ?;
        ''',(contractor_id,))
        _data = self.cursor.fetchone()
        return _data

    def get_data2(self,cont_name):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT * FROM db_contractor
            WHERE cont_name = ?;
        ''',(cont_name,))
        _data = self.cursor.fetchone()
        return _data

    def get_data3(self,contractor):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT * FROM db_contractor
            WHERE contractor = ?;
        ''',(contractor,))
        _data = self.cursor.fetchone()
        return _data

    def search_data1(self,contractor_data):
        self.connect_cursor()
        self.cursor.execute(f'''
            SELECT * FROM db_contractor
            WHERE contractor LIKE ?;
        ''',(f'%{contractor_data}%',))
        _data = self.cursor.fetchall()
        return _data

    def search_data2(self,cont_name_data):
        self.connect_cursor()
        self.cursor.execute(f'''
            SELECT * FROM db_contractor
            WHERE cont_name LIKE ?;
        ''',(f'%{cont_name_data}%',))
        _data = self.cursor.fetchall()
        return _data

    def change_data1(self,debt,contractor_id):
        self.connect_cursor()
        self.cursor.execute('''
            UPDATE db_contractor
            SET debt = debt + ?
            WHERE contractor_id = ? AND remain >= 0;
        ''',(debt,contractor_id))
        self.cursor.execute('''
            UPDATE db_contractor
            SET paid = paid - ?
            WHERE contractor_id = ? AND remain < 0 AND ? < paid;
        ''',(debt,contractor_id,debt))
        self.cursor.execute('''
            UPDATE db_contractor
            SET debt = ? - paid,paid = 0
            WHERE contractor_id = ? AND remain < 0 AND ? >= paid;
        ''',(debt,contractor_id,debt))
        self.connection.commit()
        self.connection.close()

    def change_data2(self,paid,contractor_id):
        self.connect_cursor()
        self.cursor.execute('''
            UPDATE db_contractor
            SET paid = paid + ?
            WHERE contractor_id = ? AND remain <= 0;
        ''',(paid,contractor_id))
        self.cursor.execute('''
            UPDATE db_contractor
            SET debt = debt - ?
            WHERE contractor_id = ? AND remain > 0 AND ? < debt;
        ''',(paid,contractor_id,paid))
        self.cursor.execute('''
            UPDATE db_contractor
            SET paid = ? - debt,debt = 0
            WHERE contractor_id = ? AND remain > 0 AND ? >= debt;
        ''',(paid,contractor_id,paid))
        self.connection.commit()
        self.connection.close()

    def update_data(self,contractor_id):
        self.connect_cursor()
        self.cursor.execute('''
            UPDATE db_contractor
            SET remain = debt - paid
            WHERE contractor_id = ?;
        ''',(contractor_id,))
        self.connection.commit()
        self.connection.close()