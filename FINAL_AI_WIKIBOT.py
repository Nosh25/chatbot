import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
from tkinter import *
from datetime import date

today = date.today()
root =Tk()
txt=Text(root)
txt.grid(row=0,column=0, columnspan=2)





def Mainmenu():
    txt.insert(END,"\n"+"Bot >> Welcome to the Main Menu!")
    txt.insert(END,"\n"+"Bot >> Below are some of the functions I perform:")
    txt.insert(END,"\n"+"Bot >> -- Get summary details.")
    txt.insert(END,"\n"+"Bot >> -- Get URL Link.")
    txt.insert(END,"\n"+"Bot >> -- Exit.")
    txt.insert(END,"\n"+"Bot >>  Enter the name of title you want to search for:")
   

       
def summary(info):
           
    page_py = wiki_wiki.page(info)

    if page_py.exists() == True:
                txt.insert(END,"\n"+"Here you go:")
                txt.insert(END, "\n"+"Page - Title: %s" % page_py.title)
                txt.insert(END,"\n"+"Page - Summary:%s" % page_py.summary ) 
                txt.insert(END,"\n")
                txt.insert(END,"\n"+"Bot >> Return to the Main menu?")
    else:
        txt.insert(END,"\n"+ "Bot >> Sorry, I was unable to process it.")
        txt.insert(END,"\n"+ "Can you repeat?")


def send():
    send=e.get()
    addt = "You >> "+e.get()
    input=send.lower()
    page_py = wiki_wiki.page(input)
    txt.insert(END,"\n"+addt)

    if(input=="hello"):
        txt.insert(END,"\n"+"Bot >>  Hello there!")
        txt.insert(END,"\n"+"Bot >> Hope you're having a nice day.")
        txt.insert(END,"\n"+"Bot >> How may I help you?")
        txt.insert(END,"\n"+"Bot >> You can see my functions by typing Mainmenu")
    elif(input=="hey"):
        txt.insert(END,"\n"+"Bot >> Hello there!")
        txt.insert(END,"\n"+"Bot >> Hope you're having a nice day.")
        txt.insert(END,"\n"+"Bot >> How may I help you")
        txt.insert(END,"\n"+"Bot >> You can see my functions by typing Mainmenu")
    elif(input=="hi"):
        txt.insert(END,"\n"+"Bot >> Hello there!")
        txt.insert(END,"\n"+"Bot >> Hope you're having a nice day.")
        txt.insert(END,"\n"+"Bot >> How may I help you")
        txt.insert(END,"\n"+"Bot >> You can see my functions by typing Mainmenu")
    elif(input=="Good morning"):
        txt.insert(END,"\n"+"Bot >> Hello there!")
        txt.insert(END,"\n"+"Bot >> Hope you're having a nice day.")
        txt.insert(END,"\n"+"Bot >> How may I help you")
        txt.insert(END,"\n"+"Bot >> You can see my functions by typing Mainmenu")
    elif(input=="hey there"):
        txt.insert(END,"\n"+"Bot >> Hello there!")
        txt.insert(END,"\n"+"Bot >> Hope you're having a nice day.")
        txt.insert(END,"\n"+"Bot >> How may I help you.")
        txt.insert(END,"\n"+"Bot >> You can see my functions by typing Mainmenu")
    elif(input=="what is your name?"):
        txt.insert(END,"\n"+"Bot >> My name is Wiki Bot")
        txt.insert(END,"\n"+"Bot >> Designed to fetch you data from Wikipedia in an instant!")
        txt.insert(END,"\n"+"Bot >> You can type Mainmenu to check all my functions.")
    elif(input=="are you a robot?"):
        txt.insert(END,"\n"+"Bot >> Yes, I am a Wiki Bot")
        txt.insert(END,"\n"+"Bot >> Designed to fetch you data from Wikipedia in an instant!")
        txt.insert(END,"\n"+"Bot >> Type Mainmenu to check all my Functions.")
    elif(input=="who made you?"):
        txt.insert(END,"\n"+"Bot >> I was made as a part of ISL mini project")
        txt.insert(END,"\n"+"Bot >> My creators are: Chandan Kashyap & Tejas Karande ")
        txt.insert(END,"\n"+"Bot >> You can see my functions by typing Mainmenu.")
    elif("function" in input):
        txt.insert(END,"\n"+"Bot >> I am Wikibot!")
        txt.insert(END,"\n"+"Bot >> Designed to fetch you different types of data from Wikipedia in an instant!")
        txt.insert(END,"\n"+"Bot >> You can see my functions by typing Mainmenu")
    elif(input=="what can you do?"):
        txt.insert(END,"\n"+"Bot >> I am Wikibot!")
        txt.insert(END,"\n"+"Bot >> Designed to fetch you different types of data from Wikipedia in an instant!")
        txt.insert(END,"\n"+"Bot >> You can see my functions by typing Mainmenu")
    elif(input=="mainmenu"):
        Mainmenu()
    elif(input=="main menu"):
        Mainmenu()
    elif(input=="yes"):
        Mainmenu()    
    elif(input=="no"):
        txt.insert(END,"\n"+"Bot >> Search another title: ")
    elif (input == "exit"):
        txt.insert(END,"\n"+"Bot >> Are you sure you want to exit?")
        txt.insert(END,"\n"+"Bot >> Type (Confirm) to exit.")
    elif (input == "confirm"):
        txt.insert(END,"\n"+"Bot >> Thankyou for visiting, Goodbye!")
        txt.insert(END,"\n"+"Bot >> Have a nice day!")
    elif (input == "goodbye"):
        txt.insert(END,"\n"+"Bot >> Thankyou for visiting, Goodbye!")
        txt.insert(END,"\n"+"Bot >> Have a nice day!")
    elif (input == "goodbye!"):
        txt.insert(END,"\n"+"Bot >> Thankyou for visiting, Goodbye!")
        txt.insert(END,"\n"+"Bot >> Have a nice day!")
    elif ("day" in input):
        d2 = today.strftime("%B %d, %Y")
        txt.insert(END,"\n"+"Bot >> Todays day is "+d2)
    else:
        summary(send)
        test =page_py.fullurl

    if (input == "link"):
        txt.insert(END,"\n"+"TEST LINK"+test)
        
    
    
    e.delete(0,E)

e = Entry(root,width=100)
send=Button(root,text="Send", command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Chatbot")
root.mainloop()