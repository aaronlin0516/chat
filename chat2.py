#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r' ,encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())  #先把多餘的符號清除(strip)再用','切割(split)
	return lines

#轉換檔案
def convert(lines):
	person = None						#先行宣告person，避免一開始沒有person的變數
	aaron_word_count = 0
	aaron_sticker_count = 0
	aaron_image_count = 0
	alex_word_count = 0
	alex_sticker_count = 0
	alex_image_count = 0
	for line in lines:  				#一行一行讀取
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Aaronlin':
			if s[2] == '貼圖':
				aaron_sticker_count += 1
			elif s[2] == '圖片':
				aaron_image_count +=1
			else:
				for m in s[2:]:
					aaron_word_count += len(m)
		elif name == 'Alexlee':
			if s[2] == '貼圖':
				alex_sticker_count += 1
			elif s[2] == '圖片':
				alex_image_count +=1
			else:
				for m in s[2:]:
					alex_word_count += len(m)
	print('Aaron說了', aaron_word_count, '個字')
	print('Aaron貼了', aaron_sticker_count, '貼圖')
	print('Aaron貼了', aaron_image_count, '圖片')
	
	print('Alexlee說了', alex_word_count, '個字')
	print('Alexlee貼了', alex_sticker_count, '貼圖')
	print('Alexlee貼了', alex_image_count, '圖片')

#寫入檔案
def write_file(filename,lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]Alexlee.txt')
	lines = convert(lines)				#回傳出來的值覆蓋掉lines
	#write_file('output.txt', lines)

main()