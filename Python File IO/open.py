#Week4A 28.9.19

# f =open('test.txt' , 'r')    # r - read

# print(f.name)

# f.close()

# with open('test.txt', 'a') as g:

# 	g.write('This is line number 6'+"\n")

with open('test.txt', 'r') as f:

	# for line in f:
	# 	print(line,end='')

	size_to_read = 500
	f_text = f.read(size_to_read)

	while len(f_text) > 0:
		print(f_text,end='')


	# f-text = f.readline()
	# print(f_text,end='')

	# f_text = f.readline()
	# print(f_text,end='')



	# f_text = f.read(500)
	# print(f_text,end='')

	# g = open('test.txt', 'a')
	# i = g.write('This is line number 6'+"\n")
	# print(i,end='')