
from tkinter import *
from tkinter import messagebox 

import random 
import time 
import datetime 


root = Tk() 



root.geometry("1200x6000") 

root.title("Weather forecast") 

Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP) 

f1 = Frame(root, width = 800, height = 700,relief = SUNKEN) 
f1.pack(side = LEFT) 



localtime = time.asctime(time.localtime(time.time())) 

lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'), 
		text = "Weather - Forecast", 
					fg = "Black", bd = 10, anchor='w') 
					
lblInfo.grid(row = 0, column = 0) 

lblInfo = Label(Tops, font=('arial', 20, 'bold'), 
			text = localtime, fg = "Steel Blue", 
						bd = 10, anchor = 'w') 
						
lblInfo.grid(row = 1, column = 0) 

rand = StringVar() 
Result = StringVar() 
weather = StringVar()
speed = StringVar()

def qExit(): 
	root.destroy() 


def Reset(): 
	rand.set("") 
	Result.set("") 
	weather.set("")
	speed.set("")



lblReference = Label(f1, font = ('arial', 16, 'bold'), 
				text = "City :", bd = 16, anchor = "w") 
				
lblReference.grid(row = 0, column = 1) 

txtReference = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = rand, bd = 10, insertwidth = 4, 
						bg = "powder blue", justify = 'right') 
						
txtReference.grid(row = 0, column = 2) 



lblService = Label(f1, font = ('arial', 16, 'bold'), 
			text = "Temp (celsius) -", bd = 16, anchor = "w") 
			
lblService.grid(row = 0, column = 3) 

txtService = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = Result, bd = 10, insertwidth = 4 ,
					bg = "powder blue", justify = 'right') 
						
txtService.grid(row=0,column = 4) 

lblweather = Label(f1, font = ('arial', 16, 'bold'), 
			text = "Weather (type) -", bd = 16, anchor = "w") 
			
lblweather.grid(row = 1, column = 3) 

txtweather = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = weather, bd = 10, insertwidth = 4 ,
					bg = "powder blue", justify = 'right') 
						
txtweather.grid(row=1,column = 4) 


lblspeed = Label(f1, font = ('arial', 16, 'bold'), 
			text = "Wind Speed (m/s) -", bd = 16, anchor = "w") 
			
lblspeed.grid(row = 2, column = 3) 

txtspeed = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = speed, bd = 10, insertwidth = 4 ,
					bg = "powder blue", justify = 'right') 
						
txtspeed.grid(row=2,column = 4) 



import requests







def Ref():
	url='http://api.openweathermap.org/data/2.5/weather?q='+rand.get()+'&appid=40ec861494fcce665c5a32bf3ee37e41'
	json_data=requests.get(url).json()
	try:
		temp= str(round(json_data['main']['temp'] - 273.15,2))
	
	except KeyError:
		temp = 'not found'
	
	Result.set(temp)
	return Result



def Wea():
	url='http://api.openweathermap.org/data/2.5/weather?q='+rand.get()+'&appid=40ec861494fcce665c5a32bf3ee37e41'
	json_data=requests.get(url).json()
	try:
		var1=json_data['weather'][0]['description']
	
	except KeyError:
		var1 = 'not found'
	
	weather.set(var1)
	return weather

def Spd():
	url='http://api.openweathermap.org/data/2.5/weather?q='+rand.get()+'&appid=40ec861494fcce665c5a32bf3ee37e41'
	json_data=requests.get(url).json()
	try:
		var2=str(json_data['wind']['speed'])
	
	except KeyError:
		var2 = 'not found'
	
	speed.set(var2)
	return speed




btnTemp = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
						font = ('arial', 16, 'bold'), width = 10, 
					text = "Temperature ", bg = "powder blue", 
						command = Ref).grid(row = 5, column = 2) 

btnweather = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
						font = ('arial', 16, 'bold'), width = 10, 
					text = "Weather ", bg = "powder blue", 
						command = Wea).grid(row = 7, column = 2) 

btnspeed = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
						font = ('arial', 16, 'bold'), width = 10, 
					text = "Speed ", bg = "powder blue", 
						command = Spd).grid(row = 9, column = 2) 

btnReset = Button(f1, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('arial', 16, 'bold'), 
					width = 10, text = "Reset", bg = "green", 
				command = Reset).grid(row = 11, column = 2) 

btnExit = Button(f1, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('arial', 16, 'bold'), 
					width = 10, text = "Exit", bg = "red", 
				command = qExit).grid(row = 13, column = 2) 


root.mainloop() 












