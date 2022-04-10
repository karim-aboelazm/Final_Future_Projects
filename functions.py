# Importing Libraries We Need 
import os
import time 
import requests
import speedtest
import datetime
import webbrowser 
import wikipedia
import pywhatkit
import pywikihow
import wolframalpha
import bs4

from pyautogui import click
from keyboard import press,write

from newscatcherapi import NewsCatcherApiClient
from voice_output import Say
from voice_input import Listen

# Function That return Time Now
def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    Say(f"Time Now Is  {time}")

# Function That return Current Date 
def get_date():
    date = datetime.date.today()
    Say(f"Today's Date Is  {date}")

# Function That return Current day
def get_day():
    today = datetime.datetime.now().strftime("%A")
    Say(f"Today Is  {today}")

# Function That returns Global news of the Univers
def get_nasa_news():
    Say('Getting Data from Nasa ....')
    Api_key = "TDhA4g5vdtJFf41rQdx1pRfrNJiT2CneJVgwEVLs"
    url = "https://api.nasa.gov/planetary/apod?api_key="+str(Api_key)
    today = datetime.date.today()
    date = today
    parameters = {'date':str(date)}
    request = requests.get(url,params=parameters)
    Data = request.json()
    Info = Data['explanation']
    title = Data['title']
    image_url = Data['url']
    webbrowser.open(image_url)
    Say(f"title : {title}")
    Say(f"According to Nasa : {Info}")

# Function that returns The Internet Speed 
def get_internet_speed():
    Say("Getting The Internet Speed .....")
    speed = speedtest.Speedtest()
    download_speed,upload_speed = speed.download(),speed.upload()
    current_ds , current_us = int(download_speed/800000),int(upload_speed/800000)
    Say(f"Current Download Speed : {current_ds} kb/s\nCurrent Upload Speed : {current_us} kb/s")

# Function that return The Egyptian news
def get_egyptian_news():
    Say("Getting Data From The Internet ....")
    url = "https://english.ahram.org.eg/Portal/1/Egypt.aspx"
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text,"lxml")
    category = []
    descriptions = []
    news = soup.find_all('div',class_="portal-section")
    for new in news :
        cat = new.find('h3')
        desc = new.find('p')
        category.append(cat.string)
        descriptions.append(desc.string)
    Say(f"Category [1] : {category[0]}")
    Say(f"Description : {descriptions[0]}")
    print("="*100)
    i = 1
    stm = ''
    while i < len(category)-1:
        stm = Listen()
        if stm == 'next':
            Say(f"Category [{i+1}] : {category[i+1]}")
            Say(f"Description : {descriptions[i+1]}")
            print("="*100)
            i+=1
        else:
            break
# -----------------------------------------
# Systems Apps
# --------------------------------------

def open_word():
    Say("Open Online Or Local Sir ...")
    stm = Listen()
    if str(stm).lower()=="local":
        click(x=22, y=751)
        time.sleep(2)
        write('word')
        time.sleep(2)
        press('enter')
    elif str(stm).lower()=="online":
        webbrowser.open("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=637852268094383681.ZmQwMmUzMjctNzg0ZC00YThiLWEyNTUtZDBhNjRiNjVhZDkxZjM0ZDIyOGQtNDdlOC00NGViLWE0MzQtOTQ2ODEyMmFmMTc4&ui_locales=en-US&mkt=en-US&client-request-id=52e8b32d-9213-4910-9580-4ffd9948b5bc&state=RAchbeV9q0zY3NLaoEsNUMBcZesUo6JZeboUdsugu0OmfachSTQsb3uz9-iO5AJ0hghqFNT4sjgXtnyX1kEQUmeBkGruqjTBy3O5HsaFTP22YAhDx_Cqk3qDys3uLtX_7oX7SHekQz3qmieJysa0thdP9osv4W2wO_19WGu9JpowS69Z5iM_gxj3rFek1cxeSk0EySOSmFsp96FXzCFSUHz46h277aYD0-AtH3_xMpdrllmnkPC7iTyiWlvaBtTsN2SnDwKrsByDpOamNa7-f67KqcOkN_EdzAenNtJ5TqY&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.12.1.0")
    
