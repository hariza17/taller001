class Graph():
    jobs = []

    def initt(self):


class Edge():
    def __init__(self, from_, capacity, flow, to):
        self.from_ = from_
        self.capacity = capacity
        self.flow = flow
        self.to = to


class Flow():
    def __init__(self, source_job, job_frame, frame_sink):
        self.source_job = source_job
        self.job_frame = job_frame
        self.frame_sink = frame_sink

    def calc_source_job(self, job):
        edge = Edge(from_='source', capacity=job.task.ex_time, flow=job.task.ex_time, to=job.name)
        self.source_job = edge

    def calc_job_frame(self, job):
        edge = Edge(from_=job.name, capacity=job.frame.value, flow=job.frame.capacity -, to=job.name)
        self.source_job = edge
