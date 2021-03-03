import os
import time
import getpass
from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#CLI BASED TOOL
def home():
	f1 = Figlet(font='rounded')
	f2 = Figlet(font='digital')
	print ("Name: MS-Teams-b0t")
	print ("version: 1.0")
	print ("@whitedevil369")
	print (f1.renderText('MS-Teams-b0t'))
	print (f2.renderText("Made by Poornesh Adhithya"))
	print ("\nWELCOME TO MS-Teams-b0t\nMS-Teams-b0t is a MS-Teams Online Class Attendance b0t, it will automatically login and join the class\n")
	input("\nPRESS ENTER TO CONTINUE.\n\nb0t:~#> ")

home()

#ALLOW MIC AND CAM
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })
  
#INPUT
print("\nEnter your Email ID: ")
mailid = input("b0t:~#> ") #mailid@msteams.com
print("\nEnter your Password: ")
passwd = getpass.getpass("b0t:~#> ") #secret@123


#b0t STARTED
print("\nb0t:~#> b0t STARTED...")

	
#OPENING TEAMS
driver = webdriver.Chrome(options=opt)
driver.get("https://teams.microsoft.com/")
assert "teams" in driver.page_source

#LOGIN MAIL ID
elem1 = driver.find_element_by_id("i0116")
elem1.send_keys(mailid) #mailid@msteams.com
elem1.send_keys(Keys.RETURN)
time.sleep(2)

#LOGIN PASSWORD
elem2 = driver.find_element_by_id("i0118")
elem2.send_keys(passwd) #secret@123
time.sleep(2)

elem3 = driver.find_element_by_id("idSIButton9")
elem3.click()

#CONFIRM
elem4 = driver.find_element_by_id("idSubmit_ProofUp_Redirect")
time.sleep(2)
elem4.click()

time.sleep(10)

#SKIP
elem5 = driver.find_element_by_xpath("//a[@class='_1gOPL-4bTsJrmq-tOA4heK']")
time.sleep(2)
elem5.click()

time.sleep(5)

#DO NOT REMEMBER
elem6 = driver.find_element_by_id("idBtn_Back")
time.sleep(2)
elem6.click()

time.sleep(20)

#OPEN THROUGH BROWSER
elem7 = driver.find_element_by_xpath('//*[@id="download-desktop-page"]/div/a')
time.sleep(2)
elem7.click()

time.sleep(20)

#OPEN CALENDAR
elem8 = driver.find_element_by_xpath('//*[@id="teams-app-bar"]/ul/li[5]')
time.sleep(2)
elem8.click()

time.sleep(5)

'''
#MEET NOW (START A MEETING)
elem9 = driver.find_element_by_xpath('//*[@id="header_meet_now_button"]')
time.sleep(2)
elem9.click()
'''

#SELECT THE SUBJECT
elem13 = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div/calendar-bridge/div/div/div[4]/div[2]/div/div/div[1]/div/div[3]/div[5]/div[3]/div[1]')
time.sleep(2)
elem13.click()

time.sleep(2)

#JOIN THE MEETING
elem14 = driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div[3]/div/div/div[1]/div[2]/div[3]/button[1]')
time.sleep(2)
elem14.click()

time.sleep(2)

#TURN OFF VIDEO
elem10 = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
time.sleep(2)
elem10.click()

time.sleep(2)

#TURN OFF AUDIO
elem11 = driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
time.sleep(2)
elem11.click()

#CONFIRM AND JOIN THE MEETING
elem12 = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
time.sleep(2)
elem12.click()

time.sleep(2)

print("b0t:~#> JOINED THE MEETING SUCCESSFULLY! :)")



