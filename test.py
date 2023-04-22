import itertools
import zipfile
import tkinter

# 암호 해독 함수
def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len+1):
        to_attempt = itertools.product(passwd_string, repeat=len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            listbox.insert(tkinter.END, str(passwd))
            listbox.see(tkinter.END)
            frame1.update_idletasks()
            try:
                zFile.extractall(pwd=passwd.encode())
                print(f"비밀번호는 {passwd} 입니다!")
                tkinter.Label(window, relief="solid", text=passwd)
                result_label2.config(text=passwd)
                frame1.update_idletasks()
                return 1
            except:
                pass

def un_zip_base():

    # 암호관련 기본값
    passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    zFile = zipfile.ZipFile('123.zip')

    min_len = int(entry1.get())
    max_len = int(entry2.get())
    un_zip(passwd_string, min_len, max_len, zFile)

# GUI
window=tkinter.Tk()
window.title("Zipfile 암호해제")
window.geometry("400x400+100+100")
window.resizable(False, False)

label1=tkinter.Label(window, relief="solid" ,text="반드시 암호 해제를 원하는 파일 명을 123.zip으로 변경하셔야합니다")
label2=tkinter.Label(window, relief="solid", text="반드시 해제를 원하는 파일을 같은 경로에 두어야합니다")
label3 = tkinter.Label(window)
label4 = tkinter.Label(window, relief="solid", text="비밀번호최소길이 : ")
label5 = tkinter.Label(window, relief="solid", text="비밀번호최대길이 : ")
label1.grid(row=0)
label2.grid(row=1)
label3.grid(row=2)
label4.grid(row=3, sticky="w")
label5.grid(row=4, sticky="w")
entry1 = tkinter.Entry(window)
entry2 = tkinter.Entry(window)
entry1.grid(row=3)
entry2.grid(row=4)
button = tkinter.Button(window, text="시작", command=un_zip_base, repeatdelay=1000,)
button.grid(row =4, sticky="e")
frame1=tkinter.Frame(window, relief="solid")
frame1.grid(row=5, sticky="n")
listbox = tkinter.Listbox(frame1, width=54)

listbox.pack(side="left", fill="y")


scrollbar = tkinter.Scrollbar(frame1, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)

result_label1 = tkinter.Label(window, relief="solid", text="password")
result_label1.grid(row=6)
result_label2 = tkinter.Label(window, relief="solid", text="기다려주세요")
result_label2.grid(row=7)

window.mainloop()