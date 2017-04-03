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

