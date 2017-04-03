# gem5 tutorial
What is gem5?

[gem5.org](http://gem5.org/Main_Page) says:
> The gem5 simulator is a modular platform for computer-system architecture research, encompassing system-level architecture > as well as processor microarchitecture.

### Features, what it offers:
* gem5 is a discreet event simulator. To do anything in gem5, you need to enqueue events and use the event driven process.
* User interface for gem5 is not command line. The user interface for gem5 is **python scripts**

## Installation and Building in Ubuntu
Install dependencies, in my case I needed these two:
```
sudo apt install swig scons

# for arch linux
pacman -S swig scons
```

#### Get gem5
```
git clone https://gem5.googlesource.com/public/gem5
```

#### Build gem5
```
cd gem5
git checkout hpca
scons build/X86/gem5.opt -j5
```

`scons` is a build system that gem5 uses. 
> Its like make but a million times more complicated.
But used for felxibility. It is basically a python file which will be interpreted by a regular python interpreter.
More info in [scons.org](http://scons.org)

`build/X86/gem5.opt` is a parameter sent to the `Sconscript`file. 
> This says, I want to build a `build` directory with the default build option as `X86`, and `.opt` is the optimized version of the binary, faster than debug but not as fast as fast and `-j5` to specify the number of cores

## SimObjects
Almost every thing is gem5 is a SimObject. It is an abstraction. All c++ object are SimObjects

### One thing SimObjects can do is enqueue events
Events are shot based on time. An event is shot at a specific time. 
> And to do anything in gem5, you need to enqueue and dequeue events.

<img src='https://github.com/sammanthp007/gem5-tutorial/blob/master/screenshots/simobject_and_events/output.gif' title='event driven process' width='' alt='event driven process' />

## Python Scripts
The user interface for gem5

### Interfacing
> Write a python script that configures the simulator, runs the simulator, executes the simulator

* Scripts define system to model
* Control the simulation: All C++ SimObjects in the source folder are exposed to python

#### Exercise: Simulating a system
We are simulating the following system:

<img src='https://github.com/sammanthp007/gem5-tutorial/blob/master/screenshots/simple_script/simple_script.jpg' title='simple system' width='' alt='simple system' />

```
# Create a configs directory: All configurations scripts go here
mkdir -p configs/hpca_tutorials
vim configs/hpca_tutorials/simple.py
```
You can find the configuration of the simulation [here](https://github.com/sammanthp007/gem5-tutorial/blob/master/simple.py)

To run: Go to your root directory and
```
# the binary is a built in python interpreter
build/X86/gem5.opt configs/hpca_tutorial/simple.py
```


# Reference:
[Learning gem5 HPCA tutorial](https://www.youtube.com/watch?v=5UT41VsGTsg)
