from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import tkinter.messagebox	
import cv2
import PIL.Image
root = tk.Tk()
root.title('湧泉相報系統')
root.geometry('1024x600')
root.configure(bg="#FBE5D6")
global button_function_train,button_history,show_top_bar,show_title,show_eye,show_drown,show_train_title



###############################################################################################
img_start_1 = Image.open("./image/top_bar.png")
img_start_2 = img_start_1.resize((1024,100),Image.ANTIALIAS)
img_start_3 = ImageTk.PhotoImage(img_start_2)
#首頁標題
img_title_1 = Image.open("./image/title.png")
img_title_2 = img_title_1.resize((380,90),Image.ANTIALIAS)
img_title_3 = ImageTk.PhotoImage(img_title_2)
#眼睛圖示
img_eye_1 = Image.open("./image/eye_icon.png")
img_eye_2 = img_eye_1.resize((150,90),Image.ANTIALIAS)
img_eye_3 = ImageTk.PhotoImage(img_eye_2)
#空拍機圖示
img_drown_1 = Image.open("./image/drown_icon.png")
img_drown_2 = img_drown_1.resize((150,90),Image.ANTIALIAS)
img_drown_3 = ImageTk.PhotoImage(img_drown_2)
#訓練按鈕
train_btn_1 = Image.open("./image/train_btn.png")
train_btn_2 = train_btn_1.resize((300,90),Image.ANTIALIAS)
train_btn_3 = ImageTk.PhotoImage(train_btn_2)
#歷史按鈕
history_btn_1 = Image.open("./image/history.png")
history_btn_2 = history_btn_1.resize((300,90),Image.ANTIALIAS)
history_btn_3 = ImageTk.PhotoImage(history_btn_2)
################################################################################################
#訓練模式                                                                                      #
train_title_image = Image.open("./image/train_title.png").resize((380,90),Image.ANTIALIAS)     #

train_title = ImageTk.PhotoImage(train_title_image)

#返回按鈕圖示
return_icon_1 = Image.open("./image/return_icon.png")
return_icon_2 = return_icon_1.resize((90,90),Image.ANTIALIAS)
return_icon = ImageTk.PhotoImage(return_icon_2)

#home鍵按鈕圖示
home_icon_1 = Image.open("./image/home_icon.png")
home_icon_2 = home_icon_1.resize((90,90),Image.ANTIALIAS)
home_icon = ImageTk.PhotoImage(home_icon_2)

#home鍵按鈕圖示
home_icon_1 = Image.open("./image/home_icon.png")
home_icon_2 = home_icon_1.resize((90,90),Image.ANTIALIAS)
home_icon = ImageTk.PhotoImage(home_icon_2)

#確認鍵按鈕圖示
confirm_icon_1 = Image.open("./image/confirm_icon.png")
confirm_icon_2 = confirm_icon_1.resize((300,90),Image.ANTIALIAS)
confirm_icon = ImageTk.PhotoImage(confirm_icon_2)
###############################################################################################
#報告判斷區sidebar
report_judgment_area_1 = Image.open("./image/report_judgment_area.png")
report_judgment_area_2 = report_judgment_area_1.resize((300,495),Image.ANTIALIAS)
report_judgment_area = ImageTk.PhotoImage(report_judgment_area_2)

#開始報告btn
report_start_icon_1 = Image.open("./image/report_start_icon.png")
report_start_icon_2 = report_start_icon_1.resize((100,60),Image.ANTIALIAS)
report_start_icon = ImageTk.PhotoImage(report_start_icon_2)

#結束報告btn
report_finish_icon_1 = Image.open("./image/report_finish_icon.png")
report_finish_icon_2 = report_finish_icon_1.resize((100,60),Image.ANTIALIAS)
report_finish_icon = ImageTk.PhotoImage(report_finish_icon_2)

#報告名稱的區域                                                                                
report_name_area_1 = Image.open("./image/report_name_area.png")                               
report_name_area_2 = report_name_area_1.resize((210,70),Image.ANTIALIAS)                      
report_name_area = ImageTk.PhotoImage(report_name_area_2)                                     
                                                                                              
