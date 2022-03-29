from colorama import Fore, Style
import sys
file_name = ""
debug = False
if len(sys.argv) >= 2:
	for arg in sys.argv:
		if ".box" in arg:
			file_name = arg
		if "-debug" in arg:
			debug = True
		if "-help" in arg:
			print(Fore.CYAN + "Usage:" + Style.RESET_ALL + " python main.py FILE_NAME.box\n" + Fore.CYAN + "Flags:" + Style.RESET_ALL + "\n-debug (Show hor, diag and ver for each stage)\n-help (Show this help command)\n" + Fore.CYAN + "Documentation:" + Style.RESET_ALL + " [Add link to docs or something]")
			exit()
else:
	print(Fore.CYAN + "Usage:" + Style.RESET_ALL + " python main.py FILE_NAME.box\n" + Fore.CYAN + "Flags:" + Style.RESET_ALL + "\n-debug (Show hor, diag and ver for each stage)\n-help (Show this help command)\n" + Fore.CYAN + "Documentation:" + Style.RESET_ALL + " [Add link to docs or something]")
	exit()
def load():
	try:
		file = open(file_name, 'r')
		return file.readline().replace('\n', '').split(','), file.readline().replace('\n', '').split(','), file.readline().replace('\n', '').split(',')
	except FileNotFoundError:
		print("File not found")
		exit()
  
hor, diag, ver = load()

def check():
	if len(hor) > 0 and len(diag) > 0 and len(ver) > 0:
		return True
	return False

def check_math():
	if str(hor[0]).find("save") == -1 and str(hor[0]).find("out") == -1:
		if str(hor[0]).find('+') != -1 or str(hor[0]).find('-') != -1 or str(hor[0]).find('*') != -1 or str(hor[0]).find('/') != -1:
			hor[0] = math(hor[0])
	if str(diag[0]).find("save") == -1 and str(diag[0]).find("out") == -1:
		if str(diag[0]).find('+') != -1 or str(diag[0]).find('-') != -1 or str(diag[0]).find('*') != -1 or str(diag[0]).find('/') != -1:
			diag[0] = math(diag[0])
	if len(diag)-1 > 0:
		if str(diag[1]).find("save") == -1 and str(diag[1]).find("out") == -1:
			if str(diag[1]).find('+') != -1 or str(diag[1]).find('-') != -1 or str(diag[1]).find('*') != -1 or str(diag[1]).find('/') != -1:
				diag[1] = math(diag[1])
	if str(ver[0]).find("save") == -1 and str(ver[0]).find("out") == -1:
		if str(ver[0]).find('+') != -1 or str(ver[0]).find('-') != -1 or str(ver[0]).find('*') != -1 or str(ver[0]).find('/') != -1:
			ver[0] = math(ver[0])

def math(s):
	if s.find('+') != -1:
		a, b = s.split('+')
		return str(int(a) + int(b))
	if s.find('-') != -1:
		a, b = s.split('-')
		return str(int(a) - int(b))
	if s.find('*') != -1:
		a, b = s.split('*')
		return str(int(a) * int(b))
	if s.find('/') != -1:
		a, b = s.split('/')
		return str(int(a) // int(b))

storage = {}

def check_save():
	if str(hor[0]).find("save") != -1:
		save(hor[0])
		hor[0] = "0"
	if str(diag[0]).find("save") != -1:
		save(diag[0])
		diag[0] = "0"
	if len(diag)-1 > 0:
		if str(diag[1]).find("save") != -1:
			save(diag[1])
			diag[1] = "0"
	if str(ver[0]).find("save") != -1:
		save(ver[0])
		ver[0] = "0"

def save(s):
	commands = s.split('-')
	commands.pop(0)
	for command in commands:
		a, index = command.split("to")
		arr = ""
		i = ""
		if a.find("hor") != -1:
			arr = a[:3]
			i = a[3:len(a)]
		elif a.find("diag") != -1:
			arr = a[:4]
			i = a[4:len(a)]
		elif a.find("ver") != -1:
			arr = a[:3]
			i = a[3:len(a)]
		exec(f"storage[{index}] = {arr}[{i}]")

def check_load():
	if hor[0].find("load") != -1:
		load(hor[0], "hor[0]")
	if diag[0].find("load") != -1:
		load(diag[0], "diag[0]")
	if len(diag)-1 > 0:
		if diag[1].find("load") != -1:
			load(diag[1], "diag[1]")
	if ver[0].find("load") != -1:
		load(ver[0], "ver[0]")
	
def load(s, temp):
	commands = s.split('-')
	commands.pop(0)
	for command in commands:
		index, a = command.split("to")
		arr = ""
		i = ""
		if a.find("hor") != -1:
			arr = a[:3]
			i = a[3:len(a)]
		elif a.find("diag") != -1:
			arr = a[:4]
			i = a[4:len(a)]
		elif a.find("ver") != -1:
			arr = a[:3]
			i = a[3:len(a)]
		exec(temp+"=0")
		exec(f"{arr}[{i}] = storage[{index}]")
		check_input()
		check_math()
		check_save()

def check_input():
	if hor[0] == 'i':
		hor[0] = input()
	if diag[0] == 'i':
		diag[0] = input()
	if len(diag)-1 >0:
		if diag[1] == 'i':
			diag[1] = input()
	if ver[0] == 'i':
		ver[0] = input()

def check_output():
	if str(hor[0]).find("-out") != -1:
		print(chr(int(hor[0].split("-out")[0])), end="")
		hor[0] = 0
	if str(diag[0]).find("-out") != -1:
		print(chr(int(diag[0].split("-out")[0])), end="")
		diag[0] = 0
	if len(diag)-1 > 0:
		if str(diag[1]).find("-out") != -1:
			print(chr(int(diag[1].split("-out")[0])), end="")
			diag[1] = 0
	if str(ver[0]).find("-out") != -1:
		print(chr(int(ver[0].split("-out")[0])), end="")
		ver[0] = 0

while check():
	print("Debug: ", hor, diag, ver, storage) if debug == True else print(end="")
	check_save()
	check_load()
	check_save()
	check_math()
	check_output()
 	
	diag[0] = str(max(int(hor[0]), int(diag[0]), int(diag[min(1, len(diag)-1)]), int(ver[0])))
	hor.pop(0)
	diag.pop(min(len(diag)-1, 1))
	ver.pop(0)
