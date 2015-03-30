import random 
import timeit

#A = [1, 4, 6, 3, 6, 20, 39, 1, 2, 124, 53, 24, 35]

def swap(A, i, j):
	temp = A[i] 
	A[i] = A[j]
	A[j] = temp

	
def medianPartition(A, p, r, pivot):
	#calculate online median
	leftCounts = [0,0]
	rightCounts = [0,0]
	leftLow = rightLow = -float('inf')
	leftHigh = rightHigh = float('inf')
	
	i = p - 1
	for j in xrange(p, r + 1):
		curr = A[j]

		if curr < pivot or (curr == pivot and random.random() < 0.5):
			if leftLow != leftHigh: 
				if leftCounts[0] < leftCounts[1]:
					leftCounts[0] += 1
					if curr > leftLow:
						leftLow = curr
				else:
					leftCounts[1] += 1
					if curr < leftHigh:
						leftHigh = curr
				if leftLow > leftHigh:
					temp = leftLow
					leftLow = leftHigh
					leftHigh = temp
		
			i += 1
			swap(A, i, j)
		else:
			if rightLow != rightHigh:
				if rightCounts[0] < rightCounts[1]:
					rightCounts[0] += 1
					if curr > rightLow:
						rightLow = curr
				else:
					rightCounts[1] += 1
					if curr < rightHigh:
						rightHigh = curr
				if rightLow > rightHigh:
					temp = rightLow
					rightLow = rightHigh
					rightHigh = temp
	#print pivot, leftLow, leftHigh, rightLow, rightHigh, A

	return i + 1, float((leftLow + leftHigh) / 2), float((rightLow + rightHigh) / 2)
	
#QuickSort with informed pivot. A: list, l:left-most index, r: right-most index, pivot: pivot value
def quickSortIP(A, p, r, pivot):
	if p < r:
		q, leftPivot, rightPivot = medianPartition(A, p, r, pivot)
		
		quickSortIP(A, p, q - 1, leftPivot)
		quickSortIP(A, q, r, rightPivot)



#randomized quicksort first iter, informed pivot quicksort next iters 
def partition(A, p, r):

	#calculate online median
	leftCounts = [0,0]
	rightCounts = [0,0]
	leftLow = rightLow = -float('inf')
	leftHigh = rightHigh = float('inf')
	
	pivot = A[r]
	i = p - 1
	for j in xrange(p, r):
		curr = A[j]
		if curr <= pivot:
			if leftLow != leftHigh: 
				if leftCounts[0] < leftCounts[1]:
					leftCounts[0] += 1
					if curr > leftLow:
						leftLow = curr
				else:
					leftCounts[1] += 1
					if curr < leftHigh:
						leftHigh = curr
				if leftLow > leftHigh:
					temp = leftLow
					leftLow = leftHigh
					leftHigh = temp
		
				
			i += 1
			swap(A, i, j)
		else:
			if rightLow != rightHigh:
				if rightCounts[0] < rightCounts[1]:
					rightCounts[0] += 1
					if curr > rightLow:
						rightLow = curr
				else:
					rightCounts[1] += 1
					if curr < rightHigh:
						rightHigh = curr
				if rightLow > rightHigh:
					temp = rightLow
					rightLow = rightHigh
					rightHigh = temp
	
	#print leftLow, leftHigh, rightLow, rightHigh, A
	swap(A, i + 1, r)
	return i + 1, float((leftLow + leftHigh) / 2), float((rightLow + rightHigh) / 2)
	
	

def randomizedQuicksortIP(A, p, r):
	pivotIndex = random.randint(p, r)
	swap(A, pivotIndex, r)
	q, leftPivot, rightPivot = partition(A, p, r)
	
	quickSortIP(A, p, q - 1, leftPivot)
	quickSortIP(A, q, r, rightPivot)
	

#timeit.timeit('randomizedQuicksortIP(A, 0, len(A) - 1)')
#randomizedQuicksortIP(A, 0, len(A) - 1)

print min(timeit.Timer('a=A[:];randomizedQuicksortIP(A, 0, len(A) - 1)').repeat(7))
#print A




