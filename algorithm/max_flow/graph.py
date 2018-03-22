# coding=UTF-8


class Graph:
    def __init__(self):
        self.source_job = Edge
        self.job_frame = Edge
        self.frame_sink = Edge


class Edge:
    def __init__(self, from_, capacity, flow, to):
        self.from_ = from_
        self.capacity = capacity
        self.flow = flow
        self.to = to


class Flow:
    def __init__(self):
        self.source_job = Edge
        self.job_frames = []
        self.frame_sink = Edge

    def calc_source_job(self, job):
        self.source_job = Edge(from_='source', capacity=job.task.ex_time, flow=job.task.ex_time, to=job)

    def calc_job_frames(self, job):
        edges = []
        for frame in job.frames:
            i = job.ex_time
            while i > 0:
                if frame.capacity >= i and job.status == 1:
                    if i == job.ex_time:
                        job.status = 2
                    frame.capacity -= i
                    job.ex_time -= i
                    edges.append(
                    Edge(from_=job, capacity=frame.value, flow=i, to=frame))
                i -= 1
        if job.status != 2:
            print("the job {} from task {} couldnt be allocated".format(job.name, job.task.name))
        self.job_frames = edges

    def calc_frame_sink(self, frame):
        self.frame_sink = Edge(from_=frame, capacity=frame.value, flow=frame.value - frame.capacity, to="sink")
