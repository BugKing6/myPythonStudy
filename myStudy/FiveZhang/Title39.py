#通过@classmethod多态来构造同一体系的各类对象
#python中，不仅对象支持多态，类也支持多态
class  InputData:
    def read(self):
        raise NotImplementedError

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        with open(self.path,'r') as f:
            return f.read()



class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result

import os

def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield  PathInputData(os.path.join(data_dir, name))

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

from threading import Thread

def execute(works):
    threads = [Thread(target=w.map) for w in works]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    filter, *rest = works
    for worker in rest:
        filter.reduce(worker)
    return filter.result


# def mapreduce(data_dir):
#     inputs = generate_inputs(data_dir)
#     workers = create_workers(inputs)
#     return execute(workers)


import os
import random

# def wtite_test_files(tmpdir):
#     os.makedirs(tmpdir)
#     for i in range(100):
#         with open(os.path.join(tmpdir,str(i)),'w') as f:
#             f.write('\n' * i)
#
#
# tmpdir = 'test_inputs'
# wtite_test_files(tmpdir)
# result = mapreduce(tmpdir)
#
# print(f'There are {result} lines')



print("================================================")

class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError



class PathInputData(GenericInputData):

    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        with open(self.path,'r') as f:
            return f.read()


    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def create_worker(cls, input_class, config):
        worker = []
        for input_data in input_class.generate_inputs(config):
            worker.append(cls(input_data))
        return worker

class LineCountWorker(GenericWorker):

    def map(self):
        self.result = self.input_data.read().count('\n')

    def reduce(self, other):
        self.result += other.result

def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_worker(input_class, config)
    return execute(workers)

config = {'data_dir':'test_inputs'}
result = mapreduce(LineCountWorker, PathInputData, config)

print(f'There are {result} lines')

#总结
#python只允许每个类有一个构造方法，也就是__init__方法。
#如果想在超类中用通用代码构造子类的实例。那么可以考虑定义@classmethod方法，并在里面用cls（...)形式构造具体的子类对象
#通过类的方法多态机制，能够以通用的形式构造并拼接具体的子类对象。