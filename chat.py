
def read_file(filename):
	lines = []
	with open(filename, 'r') as f:
		for line in f:
			lines.append(line.strip())  #先把多餘的符號清除(strip)再用','切割(split)
	return lines

def convert(lines):
	new = []
	person = None						#先行宣告person，避免一開始沒有person的變數
	for line in lines:  				#一行一行讀取
		if line == 'Aaron':				#如果line=Aaron的話，把Aaron的值存進去person
			person = 'Aaron'
			continue
		elif line == 'Tom':				#如果line=Tom的話，把Tom的值存進去person
			person = 'Tom'
			continue
		if person:						#如果person有值，就會執行下面code
			new.append(person + ': ' + line)
	return new

def write_file(filename,lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)				#回傳出來的值覆蓋掉lines
	write_file('output.txt', lines)

main()