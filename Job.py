class Job():
    def __init__(self, task, name, release, deadline, frame):
        self.task = task
        self.name = name
        self.start = release
        self.end = deadline
        self.frame = frame
