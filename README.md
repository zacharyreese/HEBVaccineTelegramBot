# HEBVaccineTelegramBot
This is a bot that scrapes the HEB vaccine portal for open appointments within a search radius for a select zip code, then posts the link in a telegram channel in real time.
Gets content from here: https://vaccine.heb.com/scheduler?q=78705

Preview: https://i.gyazo.com/9b5e706983f4c5bd1862f416d044f14a.png

Requires ChromeDriver from here: https://chromedriver.chromium.org/downloads place this in your main directory.

https://pastebin.com/pXW56Qqg

## Objective: Get to the HEB vaccination registration as fast as possible. You need to select a date and timeslot, then press continue to guarantee yourself a spot. 

# **YOU CURRENTLY HAVE LESS THAN 5 SECONDS TO GET ONE WITH CURRENT DEMAND (03/31/2021)** 
 
ZIP Code: 78705 (Center of Austin)
Search radius: 60 miles
 
If there is a vaccination appointment available within the search radius, the bot will post a message in the chat with details of the listing as well as the direct registration link. This link has the date and timeslot of the appointment. You need to manually select these each time. If you click on the link and it says that there are no more slots available, all the appointments got filled.
 
# HOW TO BE COMPETITIVE FOR A SPOT:
1. Join channel
2. Have telegram window somewhere on your monitor that you can click quickly with minimal mouse movement. Every second counts!
3. On windows: CTRL + Click on the link to directly open the link in the browser. On Mac: Command + Click on the link to directly open it.
4. If you successful get to the registration page, you will need to select a date, select a timeslot, then click continue as fast as possible.
5. If you manage to beat everyone to the timeslot, another registration page will open asking for more details (Insurance, DoB, etc). You are guaranteed this spot for the next 10 minutes.
	- If you are not successful, a red banner will show at the top saying that the appointment is no longer available. Try your luck with the next one :)
 
# HEADS UP: This bot spams the channel every 2 seconds that the appointment is available, you should mute the channel whenever you aren't actively trying to secure a spot, otherwise you will get a ton of notifications.
