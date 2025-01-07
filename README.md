

# prebuilt_static_bins
一些有用的可执行文件（通过muslibc或uClibc静态链接），用于不同架构的嵌入式设备 [@mzpqnxow](https://github.com/akpotter/embedded-toolkit) 。
- gawk 
- gdbserver 
- lsof 
- mawk
- tcpdump 
- tsh

## 基地址搜索

- `basefind.py` 暴力搜索二进制加载的起始地址，单线程，速度慢，[@mncoppola's](https://github.com/mncoppola) [basefind.py](https://github.com/mncoppola/ws30/blob/master/basefind.py) & [@rsaxvc's](https://github.com/rsaxvc) [basefind.cpp](https://github.com/mncoppola/ws30/blob/master/basefind.cpp)
- `rbasefind.tar.gz` 使用rust语言重新编写的基地址查找工具，多线程，速度快，此文件是根据 [@sgayou](https://github.com/sgayou) 的代码，进行编译生成的二进制文件，可以直接运行。
- 推荐使用新工具：[binbloom](https://github.com/quarkslab/binbloom)

## 固件修复
### 添加elf信息
- `addelfinfo-arm32.py` 根据glibc中的ELF定义，为原始的固件增加ELF头和节表。方便IDA直接识别。
- 推荐使用新工具：[elfspirit](https://github.com/liyansong2018/elfspirit)

### Bare-Meta

- [SVD-Loader-Ghidra](https://github.com/leveldown-security/SVD-Loader-Ghidra)自动加载内存映射寄存器表的Ghidra插件，针对CotexM系列芯片
- [Reverse Engineering Radios – ARM Binary Images in IDA Pro](https://do1alx.de/2022/reverse-engineering-radios-arm-binary-images-in-ida-pro/)
- [硬件安全系列——ARM Cortex-M4固件逆向分析](https://www.anquanke.com/post/id/209364)

## 仿真

Bare-Meta(裸机程序)

- [SHiFT](https://github.com/RiS3-Lab/SHiFT)
- [MultiFuzz](https://github.com/MultiFuzz/MultiFuzz)
- [fuzzware](https://github.com/fuzzware-fuzzer/fuzzware)
- [uEmu](https://github.com/MCUSec/uEmu)

Linux系统

- [Firmadyne](https://github.com/firmadyne/firmadyne)
- [Fap](https://github.com/liyansong2018/firmware-analysis-plus)
- [EMUX](https://github.com/therealsaumil/emux)
