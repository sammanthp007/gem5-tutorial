# gem5 tutorial

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
