#--------------------------------------------------importing libraries------------------------------------------------------------------------
from tkinter import*
import tkinter as tk
from geopy.geocoders import  Nominatim
from timezonefinder import TimezoneFinder
from datetime import*
import requests
import pytz
from PIL import Image,ImageTk


#-----------------------------------------------------creating main/root window---------------------------------------------------------------
root=Tk()
root.title("Weather App")
root.geometry("800x470+50+50")
root.configure(bg="#57aaff")
root.resizable(False,False)


#------------------------------------------------declaring function for search icon-------------------------------------------------------------
def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()


    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)


    #--------------------------------------------fetching weather using weather api-------------------------------------------------------------
    api_url="https://api.openweathermap.org/data/2.5//weather?q="+city+"&appid=7028d07d0f4613bd0455637e1251955a"
    json_data=requests.get(api_url).json()
    

    #------------------------------------------------- fetching weather details----------------------------------------------------------------
    temp = int(json_data ["main"]['temp']-273.15)
    humidity = json_data ["main"]['humidity']
    pressure = json_data ["main"]['pressure']
    wind = json_data ["wind"]['speed']
    description = json_data ["weather"][0]['description']

    #---------------------------------------------------displaying weather details---------------------------------------------------------------
    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=(description))


#------------------------------------------------------------icon for the app------------------------------------------------------------------
image_icon=PhotoImage(file="C:/Users/hp/Documents/trainings & projects/weather app/Images/logo.png")
root.iconphoto(False,image_icon)


#-----------------------------------------------------------sunny image-------------------------------------------------------------------------
image=Image.open("C:/Users/hp/Documents/trainings & projects/weather app/Images/sun.png")
resize_image=image.resize((180,180))
photo=ImageTk.PhotoImage(resize_image)
label=Label(root,image=photo,bg="#57adff")
label.image=photo
label.place(x=30,y=30)



#------------------------------------------------------------search box-------------------------------------------------------------------------
Search_image=PhotoImage(file="C:/Users/hp/Documents/trainings & projects/weather app/Images/Rounded Rectangle 3.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)


#--------------------------------------------------------clouds image on search bar-------------------------------------------------------------
weat_image=PhotoImage(file="C:/Users/hp/Documents/trainings & projects/weather app/Images/Layer 7.png")
weather_image=Label(root,image=weat_image,bg="#203243")
weather_image.place(x=290,y=127)


#--------------------------------------------------------text field in the search bar-----------------------------------------------------------
textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()


#-------------------------------------------------------search icon on the search bar-----------------------------------------------------------
Search_icon=PhotoImage(file="C:/Users/hp/Documents/trainings & projects/weather app/Images/Layer 6.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)



#----------------------------------------------------------------bottom box---------------------------------------------------------------------
frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)


#----------------------------------------------------boxes inside the bottom box----------------------------------------------------------------
firstbox=PhotoImage(file="C:/Users/hp/Documents/trainings & projects/weather app/Images/Rounded Rectangle 2.png")
secondbox=PhotoImage(file="C:/Users/hp/Documents/trainings & projects/weather app/Images/Rounded Rectangle 2 copy.png")

lbl1=Label(frame,image=firstbox,bg="#212120")
lbl1.place(x=30,y=20)

lbl2=Label(frame,image=secondbox,bg="#212120")
lbl2.place(x=300,y=30)

lbl3=Label(frame,image=secondbox,bg="#212120")
lbl3.place(x=400,y=30)

lbl4=Label(frame,image=secondbox,bg="#212120")
lbl4.place(x=500,y=30)

lbl5=Label(frame,image=secondbox,bg="#212120")
lbl5.place(x=600,y=30)

lbl6=Label(frame,image=secondbox,bg="#212120")
lbl6.place(x=700,y=30)

lbl7=Label(frame,image=secondbox,bg="#212120")
lbl7.place(x=800,y=30)


#------------------------------------------------------------------timezone---------------------------------------------------------------------
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=500,y=20)

long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=540,y=50)



#--------------------------------------------------------------first cell in the bottom box------------------------------------------------------
firstframe=Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=315)

day1=Label(firstframe,text="Current Time",font=("arial",20),bg="#282829",fg="#fff")
day1.place(x=10,y=5)

#----------------------------------------------------------clock(here we will place time)-------------------------------------------------------
clock=Label(firstframe,font=("Helvetica",30,"bold"),fg="white",bg="#282829")
clock.place(x=30,y=50)


#--------------------------------------------------------------second cell in the bottom box----------------------------------------------------
secondframe=Frame(root,width=70,height=115,bg="#282829")
secondframe.place(x=305,y=325)

day2=Label(secondframe,text="Temp",font=("arial",10),bg="#282829",fg="#fff")
day2.place(x=14,y=5)

t=Label(secondframe,font=("Helvetica",11),fg="white",bg="#282829")
t.place(x=15,y=50)


#-----------------------------------------------------------third cell in the bottom box--------------------------------------------------------
thirdframe=Frame(root,width=70,height=115,bg="#282829")
thirdframe.place(x=405,y=325)

day3=Label(thirdframe,text="Humidity",font=("arial",10),bg="#282829",fg="#fff")
day3.place(x=7,y=5)

h=Label(thirdframe,font=("Helvetica",11),fg="white",bg="#282829")
h.place(x=20,y=50)


#-------------------------------------------------------------fourth cell in the bottom box------------------------------------------------------
fourthframe=Frame(root,width=70,height=115,bg="#282829")
fourthframe.place(x=505,y=325)

day4=Label(fourthframe,text="Pressure",font=("arial",10),bg="#282829",fg="#fff")
day4.place(x=7,y=5)

p=Label(fourthframe,font=("Helvetica",11),fg="white",bg="#282829")
p.place(x=3,y=50)

#--------------------------------------------------------------fifth cell in the bottom box-----------------------------------------------------
fifthframe=Frame(root,width=70,height=115,bg="#282829")
fifthframe.place(x=605,y=325)

day5=Label(fifthframe,text="Wind",font=("arial",10),bg="#282829",fg="#fff")
day5.place(x=14,y=5)

w=Label(fifthframe,font=("Helvetica",11),fg="white",bg="#282829")
w.place(x=7,y=50)

#--------------------------------------------------------------sixth cell in the bottom box-----------------------------------------------------
sixthframe=Frame(root,width=70,height=115,bg="#282829")
sixthframe.place(x=705,y=325)

day6=Label(sixthframe,text="Description",font=("arial",10),bg="#282829",fg="#fff")
day6.place(x=2,y=5)

d=Label(sixthframe,font=("Helvetica",11),fg="white",bg="#282829")
d.place(x=6,y=50)


root.mainloop()