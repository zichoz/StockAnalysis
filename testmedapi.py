import ondemand
from Stock import Stock


od = ondemand.OnDemandClient(api_key='5dbee5d0272ae52936a8cabbdcef6ea6', end_point='https://marketdata.websol.barchart.com/')

quotes = od.quote('DDD,MMM,WBAI,WUBA,EGHT,AHC,ATEN,AAC,AIR,AAN,ABB,ABT,ABBV,ANF,GCH,ACP,JEQ,SGF,ABM,AKR,ACN,ACCO,ATV,ATU,AYI,GOLF,ADX,PEO')['results']


resp = od.get('getQuote', symbols='AAPL,EXC', fields='bid,ask')

stocks = []


for q in quotes: 	#Creates a object and saves it in the list "stocks"
	stockObj = Stock(q['symbol'], q['name'], q['lastPrice'], q['dayCode'])
	counter =+ 1
	stocks.append(stockObj)




def findStockData(): #method for finding stockdata for the user 
	nameSearch = input("What stock do you want to check out?")
	print(nameSearch)
	for q in stocks:
		if nameSearch in q.name:
			print("Name :" + q.name + "   Symbol : " + q.symbol +  "   Last Price :" + str(q.lastPrice))
		
	
			





#def getStockNames():
#	
#	for q in quotes:        #iterates through the list. 
#		print('Symbol: %s, sistepris: %s' % (q['symbol'], q['lastPrice']))
#		name = (q['symbol'])
#		aksjenavn.append(name)
    


#print(len(aksjenavn))
#getStockNames()
#print(len(aksjenavn))







#resp = od.history('ATVI', 'minutes', maxRecords=50, interval=1)
#od = ondemand.OnDemandClient(api_key='5dbee5d0272ae52936a8cabbdcef6ea6')
#I use Barchart.com's API for intra day stock data


#od = ondemand.OnDemandClient(api_key='5dbee5d0272ae52936a8cabbdcef6ea6')
#I use Barchart.com's API for intra day stock data
#odDivdend = ondemand.getDividendData(api_key='5dbee5d0272ae52936a8cabbdcef6ea6', end_point='https://marketdata.websol.barchart.com/')
# get quote data for Apple and Microsoft

#print (resp)
#for r in resp: 
#	print('Symbol: %s, Volume: %s' % (r['symbol'], r['volume']))
#print (od.quote('AMZN,MSFT'))
#divdendPay = od.divdend('AAPL,MSFT')