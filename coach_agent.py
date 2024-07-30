from base_agent import Agent
from database import Database
from external_api import ExternalAPI

class CoachAgent(Agent):
    def __init__(self):
        self.db = Database()
        self.api = ExternalAPI()

    def process(self, task, student_id):
        coaching = self.provide_personalized_coaching(student_id)
        return f"Personalized coaching for student {student_id}: {coaching}"

    def provide_personalized_coaching(self, student_id):
        student_performance = self.db.get_student_performance(student_id)
        learning_style = self.db.get_student_learning_style(student_id)
        recent_activities = self.db.get_student_recent_activities(student_id)
        
        coaching_advice = self.api.generate_coaching_advice(student_performance, learning_style, recent_activities)
        
        return {
            "strengths": coaching_advice['strengths'],
            "areas_for_improvement": coaching_advice['areas_for_improvement'],
            "study_tips": coaching_advice['study_tips'],
            "motivation": coaching_advice['motivation']
        }
