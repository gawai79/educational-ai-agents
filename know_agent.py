from base_agent import Agent
from database import Database  # Assume we have a Database class for interactions

class KnowAgent(Agent):
    def __init__(self):
        self.db = Database()

    def process(self, task, student_id):
        info = self.get_student_info(student_id)
        return f"Student {student_id} information: {info}"

    def get_student_info(self, student_id):
        # Fetch real-time data from database
        return self.db.get_student_info(student_id)
