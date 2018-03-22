class Job:
    def __init__(self, task, name, release, deadline, ex_time, status):
        """
        task: Task = Parent task
        name: Str = Number of job divided in the task
        release: Int = time where the job is released. (start)
        deadline: Int = time of the job's deadline. (end)
        frames : [Frame] = Array of Frames that the job can fit into
        ex_time: Int = time of execution needed from the processor for this job to finish
        status: Int (1, 2, 3) : 1 = to be executed. 2: It has been executed. 3: It couldn't be executed.
        """
        self.task = task
        self.name = name
        self.start = release
        self.end = deadline
        self.ex_time = ex_time
        self.status = status
        self.frames = []

    def determine_frames(self, frames):
        possible_frames = []
        for frame in frames:
            if frame.start >= self.start or frame.end >= self.end:
                possible_frames.append(frame)
        self.frames = possible_frames
