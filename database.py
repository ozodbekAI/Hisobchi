import sqlite3 

class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def get_user_data(self, user_id):
        result = self.cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        return result.fetchone()

    def add_user(self, user_id, channel_id, count=1):
        self.cursor.execute("INSERT INTO users (user_id, channnel_id, count) VALUES (?,?,?)", (user_id, channel_id, count))
        self.connection.commit()

    def get_count(self, user_id, channel_id):
        result = self.cursor.execute("SELECT count FROM users WHERE user_id=? AND channnel_id=?", (user_id, channel_id))
        fetched_result = result.fetchone()
        if fetched_result is not None:
            return fetched_result[-1]
        else:
            self.add_user(user_id, channel_id, count=0)
            return 0

    def update_count_user(self, user_id, channel_id, count):
        new_count = self.get_count(user_id, channel_id) + count
        
        self.cursor.execute("UPDATE users SET count=?  WHERE channnel_id=? AND user_id=?", (new_count, channel_id, user_id))
        self.connection.commit()

    

