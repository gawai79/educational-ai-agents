from base_agent import Agent

class CoachAgent(Agent):
    def process(self, task, student_id):
        coaching = self.provide_personalized_coaching(student_id)
        return f"Personalized coaching for student {student_id}: {coaching}"

    def provide_personalized_coaching(self, student_id):
        # Logic to provide personalized coaching based on student's profile
        return {
            "strengths": "Strong analytical skills and creativity",
            "areas_for_improvement": "Time management and consistent practice",
            "study_tips": [
                "Set up a regular study schedule",
                "Use project-based learning for programming",
                "Join online forums for environmental science discussions"
            ],
            "motivation": "Your progress in robotics is impressive. Keep pushing your boundaries!"
        }