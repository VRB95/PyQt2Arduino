<!-- PROJECT LOGO -->
<p align="center">
  <img src="img\logo.png" alt="Logo">
</p>

  <h3 align="center">PyQt2Arduino</h3>




<!-- TABLE OF CONTENTS -->
## Table of Contents


- [Table of Contents](#table-of-contents)
- [About The Project:](#about-the-project)
  - [Built With:](#built-with)
- [Prerequisites](#prerequisites)
- [Setup/Installation:](#setupinstallation)
- [Usage](#usage)
  - [Graphical User Interface](#graphical-user-interface)
  - [Arduino2PyQt Examples](#arduino2pyqt-examples)
      - [Send_Recive:](#sendrecive)
    - [I. Display_Text](#i-displaytext)
      - [Parts List:](#parts-list)
      - [Circuit Diagram](#circuit-diagram)
      - [Application Usage](#application-usage)
      - [Recive_Light_Intensity](#recivelightintensity)
      - [Recive_Temperature](#recivetemperature)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project:

PyQt2Arduino is mainly a terminal for serial comunication with Arduino, but it has a set of custom tabs for different functions, like displaying a text send from graphical user interface to an 16x2 lcd connected to Arduino, or displaying the temperature or ligh intensity recived from external sesnors. The application is writen in python and pyqt5 (gui part and also for serial communication it use QSerialPort) and can be easly modified for adapting it to a large variety of sensors, extra tab can be add in GUI and other functions can be create.

### Built With:
* [PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro/index.html)
* [Python](https://www.python.org)

## Prerequisites

I'll asume you already have installed python 3.x, now install [PyQt5](https://rsync.samba.org) packages:

* via pip
```sh
pip3 install PyQt5
```
* via apt-get (Ubuntu)
```sh
sudo apt-get install qtcreator pyqt5-dev-tools
```

## Setup/Installation:

1. Clone the repo:
```sh
git clone https://github.com/Vesa95/PyQt2Arduino.git
```
2. Upload to Arduino any example you want from Arduino2PyQt folder, but for the first steps with this application I highly recommand to upload "Send_Recive.ini" example first. With this code you send data (text) from PyQt2Arduino graphical user interface to Arduino, and Arduino will print on console (monitor) what it recived.
3. After you uploaded any example on Arduino, run PyQt2Arduino.py:
```sh
python3 PyQt2Arduino.py
```


<!-- USAGE EXAMPLES -->
## Usage
In this part, I'll show you how to work with this application and with every example from Arduino2PyQt folder.
1. Send_Recive;
2. Display_Text;
3. Recive_Light_Intensity;
4. Recive_Temperature;
5. All_In_One;
   
### Graphical User Interface
The GUI consists of 5 tabs: 2 main tabs and 3 custom tabs.
Every tab consists of other widgets.
1. Connect tab:
   * From here you can select all the settings for serial communication, such as PORT, BAUDRATE, DATABITS, PARTIY, and STOPBITS.
   * The default setting are: Baudrate: 9600, Databits: 8, StopBits: 1, Parity: NoParity, and only port need to be selected.

<p align="center">
  <img src="img\screen_1.png" alt="screenshot_1">
</p>  

2. Console tab:
   * This is the "Serial Monitor", from here you can send data to Arduino via "Send widget" and display in "Read widget" what Arduino send back to you.
   * Also, any data sended or recived will be saved in logfile.

<p align="center">
  <img src="img\screen_2.png" alt="screenshot_1">
</p> 

### Arduino2PyQt Examples

##### Send_Recive:
1. Upload this *.ini
2. Open PyQt2Arduino and check "Use Default Settings"
3. Go in Console tab and in "Send widget" write any text you want to send to Arduino, click Send button, and Arduino will send back to PyQt2Arduino, who will print it on "Read widget".
  
#### I. Display_Text
##### Parts List:
1. Arduino UNO
2. LCM 1602 IIC
3. LCD 1602   
##### Circuit Diagram
<p align="center">
  <img src="img\sch_display.png" alt="screenshot_1">
</p> 
##### Application Usage
1. Upload this *.ini
2. Open PyQt2Arduino and check "Use Default Settings"
3. Go to Display tab
4. Click on Connect button
5. Type whatever you want to be displayed on 16x2 lcd and click Send

<p align="center">
  <img src="img\screen_3.png" alt="screenshot_1">
</p> 
   
##### Recive_Light_Intensity
1. Upload this *.ini
2. Open PyQt2Arduino and check "Use Default Settings"
3. Go to Light S. tab
4. Click on Start Reading button
   
<p align="center">
  <img src="img\screen_4.png" alt="screenshot_1">
</p> 
  
##### Recive_Temperature
1. Upload this *.ini
2. Open PyQt2Arduino and check "Use Default Settings"
3. Go to Temperature. tab
4. Click on Start Reading button

<p align="center">
  <img src="img\screen_5.png" alt="screenshot_1">
</p> 

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Vesa Bogdan - vesabogdan95@gmail.com

Project Link: [https://github.com/vesa95/PyQt2Arduino](https://github.com/vesa95/PyQt2Arduino)





<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/mit
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/screenshot.png
