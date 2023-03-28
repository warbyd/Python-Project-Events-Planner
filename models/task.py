class Task:
    def __init__(self, description, completed, event_id, id=None):
        self.id = id
        self.description = description
        self.completed = completed
        self.event_id = event_id
