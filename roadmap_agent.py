from base_agent import Agent
from database import Database
from external_api import ExternalAPI

class RoadmapAgent(Agent):
    def __init__(self):
        self.db = Database()
        self.api = ExternalAPI()

    def process(self, task, student_id):
        roadmap = self.create_personalized_roadmap(student_id)
        return f"Personalized learning roadmap for student {student_id}: {roadmap}"

    def create_personalized_roadmap(self, student_id):
        student_profile = self.db.get_student_profile(student_id)
        current_skills = self.db.get_student_skills(student_id)
        career_goals = self.db.get_student_career_goals(student_id)
        
        return self.api.generate_learning_roadmap(student_profile, current_skills, career_goals)
