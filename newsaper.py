from tkinter import *
from tkinter import scrolledtext
import requests
import pyttsx3
import threading

root=Tk()
engine = pyttsx3.init()

root.geometry("1000x700")
root.state('zoomed')

root.minsize(400,200)
root.title("NEWSPAPER")
# root.iconbitmap("C:\\Users\\vedan\\Desktop\\Python Course with Notes\\my learning\\tkinter\\icon.ico")
root.iconbitmap(default="C:\\Users\\vedan\\Desktop\\Python Course with Notes\\my learning\\tkinter\\icon.ico")

def getNews():
    # tech_url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=4cfc5b9f4cb347a18193c9739f045425"
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=4cfc5b9f4cb347a18193c9739f045425"
    news=requests.get(url).json()

    articles=news["articles"]
    my_articles=[]
    global my_news
    my_news=""

    for article in articles:
        # my_articles.append(article["title"])
        my_articles.append(str(article["title"])+ "\n" + "\n" + "➡  " +str(article["description"])+"\n" )
        

    for i in range(len(articles)):
        my_news= my_news+str(i+1) + " . " +my_articles[i] + "\n"
            
    
    with open ("news.txt",'w',encoding="utf-8") as f:
        f.write(str(my_news))
    
    news_frame=Frame(root, bg="#EBD757", borderwidth=8, relief=RAISED)
    news_frame.pack(fill=BOTH,expand=1)
    # news_label=Label(news_frame, text=my_news, font="Oswald 5", justify="left" , bg="#EBD757")
    # news_label.pack()
    font_n="Oswald 13"
    scrText=scrolledtext.ScrolledText(news_frame,wrap=WORD,bg="#FFFD95",font=font_n)
    scrText.pack(fill=BOTH,expand=2)
    scrText.insert('insert',my_news)



f=Frame(root,bg="#57EB60", borderwidth=8, relief=SUNKEN, padx=50)
f.pack(side=TOP, fill=X)
label2=Label(f, text="Newspaper", font="Lobster 30", anchor=CENTER , bg="#57EB60")
label2.pack()

# f1=Frame(root,bg="#3AE3B5", borderwidth=8, relief=SUNKEN, padx=50)
# f1.pack(side=LEFT, fill=Y)
# label=Label(f1, text="    Images   ", font="Lobster 20", anchor=CENTER , bg="#3AE3B5")
# label.pack()

f2=Frame(root, bg="#CFB784", borderwidth=8, relief=RAISED)
f2.pack(side=TOP, fill=X)
label1=Label(f2, text="News", font="Impact 25", anchor="nw", bg="#CFB784")
label1.pack()

f3=Frame(root, bg="#6D9886", borderwidth=8, relief=RAISED)
f3.pack(side=BOTTOM, fill=BOTH)
label3=Label(f3, text="© Copyright to Vedansh Baranwal \n 2021", font="Impact 15", bg="#6D9886")
label3.pack()


getNews()

def readnews():
    engine.say(my_news)
    engine.runAndWait()



print(my_news)



btn=Button(f,text="Listen News",command=lambda: threading.Thread(target=readnews, daemon=True).start())
btn.pack()


root.mainloop()