def close_word():
    time.sleep(1)
    os.system('taskkill /f /im WINWORD.EXE')

def open_powerpoint():
    Say("Open Online Or Local Sir ...")
    stm = Listen()
    if str(stm).lower()=="local":
        click(x=22, y=751)
        time.sleep(2)
        write('powerpoint')
        time.sleep(2)
        press('enter')
    elif str(stm).lower()=="online":
        webbrowser.open("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=4765445b-32c6-49b0-83e6-1d93765276ca&redirect_uri=https%3A%2F%2Fwww.office.com%2Flandingv2&response_type=code%20id_token&scope=openid%20profile%20https%3A%2F%2Fwww.office.com%2Fv2%2FOfficeHome.All&response_mode=form_post&nonce=637852268094383681.ZmQwMmUzMjctNzg0ZC00YThiLWEyNTUtZDBhNjRiNjVhZDkxZjM0ZDIyOGQtNDdlOC00NGViLWE0MzQtOTQ2ODEyMmFmMTc4&ui_locales=en-US&mkt=en-US&client-request-id=52e8b32d-9213-4910-9580-4ffd9948b5bc&state=RAchbeV9q0zY3NLaoEsNUMBcZesUo6JZeboUdsugu0OmfachSTQsb3uz9-iO5AJ0hghqFNT4sjgXtnyX1kEQUmeBkGruqjTBy3O5HsaFTP22YAhDx_Cqk3qDys3uLtX_7oX7SHekQz3qmieJysa0thdP9osv4W2wO_19WGu9JpowS69Z5iM_gxj3rFek1cxeSk0EySOSmFsp96FXzCFSUHz46h277aYD0-AtH3_xMpdrllmnkPC7iTyiWlvaBtTsN2SnDwKrsByDpOamNa7-f67KqcOkN_EdzAenNtJ5TqY&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.12.1.0")
      
def close_powerpoint():
    time.sleep(1)
    os.system('taskkill /f /im POWERPNT.EXE')

# Functions with single command
def get_command(query): 
    query = str(query)
    if 'time' in query:
        get_time()
    elif 'date' in query:
        get_date()
    elif 'day' in query:
        get_day()
    elif 'nasa' in query:
        get_nasa_news()
    elif 'speed' in query:
        get_internet_speed()
    elif 'egyptian news' in query:
        get_egyptian_news()
    # ----------------------
    #  system apps
    # ---------------------
    elif 'open word' in query:
        open_word()
    elif 'open powerpoint' in query:
        open_powerpoint()
    elif 'close word' in query:
        close_word()
    elif 'close powerpoint' in query:
        close_powerpoint()
        
# Function of setting wolframalpha API
def wolframalpha_settings(query):
    api_key = 'WY8246-ERXY7J3P5Y'
    request = wolframalpha.Client(api_key)
    response = request.query(query)
    try:
        return next(response.results).text
    except:
        Say('This query Is Not Defined')

# Function That return Search result in wikipedia 
def wikipedia_search(query):
    search = str(query).replace("who is","").replace("what is","").replace("about","").replace("which is","")
    result = wikipedia.summary(search)
    Say(f"The wikipedia result is :\n {result}")

# Function That return Search result in google  
def google_search():
    Say("Searching For What Sir ....")
    stm = Listen()
    search = str(stm)
    pywhatkit.search(search)

# Function That open any site
def open_any_website(query):
    site = str(query).replace("open","").replace(" ","")
    web = "https://www."+str(site)+".com/"
    webbrowser.open(web)

