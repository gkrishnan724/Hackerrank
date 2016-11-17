x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

vrel1 = v2 - v1
flag = 0
if vrel1 > 0:
	if x2 > x1:
		print "NO"
	else:
		while(x2<=x1):
			if x1 == x2:
				print "YES"
				flag = 1
				break
				
			else:
				x2 += v2
				x1 += v1
		if flag == 0:
			print "NO"


elif vrel1 < 0:
	if x2 < x1:
		print "NO"
	else:
		while(x1<=x2):
			if x1 == x2:
				print "YES"
				flag = 1
				break 
				
			else:
				x2 += v2
				x1 += v1
		if flag == 0:
			print "NO"


else:
	if x2 == x1:
		print "YES"
	else:
		print "NO"




