class Item:
    	def __init__(self, profit, weight):
		    self.profit = profit
		    self.weight = weight


def fractionalKnapsack(W, arr):

	
	arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)

	
	finalvalue = 0.0

	for item in arr:

		
		if item.weight <= W:
			W -= item.weight
			finalvalue += item.profit

		
		else:
			finalvalue += item.profit * W / item.weight
			break
	
	
	return finalvalue


if __name__ == "__main__":
	W = 50
	arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
	max_val = fractionalKnapsack(W, arr)
	print(max_val)
