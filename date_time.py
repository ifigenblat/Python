from datetime import datetime

print(datetime.now().second)

# write a while loop that wait 2 seconds before printing

wait_until = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until:
	pass
print (f'we are at {wait_until} seconds!')

#pass - 
#break - break the loop
#continue - skip the line that follow it.

wait_until = (datetime.now().second + 2) % 60

while True:
	if datetime.now().second < wait_until:
		continue
	break
print (f'we are at {wait_until} seconds!') 






















































