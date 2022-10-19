def bs(seq,val):
	left = 0
	right = len(seq) -1
	mid = (len(seq))//2
	if int(seq[mid]) == val:
		    return mid
	elif int(seq[mid])>val:
		    right = mid-1
	elif int(seq[mid])<val:
		    left = mid+1
	mid = (right+left)//2

	return bs(seq,val)
