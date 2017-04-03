# import the m5 library
import m5

# import all the simobjects that was compiled into the namespace in this python class
from m5.objects import *

# instantiate a system
system = System()

""" set defaults
"""

## set the clock
# instantiate a clock domain
system.clk_domain = SrcClockDomain()

# set the clock domain
system.clk_domain.clock = '1GHz'
# set the default voltage domain, we are good with the default of the instantiation
system.clk_domain.voltage_domain = VoltageDomain()

# set the systems memory mode. different memory mode: timing, atomic, etc. Mostly use timing. Atomic is mostly for
# fast forwarding and warming caches. Does not actually give timing information. To get timing information, you need
# timing mode
system.mem_mode = 'timing'

# set physical memory range
system.mem_ranges = [AddrRange('512MB')]

# create a cpu: simple simple timing cpu: simple cpu that has single cycle cpu, every thing EXECUTES in one CPU cycle
# except memory operation, which depends on memory system
system.cpu = TimingSimpleCPU()

# create the mem bus as shown in the picture
system.membus = SystemXBar()

# hook the cpu to the memory bus: cpu and membus are memory objects, so they have a port interface between them, so we
# set up the ports the CPU has to connect up to the memory bus port
system.cpu.icache_port = system.membus.slave
system.cpu.dcache_port = system.membus.slave

# X86 specific stuffs:
# create a interrupt controller
system.cpu.createInterruptController()
# set the X86 cpu so the interrupt works
system.cpu.interrupts[0].pio = system.membus.master
system.cpu.interrupts[0].int_master = system.membus.slave
system.cpu.interrupts[0].int_slave = system.membus.master

system.system_port = system.membus.slave

# create the memory controller, as shown in the diagram
system.mem_ctrl = DDR3_1600_x64()
# set this mem_ctrl to our systems range
system.mem_ctrl.range = system.mem_ranges[0]
# hook this mem_ctrl to the memory bus
system.mem_ctrl.port = system.membus.master

# give this system we just created a binary to run 
process = LiveProcess()
# give the process a command, inbuilt compiled: in this case is a hello world binary
process.cmd = ['tests/test-progs/hello/bin/x86/linux/hello']
# set the cpus workload to be this process
system.cpu.workload = process
# create our cpu threads
system.cpu.createThreads()

# create a root object and pass it our system: all gem5 simluations MUST have a root object
root = Root(full_system=False)
root.system = system

# takes all this python objects that we have instantiated and walkthrough all this python object and actually perform
# the c++ constructors, NOW THE C++ objects ARE CONSTRUCTED
m5.instantiate()

print "Beginning simulation"
exit_event = m5.simulate()

# m5.curTick is the tick that the simulation is on while it exits
print "Done simulating at tick %d because %s" % (m5.curTick(),
            exit_event.getCause())
