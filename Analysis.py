import ondemand
from Stock import Stock
from Industry import Industry

od = ondemand.OnDemandClient(api_key='5dbee5d0272ae52936a8cabbdcef6ea6', end_point='https://marketdata.websol.barchart.com/')
#The stocks i use are just random picked from the stock exchange
quotes = od.quote('DDD,MMM,WBAI,WUBA,EGHT,AHC,ATEN,AAC,AIR,AAN,ABB,ABT,ABBV,ANF,GCH,ACP,JEQ,SGF,ABM,AKR,ACN,ACCO,ATV,ATU,AYI,GOLF,ADX,PEO,AGRO,ADNT,ATGE,AAP,ADSW,WMS,ASX,ASIX,AAV,AVK,AGC,LCM,ACM,ANW,AEB,AED,AEG,AEH,AEK,AER,HIVE,AJRD,AET,AMG,AFL,MITT,MITT^A,MITT^B,AGCO,A,AEM,ADC,AGU,AL,APD,AYR,AKS,ALP^Q,ALG,AGI,ALK,AIN,ALB,AA,ALEX,ALX,ARE,ARE^D,AQN,BABA,Y,ATI,ALLE,AGN,AGN^A,ALE,AKP,ADS,AFB,AOI,AWF,AB,LNT,CBH,NCV,NCZ,ACV,NIE,NFJ,ALSN,ALL,ALL^A,ALL^B,ALL^C,ALL^D,ALL^E,ALL^F,ALLY,ALLY^A,ALDW,AGD,AWP,AOD,AYX,ATUS,RESI,MO,ACH,AMBR,ABEV,AMC,AEE,AMRC,AMOV,AMX,AAT,AXL,ACC,AEO,AEP,AEL,AXP,AFG,AFGE,AFGH,AMH,AMH^C,AMH^D,AMH^E,AMH^F,AMH^G,AIG,AIG.WS,AMID,ARL,ARA,AWR', 'dividendRateAnnual')['results']


resp = od.get('getQuote', symbols='AAPL,EXC', fields='bid,ask')

stocks = []
industries = []
industriTxt = open('Betas.txt','r')
for q in quotes: 	#Creates a object and saves it in the list "stocks"
	stockObj = Stock(q['symbol'], q['name'], q['dayCode'], q['serverTimestamp'], q['mode'], q['lastPrice'], q['tradeTimestamp'], q['netChange'], q['percentChange'], q['unitCode'], q['open'], q['high'], q['low'], q['close'], q['dividendRateAnnual'])
	counter =+ 1
	stocks.append(stockObj)

#This reades the file to find the industry information

#industryObj = Industry()

for line in industriTxt:
		for line in industriTxt:
			currentline = line.split(",")
			print(currentline[0] + "  "+currentline[2])
			industryObj = Industry(currentline[0], currentline[1], currentline[2], currentline[3], currentline[4], currentline[5], currentline[6], currentline[7], currentline[8], currentline[9],  currentline[10])
			print (industryObj.beta)
			industries.append(industryObj)
			#industryObj = Industry(str(currentline[0]) + int(currentline[1])+float(currentline[2]))
			
print (len(industries))
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
def findDividendStocks(): #functions from finding dividendStocks from iterating throug the Stocks list 
	noDividendStock = "0"
	for q in stocks:
			if (q.dividendRateAnnual != "0"): 
				if (q.dividendRateAnnual != None): 
					dividendStocks.append(q)
					#Checks if the returned variable is not 0 and not None then adds them to the list
			else: 
				noDividendStocks.append(q)
				#adds a stock that does not pay dividend in a list.

