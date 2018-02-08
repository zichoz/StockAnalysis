class Stock:
	
	#Creates a object for each stock where the name and last price is saved 
	def __init__(self, symbol, name, dayCode, serverTimestamp, mode, lastPrice, tradeTimestamp, netChange, percentChange, unitCode, open, high, low, close, dividendRateAnnual):	
		self.symbol = symbol
		self.name = name
		self.dayCode = dayCode
		self.serverTimestamp = serverTimestamp
		self.mode = mode
		self.lastPrice = lastPrice
		self.tradeTimestamp = tradeTimestamp
		self.netChange = netChange
		self.percentChange = percentChange
		self.unitCode = unitCode
		self.open = open
		self.high = high
		self.low = low
		self.close = close
		self.dividendRateAnnual = dividendRateAnnual
		