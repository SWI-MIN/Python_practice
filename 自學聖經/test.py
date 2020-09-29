import tkinter as tk
def kwhp():
    if(kwhpin.get() != 0):
        kwtohp = kwhpin.get() * 1.34102209
        kwtohpans.set(str(kwhpin.get()) + ' kw = ' + str(round(kwtohp,2)) + ' hp')
    else:
        pass
    if(hpkwin.get() != 0):
        hptokw = hpkwin.get() * 0.745699872
        hptokwans.set(str(hpkwin.get()) + ' hp = ' + str(round(hptokw,2)) + ' kw')
    else:
        pass

swim = tk.Tk()
kwhpin = tk.DoubleVar()
kwtohpans = tk.DoubleVar()
hpkwin = tk.DoubleVar()
hptokwans = tk.DoubleVar()

swim.geometry('720x480')
swim.title('KW to HP & HP to KW')
# while(True):
text1 = tk.Label(swim, text = 'KW to HP', padx = 30, pady = 10, font = 30)#, width =30, height = 10, bg = 'grey', fg = 'black', font = ('標楷體',12))
text1.pack()
entry1 = tk.Entry(swim, textvariable = kwhpin, font = 30)
entry1.pack()
ans1 = tk.Label(swim, textvariable = kwtohpans, font = 30)
ans1.pack(pady = 10)
text2 = tk.Label(swim, text = 'HP to KW', padx = 30, pady = 10, font = 30)#, width =30, height = 10, bg = 'grey', fg = 'black', font = ('標楷體',12))
text2.pack()
entry2 = tk.Entry(swim, textvariable = hpkwin, font = 30)
entry2.pack()
ans2 = tk.Label(swim, textvariable = hptokwans, font = 30)
ans2.pack(pady = 10)
button1 = tk.Button(swim, text = '確認', command = kwhp, font = 30)
button1.pack(pady = 10)

swim.mainloop()
