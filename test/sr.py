import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import smtplib, ssl
import getpass
import time

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "attacker.chingari@gmail.com"
receiver_email = "faceprepindia@gmail.com"
print ("Please Enter Sender's (attacker.chingari@gmail.com) Password")
passwd = getpass.getpass("b0t:~#> ")
message = """\
Subject: ALERT!

Your name has been called by faculty."""

context = ssl.create_default_context()

r = sr.Recognizer()

while True:
	
	try:
		
		with sr.Microphone() as source:
			print("Listening...")
			r.adjust_for_ambient_noise(source)
			voice = r.listen(source)
			text = r.recognize_google(voice)
			text = text.lower()
			
			if 'bob' in text:
				print(text)
				sound = AudioSegment.from_mp3('voice.mp3')
				play(sound)
				with smtplib.SMTP(smtp_server, port) as server:
					server.ehlo()  # Can be omitted
					server.starttls(context=context)
					server.ehlo()  # Can be omitted
					server.login(sender_email, passwd)
					server.sendmail(sender_email, receiver_email, message)
					
				
	except:
		pass
