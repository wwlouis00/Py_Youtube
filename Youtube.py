import tkinter as tk
#--建立主視窗--#
window = tk.Tk()    #建立主視窗
window.geometry('640x480')     #設立尺寸為300*150
window.title('Youtube 極速下載器')  #設立視窗標題
input_fm = tk.Frame(window, bg='red',width=640,height=120)  #建立Frame
input_fm.pack() #設定排版方法

lb = tk.Label(input_fm,
                bg= 'red',fg='white',
                text="請輸入Youtube網址",
                font=("標楷體",20),padx=50,pady=80)
lb.pack()
window.mainloop()   #啟動主視窗
