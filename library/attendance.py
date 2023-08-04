from db.db_connector import get_db_connection
from datetime import datetime, time


# Polymorphism for class ForenoonAttendance and class AfternoonAttendance
class ForenoonAttendance:
    @staticmethod
    def is_attendance_open(current_time):
        forenoon_start_time = time(8, 45)
        forenoon_end_time = time(11, 59)
        return forenoon_start_time <= current_time <= forenoon_end_time

    @staticmethod
    def get_attendance_type():
        return 'FN'


class AfternoonAttendance:
    @staticmethod
    def is_attendance_open(current_time):
        afternoon_start_time = time(12, 30)
        afternoon_end_time = time(17, 30)
        return afternoon_start_time <= current_time <= afternoon_end_time

    @staticmethod
    def get_attendance_type():
        return 'AN'


class Attendance:
    def __init__(self, attendance_type=None):
        self.db_connection = get_db_connection()
        self.attendance_type = attendance_type
        self.create_attendance_table()

    def create_attendance_table(self):
        cursor = self.db_connection.cursor()
        query = """CREATE TABLE IF NOT EXISTS attendance (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            username VARCHAR(15) NOT NULL,
                            attendance_date DATE NOT NULL,
                            attendance_time TIME NOT NULL,
                            attendance_type VARCHAR(2) NOT NULL
                        )"""
        cursor.execute(query)
        self.db_connection.commit()
        cursor.close()

    def record_attendance(self, username):
        cursor = self.db_connection.cursor()
        current_time = datetime.now().time()

        if not self.attendance_type:
            self.attendance_type = ForenoonAttendance.get_attendance_type() if ForenoonAttendance.is_attendance_open(current_time) else AfternoonAttendance.get_attendance_type()

        query = """INSERT INTO attendance (username, attendance_date, attendance_time, attendance_type) 
                   VALUES (%s, %s, %s, %s)"""
        data = (username, datetime.now().date(), current_time, self.attendance_type)
        cursor.execute(query, data)
        self.db_connection.commit()
        print(f"Current time is {current_time}")
        print("Attendance recorded successfully.")
        cursor.close()
