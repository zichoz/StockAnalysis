import ondemand
from Stock import Stock
from Industry import Industry

od = ondemand.OnDemandClient(api_key='5dbee5d0272ae52936a8cabbdcef6ea6', end_point='https://marketdata.websol.barchart.com/')
#The stocks i use are just random picked from the stock exchange
quotes = od.quote('DDD,MMM,WBAI,WUBA,EGHT,AHC,ATEN,AAC,AIR,AAN,ABB,ABT', 'dividendRateAnnual')['results']
nyseSymbolsCsv = open('NYSE.csv','r')
industriTxt = open('Betas.txt','r')

resp = od.get('getQuote', symbols='AAPL,EXC', fields='bid,ask')
#Lists i user
stocks = []
industries = []
nyseStockSymbols = []

"""
for q in quotes: 	#Creates a object and saves it in the list "stocks"
	stockObj = Stock(q['symbol'], q['name'], q['dayCode'], q['serverTimestamp'], q['mode'], q['lastPrice'], q['tradeTimestamp'], q['netChange'], q['percentChange'], q['unitCode'], q['open'], q['high'], q['low'], q['close'], q['dividendRateAnnual'])
	counter =+ 1
	#print(stockObj.dividendRateAnnual)
	stocks.append(stockObj)
"""
#This reades the file to find the industry information

#industryObj = Industry()
						#reads the industry information from industries.txt and creates and object for each industry and puts it in the list: industries[]





								#Reads from the NYSE STOCK FILE

											#
for line in nyseSymbolsCsv:
	currentSymbol = line.split(",")				#Function for making a list with all the stock symbols from the NYSE.CSV
	
	for i in range(len(currentSymbol)):
			nyseStockSymbols.append(currentSymbol[i]+",")

someStocks = (nyseStockSymbols[622]+ nyseStockSymbols[352])		
print (someStocks)
nyseStockSymbols[3139] = "ZYME"


def readTodaysStockDataFromNyse():         #Working to make this a function where i can request 100 tickets for each request i can make, as i only can make 2500 a day

	dailyQuotes = od.quote(someStocks, 'dividendRateAnnual')['results']
	for q in dailyQuotes: 
		stockObj = Stock(q['symbol'], q['name'], q['dayCode'], q['serverTimestamp'], q['mode'], q['lastPrice'], q['tradeTimestamp'], q['netChange'], q['percentChange'], q['unitCode'], q['open'], q['high'], q['low'], q['close'], q['dividendRateAnnual'])
		print (stockObj.name)
		stocks.append(stockObj)




#print (len(stockObj))





for line in industriTxt:
	currentline = line.split(",")
	#print(currentline[0] + "  "+currentline[2])
	industryObj = Industry(currentline[0], currentline[1], currentline[2], currentline[3], currentline[4], currentline[5], currentline[6], currentline[7], currentline[8], currentline[9],  currentline[10])
	#print (industryObj.beta)
	industries.append(industryObj)
	#industryObj = Industry(str(currentline[0]) + int(currentline[1])+float(currentline[2]))
			
"""print (len(industries))
for q in industries: 
	print (q.industryName + " " + q.unleveredBeta)
"""


def findStockData(): #method for finding stockdata for the user 
	nameSearch = input("What stock do you want to check out?")
	print(nameSearch)
	for q in stocks:
		if nameSearch in q.name:
			print("Name :" + q.name + "   Symbol : " + q.symbol +  "   Last Price :" + str(q.lastPrice))
		
	
text_file = open("Output.txt", "w")
for q in stocks:

	text_file.write(q.name + ", ")
text_file.close()

dividendStocks = []
noDividendStocks = []
stockYield = 0.00
def findDividendStocks(): #functions from finding dividendStocks from iterating throug the Stocks list 
	noDividendStock = "0"
	for q in stocks:
			if (q.dividendRateAnnual != "0"): 
				if (q.dividendRateAnnual != None): 
					dividendStocks.append(q)
					stockYield = float(q.dividendRateAnnual)/float(q.lastPrice)
					#print (str(q.name) + "     " + str(stockYield))
					#Checks if the returned variable is not 0 and not None then adds them to the list
			else: 
				noDividendStocks.append(q)
				#adds a stock that does not pay dividend in a list.

#readTodaysStockDataFromNyse()