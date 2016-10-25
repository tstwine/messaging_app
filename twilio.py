from twilio.rest import TwilioRestClient

# messaging Regional to State Leader to Team Leaders

ACCOUNT_SID = "ACaaaaf1975e4dcc6dde6d42ddda6743e"
AUTH_TOKEN = "8b17826f30ea9747c8a3c381e198b196"
client = TwilioRestClient(account_sid, auth_token)

client.messages.create(
	to="+12153338800" #RL
	from="+12155551212" #SL
	body="You have 10 TL, 8 TM. You have to assign the vans for TL." #SL
	#url="https://twilio.com/user/account"
	)

client.messages.create(
	to="+12155551212" #SL
	from="+12153338800" #RL
	body="Text me the van information, so I can assign them to TL." #RL
	) 

client.messages.create(
	to="+12157898671" #TL
	from="+12153338800" #RL
	body="How many TM do I have in my group?" #TL
	

client.messages.create(
	to="+12157898671" #TL
	from="+12155551212"#SL
	body="One of the vans is missing the vehicle registration. \n" #TL
		  "The RL told me to contact you about it. \n" #TL
		  "Can you assist with locating the van registration.\n" #TL
	
)


	