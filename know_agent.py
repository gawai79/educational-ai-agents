from base_agent import Agent

class KnowAgent(Agent):
    def process(self, task, student_id):
        info = self.get_student_info(student_id)
        return f"Student {student_id} information: {info}"

    def get_student_info(self, student_id):
        # Logic to get comprehensive student information
        return {
            "name": "James Paul",
            "age": 17,
            "grade": "12th",
            "subjects": ["Math", "Science", "Biology"],
            "academic_performance": "A+",
            "extracurricular_activities": ["Chess Club", "Football Team"]
        }
