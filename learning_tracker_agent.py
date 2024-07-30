from base_agent import Agent
from database import Database
from external_api import ExternalAPI  # Assume we have an ExternalAPI class for API calls

class LearningTrackerAgent(Agent):
    def __init__(self):
        self.db = Database()
        self.api = ExternalAPI()

    def process(self, task, student_id):
        interests = self.get_interests(student_id)
        future_learning = self.suggest_future_learning(student_id)
        technical_assessment = self.assess_technical_level(student_id)
        summary = self.generate_summary(student_id)
        
        return {
            "interests": interests,
            "future_learning": future_learning,
            "technical_assessment": technical_assessment,
            "summary": summary
        }

    def get_interests(self, student_id):
        return self.db.get_student_interests(student_id)

    def suggest_future_learning(self, student_id):
        current_skills = self.db.get_student_skills(student_id)
        return self.api.get_learning_suggestions(current_skills)

    def assess_technical_level(self, student_id):
        assessment_results = self.db.get_latest_assessment(student_id)
        return self.api.interpret_assessment(assessment_results)

    def generate_summary(self, student_id):
        student_data = self.db.get_comprehensive_student_data(student_id)
        return self.api.generate_learning_summary(student_data)
