import random
import string
import time
import sys

found = 0
showvalues = True
value = 0
keys = []
temp = []
letters = {
'A':'60','B':'61','C':'62','D':'63','E':'64','F':'65','G':'66','H':'67','I':'68','J':'69','K':'70','L':'71','M':'72','N':'73','O':'74','P':'75','Q':'76','R':'77','S':'78','T':'79','U':'80','V':'81','W':'82','X':'83','Y':'84','Z':'85','0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'
}
try:
	maximum = int(input("How many letters do you want? --> "))
	if maximum < 1:
		print("PLEASE AT LEAST TYPE 1")
		sys.exit()
	print(f"NUMBER OF LETTERS SET TO {maximum}\n")
	show = str(input("Wanna see integer value of the keys? (YES/NO) --> "))
	if show == "YES" or show == "yes" or show == "y" or show == "Y":
		showvalues = True
		print("SHOW VALUES(IF LETTERS NO. LESS THAN 8 IT WON'T APPEAR) : ON\n")
	elif show == "NO" or show == "no" or show == "n" or show == "N":
		showvalues = False
		print("SHOW VALUES : OFF\n")
	else:
		print("PLEASE TYPE YES OR NO")
		sys.exit()
	thelimit = int(input("HOW MANY KEYS DO YOU WANT? --> "))
	print(f"GENERATING {thelimit} KEYS IN A MOMENT.\n")
	if thelimit < 1:
		print("TYPE AT LEAST 1")
		sys.exit()
except ValueError:
	print("PLEASE ENTER AN INTEGER NUMBER")
	sys.exit()
except KeyboardInterrupt:
	print("\n EXITING...")
	sys.exit()
except:
	print("AN ERROR OCCURED PLEASE CHECK YOUR CHOICES")
	sys.exit()
starttime = time.time()
try:
	while True:
		randomkey = "".join(random.choices(string.ascii_uppercase + string.digits, k=maximum))
		for i in randomkey:
			value = value+int(letters[i])
		if maximum * int(letters['O']) <= value <= maximum * int(letters['Z']):
			endtime = time.time()
			found += 1
			print (f"{found} FOUND! in " + str(endtime - starttime) + " s\n")
			for i in range(0, maximum, 4):
				temp.append(randomkey[i:i+4])#here for loop will go like 0 4 8 12 so that we can use it to take 4 characters each
			key = "-".join(temp)
			if showvalues and maximum >= 8:
				finalformat = key + ":" + str(value)
				keys.append(finalformat)
			else:
				keys.append(key)
			temp = []
			value = 0
			if len(keys) == thelimit:
				endtime = time.time()
				final = endtime - starttime
				for key in keys:
					print(key)
				if final < 90:
					print(f"\nTIME TAKEN: {final} s")
				else:
					print("\nTIME TAKEN: " + str(final/60) + " min")
				break
			else:
				pass
		else:
			value = 0
			pass
except KeyboardInterrupt:
	print("\n EXITING...")
	sys.exit()
except:
	print("AN ERROR OCCURED PLEASE CHECK YOUR CODE")
	sys.exit()
