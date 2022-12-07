# 473-Project

Stage 1

From https://github.com/hanyazou/TelloPy I followed the instructions listed. I first had to download tellopy to my machine by typing in ‘pip install tellopy’. I got an error saying ‘pip: command not found’ so I had to figure out that issue. I eventually got pip to install using the command ‘curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py’. After trying to install tellopy again it still gave the error ‘pip: command not found’. I tried to install/use pip3 instead with the command ‘pip3 install requests’. It was successfully installed, so then I called ‘pip3 install tellopy’. That worked and I then had tellopy installed on my machine. I then installed av by entering ‘pip3 install av’. Then ‘pip3 install opencv-python’. Finally, I installed pygame by using the command ‘pip3 install pygame’. 
I first tried the command ‘python -m tellopy.examples.simple_takeoff’ but it did not work, and I got an error saying ‘no module named pygame’. After trying many different things and trying to reinstall pygame using the github repo, I found that ‘python3 -m tellopy.examples.simpe_takeoff’ worked. The drone took off, hovered, then landed soon after.
 I then tried calling ‘python3 -m tellopy.examples.joystick_and_video’ to get the drone to work with a controller, but got an error saying that ‘no supported joystick found’. 
We then had to figure out what was wrong with the code and test to see why the controller would not connect. The controller connected to my laptop for sure because when you go to check in USB, it shows that a controller is connected to my laptop. It shows the name and all the information about it. We tried changing the elif statements to include the names listed in the information on my laptop, but nothing was working and the controller still wasn’t connecting. We had no idea why. I googled a bunch of things trying to figure out how to connect the controller and we tried many different ideas suggested on the internet. 
Eventually, once looking at more of the code in depth other than just the try block and elif statements, I realized that the except statement stated if there was any error, it would just pass the rest of the code and not look at it at all. The elif statements that we were changing were not getting looked at at all. By debugging using print statements, I figured out that there was an error with the line ‘js = pygame.joystick.Joystick(0)’ and the error was ‘pygame.error: Invalid joystick device number’. I tried different numbers but I wasn’t exactly sure what it was supposed to be. I googled the error but I tried many of the suggestions, and none of them worked. We googled many different questions and searched for solutions, but could not find any. I saw a lot of errors with people using MacBooks and that some things weren’t working for them, so I feel like that could be an issue. Something that the new MacBooks have different builds or different features that don’t work correctly with the programs and what we needed. In the end, we could not get the drone to fly with a controller after trying many different things. We got simple takeoff to work, but not the controller.

Stage 2

DynamoDB Table

First we wrote down what kind of columns we wanted for the tables. We created the FlightData table first, which will contain all the flights taken by the pilots. There will be the pilot by first and last name which will be a String, then the pilot’s academic department which is a String. The partition key will be ‘success’ noting whether the flight was successful or not, and the sort key will be the flight time starting from smallest to largest. The rest of the attributes are as follows:

checkpoints - which checkpoint out of 4 has the pilot made it to (number)  
success - if they make it to the target or not (String)  
final landing point - what the coordinates are of where they end up (number)  
controller type - what kind of controller they used (String)  

Then we decided to implement the main table into DynamoDB. We went to the AWS Academy Canvas page, then went to AWS Academy Learner Lab. Then we started the lab, and accessed the AWS Management Console. We then went to the DynamoDB console, to create a table. We clicked create a table, and for the table details it asked for the table name, partition key, sort key, and table settings. For the table name we called it “FlightData”. The partition key we named “Pilot” of type String, and the sort key was “Flight Time” also of type String. We kept the table settings to the default settings, then created the table. Once the status changed to active, we clicked in the FlightData table and then under actions clicked create item. Then we proceeded to create all the items listed above. For specific values we made up mock data to insert into the table. We wrote code to insert flight data to our table in DynamoDB, as seen in insert.py in our github repository. Unfortunately we could not test to see if this code actually does insert data into our tables because we were unable to get the drone to fly with the controller after several attempts.

