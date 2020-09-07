import tkinter as tk

F = 'Temp F'
C = 'Temp C'

def swapConvertion(event):
    global toCel
    global C
    global F
    global inputlable
    global outLable
    if toCel:
        inputlable['text'] = C
        outLable['text'] = F
    else:
        inputlable['text'] = F
        outLable['text'] = C
    toCel = not toCel

def convert(event):
    global toCel
    global outResult
    global inputbox
    if toCel:
        temp = (int(inputbox.get())-32)*(5/9)
        outResult['text'] = str(temp)
    else:
        temp = int(inputbox.get())*(9/5)+32
        outResult['text'] = str(temp)

toCel = True

window = tk.Tk()

for i in range(2):
    window.columnconfigure(i,weight=1,minsize=20)
    window.rowconfigure(i, weight=1,minsize=20)

inputlable = tk.Label(text=F)
inputlable.grid(row=0,column=0)

outLable = tk.Label(text=C)
outLable.grid(row=0,column=2,sticky='s')

outResult = tk.Label()
outResult.grid(row=1,column=2,sticky='w')

inputbox = tk.Entry()
inputbox.insert(0,'0')
inputbox.grid(row=1,column=0)

swap = tk.Button(text='Swap conversion')
swap.grid(row=0,column=1)
swap.bind('<Button-1>',swapConvertion)

print(swap.winfo_width())

convertButton = tk.Button(text='->',width=swap.winfo_width())
convertButton.bind('<Button-1>',convert)
convertButton.grid(row=1,column=1)


window.mainloop()