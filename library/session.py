from db.db_connector import get_db_connection

from tabulate import tabulate


class ScheduleManager:

    def __init__(self):
        self.db_connection = get_db_connection()

    def view_schedule(self, intern):
        cursor = self.db_connection.cursor()

        query = """SELECT session_id, session_title, handled_by, time, duration FROM schedules"""

        cursor.execute(query)
        sessions = cursor.fetchall()
        print(f"The sessions for {intern}")
        if sessions:
            headers = ["Session ID", "Title", "Handled By", "Time", "Duration"]
            print(tabulate(sessions, headers=headers, tablefmt="grid"))
        else:
            print("No sessions found in the database.")
        print("\n")
        cursor.close()
