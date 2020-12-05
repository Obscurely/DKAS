from selenium.webdriver import Firefox #Selenium Driver to launch Browser
from selenium.webdriver.common.by import By #Selenium "By" funtion for searching elements
from selenium import webdriver #For complex actions such as contex-clicking
from pynput import keyboard #For Hotkeys
import time #For delays

#Firefox Driver and Browser intialization
driver = webdriver.Firefox('C:/WebDriver/bin/')
driver.get('https://discord.com/login')


#Login to Discord
email = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input')
email.send_keys('adrianjuniorc@gmail.com')
password = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
password.send_keys('^Ll499McoilY4#2e8No!eAygV!U$&utk')
blogin = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div/div/div[1]/div[3]/button[2]')
blogin.click()

time.sleep(7) #Time for page to fully load

#Enter discord group
dgroup = driver.find_element_by_xpath('//*[@id="private-channels-3"]')
dgroup.click()


#Removes GascaMascata from call
def kill_switch():
    bGascaMascata = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div')
    webdriver.ActionChains(driver).context_click(bGascaMascata).perform()
    bGascaMascata.click('//*[@id="user-context-remove"]')

#Adds GascaMascata to call
def add_switch():
    bAdd = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/section/div[2]/div[4]')
    bAdd.click()
    bSearchBar = driver.find_element_by_xpath('/html/body/div/div[6]/div/div/div/div/div[1]/div[2]/div[1]/div/input')
    bSearchBar.send_keys('GascaMascata')
    bGascaMascata = driver.find_element_by_xpath('//*[@id="user-row-0"]')
    bGascaMascata.click()
    bAddUser = driver.find_element_by_xpath('/html/body/div/div[6]/div/div/div/div/div[1]/div[2]/div[2]')
    bAddUser.click()

#Keyboard listener for hotkeys
with keyboard.GlobalHotKeys({
        '<alt>+<ctrl>+r': kill_switch,
        '<alt>+<ctrl>+a': add_switch}) as h:
    h.join()


"""For feature updates:
    -use link_by_text instead of xpath (for making the software versetile)
    -add promts at program start to ask user about what user to manipulate and what in what group chat
    -add try and catch block to avoid crashes beacuse of slow page loading"""