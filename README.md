#Discord_Kill_Add_SWITCH or DKAS
------

##Summary:

Discord_Kill_Add_SWITCH or DKAS for short is quite a simple program made in python that can kick or add a person in a discord group for the moment... in the future i may add more features. It uses the selenium and pynput modules in order to work. If you want to know more keep reading.

----

##Program pre requirements:
  
    - Install python 3.x from the offcial site: https://www.python.org/
    - Install selenium using this pip command: pip3 install selenium
    - Install pynput using this pip command: pip3 install pynput
    - Download the firefox geckodriver (from: https://github.com/mozilla/geckodriver/releases) and put it in C:\WebDriver\bin
    - Execute this command: setx /m path "%path%;C:\WebDriver\bin\". If this does not work than do this: 1.Right click "This PC" and click properties. | 2.In the left column click "Adveanced system settings" | 3.Click down the promp on "Environment variables" | 4.Click on "Path" in the top box | 5.Press on edit | 6.On the next prompt press new and paste this: C:\WebDriver\bin\ | 7.Now click "Ok", "Ok" and exit out
   

----

##How to Run the Program:<br />
  * 1.Open a terminal window in the folder you have the DKAS.py script (shift+rightClick and click Open Command Prompt Window) and run the folowing command: py DKAS.py<br />
* 2.Read everything the program prompts you.<br />
 * 3.Make sure the group chat you want to work with is the first in list until the program fully loads.<br />
* 4.Complete the "q&a" program prompts you.<br />
* 5.Wait until you see the program fully loaded to the group you selected.<br />
* 6.Now you need the leave the browser running in the background and the hotkeys are: - to kick the person and * to add the person.
---

##Issues you may encounter while using the program and how to solve them:<br />
* 1.After you used a hotkeys once the next time you will need to press it twice in order for it to work. I am trying to find a fix as soon as I can.<br />
* 2.The program will try to login you automatically but it may fail due to some Discord/Browser error or because a Robot Verification appears. If you encounter such an issue please look at the browser, if you see is because a robot verification appeard inside the selenium driven browser search for discord and login manually and click on the group you want to work with and after that the program should work as intended.<br />
* 3.If you can't kick a user: make sure he is in the group, try pressing the button a few times again, try restarting the program, check if you have installed everything correctly. If neither of these work please post your issue in the issues tab on github with as much details as possible and i will try to help you/fix the issues if it's program related.<br />
* 4.If you can't add a user: make sure he is in the group, try pressing the button a few times again, try restarting the program, check if you have installed everything correctly. If neither of these work please post your issue in the issues tab on github with as much details as possible and i will try to help you/fix the issues if it's program related.<br />
* 5.If your hotkeys don't work at all first make sure you pynput installed and install the latest version of python3.<br />
* 6.If you are having any other issues feel free to use Google and Stack Overflow as they don't cost nothing before posting here, but if you can't find a fix or there is something wrong with the program post it in the issues tab.<br />
<br />
---

##How does the program work:

>The program is based on selenium (for the browser part) and pynput (for the hotkeys part). What the program does basically is: It opens Disocrd in the browser and logs you in automatically and clicks on the first chat (that's why you need to have the group first until the program loads), than if you press "-" the program will automate the procces of kicking a person from a discord call in like under hald a second and if you press "\*" it will automate the procces of adding that person back in the call in like under half a second aswell. It's not a really complicated program but it takes some time to make it.<br />
---

##Feature requests:
>I am open to any feature request just ask me ofr it and i will try my best to implement it if it's worth doing so.
    
##If you want to use my work:

>You are free to use my work as long as you credit me and link the github post.
