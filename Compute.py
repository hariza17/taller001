from Task import Task
from Job import Job
from Frame import Frame


class Compute():
    def __init__(self, H, F, tasks):
        self.H = H
        self.F = F
        self.tasks = tasks

    def get_jobs(self):
        jobs = {

        }
        for task in self.tasks:
            jobs[task.name] = []
            for job_number in range(0, task.get_number_of_jobs(self.H)):
                start = task.phase + task.period * job_number
                end = task.deadline + task.period * job_number + task.phase
                frame = self.assignate_frame(start, end)
                job = Job(task=task, name=job_number + 1, release=start, deadline=end, frame=frame)
                jobs[task.name].append(job)

        return jobs

    def assignate_frame(self, start, end):
        frames = []
        c = False
        for i in range(0, self.H):
            if i % self.F == 0:
                frame_end = (i + self.F)
                c = end >= frame_end
            if i % self.F == 0 and start <= i and c:
                name = (i / self.F) + 1
                frame = Frame(name=name, start=i, end=frame_end, capacity=self.F, value=self.F)
                frames.append(frame)
        return frames
