from tkinter import *
import speedtest

def speedCheck():
    lab_processing.config(text="Fetching data...")  # Display processing message
    sp = speedtest.Speedtest()
    sp.get_best_server()
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str( round(sp.download()/(10**6),2))+" MBPS"
    up= str( round(sp.upload()/(10**6),2))+" MBPS"
    lab_down.config(text=down)
    lab_up.config(text=up)
    lab_processing.config(text="Data fetched successfully")


sp = Tk()
sp.title("Internet Speed Testometer ")
sp.geometry('450x500')
sp.config(bg="Red")

lab = Label(sp, text='Internet Speed Tester', font=('Roman',30,'bold'),bg='red')
lab.place(x=40,y=40,height=50,width=370)

lab = Label(sp, text='Download Speed', font=('Roman',20,'bold'),bg='red')
lab.place(x=60,y=140,height=30,width=300)

lab_down = Label(sp, text='00', font=('Roman',20,'bold'),bg='red')
lab_down.place(x=60,y=190,height=30,width=300)

lab = Label(sp, text='Upload Speed', font=('Roman',20,'bold'),bg='red')
lab.place(x=60,y=290,height=30,width=300)

lab_up = Label(sp, text='00', font=('Roman',20,'bold'),bg='red')
lab_up.place(x=60,y=340,height=30,width=300)

lab_processing = Label(sp, text='', font=('Roman', 18), bg='red')
lab_processing.place(x=60, y=430, height=30, width=300)

button = Button(sp,text='Check',font=('Roman',20,'bold'),relief=RAISED,command=speedCheck)
button.place(x=130,y=380,height=40,width=160)
sp.mainloop()