# coding=UTF-8

from core.task import Task
from algorithm.max_flow.max_flow import MaxFlow
from algorithm.max_flow.graph import Flow


def print_job(job):
    frames_str = ""
    frame_counter = 1
    for frame in job.frames:
        if frame_counter < len(job.frames):
            frames_str += str(frame.name) + ","
        else:
            frames_str += str(frame.name) + "."
        frame_counter += 1
    print ("Job {} from task {} is allocated on frame(s): {}".format(job.name, job.task.name, frames_str))


if __name__ == '__main__':
    task1 = Task(name='t1', phase=0, ex_time=1, period=4, deadline=4)
    task2 = Task(name='t2', phase=0, ex_time=2, period=5, deadline=7)
    task3 = Task(name='t3', phase=0, ex_time=5, period=20, deadline=20)

    tasks_array = [task1, task2, task3]
    flows = []
    max_flow = MaxFlow(H=20, F=4, tasks=tasks_array)
    jobs = max_flow.get_jobs()
    frames = max_flow.get_frames()
    for job in jobs:
        flow = Flow()
        job.determine_frames(frames)
        flow.calc_source_job(job)
        flow.calc_job_frames(job)
        flows.append(flow)
    for flow in flows:
        for frame in frames:
            for f in flow.job_frames:
                if frame.name == f.to.name:
                    flow.calc_frame_sink(frame)
                    break
    for flow in flows:
        output_sj = 'Source -> Job({}-{}) : [{} ---- capacity ({}), flow {} ---> Job{}]' \
            .format(flow.source_job.to.task.name, flow.source_job.to.name, flow.source_job.from_,
                    flow.source_job.capacity, flow.source_job.flow, flow.source_job.to.name)
        output_jf = ""
        for edge in flow.job_frames:
            output_jf += 'Job -> Frame: [Job{} ---- capacity ({}), flow {} ---> Frame{}]' \
                .format(edge.from_.name, edge.capacity, edge.flow, edge.to.name)

        output_fs = 'Frame -> Sink: [Frame{} ---- capacity ({}), flow {} ---> {}]' \
            .format(flow.frame_sink.from_.name, flow.frame_sink.capacity, flow.frame_sink.flow, flow.frame_sink.to)

        output = '| {} | {} | {} |'.format(output_sj, output_jf, output_fs)
        print output