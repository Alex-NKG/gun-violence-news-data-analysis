import db_con


class write_db:
    def __init__(self):
        self.db = db_con.connect_DB()

    def write_db(self, sql_query, vals):
        self.db.query(sql_query, vals)
        self.db.commit()