#顯示判斷區域                                                                                
judge_area_1 = Image.open("./image/judge_area.png")                               
judge_area_2 = judge_area_1.resize((170,70),Image.ANTIALIAS)                      
judge_area = ImageTk.PhotoImage(judge_area_2)                                     
###############################################################################################
#顯示肢體判斷區域                                                                                
body_score_1 = Image.open("./image/body_score.png")                               
body_score_2 = body_score_1.resize((420,385),Image.ANTIALIAS)                      
body_score = ImageTk.PhotoImage(body_score_2) 

#顯示眼神判斷區域    
eye_score_1 = Image.open("./image/eye_score.png")                               
eye_score_2 = eye_score_1.resize((420,385),Image.ANTIALIAS)                      
eye_score = ImageTk.PhotoImage(eye_score_2) 

###############################################################################################

#顯示歷史標題    
history_icon_1 = Image.open("./image/history_icon.png")
history_icon_2 = history_icon_1.resize((380,90),Image.ANTIALIAS)
history_icon = ImageTk.PhotoImage(history_icon_2)

#顯示歷史報告按鈕
report_history_btn_1 = Image.open("./image/report_history_btn.png")
report_history_btn_2 = report_history_btn_1.resize((400,140),Image.ANTIALIAS)
report_history_btn = ImageTk.PhotoImage(report_history_btn_2)

###############################################################################################
show_top_bar = tk.Label(root, image=img_start_3)
show_title = tk.Label(root, image=img_title_3, bg="#FFD966")
show_eye = tk.Label(root, image=img_eye_3, bg="#FFD966")
show_drown = tk.Label(root, image=img_drown_3, bg="#FFD966")

                      
                      
                      
panel_for_trt = tk.Label(root,height=500,width=720,bg="#000000")  # initialize image panel2
def open_cam():
    global cap
    # camera 
    width, height = 720, 500
    cap = cv2.VideoCapture(1)
    if cap is None:
        print("Camera Open Error")
        sys.exit(0)
def vid_stream():
    global panel_for_trt,imgtk
    success,img = cap.read()
    img = cv2.resize(img, dsize=(720, 500), interpolation=cv2.INTER_AREA)      
    cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)#转换颜色从BGR到RGBA
    current_image = PIL.Image.fromarray(cv2image)#将图像转换成Image对象
    imgtk = PIL.ImageTk.PhotoImage(image=current_image)
    panel_for_trt.imgtk = imgtk
    panel_for_trt.config(image=imgtk)
    root.after(1, vid_stream)
def del_cap():
    global cap,imgtk
    cap.release()
    imgtk=""   
def del_main():
    global button_function_train,button_history,show_top_bar,show_title,show_eye,show_drown
    button_function_train.place_forget(),button_history.place_forget(),show_title.place_forget(),show_eye.place_forget(),show_drown.place_forget()

def del_train_init_page():
    global show_train_title,button_return_icon,button_home_icon,button_confirm_icon,text,content
    show_train_title.place_forget(),button_return_icon.place_forget(),button_home_icon.place_forget(),button_confirm_icon.place_forget(),text.place_forget(),
    content.place_forget()
def del_train_start_page():
    global show_report_judgment_area,button_return_icon,button_home_icon,panel_for_trt,show_train_title,report_start_icon_btn,report_finish_icon_btn,show_report_name_area
    global show_judge_area_fun1,show_judge_area_fun2,show_title,fun1_text,fun2_text
    show_report_judgment_area.place_forget(),button_return_icon.place_forget(),button_home_icon.place_forget(),panel_for_trt.place_forget(),
    show_train_title.place_forget(),report_start_icon_btn.place_forget(),report_finish_icon_btn.place_forget(),show_report_name_area.place_forget(),
    show_judge_area_fun1.place_forget(),show_judge_area_fun2.place_forget(),show_title.place_forget()
    del fun1_text,fun2_text
def del_train_finish_page():
    global button_return_icon,button_home_icon,show_train_title,show_eye_score,show_body_score
    button_return_icon.place_forget(),button_home_icon.place_forget(),show_train_title.place_forget(),show_eye_score.place_forget(),show_body_score.place_forget()
