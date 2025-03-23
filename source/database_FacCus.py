#Copyright (c) 2025 @sarlakmohammad
    #All rights reserved

import sqlite3

class DBFacCus:
    def __init__(self,filename):
        self._db_name = filename
        self.connection = sqlite3.connect(self._db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS db_FacCus(
            factor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            factor NVARCHAR(15) NOT NULL UNIQUE,
            date DATE,
            customer_id INTEGER NOT NULL REFERENCES db_customer(customer_id),
            project_id INTEGER NOT NULL REFERENCES db_project(project_id),
            cost BIGINT(20) NOT NULL,
            state BOOLEAN DEFAULT FALSE
        );
        ''')
        self.connection.close()

    def connect_cursor(self):
        self.connection = sqlite3.connect(self._db_name)
        self.cursor = self.connection.cursor()

    def update_project(self,project_id):
        self.cursor.execute('''
            UPDATE db_project
            SET contradiction = paid - cost
            WHERE project_id = ?;
        ''', (project_id,))
        self.cursor.execute('''
            UPDATE db_project
            SET state = TRUE
            WHERE project_id = ? AND estimate = paid;
        ''', (project_id,))
        self.cursor.execute('''
            UPDATE db_project
            SET state = FALSE
            WHERE project_id = ? AND estimate <> paid;
        ''', (project_id,))

    def update_cus(self,customer_id):
        self.cursor.execute('''
            UPDATE db_customer
            SET remain = debt - paid
            WHERE customer_id = ?;
        ''', (customer_id,))

    def add_debt_to_cus(self,debt,customer_id):
        self.cursor.execute('''
            UPDATE db_customer
            SET debt = ? + debt
            WHERE customer_id = ? AND remain >= 0;
        ''', (debt, customer_id))
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
        self.update_cus(customer_id)

    def add_paid_to_cus(self,paid,customer_id):
        self.cursor.execute('''
            UPDATE db_customer
            SET paid = paid + ?
            WHERE customer_id = ? AND remain <= 0;
        ''', (paid, customer_id))
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
        self.update_cus(customer_id)

    def insert_into(self,
                    factor,
                    date,
                    customer_id,
                    project_id,
                    cost
                    ):
        self.connect_cursor()
        self.cursor.execute('''
            INSERT OR IGNORE INTO db_FacCus(factor,date,customer_id,project_id,cost)
            VALUES(?,?,?,?,?);
        ''',(factor,date,customer_id,project_id,cost))
        ####
        self.add_debt_to_cus(cost,customer_id)

        self.connection.commit()
        self.connection.close()

    def show_data(self):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT factor_id,factor,db_FacCus.date,company,project,db_FacCus.cost,db_FacCus.state
            FROM ((db_FacCus
            INNER JOIN db_customer ON db_FacCus.customer_id = db_customer.customer_id)
            INNER JOIN db_project ON db_FacCus.project_id = db_project.project_id);
        ''')
        _data = self.cursor.fetchall()
        return _data

    def change_state(self,factor_id):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT state,cost,project_id,customer_id
            FROM db_FacCus
            WHERE factor_id = ?;
        ''',(factor_id,))
        _list = self.cursor.fetchone()
        _state = _list[0]
        _money = _list[1]
        _project_id = _list[2]
        _customer_id = _list[3]
        if not _state:
            self.add_paid_to_cus(_money,_customer_id)
            self.cursor.execute('''
                UPDATE db_project
                SET paid = paid + ?
                WHERE project_id = ?;
            ''',(_money,_project_id))
            self.cursor.execute('''
                UPDATE db_FacCus
                SET state = TRUE
                WHERE factor_id = ?;
            ''',(factor_id,))
        else:
            self.add_debt_to_cus(_money,_customer_id)
            self.cursor.execute('''
                UPDATE db_project
                SET paid = paid - ?
                WHERE project_id = ?;
            ''', (_money, _project_id))
            self.cursor.execute('''
                UPDATE db_FacCus
                SET state = FALSE
                WHERE factor_id = ?;
            ''', (factor_id,))

        self.update_project(_project_id)
        self.connection.commit()
        self.connection.close()

    def delete_data(self,factor):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT state,cost,customer_id,project_id
            FROM db_FacCus
            WHERE factor = ?;
        ''',(factor,))
        #### data
        _list = self.cursor.fetchone()
        _state = bool(_list[0])
        _money = int(_list[1])
        _customer_id = int(_list[2])
        _project_id = int(_list[3])
        #### check for other tables
        if _state:
            self.cursor.execute('''
                UPDATE db_project
                SET paid = paid - ?
                WHERE project_id = ?;
            ''',(_money,_project_id))
        else:
            self.add_paid_to_cus(_money, _customer_id)
        self.update_project(_project_id)
        #### delete factor
        self.cursor.execute('''
            DELETE FROM db_FacCus
            WHERE factor = ?;
        ''',(factor,))
        self.connection.commit()
        self.connection.close()

    def search_data(self,factor):
        self.connect_cursor()
        self.cursor.execute(f'''
            SELECT factor_id,factor,db_FacCus.date,company,project,db_FacCus.cost,db_FacCus.state
            FROM ((db_FacCus
            INNER JOIN db_customer ON db_FacCus.customer_id = db_customer.customer_id)
            INNER JOIN db_project ON db_FacCus.project_id = db_project.project_id)
            WHERE factor LIKE ?;
        ''',(f'%{factor}%',))
        _data = self.cursor.fetchall()
        return _data