# pass: Does nothing and continues to the next statement.
# continue: Skips the current iteration of a loop and proceeds to the next iteration.
# break: Exits the loop entirely.

from datetime import datetime

print(datetime.now().second)

# write a while loop that wait 2 seconds before printing

wait_until = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until:
	pass
print (f'we are at {wait_until} seconds!')

wait_until = (datetime.now().second + 2) % 60

while True:
	if datetime.now().second < wait_until:
		continue
	break
print (f'we are at {wait_until} seconds!') 






















































