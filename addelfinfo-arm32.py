import sys
import struct

def addelfinfo():
	with open(sys.argv[2]) as fs:
		fs.seek(0, 2)
		file_length = fs.tell()
		fs.seek(0, 0)
		print("[*] source file length is: 0x%x" % file_length)

		base_address = sys.argv[3]
		base_address = int(base_address, 16)
		print("[*] base address is: 0x%x" % base_address)

		with open(sys.argv[2] + ".elf", "wb+") as fn:
			# ELF header: 0 ~ 0x33 (54 Bytes)
			fn.write("\x7fELF")		# EI_MAG0-3
			fn.write("\x01")		# EI_CLASS	ELFCLASS32=1

			if sys.argv[1] == "little": # EI_DATA
				fn.write("\x01")
			elif sys.argv[1] == "big":
				fn.write("\x02")

			fn.write("\x01")		# EI_VERSION
			fn.write("\x00")		# EI_OSABI
			fn.write("\x00")		# EI_ABIVERSION
			fn.write("\x00" * 7)	# EI_PAD

			fn.write("\x02\x00")	# e_type
			fn.write("\x28\x00")	# e_machine
			fn.write("\x01\x00\x00\x00")	# e_version
			fn.write(struct.pack("<I", base_address))	# e_entry
			fn.write("\x00\x00\x00\x00")	# e_phoff: the program header table's file offset
			fn.write("\x34\x00\x00\x00")	# e_shoff: section header table's file offset
			fn.write("\x00\x02\x00\x05")	# e_flags
			fn.write("\x34\x00")	# e_ehsize
			fn.write("\x20\x00")	# e_phentsize
			fn.write("\x00\x00")	# e_phnum
			fn.write("\x28\x00")	# e_shentsize: sections header's  size
			fn.write("\x02\x00")	# e_shnum
			fn.write("\x00\x00")	# e_shstrndx: section header

			# Section Header Table
			fn.write("\x00" * 0x28) 		# null section header
			fn.write("\x00\x00\x00\x00")	# sh_name
			fn.write("\x01\x00\x00\x00")	# sh_type
			fn.write("\x07\x00\x00\x00")	# sh_flags
			fn.write(struct.pack("<I", base_address))	# sh_addr
			fn.write("\x90\x00\x00\x00")	# sh_offset
			fn.write(struct.pack("<I", file_length))	# sh_size
			fn.write("\x00\x00\x00\x00")	# sh_link
			fn.write("\x00\x00\x00\x00")	# sh_info
			fn.write("\x01\x00\x00\x00")	# sh_addralign
			fn.write("\x00\x00\x00\x00")	# sh_entsize

			fn.write("\x00" * 0x0c)			# pad

			# copy source file
			fn.write(fs.read())
			flag = file_length & 0xfff
			if flag != 0:
				fn.write("\x00" * (0x1000 - flag))
				print("[*] add 0x%x pad" % (0x1000 - flag))


if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("usage: %s <little|big endian> <filename> <base_address>" % sys.argv[0])
	else:
		addelfinfo()