# Function That play any music or vedio on youtube
def play_music_on_youtube(query):
    sound = str(query).replace("play","").replace("play music","").replace("music", "").replace("play video","").replace("youtube","").replace(" ","")
    pywhatkit.playonyt(sound)

# Function That making calculate
def sample_calculator(query):
    operation = str(query).replace("plus","+")
    operation = str(query).replace("in","*")
    operation = str(query).replace("multiply","*")
    operation = str(query).replace("into","*")
    operation = str(query).replace("power","**")
    operation = str(query).replace("to the power","**")
    operation = str(query).replace("minus","-")
    operation = str(query).replace("from","-")
    operation = str(query).replace("div","/")
    operation = str(query).replace("divide","/")
    operation = str(query).replace("divide","/")
    operation = str(query).replace("over","/")
    result = eval(str(operation))
    Say(f"The Result is {result}")

# Function That Getting how to making any thing
def how_to(query):
    how = str(query)
    max_result = 1
    search = pywikihow.search_wikihow(how,max_result)
    assert len(search) == max_result
    Say(search[0].summary)

# Function That Getting Tempreture
def get_tempreture(query):
    temp = str(query).replace("What is the tempreture","tempreture in")
    temp = str(query).replace("tempreture for","tempreture in")
    Say(wolframalpha_settings(temp))

# Function That getting Full weather description information

def get_weather_info(query):
    city = str(query).replace("weather in","").replace("weather for","").replace("what is weather in","")
    api_key = "992213628dbceb7e7fb06cf59035697d"
    root_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = f"{root_url}appid={api_key}&q={city}"
    r = requests.get(url)
    data = r.json()
    if data['cod'] == 200:
        temp = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        descr = data['weather'][0]['description']
        wind = data['wind']['speed']
        Say(f"Weather Information In : {city}")
        Say(f"The Weather Condition is {descr}")
        Say(f"The temperature is {temp} kelvin")
        Say(f"The pressure is {pressure} hPa")
        Say(f"The humidity is {humidity} %")
        Say(f"The speed of wind is {wind} m/s")
    else:
        Say("Something Went Wrong")

def welcome_person(query):
    name = str(query).replace("he is " ,"")
    name = str(query).replace("she is " ,"")
    name = str(query).replace("I am " ,"")
    name = str(query).replace("I'm " ,"")
    name = str(query).replace("i am " ,"")
    Say(f"Hello {name} It's Nice To meet you .. ")

def covid_19(query):  
    command = str(query).replace(" ","")
    Say("Tell Which country dou want to know It's Covid statistics ...")
    country = Listen()
    country = str(country).lower()
    url = f"https://www.worldometers.info/coronavirus/country/{country}/"
    result = requests.get(url)
    Data = []
    soup = bs4.BeautifulSoup(result.text,"lxml")
    corona = soup.find_all('div',class_="maincounter-number")
    for case in corona:
        span = case.find('span')
        Data.append(span.string)
    all_casses,death_casses,recovered_casses = Data
    Say(f"The corona virus in {country} statistics...")
    Say(f"All Cases     Number  : {all_casses}   person")
    Say(f"All Death     Number  : {death_casses} person")
    Say(f"All Recovered Number  : {recovered_casses}   person")
    webbrowser.open(f"https://www.google.com/search?q={country.lower()}+coronavirus")

# Functions with query command
def get_input_command(tag,query):
    if "wikipedia" in tag:
        wikipedia_search(query)
    elif "google" in tag:
        google_search()
    elif "website" in tag:
        open_any_website(query)
    elif "playmusic" in tag:
        play_music_on_youtube(query)
    elif "calculate" in tag:
        sample_calculator(query)
    elif "how" in tag:
        how_to(query)
    elif "temperature" in tag:
        get_tempreture(query)
    elif "weather" in tag:
        get_weather_info(query) 
    elif "recognize" in tag:
        welcome_person(query)
    elif "corona" in tag:
        covid_19(query)
