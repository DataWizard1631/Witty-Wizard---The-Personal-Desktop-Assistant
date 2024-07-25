# CREATED BY DATA WIZARD !!!

'''-------For Speech------'''
import os
import speech_recognition as sr     #pip install SpeechRecognition,# ensure to install pyaudio with speechrecognition : brew install portaudio

'''-------To Wish------'''
import datetime
import time

'''-------To Handel Camera------''' 
import cv2                          #pip install opencv-python

'''-------To know ip address------'''
from requests import get

'''-------To get Wikipedia Stuff------'''
import wikipedia                    #pip install wikipedia

'''-------To access webbrowser------'''
import webbrowser

'''-------To Handle Whatsapp,Youtube------'''
import pywhatkit                    #pip install pywhatkit

'''-------To Shut Down Witty Wiz------'''
import sys

'''-------Beast Mode Activate------'''

'''-------To Tell News------'''
from bs4 import BeautifulSoup      #pip install bs4 

'''-------To Tell Me A Joke------'''
import pyjokes                     #pip install pyjokes


'''   Funtions   '''
#Function Building....
def display_witty_wizz_logo():
    print("""


 __      __ .__   __     __             __      __ .__                             .___
/  \    /  \|__|_/  |_ _/  |_  ___.__. /  \    /  \|__|_____________   _______   __| _/
\   \/\/   /|  |\   __||   __\<   |  | \   \/\/   /|  |\___   /\__  \  \_  __ \ / __ | 
 \        / |  | |  |   |  |   \___  |  \        / |  | /    /  / __ \_ |  | \// /_/ | 
  \__/\  /  |__| |__|   |__|   / ____|   \__/\  /  |__|/_____ \(____  / |__|   \____ | 
       \/                      \/             \/             \/     \/              \/ 



""")
#to speak
def speak(speech):
    os.system (f"say '{speech}'")
    print(f"Witty Wiz : {speech}")
    
#to recognize
def SpeechRecognition():

    #Init Recognizer
    start_recognition = sr.Recognizer()

    # Use The Default Microphone as source
    with sr.Microphone() as source:
        #with statement is used for the resource management.Here the resource is microphone.
        #Here with sr.Microphone() inits the microphone.
        #as source ---> assigns the variable source to sr.Microphone() within with
        #Inside this context block, the microphone is available through the source variable.
        #Once the code block within the with statement ends, the sr.Microphone() context manager
        #automatically releases the resources associated with the microphone, ensuring proper cleanup, 
        #regardless of whether an exception occurs.
        print("speak something...")
        listen_audio = start_recognition.listen(source)

        # understand_audio = start_recognition.recognize_google(listen_audio)
        # print(f"You Said : {understand_audio}")

        try:
          print("Recognizing...")
          understand_audio = start_recognition.recognize_google(listen_audio)
          print(f"You Said : {understand_audio}")
        except:
          print("Sorry I Could Not Understand The Audio.")
        
        return understand_audio
         # If The Audio is not recoginized then try : brew install flac
         # Use Virtual Environment and then Install All required imports.

# To Wish

def Wish():
      hour=int(datetime.datetime.now().hour)
     
      if hour >=0 and hour<12:
          speak("Good Morning !!")
      elif hour>=12 and hour<18:
          speak("Good Afternoon !!")
      else:
          speak("Good Evening !!")
      speak("I am Witty-Wizard ! Please Tell Me How Can I Assist You Today ?")
      time.sleep(1)
    
# Basic File Manage Ment
def make_folder(name_folder):
  try:
    os.mkdir(name_folder)
    speak(f"The New Folder Named {name_folder} is created")
  except FileExistsError:
     speak("Fodler with name {name_folder} is already exist")
  except Exception as e:
     speak(f"Error Creating Folder {name_folder}")

#Function to delete the folder
def delete_folder(name_folder):
   try:
      os.rmdir(name_folder)
      speak(f"The Folder Named {name_folder} is Deleted Successfully")
   except FileNotFoundError:
      speak(f"Folder Named {name_folder} not found")

