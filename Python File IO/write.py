#Week 4A 

# with open('test.txt', 'r') as rf:
# 	with open('testCOPY.txt', 'w') as wf:

# 		for line in rf:
# 			wf.write(line)

# with open('taeyeon.jpeg', 'rb') as rf:
# 	with open('taeyeon_copy.png', 'wb') as wf:

# 		for line in rf:
# 			wf.write(line)

with open('taeyeon.jpeg', 'rb') as rf:
	with open('taeyeon_copy.png', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)

		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)