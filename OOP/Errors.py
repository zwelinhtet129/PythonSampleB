# try:
# 	text = input('Enter Something--> ')
# except EOFError:
# 	print('Why did you do an EOF on me')
# except KeyboardInterrupt:
# 	print('You cancelled the operation.')
# else:
# 	print('You entered.{}'.format(text))
#
# class ShortInputException(Exception):
# 	def __init__(self, length,atleast):
# 		Exception .__init__(self)
# 		self.length = length
# 		self.atleast = atleast
#
# try:
# 	text = input('Enter something-->')
# 	if len(text) < 3:
# 		raise ShortInputException(len(text), 3)
# except EOFError:
# 	print('Why did you do an EOF on me?')
#
# except ShortInputException as ex:
# 	print(('ShortInputException: The input was '
# 		'{0} long, excepted at least{1}').format(ex.length, ex.atleast))
# else:
# 	print('No exception was raised.')

import sys
import time

f = None
try:
	f = open('poem.txt')

	while Trun:
		line = f.readline()
		if len(line) == 0:
			break
		print(line, end='')
		sys.stdout.flush()
		print('Press ctrl+c now')

		time.sleep(2)

except IOError:
	print('Could not find poem.txt')
except KeyboardInterrupt:
	print('!! You cancelled the reading from the file.')

finally:
	if f:
		f.close()
	print('(Cleaning up : Closed the file)')