def del_history_init_page():
    global show_history_icon,button_return_icon,button_home_icon,report_history_btn1,report_history_btn2,report_history_btn3,report_history_btn4
    show_history_icon.place_forget(),button_return_icon.place_forget(),button_home_icon.place_forget(),report_history_btn1.place_forget(),
    report_history_btn2.place_forget(),report_history_btn3.place_forget(),report_history_btn4.place_forget()
#輸入主題頁面
def train_init_page():
    global show_train_title,button_return_icon,button_home_icon,button_confirm_icon,text,content,theme_var
    show_train_title = tk.Label(root,bg="#FFD966", image = train_title)
    button_return_icon= tk.Button(root, image=return_icon,bg="#FFD966",command=lambda:[del_train_init_page(),main()], activebackground="#FFD966",bd=0)
    button_home_icon= tk.Button(root, image=home_icon,bg="#FFD966",command=lambda:[del_train_init_page(),main()], activebackground="#FFD966",bd=0) 
    #
    button_confirm_icon= tk.Button(root, image=confirm_icon,bg="#FBE5D6",command=lambda:[del_train_init_page(),train_start_page(content.get())], activebackground="#FBE5D6",bd=0)
    #
    show_train_title.place(x=320,y=5)
    button_return_icon.place(x=20,y=5)
    button_home_icon.place(x=900,y=5) 
    button_confirm_icon.place(x=360, y=344) 
    #輸入框
    text = tk.Label(root,font=("Calibri",36), text='請輸入報告主題',bg="#FBE5D6")
    text.place(x=345, y=180)
    theme_var = tk.StringVar()
    content = tk.Entry(root,textvariable=theme_var, bd=3,width=16,font=("Calibri",36))
    content.place(x=320, y=267)

#報告開始頁面
def train_start_page(theme_value):
    global theme_var,cap
    if theme_value == "":
        train_init_page()
        messagebox = tkinter.messagebox.showinfo('警告','請輸入報告主題')
    else:
        i = 0
        global show_report_judgment_area,button_return_icon,button_home_icon,panel_for_trt,show_train_title,report_start_icon_btn,report_finish_icon_btn,show_report_name_area
        global show_judge_area_fun1,show_judge_area_fun2,show_title,show_fun1,show_fun2,fun1_text,fun2_text
        show_train_title = tk.Label(root,bg="#FFD966", image = train_title)
        show_report_judgment_area = tk.Label(root,bg="#FBE5D6", image = report_judgment_area)
        button_return_icon= tk.Button(root, image=return_icon,bg="#FFD966",command=lambda:[del_train_start_page(),main()], activebackground="#FFD966",bd=0)
        button_home_icon= tk.Button(root, image=home_icon,bg="#FFD966",command=lambda:[del_train_start_page(),main()], activebackground="#FFD966",bd=0) 
        report_start_icon_btn = tk.Button(root, image=report_start_icon, bg="#FFF2CC",command=lambda:[open_cam(),vid_stream()], activebackground="#FFF2CC",bd=0)
        report_finish_icon_btn = tk.Button(root, image=report_finish_icon, bg="#FFF2CC",command=lambda:[del_cap(),del_train_start_page(),train_finish_page()], activebackground="#FFF2CC",bd=0)
        show_report_name_area = tk.Label(root,bg="#FFF2CC", image = report_name_area)
        show_judge_area_fun1 = tk.Label(root,bg="#FFF2CC", image = judge_area)   
        show_judge_area_fun2 = tk.Label(root,bg="#FFF2CC", image = judge_area)   
        show_title = tk.Label(show_report_name_area,bg="#F4B183",text=theme_value,font=("Calibri",26))
                              
        fun1_text = tk.StringVar()         
        fun1_text.set("眼神偏移次數:0")
        fun2_text = tk.StringVar()         
        fun2_text.set("身體晃動次數:0")  
        show_fun1 = tk.Label(show_judge_area_fun1,bg="#FBE5D6",textvariable=fun1_text,font=("Calibri",14))
                             
        show_fun2 = tk.Label(show_judge_area_fun2,bg="#FBE5D6",textvariable=fun2_text,font=("Calibri",14))
                             
        show_train_title.place(x=320,y=5)
        button_return_icon.place(x=20,y=5)
        button_home_icon.place(x=900,y=5)
        show_report_judgment_area.place(x=0,y=102)
        show_report_name_area.place(x=45,y=140)
        show_judge_area_fun1.place(x=63,y=230)
        show_judge_area_fun2.place(x=63,y=330)    
        report_start_icon_btn.place(x=30,y=450)
        report_finish_icon_btn.place(x=170,y=450)
        panel_for_trt.place(x=304,y=102)
        show_title.place(x=10,y=10)
        show_fun1.place(x=10,y=17)
        show_fun2.place(x=10,y=17)
    theme_var=""
