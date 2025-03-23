#Copyright (c) 2025 @sarlakmohammad
    #All rights reserved

import sqlite3

class DBFacCont:
    def __init__(self,filename):
        self._db_name = filename
        self.connection = sqlite3.connect(self._db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS db_FacCont(
            factor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            factor NVARCHAR(15) NOT NULL UNIQUE,
            date DATE,
            contractor_id INTEGER NOT NULL REFERENCES db_contractor(contractor_id),
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

    def update_cont(self,contractor_id):
        self.cursor.execute('''
            UPDATE db_contractor
            SET remain = debt - paid
            WHERE contractor_id = ?;
        ''', (contractor_id,))

    def add_debt_to_cont(self,debt,contractor_id):
        self.cursor.execute('''
            UPDATE db_contractor
            SET debt = debt + ?
            WHERE contractor_id = ? AND remain >= 0;
        ''', (debt, contractor_id))
        self.cursor.execute('''
            UPDATE db_contractor
            SET paid = paid - ?
            WHERE contractor_id = ? AND remain < 0 AND ? < paid;
        ''', (debt, contractor_id, debt))
        self.cursor.execute('''
            UPDATE db_contractor
            SET debt = ? - paid,paid = 0
            WHERE contractor_id = ? AND remain < 0 AND ? >= paid;
        ''', (debt, contractor_id, debt))
        self.update_cont(contractor_id)

    def add_paid_to_cont(self,paid,contractor_id):
        self.cursor.execute('''
            UPDATE db_contractor
            SET paid = paid + ?
            WHERE contractor_id = ? AND remain <= 0;
        ''', (paid, contractor_id))
        self.cursor.execute('''
            UPDATE db_contractor
            SET debt = debt - ?
            WHERE contractor_id = ? AND remain > 0 AND ? < debt;
        ''', (paid, contractor_id, paid))
        self.cursor.execute('''
            UPDATE db_contractor
            SET paid = ? - debt,debt = 0
            WHERE contractor_id = ? AND remain > 0 AND ? >= debt;
        ''', (paid, contractor_id, paid))
        self.update_cont(contractor_id)

    def insert_into(self,
                    factor,
                    date,
                    contractor_id,
                    project_id,
                    cost
                    ):
        self.connect_cursor()
        #### create factor
        self.cursor.execute('''
        INSERT OR IGNORE INTO db_FacCont(factor,date,contractor_id,project_id,cost)
        VALUES(?,?,?,?,?);
        ''',(factor,date,contractor_id,project_id,cost))
        #### add debt to cont
        self.add_debt_to_cont(cost,contractor_id)
        #### add cost to project
        self.cursor.execute('''
            UPDATE db_project
            SET cost = cost + ?
            WHERE project_id = ?
        ''',(cost,project_id))
        self.update_project(project_id)

        self.connection.commit()
        self.connection.close()

    def show_data(self):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT factor_id,factor,db_FacCont.date,contractor,project,db_FacCont.cost,db_FacCont.state
            FROM ((db_FacCont
            INNER JOIN db_contractor ON db_FacCont.contractor_id = db_contractor.contractor_id)
            INNER JOIN db_project ON db_FacCont.project_id = db_project.project_id);
        ''')
        _data = self.cursor.fetchall()
        return _data

    def change_state(self,factor_id):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT state,cost,contractor_id
            FROM db_FacCont
            WHERE factor_id = ?;
        ''', (factor_id,))
        _list = self.cursor.fetchone()
        _state = bool(_list[0])
        _money = int(_list[1])
        _id = int(_list[2])
        if not _state:
            self.add_paid_to_cont(_money,_id)
            self.cursor.execute('''
                UPDATE db_FacCont
                SET state = TRUE
                WHERE factor_id = ?;
            ''', (factor_id,))
        else:
            self.add_debt_to_cont(_money,_id)
            self.cursor.execute('''
                UPDATE db_FacCont
                SET state = FALSE
                WHERE factor_id = ?;
            ''', (factor_id,))
        self.connection.commit()
        self.connection.close()

    def delete_data(self,factor):
        self.connect_cursor()
        self.cursor.execute('''
            SELECT state,cost,project_id,contractor_id
            FROM db_FacCont
            WHERE factor = ?;
        ''', (factor,))
        #### data
        _list = self.cursor.fetchone()
        _state = bool(_list[0])
        _money = int(_list[1])
        _project_id = int(_list[2])
        _contractor_id = int(_list[3])
        #### project
        self.cursor.execute('''
            UPDATE db_project
            SET cost = cost - ?
            WHERE project_id = ?
        ''',(_money,_project_id))
        self.update_project(_project_id)
        #### check for a condition
        if not _state:
            self.add_paid_to_cont(_money,_contractor_id)
        #### delete factor
        self.cursor.execute('''
            DELETE FROM db_FacCont
            WHERE factor = ?;
        ''', (factor,))
        self.connection.commit()
        self.connection.close()

    def search_data(self,factor):
        self.connect_cursor()
        self.cursor.execute(f'''
            SELECT factor_id,factor,db_FacCont.date,contractor,project,db_FacCont.cost,db_FacCont.state
            FROM ((db_FacCont
            INNER JOIN db_contractor ON db_FacCont.contractor_id = db_contractor.contractor_id)
            INNER JOIN db_project ON db_FacCont.project_id = db_project.project_id)
            WHERE factor LIKE ?;
        ''',(f'%{factor}%',))
        _data = self.cursor.fetchall()
        return _data