Tutorial/Issues

We attempted to try and run the program with our laptops and couldnt successfully connect the controller to the drone. Both of us have Macbooks, and we think that the issue was related to that fact. When googling to find some solutions to the issues we were having, there were many websites that said that Macbook was missing some things in the way the system is set up. There was something that differed in its build compared to other laptops. Many people with Macbooks were having issues getting the controllers to connect via pygame. We specifically looked up the issues we were having and tried pretty much everything that was suggested on Google. We still could not get the controller to connect. So we attempted to use a different kind of laptop, one other than a Macbook. I (Jordan) was able to borrow a laptop from a relative, who had one to spare. My uncle let me borrow it for a short amount of time to see if that would fix the issue. We definitely got further with this laptop than with our Macbooks. The laptop I borrowed is a Lenovo Legion. I followed all the same exact steps from these instructions: https://github.com/hanyazou/TelloPy The laptop did not have Python, so I had to install Python 3.7 from the Microsoft Team store. I used the command prompt. It did not have pip, so I had to google how to download pip onto the laptop. It directed me to the website, and I just had to download a file and run a command on the command prompt. After successfully installing all of the necessary packages, I moved the pygame and tellopy folder to somewhere I could access it more easily. 

We first ran the simple takeoff command in the command prompt, and that worked easily, just as it had on the Macbooks. I then tried to run the video and controller command, and it got farther than it had on our Macbooks, but it said ‘no supported joystick found’ once again. Although it did print the name of the joystick, which it did not do last time on our Macbooks. It printed “Joystick name: PS4 Controller”. I went into the joystick_and_video.py file to edit the code, to add in the name it gave us. I changed one of the elif statements to include the name ‘PS4 Controller’, and to set the buttons equal to JoystickPS4. We ran that code this time, and it successfully connected to the controller. When we tried to actually control the drone using the PS4 controller, we did not succeed. We tried pushing all the buttons but the drone did not budge. The command prompt terminal was printing all kinds of statements. It showed that it was getting all of the controls, but it was not showing that through the drone. The drone did not move at all. It printed what buttons I was pushing on the controller when I pushed it, and it said what that button was supposed to do (such as land, forward, backward, etc.), but did not do the action. When I moved the joysticks around, it printed out a lot of messages in the terminal at a time because there were so many positions that the joysticks could be in. I noticed that some of the commands were wrong, so I attempted to fix that to see if maybe that was the issue. In the joystick_and_video.py file, it tells you in the comments which buttons should be in control of what action, but when printing in the terminal, they did not align with what the code was saying. I figured maybe the code was wrong, and decided to try and fix the controls. When pushing the button that was supposed to be takeoff, it did not register and did not print what I was pressing nor did it say takeoff. I went to the settings of the laptop, and went to the ‘Set up USB game controllers section’. The controller was shown and connected in the settings, and I clicked on properties. Upon pushing one of the buttons, a number that corresponded to that button would light up on the screen shown. There was also a section for the joysticks, when those would move, a plus symbol would move around in a square in sync with where you moved the joystick. I used these numbers and created another class in joystick_and_video.py named PS4ALT, and assigned the buttons with the numbers I figured out from the properties screen. After saving the file and running it again, it still did not work. The joystick connected and when pressing the buttons, they printed in the terminal, but the drone did not fly. I did see it say ‘takeoff’ this time in the terminal, but the drone was not flying at all. Once again, it did not budge. We tried looking at other submissions to see what everybody else did, but nobody really had the issue we were having. The drone would not takeoff. 


Machine 1: 13 inch MacBook Air (M1, 2020)
Initial Version: macOS 11.3.1
After Updating: macOS Monterey 12.6


Machine 2: MacBook Pro (15-inch, 2019)
macOS Monterey 12.6
2.6 GHz 6_Core Intel Core i7


*Command outputs were the same for both machines*

Machine 3: Legion Y7000P-1060
Intel Core i7-8750H 6 x 2.2 - 4.1 GHz
