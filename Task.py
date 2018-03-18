class Task():
    def __init__(self, name, phase, ex_time, period, deadline):
        self.phase = phase
        self.ex_time = ex_time
        self.period = period
        self.deadline = deadline
        self.name = name

    def get_number_of_jobs(self, H):
        return H / self.period