#報告結束頁面
def train_finish_page():
    global button_return_icon,button_home_icon,show_train_title,show_eye_score,show_body_score
    show_train_title = tk.Label(root,bg="#FFD966", image = train_title)
    button_return_icon= tk.Button(root, image=return_icon,bg="#FFD966",command=lambda:[del_train_finish_page(),main()], activebackground="#FFD966",bd=0)
    button_home_icon= tk.Button(root, image=home_icon,bg="#FFD966",command=lambda:[del_train_finish_page(),main()], activebackground="#FFD966",bd=0)
    
    show_body_score = tk.Label(root,bg="#FBE5D6", image = body_score)
    show_eye_score = tk.Label(root,bg="#FBE5D6", image = eye_score)
    show_train_title.place(x=320,y=5)
    button_return_icon.place(x=20,y=5)
    button_home_icon.place(x=900,y=5)
    show_eye_score.place(x=550,y=160)
    show_body_score.place(x=50,y=160)
def history_init_page():
    global show_history_icon,button_return_icon,button_home_icon,report_history_btn1,report_history_btn1,report_history_btn2,report_history_btn3,report_history_btn4
    show_history_icon = tk.Label(root,bg="#FFD966", image = history_icon)
    button_return_icon= tk.Button(root, image=return_icon,bg="#FFD966",command=lambda:[del_history_init_page(),main()], activebackground="#FFD966",bd=0)
    button_home_icon= tk.Button(root, image=home_icon,bg="#FFD966",command=lambda:[del_history_init_page(),main()], activebackground="#FFD966",bd=0)
    report_history_btn1 = tk.Button(root, image=report_history_btn,bg="#FBE5D6",command=lambda:[del_history_init_page(),main()], activebackground="#FBE5D6",bd=0)
    report_history_btn2 = tk.Button(root, image=report_history_btn,bg="#FBE5D6",command=lambda:[del_history_init_page(),main()], activebackground="#FBE5D6",bd=0)
    report_history_btn3 = tk.Button(root, image=report_history_btn,bg="#FBE5D6",command=lambda:[del_history_init_page(),main()], activebackground="#FBE5D6",bd=0)
    report_history_btn4 = tk.Button(root, image=report_history_btn,bg="#FBE5D6",command=lambda:[del_history_init_page(),main()], activebackground="#FBE5D6",bd=0)
    show_history_icon.place(x=320,y=5)
    button_return_icon.place(x=20,y=5)
    button_home_icon.place(x=900,y=5) 
    report_history_btn1.place(x=70  ,y=180)
    report_history_btn2.place(x=70  ,y=380)
    report_history_btn3.place(x=550  ,y=180)
    report_history_btn4.place(x=550  ,y=380)
def main():
    global button_function_train,button_history,show_top_bar,show_title,show_eye,show_drown
    button_function_train= tk.Button(root, image=train_btn_3,bg="#FBE5D6",command=lambda:[del_main(),train_init_page()], activebackground="#FBE5D6",bd=0)
    button_history= tk.Button(root, image=history_btn_3,bg="#FBE5D6",command=lambda:[del_main(),history_init_page()], activebackground="#FBE5D6",bd=0) 
    show_title = tk.Label(root,bg="#FFD966", image = img_title_3)
    show_top_bar.place(x=-2,y=0)
    show_title.place(x=320,y=5)
    show_eye.place(x=20,y=5)
    show_drown.place(x=850,y=3) 
    button_function_train.place(x=360, y=222) 
    button_history.place(x=360, y=377)
main()                



root.mainloop()