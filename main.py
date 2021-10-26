from flask import Flask,render_template, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import json
from openpyxl import load_workbook
import openpyxl
import random

app = Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
@cross_origin()
def webhook():
	print('webhook')
	req = request.get_json(silent=True, force=True)
	res = processRequest(req)
	res = json.dumps(res, indent=4)
	print(res)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r
def processRequest(req):
	foods=[]
	food_name=['firstfood','2food','3food']
	quantity=['firstfood','2food','3food']
	qun=[]
	Ttime=0
	count=0
	Tprice=0
	print('processRequest')
	result = req.get("queryResult")
	intent = result.get("intent").get('displayName')
	query_text = result.get("queryText")
	filepath='./Excelfile/indian_food.xlsx'
	opn=openpyxl.load_workbook(filepath)
	opnsheet=opn.active
	frows=len(opnsheet['A'])
	trows=len(opnsheet['B'])
	prows=len(opnsheet['D'])

	
	if intent=='items_description':
		try:
			for i in range(1,4):
				name='food_items_entity'+str(i)
				# print(name)
				quntity='quantity'+str(i)
				# print(quntity)
				fn=result.get("parameters").get(name)[0]
				food_name[i-1]=fn
				print('len(food_name_____)'+str(food_name))
				qn=result.get("parameters").get(quntity)[0]
				quantity[i-1]=qn
			# print(food_name)
			# print(quantity)
				for j in range(2,frows+1):
					maf=opnsheet['A'+str(j)]
					ma1=maf.value
					# print("..............."+str(ma1))
					if ma1==food_name[i-1]:
						getprice=opnsheet['E'+str(j)].value
						gettime=opnsheet['B'+str(j)].value
						print(gettime,getprice)
						Tprice=Tprice+(int(float(quantity[0]))*int(float(getprice)))
						Ttime=Ttime+int(float(gettime))
						foods.append(food_name[i-1])
						print('foods...........',foods)
						qun.append(quantity[i-1])
						print('qun.............',qun)
						count=count+1
						break
		except Exception as E:
			print(E)
			if count>1:
				pass
			else:
				print('error')	
				webhookresponse="This Not A Proper way to order food.TYPE orderrule"



		print('intentt'+str(intent))
		print('intenffffftt'+str(food_name))

		print('intenqqqqqqq'+str(quantity))
		print('query text'+str(qun))
		print("len(qun)===="+str(len(qun)))
		if len(qun)==1:
			webhookresponse="Done,The order is placed for "+str((quantity[0]))+" "+str((food_name[0]))+" and the price is "+str(Tprice)+".It will arrive within "+str(Ttime)+" mins"
		elif len(qun)==2:
			webhookresponse="Done,The order is placed for "+str((quantity[0]))+" "+str((food_name[0]))+" and "+str((quantity[1]))+" "+str((food_name[1]))+" and the price is "+str(Tprice)+".It will arrive within "+str(Ttime)+" mins"
		elif len(qun)==0:
			pass
		else:
			Ttime=Ttime/3
			Ttime=round(Ttime)
			webhookresponse="Done,The order is placed for "+str((quantity[0]))+" "+str((food_name[0]))+","+str((quantity[1]))+" "+str((food_name[1]))+" and "+str((quantity[2]))+" "+str((food_name[2]))+" and the price is "+str(Tprice)+".It will arrive within "+str(Ttime)+" mins"

		return {

            "fulfillmentMessages": [
                {
                    "text": { 
                        "text": [
                            webhookresponse
                        ]

                    }
                }]}
	if intent=='user_order_id':
		ordernumber=result.get('parameters').get('order_id')
		if nofdig(ordernumber)==5:
			minl=random.randint(1,30)
			ordernumber=round(ordernumber)
			if minl<=10:
				webhookresponse="Order Status For Order_id:"+str(ordernumber)+"The delivery guy is in your locality will arrive with in "+str(minl)+" mins"
			elif minl<=20:
				webhookresponse="Order Status For Order_id:"+str(ordernumber)+"The delivery guy has just left the restaurant will arrive with in "+str(minl)+" mins"
			else:
				webhookresponse="Order Status For Order_id:"+str(ordernumber)+"The food is ready waiting for the delivery guy. will arrive with in "+str(minl)+" mins"
		else:
			webhookresponse="Sorry,Wrong Order Id(Order_id must be 5 digits)"			

		return {
    	"fulfillmentMessages":[
    	{
    		"text":{
    		"text":[
    				webhookresponse
    		]
    		}
    	}]
    	}	

    
    # return render_template("loginpage.html")	
def nofdig(n):
	count=0
	while(n>0):
	    count=count+1
	    n=n//10
	return count

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

if __name__=='__main__':
	app.run(port=5000, debug=True)
