from mpi4py import MPI
import time
import subprocess
import argparse
from mjolnir import Mjolnir
import numpy
import os

"""
note:

still unsure what the starting positions of rotational stage will be (i.e. unsure how it's going to be used)

aiming for basic functionality

assuming that comm.recv waits for the signal
quite lazy to look at source code, debug the next day
if it doesn't, gg

params:
	step	stepsize of motor. 1 encoder count --> 2.16 arcseconds
	deg		how many degrees to move the rotational stage (relative to initial position)
	binsize	how many data points per step


-zy 19 Nov 2015
"""
def check_dir(directory):
	if not os.path.exists(directory):
	    os.makedirs(directory)

class apdControl():
	def __init__(self,binsize):
		self.comm = MPI.COMM_WORLD
		self.binsize = binsize
		self.start_t = time.time()
		self.c = binsize
		self.data = []
		#meta = self.comm.recv(source = 1, tag = 1)
		self.id = None
		self.timestamp = None
		#self.grabData()
	def grabData(self):
		check_dir(self.timestamp)
		while self.c > 0:
			self.ping()
			time.sleep(0.2)
		with open(os.path.join(self.timestamp, str(self.id)), 'wb+') as f:
			for i in xrange(len(data)):
				f.write("{}\t{}\t{}\n".format(i, self.data[i][1][0], self.data[i][1][1]))
		comm.send("done", dest = 0, tag = 0)
    def ping(self):
        proc = subprocess.Popen(['./getresponse','COUNTS?'], stdout=subprocess.PIPE)
    	output = proc.stdout.read()
        if output =="timeout while waiting for response":
            pass
        else:
            t = time.time() - self.start_t
            data = output.rstrip().split(' ')
            data.pop(0)
            try:
                data = map(lambda x: float(x), data)
                _data = [t, data]
                self.c -= 1
                self.data.append(_data)
            except ValueError:
                pass
class thorControl():
	def __init__(self, step, deg):
		self.step = step
		self.deg = deg
	def start(self):

		comm = MPI.COMM_WORLD
		m = Mjolnir()
		x = self.deg * 3600
		x /= float(2.16)
		self.data = {}
		for i in xrange(int(x)):
			m.moveRotMotor(s)
			comm.send("next", dest = 0, tag = 0)
			comm.send([timestamp, i], dest = 0, tag = 1)
			#self.data[i] = comm.recv(source = 1, tag = 0)
			if comm.recv(source = 0, tag = 0) == "done":
				continue
			time.sleep(1)
		comm.send("terminated", dest = 0, tag = 0)
		print "completed"

def main(kwargs):
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	timestamp = time.strftime('%Y%m%d_%H%M')
	metadata = {
		'timestamp': timestamp,
		'bin_size': kwargs['binsize'],
		'step_size':kwargs['step'],
		'degrees_moved': kwargs['degree']
	}
	with open(os.path.join(timestamp, 'metadata.json'), 'w') as f:
		f.write(json.dump(metadata))
	if rank == 0:
		print "on fruitcake0: apd control"
		#a = apdControl(kwargs['binsize'])
		while True:
			a = comm.recv(source = 1, tag = 0)
			if a == "next":
				b = comm.recv(source = 1, tag = 1)
				c = apdControl(kwargs['binsize'])
				c.id = b[1]
				c.timestamp = b[0]
				c.grabData()
			else:
				break

	elif rank == 1:
		print "on fruitcake1: motorised stage control"
		b = thorControl(kwargs['step'], kwargs['degree'])
		b.start()


def init():
	parser = argparse.ArgumentParser(description = "Script to control motor for characterisation of APD flash breakdown")
	parser.add_argument('degrees', metavar = 'd', type = int, nargs = '+')
	parser.add_argument('stepsize', metavar = 's', type = int, nargs = '+')
	parser.add_argument('binsize', metavar = 'b', type = int, nargs = '+')
	args = parser.parse_args()
	main({'degree':args.degrees, 'step':args.stepsize, 'binsize': args.binsize})


init()
