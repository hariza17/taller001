from core.frame import Frame
from core.job import Job


class PeriodicScheduler:
    def __init__(self, H, F, tasks):
        self.H = H
        self.F = F
        self.tasks = tasks

    def get_jobs(self):
        jobs = []
        for task in self.tasks:
            for job_number in range(0, task.get_number_of_jobs(self.H)):
                start = task.phase + task.period * job_number
                end = task.deadline + task.period * job_number + task.phase
                job = Job(task=task, name=job_number + 1, release=start,
                          deadline=end, ex_time=task.ex_time, status=1)
                jobs.append(job)
        return jobs

    def get_frames(self):
        frames = []
        for i in range(0, self.H):
            if i % self.F == 0:
                frame_end = (i + self.F)
                name = (i / self.F) + 1
                frame = Frame(name=name, start=i, end=frame_end, capacity=self.F, value=self.F)
                frames.append(frame)
        return frames