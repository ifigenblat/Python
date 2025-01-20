import threading
import time

results = {}

def longSqure(num, results):
	time.sleep(1)
	results[num] = num **2

# print([longSqure(n, results) for n in range(0,5)])

start = time.time()

t1 = threading.Thread(target=longSqure, args=(1, results))
t2 = threading.Thread(target=longSqure, args=(2, results))

t1.start()
t2.start()

t1.join()
t2.join()

print(results)
print(f'Two threads took {time.time() - start} seconds to execute')

'''
It's a common pattern to put all these in a list
t1 = threading.Thread(target=longSqure, args=(1, results))
t2 = threading.Thread(target=longSqure, args=(2, results))

t1.start()
t2.start()

t1.join()
t2.join()

For examnple:
'''

def longSqure(num, results):
	time.sleep(1)
	results[num] = num **2

results = {}

start = time.time()

threads = [threading.Thread(target=longSqure, args=(n,results)) for n in range(0, 100)]
[t.start() for t in threads]
[t.join() for t in threads]

print(results)
print(f'Multi threads took {time.time() - start} seconds to execute')