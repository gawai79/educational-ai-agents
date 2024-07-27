from fastapi import FastAPI
from master_agent import MasterAgent
from know_agent import KnowAgent
from learning_tracker_agent import LearningTrackerAgent
from roadmap_agent import RoadmapAgent
from coach_agent import CoachAgent

app = FastAPI()

agents = {
    'know_agent': KnowAgent(),
    'learning_tracker': LearningTrackerAgent(),
    'roadmap_agent': RoadmapAgent(),
    'coach_agent': CoachAgent()
}

master_agent = MasterAgent(agents)

@app.get("/student_info/{student_id}")
def get_student_info(student_id: int):
    return master_agent.allocate_task("student_info", student_id)

@app.get("/track_learning/{student_id}")
def track_learning(student_id: int):
    return master_agent.allocate_task("track_learning", student_id)

@app.get("/create_roadmap/{student_id}")
def create_roadmap(student_id: int):
    return master_agent.allocate_task("create_roadmap", student_id)

@app.get("/coach_student/{student_id}")
def coach_student(student_id: int):
    return master_agent.allocate_task("coach", student_id)
