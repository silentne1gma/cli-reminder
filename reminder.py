#!/bin/python3
import sys
import time
import random
import webbrowser
help_message = 	'''
	Welcome to reminder, A cli tool to reminde you of stuff\n
	made by : silentne1gma \n
	help : \n
	first argument must be the time you want to be reminded in \n
	you can set it to hours with "-h", minutes with "-m" and "-s" for seconds \n
	here is an example : \n
	reminder.py -m 3 "feed the cat" \n
	this will reminde me to feed the cat in 3 minutes\n
	notice how I added the double quotes when I added the reminder name\n
	make sure that you don't forget them as they are important for this to work
		'''

url = [
	"https://www.youtube.com/watch?v=TQ5U6LRY9vY&list=PL7i3LZxVlNlz_ALLo0Jyir0GG7VR6ZDQ_&index=9",
	"https://www.youtube.com/watch?v=SPO9M9thekA&list=PL7i3LZxVlNlz_ALLo0Jyir0GG7VR6ZDQ_&index=12",
	"https://www.youtube.com/watch?v=2yDwDKy1YtM&list=PL7i3LZxVlNlz_ALLo0Jyir0GG7VR6ZDQ_&index=13",
	"https://www.youtube.com/watch?v=D70adBEEv-s&list=PL7i3LZxVlNlz_ALLo0Jyir0GG7VR6ZDQ_&index=15",
	"https://www.youtube.com/watch?v=lp8C0GJ8xXU&list=PL7i3LZxVlNlz_ALLo0Jyir0GG7VR6ZDQ_&index=18",
	"https://www.youtube.com/watch?v=K82eddpJ0SI&list=PL7i3LZxVlNlz_ALLo0Jyir0GG7VR6ZDQ_&index=23",
	"https://www.youtube.com/watch?v=kaBmFLLYD2A&list=PL7i3LZxVlNlz_ALLo0Jyir0GG7VR6ZDQ_&index=25",
	"https://www.youtube.com/watch?v=B6zV4fcktc4&list=PL7i3LZxVlNlz_ALLo0Jyir0GG7VR6ZDQ_&index=26",
	"https://www.youtube.com/watch?v=YVgMUiAz6wU&list=PL7i3LZxVlNlz_ALLo0Jyir0GG7VR6ZDQ_&index=30",
	"https://www.youtube.com/watch?v=etH_NGhkhbU&list=PL7i3LZxVlNlz_ALLo0Jyir0GG7VR6ZDQ_&index=34"
]

if len(sys.argv) != 4:
	exit(help_message)

time_unit = sys.argv[1]
str_time = sys.argv[2]
int_time = int(str_time)
reason = sys.argv[3]
if time_unit == "-s":
	print(f"ok, reminding you to {reason} in {int_time} seconds, a shipost video will pop up")
	time.sleep(int_time)
	webbrowser.open(random.choice(url), new=2)
	print(f"{int_time} seconds have passed get your things done")
elif time_unit == "-m":
	print(f"ok, reminding you to {reason} in {int_time} minutes, a shipost video will pop up")
	time.sleep(int_time * 60)
	webbrowser.open(random.choice(url), new=2)
	print(f"{int_time} minutes have passed, get up and {reason}")
elif time_unit == "-h":
	print(f"ok, reminding you to {reason} in {int_time} hours, don't close this window. a shipost video will pop up")
	time.sleep(int_time * 3600)
	webbrowser.open(random.choice(url), new=2)
	print(f"{int_time} hours have passed, did you {reason}?")
