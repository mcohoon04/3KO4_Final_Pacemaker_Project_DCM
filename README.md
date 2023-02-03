# 3KO4_Final_Pacemaker_Project_DCM
### Description:
This repository includes the python files for the DCM I created for the McMaster University 3KO4 Software
Development final project. This was a group project in which we split into two teams, one to handle the 
coding of the physical pacemaker and one to handle the coding of the DCM. I collaborated with Ahmed Sabrah on 
the DCM python code. The DCM acted as a UI for doctors and patients to log in, connect there pacemaker, 
adjust settings, and observe performance (via output ECG). This program communicates serially with a K64F 
microcontroller that the other team coded in Simulink to work as a pacemaker. The DCM and pacemaker also 
interfaced with an additional microcontroller that was pre-coded and provided to us to act as a heart for 
testing purposes.

### Notes if Attempting to Run:
~~After logging into the system, you will quickly realize that most of the function is prohibited as no 
“pacemaker” is connected. To override this, the code has been modified so you may fake a connection by 
connecting any device capable of serial UART communication. If using windows, you can then search for “Device 
Manager” and scroll down the list to find “Ports (COM & LPT)”. After clicking this dropdown menu you should 
see a COM# port that mentions UART. Remember this identifier (ex. “COM5”). After logging in, type the 
identifier into the Device text field and then press connect. Now all functionalities should be able to be 
tested ignoring the fact that the program is not actually interacting with a pacemaker. For convenience a 
fake ECG graph can be seen after sending data to the “pacemaker” in place of actual data.~~

### Update for running:
I altered the code so that it may appear to run with majority of functionality without faking a pacemaker
connection to an actual device capable of UART connection. Please note the imitated graph doesn't work 
perfectly especially when starting and stoping.
