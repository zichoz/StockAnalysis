class Stock:
	stockCount= 0
	#Creates a object for each stock where the name and last price is saved 
	def __init__(self, symbol, name, lastPrice, dayCode):	
		self.symbol = symbol
		self.name = name
		self.lastPrice = lastPrice
		self.dayCode = dayCode
		Stock.stockCount += 1
		#print("nå er jeg inni klassen")
