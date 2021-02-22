

# prebuilt_static_bins
一些有用的可执行文件（通过muslibc或uClibc静态链接），用于不同架构的嵌入式设备 [@mzpqnxow](https://github.com/akpotter/embedded-toolkit) 。
- gawk 
- gdbserver 
- lsof 
- mawk
- tcpdump 
- tsh

# addelfinfo-arm32.py
根据glibc中的ELF定义，为原始的固件增加ELF头和节表。

用法：python addelfinfo-arm32.py <little|big endian> <filename> <base_address>

# basefind.py
暴力搜索二进制加载的起始地址，单线程，速度慢，[@mncoppola's](https://github.com/mncoppola) [basefind.py](https://github.com/mncoppola/ws30/blob/master/basefind.py) & [@rsaxvc's](https://github.com/rsaxvc) [basefind.cpp](https://github.com/mncoppola/ws30/blob/master/basefind.cpp)

# rbasefind.tar.gz
使用rust语言重新编写的基地址查找工具，多线程，速度快，此文件是根据 [@sgayou](https://github.com/sgayou) 的代码，进行编译生成的二进制文件，可以直接运行。