#Function to open apps
def open_apps():
    #app accessed
    #add more app
    list_apps = [  ['text edit','/System/Applications/TextEdit.app'],                                                                           #For MacOs
                  #  ['note pad','C:\Users\DELL\AppData\Local\Microsoft\WindowsApps\ notepad.exe'],                                               #For Windows
                   ['terminal','/System/Applications/Utilities/Terminal.app'],                                                                  #For MacOs
                  #  ['command prompt','"C:\Users\DELL\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk"'],  #For Windows
                   ['minecraft','/Users/deep/TLauncher-2.895 2/TLauncher-2.895.jar'],
            ]
    for app in list_apps:
         if f'open {app[0]}' in command:
            try:
               os.system(f'open -a {app[-1]}')  #For Mac Users
            except:
               os.startfile(f"{app[-1]}")       #For Windows Users

# def close_apps():
#     #app accessed
#     #add more app
#     list_apps = [  ['text edit','/System/Applications/TextEdit.app'],                                                                           #For MacOs
#                   #  ['note pad','C:\Users\DELL\AppData\Local\Microsoft\WindowsApps\ notepad.exe'],                                               #For Windows
#                    ['terminal','/System/Applications/Utilities/Terminal.app'],                                                                  #For MacOs
#                   #  ['command prompt','"C:\Users\DELL\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk"'],  #For Windows
#                    ['minecraft','/Users/deep/TLauncher-2.895 2/TLauncher-2.895.jar'],
#             ]
#     for app in list_apps:
#          if f'close {app[0]}' in command:
#             os.system(f"taskkill /f /im {app[-1]}")

#Function to open websites
def open_websites():
    #Websites accessed
    list_web  = [ ['youtube','https://www.youtube.com'],
                  ['orrisa','https://auris.ahduni.edu.in/core-emli/code/my_home/'],
                  ['google','https://www.google.com']
            ]
    for web in list_web:
         if f'open {web[0]}' in command:
            webbrowser.open(web[-1])

#Funtion to shutdown,sleep,restart the system
def to_restart_shutdown_sleep():
    
    if('restart' in command):
       speak("Ok!! First Tell Me The password")
       key=SpeechRecognition()
       if key=="1131":
            speak("OK!I'll catch you on the flip side after the reboot ")
            try:
               os.system("sudo shutdown -r now")                           #MacOs
            except:
               os.system("shutdown /r /t 5")                               #Windows
       else:
            speak("Sorry ! Wrong Key ! Access Denied.")
    if('sleep' in command):
       speak("Ok!! Sleeping .....")
       try:
            os.system("sudo pmset sleepnow")                                 #MacOs
       except:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")     #Windows
    if('shutdown' in command):
         speak("Ok!! First Tell Me The Password Key")
         key=SpeechRecognition()
         if key=="1131":
            speak("OK Shutting Down The System!  Good Bye")
            try:
               os.system("sudo shutdown -h now")                     
               time.sleep(8)
            except:
               os.system("shutdown /s /t 5")
            
         else:
            speak("Sorry ! Wrong Key !You have no access to do so!")

#Function to handle Files
def manage_files():
    print("=================================")
    print("          FILE MANAGER           ")
    print("=================================")
    print("   ")
    print("        [1] Create File            ")
    print("        [2] Read   File            ")
    print("        [3] Append File            ")
    print("        [4] delete File            ")
    print("        [5] exit                   ")
    print("   ")
    print("=================================")
    print("   ")

    # user_choice = input("Enter the option : ")
    while True:
       
     speak("Let me know your choice in terminal.")
     time.sleep(1)
   #   user_choice = SpeechRecognition().captlize()
     user_choice = input("Enter the input :  ")
     if  (user_choice=='1'):
        speak("Please Write File Name With Extension :")
        file_name = input("File Name = ")
        open(f'{file_name}',"x")
        speak(f"ok!The file with name {file_name} is created.")
     elif(user_choice=='2'):
        speak("Please Write File Name With Extension :")
        file_name = input("File Name = ")
        file = open(f'{file_name}','r')
        print(file.read())
        file.close()
     elif(user_choice=='3'):
        speak("Please Write File Name With Extension :")
        file_name = input("File Name = ")
        file =open(f'{file_name}',"a")
        prompt = input("Enter the prompt : ")
        file.write(f"{prompt}")
        file.close()
     elif(user_choice=='4'):
        speak("Please Write File Name With Extension :")
        file_name = input("File Name = ")
        os.remove(f"{file_name}")
        speak(f"The File Named {file_name} has been deleted.")
     elif(user_choice=='5'):
        break;

