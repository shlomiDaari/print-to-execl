
This scrip allow you to connect to any device that support ssh, the punch command to the remote device and then print it into excel file. 
The way that this script work it is first print it as a txt file and then convert the txt into excel file. 


Importent points:
  * If you want to add mroe commands to send please add DEVICE_ACCESS.send(b'your command here' + '\n') 
  yout can add commands as much as you want.
  
  * Sometimes you will see that it will print you just part of the output:
  Type "terminal length 0" in privileged mode to set your terminal to display without any breaks. 
  Another way is to check if the device support the command ''your command' | no-more' 
  
  
