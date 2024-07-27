class MasterAgent:
    def __init__(self, agents):
        self.agents = agents

    def allocate_task(self, task_type, *args):
        if task_type == "student_info":
            return self.agents['know_agent'].get_student_info(*args)
        elif task_type == "track_learning":
            return self.agents['learning_tracker'].track_learning(*args)
        elif task_type == "create_roadmap":
            return self.agents['roadmap_agent'].create_roadmap(*args)
        elif task_type == "coach":
            return self.agents['coach_agent'].coach_student(*args)
        else:
            raise ValueError("Unknown task type")
