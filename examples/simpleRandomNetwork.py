"""
Simple network with a 1D population of poisson spike sources
projecting to a 2D population of IF_curr_exp neurons.

Andrew Davison, UNIC, CNRS
August 2006, November 2009

$Id$
"""
from __future__ import print_function

import logging
import socket
import os

del os.environ['DISPLAY']

from pyNN.utility import get_script_args, init_logging

logger = logging.getLogger("PyNN")

simulator_name = get_script_args(1)[0]  
exec("from pyNN.%s import *" % simulator_name)

from pyNN.random import NumpyRNG

seed = 764756387
tstop = 1000.0 # ms
input_rate = 100.0 # Hz
cell_params = {'tau_refrac': 2.0,  # ms
               'v_thresh':  -50.0, # mV
               'tau_syn_E':  2.0,  # ms
               'tau_syn_I':  2.0}  # ms
n_record = 5

node = setup(timestep=0.025, min_delay=1.0, max_delay=1.0, debug=True, quit_on_end=False)
print("Process with rank %d running on %s" % (node, socket.gethostname()))


rng = NumpyRNG(seed=seed, parallel_safe=True, rank=rank(), num_processes=num_processes())

print("[%d] Creating populations" % node)
n_spikes = int(2*tstop*input_rate/1000.0)
spike_times = numpy.add.accumulate(rng.next(n_spikes, 'exponential',
                                            [1000.0/input_rate], mask_local=False))

input_population  = Population(2, SpikeSourceArray, {'spike_times': spike_times }, "input")
output_population = Population(2, IF_curr_exp, cell_params, "output")
print("[%d] input_population cells: %s" % (node, input_population.local_cells))
print("[%d] output_population cells: %s" % (node, output_population.local_cells))

print("[%d] Connecting populations" % node)
connector = FixedProbabilityConnector(0.5, weights=1.0)
projection = Projection(input_population, output_population, connector, rng=rng)

file_stem = "Results/simpleRandomNetwork_np%d_%s" % (num_processes(), simulator_name)
projection.saveConnections('%s.conn' % file_stem)

input_population.record()
output_population.record()
output_population.record_v(n_record, rng)

print("[%d] Running simulation" % node)
run(tstop)

print("[%d] Writing spikes to disk" % node)
output_population.printSpikes('%s_output.ras' % file_stem)
input_population.printSpikes('%s_input.ras' % file_stem)
print("[%d] Writing Vm to disk" % node)
output_population.print_v('%s.v' % file_stem)

print("[%d] Finishing" % node)
end()
print("[%d] Done" % node)

