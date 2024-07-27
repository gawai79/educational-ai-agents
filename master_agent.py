from base_agent import Agent

class MasterAgent(Agent):
    def __init__(self, agents):
        self.agents = agents

    def process(self, task, student_id):
        if task == "student_info":
            return self.agents['know_agent'].process(task, student_id)
        elif task == "learning_tracker":
            return self.agents['learning_tracker'].process(task, student_id)
        elif task == "create_roadmap":
            return self.agents['roadmap_agent'].process(task, student_id)
        elif task == "coach":
            return self.agents['coach_agent'].process(task, student_id)
        else:
            return f"Unknown task: {task}"

    def allocate_task(self, task, student_id):
        return self.process(task, student_id)
