import requests
import os
import time

python_boolean = input('Do you want to install python 3.9, python is required(1 = yes; 0 = no): ')
selenium_boolean = input('Do you want to install selenium module, selenium is required(1 = yes; 0 = no): ')
pynput_boolean = input('Do you want to install pynput module, pynput is required(1 = yes; 0 = no): ')
geckodriver_boolean = input('Do you want to download and put geckodriver in path, geckodriver is required(1 = yes; 0 = no): ')

def python_install():
    python_exec_request = requests.get('https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe')
    python_exec = open('python-3.9.0-amd64.exe', 'wb')
    python_exec.write(python_exec_request.content)
    python_exec.close()
    os.system('python-3.9.0-amd64.exe')
    print('Installed python')
    
def selenium_install():
    os.system('pip3 install selenium')
    print('Installed selenium')
    
def pynput_install():
    os.system('pip3 install pynput')
    print('Installed pynput')
    
def install_geckodriver():
    geckodriver_request = requests.get('https://drive.google.com/uc?export=download&id=178z2rbp6IgthlXr5E8uAY9p9571QIniA')
    geckodriver_exec = open('geckodriver.exe', 'wb')
    geckodriver_exec.write(geckodriver_request.content)
    working_directory = os.getcwd()
    os.chdir('C:/')
    os.system('mkdir WebDriver')
    os.chdir('C:/WebDriver')
    os.system('mkdir bin')
    os.chdir(working_directory)
    os.system('copy geckodriver.exe C:\\WebDriver\\bin')
    os.system('setx /m path "%path%;C:\\WebDriver\\bin\\"')
    print('Downloaded geckodriver and put it in path')
    
def setup():
    if python_boolean == '1':
        python_install()
    if selenium_boolean == '1':
        selenium_install()
    if pynput_boolean == '1':
        pynput_install()
    if geckodriver_boolean == '1':
        install_geckodriver()

setup()

print('IMPORTANT: Setup completed, now please restart you system in order for the installation to fully complete. If after restart when you launch the DKAS.py it says that it did not find the geckodriver in path please refer to github manual installation steps for geckodriver.')
print('Press enter to close!')
input() #Press enter to close