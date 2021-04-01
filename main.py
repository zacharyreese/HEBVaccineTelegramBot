from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests
import urllib.parse
import telegram_send

# DIRECTIONS/ TIPS FOR SUCCESS: https://pastebin.com/Y7R6wEZt

zip = '78705'  # Area to search from
url = 'https://vaccine.heb.com/scheduler?q=' + zip

# Create headless browser
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
browser = webdriver.Chrome(options=options)
browser.get(url)

# Telegram bot private token
bot_token = '<INSERT BOT TOKEN>'
# ID of person/group that you want the bot to send messages to
bot_chatID = '<INSERT CHAT ID>'

# Normal text sent over telegram, no links
def telegram_bot_sendtext(bot_message):
    # Telegram bot API link
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

# Link formatted telegram method
def telegram_bot_sendlink(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=<a href=\"' + bot_message + '\">CLICK HERE TO REGISTER</a>'
    response = requests.get(send_text)

    return response.json()

# Different parse mode telegram message
def telegram_bot_sendlink2(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text='
    response = requests.get(send_text)

    return response.json()


# Infinite loop to constantly refresh page and send links if within search distance
while True:
    try:
        # Wait for elements to load, then find DOM elements required to parse information
        elem = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/ul/li[1]/p"))   # This is an element in the graphql, which takes longer to render than the page
        )
        distance = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/ul/li[1]/p').text  # Distance from search area zip code
        locationName = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/ul/li/div[1]/p[1]').text  # HEB location name
        locationAddress = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/ul/li/div[1]/address').text  # HEB location address
        link = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/ul/li/div[2]/a').get_attribute('href')  # Link to sign up for vaccination
        parsedLink = link.replace('&', '%26amp;')  # Parsed link required to send over telegram, otherwise get errors from telegram
        timeSlots = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/ul/li[1]/div[1]/p[2]').text  # How many timeslots is offered
        vaccineType = browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/ul/li[1]/div[1]/p[3]').text  # What kind of vaccine (Moderna, J&J, etc.)
        # Print all results in the console
        print(locationName)
        print(locationAddress)
        print(distance)
        print('-----------')
        # print(link)
        searchDistance = 60    # Miles that you are willing to drive to get a vaccine
        if float(distance.split()[0]) <= searchDistance:
            # If an available spot is open within your search radius, send a telegram message
            messageString = locationName + '\n' + locationAddress + '\n' + distance + '\n' + timeSlots + '\n' + vaccineType
            messageString = urllib.parse.quote_plus(messageString)
            telegramMssg = telegram_bot_sendtext(messageString)
            telegramMssg2 = telegram_bot_sendlink(parsedLink)
            print(telegramMssg)
            print(telegramMssg2)
            # Refresh the browser and run method again
            browser.refresh()
            sleep(2)
        else:
            # If no results found, refresh page and run method again
            browser.refresh()
            sleep(2)
    except:
        print("No results")
        browser.refresh()
        sleep(2)