#Making the reminder using the file handling
def reminder_():
    message = SpeechRecognition().lower()
    with open("/Users/deep/Coding/Python/Real_Python_pro/pro_py/voice_ass/remember.txt", "w") as file_reminder:
       file_reminder.write(message.replace('remember that','') + "")
       speak("Ok Reminder Saved...")
    print(f"Reminder : {message.replace('remember that','')}")


def read_reminder_():
    try:
       with open("/Users/deep/Coding/Python/Real_Python_pro/pro_py/voice_ass/remember.txt","r") as file_reminder:
          reminders = file_reminder.readlines()
          if reminders:
             speak(f"Your Reminder {reminders}")
          else:
             speak("No reminders Found")
    except FileNotFoundError:
       speak("No Reminders Found")
                  
   
def news():

   print("\n============ Witty-Wiz The Reporter ============\n")

   url_ = "https://www.bbc.com/news"
   response = get(url_)

   soup_         = BeautifulSoup(response.text, 'html.parser')
   get_headlines = soup_.find('body').find_all('h3')
   dont_need     = ['BBC World News TV', 'BBC World Service Radio','News daily newsletter', 'Mobile app', 'Get in touch'] 
   
   loop_breker = 1
   for x in list(dict.fromkeys(get_headlines)): 
     if x.text.strip() not in dont_need: 
        print("[+] "+x.text.strip()) 
        speak(x.text.strip())
     if loop_breker==3:
        break
     loop_breker = loop_breker + 1
   
   print("\n================================================\n")

# ---> The Features...
      
if __name__ == "__main__":
   display_witty_wizz_logo()
   Wish()   #Calling The Wish Function

   while True:
   #  if 1:
       command = SpeechRecognition().lower()

       if 'master' in command : 
          speak("I am the basic trainned AI model trainned by my master Deep Patel DataWizard.")

       elif 'yourself' in command : 
          speak("My name is Witty-Wizard and I am a personal desktop assistant. I am scripted with the basic python language. You can tell me to do anything according to my progrrame. Since I am in develpment phase so i might not do everything that you say but once i am developed fully i will be the beast desktop assistant who can do anything like a wizard")

       elif 'time' in command:
          time_now = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir Time is {time_now}") 

       elif 'open' in command:
          open_apps()
          open_websites() 

      #  elif 'close' in command:
      #     close_apps()

       elif 'wikipedia' in command:
          speak("searching wikipedia....")
          command = command.replace("wikipedia","")
          results = wikipedia.summary(command,sentences = 3)
          speak("According to the wikipedia...")
          speak(results)

       elif 'ip address' in command:
          ip=get('https://api.ipify.org').text
          speak(f"Your Ip Is : {ip} ")

       elif "play something on youtube" in command:
         speak("Ok !! Can you please tell me the song name or the name of thing of your wish")
         your_Wish=SpeechRecognition().lower()
         speak(f"Ok   Playing {your_Wish} Enjoy!!")
         pywhatkit.playonyt(your_Wish)
       
       elif "make folder" in command:
          speak("OK!")
          speak("Please provide me the name of the folder !")
          name = input("Enter the folder name : ")
          make_folder(name)
         #  speak(f"The folder with name {name} is created")
       
       elif "delete folder" in command:
          speak("Ok! here is the list of folder in current directory.")
          print(os.listdir())
          speak("Please provide me the name of the folder you want to delete. ")
          name = input("Enter the folder name : ")
          delete_folder(name)
         #  speak(f"The folder with name {name} is deleted")
       
       elif 'file' in command:
          manage_files()   

       elif 'remember' in command:
          speak("Yes please tell me")
          reminder_()  

       elif 'remind' in command:
          read_reminder_()
          time.sleep(2)
            
       elif ('restart' in command) or ('shutdown' in command) or ('sleep' in command):
         to_restart_shutdown_sleep()
       
       elif ('news' in command):
          speak("Reporter Mode Activate ! ")
          news()
          
       elif "joke" in command:
         speak("Ok Listen......")
         joke = pyjokes.get_joke()
         # speak("Take a look at terminal")
         # print(joke)
         speak(joke)
       
       elif 'no thanks' in command:
          speak("Ok thank you for using me.")
          sys.exit()

       else:
         speak("Sorry Sir!!")
         speak("My Master Has Not Trained Me For This Command")   
      
       speak("Do you have any other work for me sir  ")

# integrate the news function in if-elif ladder
# Add more app in app list
# Add more website i n app list