# Magic_Mirror

**Goal:**
We will be building a smart mirror utilizing the raspberry pi that can give the user a welcome message, display the current date and time, and forecast for the day. The smart display will turn on when the user walks in front of the mirror, using a motion detection sensor. 

**Technologies:**
We intend to use a mirror for the screen with a similarly sized screen behind it to show through the mirror on the other side. For the programming languages we will use Python and Bash scripting. For video communications, we will be using the same motion camera used to start the mirror screen to show the user. For the weather and time, we will have the mirror connected to the internet and simply have the weather and clock boot up in the corners of the screen.

**Bill of Materials:**
A one way mirror (12x24), flat computer screen (similar size to one way mirror), wire, wood stain, wood planks, wood panel, power cable, motion camera, raspberry pi.



**Instructions for installation and code into Command Line:**
>$ git clone https://github.com/N03265566/Magic_Mirror

change directory into /code folder

*//install pip*
>$ sudo apt-get install python-pip

*//install packages in requirements.txt*
>$ sudo pip install -r requirements.txt

*//install python TKinter*
>$ sudo apt-get install python-imaging-tk

*//install beautiful soup*
>$ sudo apt-get install python-bs4
OR
>$ sudo pip install beautifulsoup4

**Instructions for building frame:**
![frameConstruction](pictures/20412.jpeg)



Utilizing Python's standard GUI, TKinter, we will be able to display the smart mirror objects to the monitor screen from the Pi.
Run the program with the following code:
>$ python smart_mirror.py
