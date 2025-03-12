import sqlite3

class DBProject:
    def __init__(self,filename):
        self._db_name = filename
        self.connection = sqlite3.connect(self._db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS db_project(
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project NVARCHAR(50) NOT NULL UNIQUE,
            customer_id INTEGER REFERENCES db_customer(customer_id),
            estimate BIGINT(20) DEFAULT 0,
            cost BIGINT(20) DEFAULT 0,
            contradiction VARCHAR(5) DEFAULT "0%",
            paid BIGINT(20) DEFAULT 0,
            date DATE,
            state BOOLEAN DEFAULT FALSE
        );
        ''')
        self.connection.close()

    def connect_cursor(self):
        self.connection = sqlite3.connect(self._db_name)
        self.cursor = self.connection.cursor()

    def insert_into(self,
                    project:str,
                    customer_id:str,
                    estimate:int,
                    date
                    ):
        self.connect_cursor()
        self.cursor.execute('''
            INSERT OR IGNORE INTO db_project(project,customer_id,estimate,date)
            VALUES(?,?,?,?);
        ''',(project,customer_id,estimate,date))
        self.connection.commit()
        self.connection.close()

    def show_data(self):
        self.connect_cursor()
        self.cursor.execute('''
                    SELECT project_id,project,customer_id,estimate,cost,contradiction,paid,state
                    FROM db_project;
                ''')
        _data = self.cursor.fetchall()
        return _data

    def delete_data1(self,project_id):
        self.connect_cursor()
        self.cursor.execute('''
            DELETE FROM db_project
            WHERE project_id = ?;
        ''',(project_id,))
        self.connection.commit()
        self.connection.close()

    def delete_data2(self,project):
        self.connect_cursor()
        self.cursor.execute('''
            DELETE FROM db_project
            WHERE project = ?;
        ''',(project,))
        self.connection.commit()
        self.connection.close()

    def get_data1(self,project_id):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT * FROM db_project
            WHERE project_id = ?;
        ''',(project_id,))
        _data = self.cursor.fetchone()
        return _data

    def get_data2(self,project):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT * FROM db_project
            WHERE project = ?;
        ''',(project,))
        _data = self.cursor.fetchone()
        return _data

    def search_data1(self,project_id):
        self.connect_cursor()
        self.cursor.execute(f'''
            SELECT * FROM db_project
            WHERE project_id LIKE ?;
        ''',(f'%{project_id}%',))
        _data = self.cursor.fetchall()
        return _data

    def search_data2(self,project):
        self.connect_cursor()
        self.cursor.execute(f'''
            SELECT project_id,project,customer_id,estimate,cost,contradiction,paid,state
            FROM db_project
            WHERE project LIKE ?;
        ''',(f'%{project}%',))
        _data = self.cursor.fetchall()
        return _data

    def change_data1(self,cost,project_id):
        self.connect_cursor()
        self.cursor.execute('''
            UPDATE db_project
            SET cost = ?
            WHERE project_id = ?;
        ''',(cost,project_id))
        self.connection.commit()
        self.connection.close()

    def change_data2(self,paid,project_id):
        self.connect_cursor()
        self.cursor.execute('''
            UPDATE db_project
            SET paid = ?
            WHERE project_id = ?;
        ''',(paid,project_id))
        self.connection.commit()
        self.connection.close()

    def update_data1(self,project_id,contradiction):
        self.connect_cursor()
        self.cursor.execute('''
            UPDATE db_project
            SET contradiction = ?
            WHERE project_id = ?;
        ''',(contradiction,project_id))
        self.connection.commit()
        self.connection.close()

    def update_data2(self,project_id):
        self.connect_cursor()
        self.cursor.execute('''
            UPDATE db_project
            SET state = TRUE
            WHERE project_id = ? AND cost = paid;
        ''',(project_id,))
        self.cursor.execute('''
            UPDATE db_project
            SET state = FALSE
            WHERE project_id = ? AND cost <> paid;
        ''', (project_id,))
        self.connection.commit()
        self.connection.close()