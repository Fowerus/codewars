# [3]Make a spiral
def spiralize(size):
	def plus(size, pl):
		counter = pl
		item = [0]*size
		left = False
		step = 0

		for j in range(0, size):
			if counter != 0:
				if left:
					item[step] = 1
					step += 2
				else:
					item[size-1-step] = 1
				left = not left
				counter -= 1
			else:
				break

		return item, pl+1

	def minus(size, mi):
		counter = mi
		item = [1]*size
		left = False
		step = 1

		for j in range(0, size):
			if counter != 0:
				if left:
					item[step] = 0
					step += 2
				else:
					item[size-1-step] = 0
				left = not left
				counter -= 1
			else:
				break

		return item, mi+1


	spiral = [0]*(size-2)

	pl = mi = 1
	resign = True
	counter = size-2

	for i in range(0, size-2):
		if resign:
			if counter != 0:
				spiral[i], pl, counter = plus(size, pl) + (counter-1,)
			if counter != 0:
				spiral[size-2-i-1], pl, counter = plus(size, pl) + (counter-1,)

		else:
			if counter != 0:
				spiral[i], mi, counter = minus(size, mi) + (counter-1,)
			if counter != 0:
				if counter == 1:
					mi += 1	
				spiral[size-2-i-1], mi, counter = minus(size, mi) + (counter-1,)

		
		resign = not resign

		if counter == 0:
			break


	return [[1]*size] + spiral + [[1]*size]
