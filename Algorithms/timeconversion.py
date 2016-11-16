time = raw_input().strip()
hour = time[:2]
hour = int(hour)
if time[8] == "P":
	if hour == 12:
		hour = "12"
	else:
		hour += 12
	hour = str(hour) + time[2:8]
	

elif time[8] == "A":
	
	if hour == 12:
		hour = "00"
		hour = str(hour) + time[2:8]
		
	else:
		print time[:8]


	

	
		
