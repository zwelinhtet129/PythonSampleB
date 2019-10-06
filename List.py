#week5B 6.10.2019

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.append('coconut')
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut']
>>> fruits.extend('cucumber')
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut', 'c', 'u', 'c', 'u', 'm', 'b', 'e', 'r']
>>> fruits.extend('apple')
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut', 'c', 'u', 'c', 'u', 'm', 'b', 'e', 'r', 'a', 'p', 'p', 'l', 'e']
>>> fruits.clear()
>>> fruits
[]
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut']
>>> fruits.reverse()
>>> fruits
['coconut', 'banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.remove('apple')
>>> fruits
['coconut', 'banana', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut']
>>> fruits.index('kiwi')
4
>>> fruits.reverse()
>>> fruits
['coconut', 'banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.index('apple')
2
>>> fruits.index('apple')
2
>>> fruits.index('apple')
2
>>> fruits.index('apple')
2
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'coconut', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'


>>> student=['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko']
>>> student
['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko']
>>> student.append('Phyu Phyu')
>>> student.append('Ni Ni')
>>> student
['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko', 'Phyu Phyu', 'Ni Ni']
>>> student.remove('Mya Mya')
>>> student
['Mg Mg', 'Aye Aye', 'Ko Ko', 'Phyu Phyu', 'Ni Ni']
>>> student.pop()
'Ni Ni'
>>> student
['Mg Mg', 'Aye Aye', 'Ko Ko', 'Phyu Phyu']


>>> from collection import deque
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'collection'
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Micheal"])
>>> queue.append('Terry')
>>> queue.append('Graham')
>>> queue
deque(['Eric', 'John', 'Micheal', 'Terry', 'Graham'])
>>> queue.popleft()
'Eric'
>>> queue.popleft()
'John'
>>> queue
deque(['Micheal', 'Terry', 'Graham'])
>>> 


>>> cube = []
>>> for i in range(10):
...     cube.append(i**2)
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube = []
>>> for i in range(20):
...     cube.append(i**3)
>>> cube
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> cube.clear()
>>> 
>>> cube = list(map(lambda x: x**3, range(10)))
>>> cube
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> cube = [x**3 for x in range(10)]
>>> cube
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]




>>> [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x !=y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

>>> combs =[]
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...             if x!=y:
...                     combs.append((x,y))
... 
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> transposed = []
>>> for i in range(4):
...     transposed_row=[]
...     for row in matrix:
...             transposed_row.append(row[i])
...     transposed.append(transposed_row)
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]