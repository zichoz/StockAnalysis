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
								#Reads from the NYSE STOCK FILE

											#
for line in nyseSymbolsCsv:
	currentSymbol = line.split(",")				#Function for making a list with all the stock symbols from the NYSE.CSV
	
	for i in range(len(currentSymbol)):
			nyseStockSymbols.append(currentSymbol[i])


	#will have to make a string which includes all the 100 tickers i want to check out

nyseStockSymbols[3139] = "ZYME"

def readTodaysStockData(stocksToAnalyze):         #Working to make this a function where i can request 100 tickets for each request i can make, as i only can make 2500 a day
	
	dailyQuotes = od.quote(stocksToAnalyze, 'dividendRateAnnual')['results']
	for q in dailyQuotes: 
		stockObj = Stock(q['symbol'], q['name'], q['dayCode'], q['serverTimestamp'], q['mode'], q['lastPrice'], q['tradeTimestamp'], q['netChange'], q['percentChange'], q['unitCode'], q['open'], q['high'], q['low'], q['close'], q['dividendRateAnnual'])
		#print (stockObj.name + "   " + str(stockObj.lastPrice))
		stocks.append(stockObj)





print (((int((int(len(nyseStockSymbols)))/100)))+1)
def gatherInfoAboutNyse(): 
	counterX = 0
	counterY = 99
	#Makes the list And sets the first item as the 100 symbols
	for i in range(0, (((int((int(len(nyseStockSymbols)))/100)))+1)): 
		print (counterY)            #takes 100 symbols from the lists and converts them to one string and then runs the function with them as an argument
		if (counterY > len(nyseStockSymbols)):

			counterY = len(nyseStockSymbols)
			print(" sant" + str(counterY))
			listWithHundredtest= str([nyseStockSymbols[x] for x in range(counterX, counterY)])
			listWithHundredtestTwo = listWithHundredtest.replace("'", "")            # Had to make this to convert the list to one string with all the items combined
			listWithHundredtestThree = listWithHundredtestTwo.replace(" ", "")
			listwithHundredtestFour = listWithHundredtestThree.replace("[", "'")
			someStocks = listwithHundredtestFour.replace("]", "'")
			#print (someStocks + " derp")
			counterX = counterX + 100
			counterY = counterY + 100
			readTodaysStockData(someStocks)
			menu()
		else : 
			print ("usant")
			listWithHundredtest= str([nyseStockSymbols[x] for x in range(counterX, counterY)])
			listWithHundredtestTwo = listWithHundredtest.replace("'", "")            # Had to make this to convert the list to one string with all the items combined
			listWithHundredtestThree = listWithHundredtestTwo.replace(" ", "")
			listwithHundredtestFour = listWithHundredtestThree.replace("[", "'")
			someStocks = listwithHundredtestFour.replace("]", "'")
			#print (someStocks + " derp")
			counterX = counterX + 100
			counterY = counterY + 100
			readTodaysStockData(someStocks)






#readTodaysStockDataFromNyse(someStocks)
#print (len(stockObj))

#readTodaysStockDataFromNyse(str(someStocks))



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
	menu()	
	
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
				print (q.name + "       " +  str(stockYield))
					#print (str(q.name) + "     " + str(stockYield))
					#Checks if the returned variable is not 0 and not None then adds them to the list
		else: 
			noDividendStocks.append(q)
			#adds a stock that does not pay dividend in a list.
	menu()
#readTodaysStockDataFromNyse()


def menu(): 	
	print ("option 1 : load new stockData from NYSE")
	print ("Option 2 : find information about one Stock")
	print ("Option 3 : Find Dividendstocks")
	print ("Option 4 : Quit")

	keyword = int(input("Type a number between 1 - 4 :      "))

	if (keyword == 1): 
		gatherInfoAboutNyse()
	elif (keyword == 2):
		findStockData()
	elif (keyword == 3):
		print ("test")
		findDividendStocks()
	elif (keyword == 4):
		print ("Quitting!")
	else: 
		menu()

menu()