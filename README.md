# 473-Project

Stage 1

From https://github.com/hanyazou/TelloPy I followed the instructions listed. I first had to download tellopy to my machine by typing in ‘pip install tellopy’. I got an error saying ‘pip: command not found’ so I had to figure out that issue. I eventually got pip to install using the command ‘curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py’. After trying to install tellopy again it still gave the error ‘pip: command not found’. I tried to install/use pip3 instead with the command ‘pip3 install requests’. It was successfully installed, so then I called ‘pip3 install tellopy’. That worked and I then had tellopy installed on my machine. I then installed av by entering ‘pip3 install av’. Then ‘pip3 install opencv-python’. Finally, I installed pygame by using the command ‘pip3 install pygame’. 
I first tried the command ‘python -m tellopy.examples.simple_takeoff’ but it did not work, and I got an error saying ‘no module named pygame’. After trying many different things and trying to reinstall pygame using the github repo, I found that ‘python3 -m tellopy.examples.simpe_takeoff’ worked. The drone took off, hovered, then landed soon after.
 I then tried calling ‘python3 -m tellopy.examples.joystick_and_video’ to get the drone to work with a controller, but got an error saying that ‘no supported joystick found’. 
We then had to figure out what was wrong with the code and test to see why the controller would not connect. The controller connected to my laptop for sure because when you go to check in USB, it shows that a controller is connected to my laptop. It shows the name and all the information about it. We tried changing the elif statements to include the names listed in the information on my laptop, but nothing was working and the controller still wasn’t connecting. We had no idea why. I googled a bunch of things trying to figure out how to connect the controller and we tried many different ideas suggested on the internet. 
Eventually, once looking at more of the code in depth other than just the try block and elif statements, I realized that the except statement stated if there was any error, it would just pass the rest of the code and not look at it at all. The elif statements that we were changing were not getting looked at at all. By debugging using print statements, I figured out that there was an error with the line ‘js = pygame.joystick.Joystick(0)’ and the error was ‘pygame.error: Invalid joystick device number’. I tried different numbers but I wasn’t exactly sure what it was supposed to be. I googled the error but I tried many of the suggestions, and none of them worked. We googled many different questions and searched for solutions, but could not find any. I saw a lot of errors with people using MacBooks and that some things weren’t working for them, so I feel like that could be an issue. Something that the new MacBooks have different builds or different features that don’t work correctly with the programs and what we needed. In the end, we could not get the drone to fly with a controller after trying many different things. We got simple takeoff to work, but not the controller.

Machine 1: 13 inch MacBook Air (M1, 2020)
Initial Version: macOS 11.3.1
After Updating: macOS Monterey 12.6


Machine 2: MacBook Pro (15-inch, 2019)
macOS Monterey 12.6
2.6 GHz 6_Core Intel Core i7

*Command outputs were the same for both machines*
