from selenium.webdriver import Firefox #Selenium Driver to launch Browser
from selenium.webdriver.common.by import By #Selenium "By" funtion for searching elements
from selenium import webdriver #For complex actions such as contex-clicking
from pynput.keyboard import HotKey, Key, KeyCode, Listener #For Hotkeys 
from colorama import init ,Fore, Back #For colored text
import time #For delays

init(convert=True) #So the text appears colored in cmd too

"""
    Discord_Kill_Add_SWITCH or DKAS for short is a FOSS made for kicking or adding a user in a discord group
    Please you this at your own risk as this may cause the loose of your google and discord account oreven damage 
    your computer and I AM NOT RESPONSIBLE FOR ANY OF THAT!
"""

#Before start requirments and warnings for the program
print(Fore.BLUE + 'Welcome to Discord_Kill_Add_SWITCH or DKAS for short, read everything carefully and have fun! :)')
print(Back.GREEN + Fore.RED + 'I am not responsible for any damage this program may do to you computer or your account. Use this at your own risk!!!' + Fore.WHITE + Back.BLACK)
print(Fore.YELLOW + 'In order for the program to fully work you need to make sure that the group chat you want to work with is the first in the list until the program fully loads and after that you can talk with anyone and do whatever from the Discord app.' + Fore.WHITE)
print(Fore.YELLOW + 'The key binds are: - to kick someone, * to add that person')
print(Fore.YELLOW + 'Important:\n1.After you used one of the keybind once for some reason next time you will need to press it twice. I am trying to find a fix for this!\n2.You may encounter a login error and the program will tell you, if it is a robot verification issue please go to the Dicord site by searching for it in the selenium driven browser and login manually!')
print(Fore.BLUE + 'Please provide your login information:\nemail:' + Fore.WHITE)
email = input()
print(Fore.BLUE + 'password:' + Fore.WHITE)
password = input()
print(Fore.BLUE + 'What user do you want to manipulate:' + Fore.WHITE)
user = input()
print(Fore.WHITE)

#Firefox Driver and Browser intialization
driver = webdriver.Firefox('C:/WebDriver/bin/')
driver.get('https://discord.com/login')

#Try to login into Discord and enter discord group
try:
    #Login part
    email_login = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input')
    email_login.send_keys(email)
    time.sleep(1)
    print(Fore.GREEN + 'Entered email, loaded 25%')
    password_login = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
    password_login.send_keys(password)
    print(Fore.GREEN + 'Entered password, loaded 50%')
    time.sleep(1)
    blogin = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div/div/div[1]/div[3]/button[2]')
    blogin.click()
    print(Fore.GREEN + 'Clicked login, loaded 75%')


    time.sleep(10) #Time for page to fully load

    #Enter discord group part
    dgroup = driver.find_element_by_xpath('//*[@id="private-channels-2"]')
    dgroup.click() 
    print(Fore.GREEN + 'Entered discord group, loaded 100%. You can now use program!' + Fore.WHITE)
    
except:
    print(Fore.RED + 'Error: We could not automatically login into your account and access the group due to an error(ussualy robot verification). Please login manually and click on the group chat' + Fore.WHITE)


#Removes User from call
def kill_switch():
    try:
        bUser = driver.find_elements_by_link_text(user)[-1]
        webdriver.ActionChains(driver).context_click(bUser).perform()
        bRemoveUser = driver.find_element_by_xpath('//*[@id="user-context-remove"]')
        bRemoveUser.click()
        print(Fore.GREEN + 'Successfully kicked ' + user + ' from the group' + Fore.WHITE)
    except:
        print(Fore.RED + 'Error: There was an issue trying to kick the user, please try again! If the problem persists try restarting the program or post your issue on github.' + Fore.WHITE)

#Adds User to call
def add_switch():
    try:
        bAdd = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/section/div[2]/div[3]')
        bAdd.click()
        bSearchBar = driver.find_element_by_xpath('/html/body/div/div[6]/div/div/div/div/div[1]/div[2]/div[1]/div/input')
        bSearchBar.send_keys(user)
        bUser = driver.find_element_by_xpath('//*[@id="user-row-0"]')
        bUser.click()
        bAddUser = driver.find_element_by_xpath('/html/body/div/div[6]/div/div/div/div/div[1]/div[2]/div[2]')
        bAddUser.click()
        print(Fore.GREEN + 'Successfully added ' + user + ' to the group' + Fore.WHITE)
    except:
        print(Fore.RED + 'Error: There was an issue trying to add the user, please try again! If the problem persists try restarting the program or post your issue on github.' + Fore.WHITE)

#Keyboard listener for hotkeys
hotkey1 = HotKey(
    [KeyCode(char='-')],
    kill_switch
)

hotkey2 = HotKey(
    [KeyCode(char='*')],
    add_switch
)

hotkeys = [hotkey1, hotkey2]

def signal_press_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.press(l.canonical(key))

def signal_release_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.release(l.canonical(key))

with Listener(on_press=signal_press_to_hotkeys, on_release=signal_release_to_hotkeys) as l:
    l.join()
