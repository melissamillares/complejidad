import tkinter as tk
import subprocess
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

#Basics window interface
aplicacion = tk.Tk()
aplicacion.geometry("510x700")
text_frame = Frame(aplicacion)
text_frame.configure(bg='#f1ecba')
text = tk.Text(text_frame, width = 90, height = 4)
text.pack(side=RIGHT, padx=20, pady=10)

title = 'Problema del periódico'
back = tk.Frame(master=aplicacion, bg='#f1ecba')
back.master.title(title)
# Don't allow the widgets inside to determine the frame's width / height
back.pack_propagate(0) 
# Expand the frame to fill the root window
back.pack(fill=tk.BOTH, expand=1) 
# label title
aplicacion.titulolbl = tk.Label(master=back, text="PROBLEMA DEL PERIÓDICO", anchor="center", font=("Ubuntu", 24), bg='#f1ecba')
aplicacion.titulolbl.place(x=80, y=10)

# function to execute minizinc and show the final result
def solucion():
    text_frame.pack()   
    # execute minizinc with data
    s = subprocess.run(["minizinc","PeriodicoGenerico.mzn","datos.dzn"], check=True, stdout=subprocess.PIPE, universal_newlines=True) 
    # result of minizinc
    o = s.stdout 
    # show info in text box
    text.delete('1.0', END)
    text.config(state=NORMAL)
    info = o
    text.delete('1.0', END)
    text.insert('1.0', info)


# create *.dzn file
def filedzn(ntopics, t, minpags, maxpags, numreaders):
    f = open("datos.dzn","w+")   
    pag = pages.get() 
    nminpag = len(minpags)
    m = []
    mx = []
    nr = [] 

    for j in range(nminpag):
        print(str(m))
        if(minpags[j].get() == "" or maxpags[j].get() == "" or numreaders[j].get() == ""):
            messagebox.showwarning("Warning","Inserte el nombre del tema, mínimo y máximo de páginas y el número de lectores")      
        elif (minpags[j].get() > maxpags[j].get()):
            messagebox.showwarning("Warning","El máximo de páginas debe ser mayor al mínimo de páginas")      
        else:
            m.append(int(minpags[j].get()))
            mx.append(int(maxpags[j].get()))
            nr.append(int(numreaders[j].get())) 

            for i in range(ntopics):             
                t[i].configure(state=DISABLED)
                minpags[i].configure(state=DISABLED)
                maxpags[i].configure(state=DISABLED)
                numreaders[i].configure(state=DISABLED)        

    f.write("minP = " + str(m) + ";\n")
    f.write("maxP = " + str(mx) + ";\n")
    f.write("readersPP = " + str(nr) + ";\n")

    f.write("l = " + pag + ";\n") #number of pages of the newspaper
    f.write("n = " + str(len(minpags)) + ";\n") #number of topics
    f.close()     
    solucion()

# create topic
def createTopic():      
    if(topics.get() == "" or pages.get() == ""):
        messagebox.showwarning("Warning","Inserte número de páginas y número de temas")
    else:
        pages.configure(state=DISABLED)
        topics.configure(state=DISABLED)
        topic.configure(state=DISABLED) 
        numTopics = topics.get()   
        y1 = 130 # y position for label and entry 
        
        for i in range(int(numTopics)):   
            # text box for topic
            topicLbl = Label(back, text="Tema: ", bg='#f1ecba')
            topicLbl.pack(side = LEFT)
            topicLbl.place(x=50,y=y1)
            t = tk.Entry(back, width=20)
            t.pack(side = RIGHT)
            t.place(x=320,y=y1)
            tpcs.append(t)
            y1 += 20             
            # text box for minimum pages
            minPagesLbl = Label(back, text="Mínimo de páginas: ", bg='#f1ecba')
            minPagesLbl.pack(side = LEFT)
            minPagesLbl.place(x=50,y=y1)
            minPages = tk.Entry(back, width=20)
            minPages.pack(side = RIGHT)
            minPages.place(x=320,y=y1)
            minpgs.append(minPages)
            y1 += 20
            # text box for maximum pages
            maxPagesLbl = Label(back, text="Máximo de páginas: ", bg='#f1ecba')
            maxPagesLbl.pack(side = LEFT)
            maxPagesLbl.place(x=50,y=y1)
            maxPages = tk.Entry(back, width=20)
            maxPages.pack(side = RIGHT)
            maxPages.place(x=320,y=y1)
            maxpgs.append(maxPages)
            y1 += 20
            # text box for interested readers
            readersLbl = Label(back, text="Lectores interesados: ", bg='#f1ecba')
            readersLbl.pack(side = LEFT)
            readersLbl.place(x=50,y=y1)
            readers = tk.Entry(back, width=20)
            readers.pack(side = RIGHT)
            readers.place(x=320,y=y1)
            reads.append(readers)
            y1 += 30       

        # button to open the image
        ejecutar = tk.Button(master=back, text="Ejecutar", command=lambda: filedzn(int(numTopics),tpcs,minpgs,maxpgs,reads))
        ejecutar.pack(side="top")
        ejecutar.place(x=225, y=y1+10)
            

# text box for number of pages
pagesLbl = Label(back, text="Número de páginas del periódico: ", bg='#f1ecba')
pagesLbl.pack(side = LEFT)
pagesLbl.place(x=50,y=50)
pages = tk.Entry(back, width=20)
pages.pack(side = RIGHT)
pages.place(x=320,y=50)
# text box for number of topics
topicsLbl = Label(back, text="Número de temas: ", bg='#f1ecba')
topicsLbl.pack(side = LEFT)
topicsLbl.place(x=50,y=70)
topics = tk.Entry(back, width=20)
topics.pack(side = RIGHT)
topics.place(x=320,y=70)
# button to create topics
topic = tk.Button(master=back, text="Crear temas", command=createTopic)
topic.pack(side="top")
topic.place(x=225, y=95)

minpgs = []
maxpgs = []
reads = []
tpcs = []

aplicacion.mainloop()
