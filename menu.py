from flask import Flask, Response
from twilio import twiml


emergencyMenu = True
	while emergencyMenu == True:
		print():

def inbound_sms():
	response = twiml.Response
	inbound_msg_body = request.form.get("Body")
	inbound_msg_from = request.form.get("From")
	menu =  "Press 1 for an emergency health care, residential, vehicle accident. \n" 
			"Press 2 for a natural disaster tornadoes, thuderstorms, hailsotrms, extreme cold weather. \n "
			"Press 3 if violence or gunshot erupts. \n "
			"Press 4 for an accident or structual failure fire, building collapse, toll or bridge/tunnel accident. \n "
			"Press 5 for a utility incidents power outage, winter storms, severe cold/exposure. \n "


	knowEmergency == input("Do you have an emergency? ").lower()
		if emergencyMenu == "yes" or emergencyMenu == "y":
			userInput = input("Please enter a menu option by the corresponding number: ")
		elif knowEmergency == " no" or emergencyMenu == "n":

		else:
			print("You have entered an invalid response.")


			
