import requests
import os
import winreg

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "referer":"https://noy1.top/",
}

def get_desktop(): # 获取桌面路径(用于保存文件)
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]

def download_all_book():
    book_num = 2
    while True: # 本子循环
        print("Download a new book. No.",book_num)
        os.chdir(get_desktop()) # 桌面路径
        os.makedirs("book_No."+str(book_num))
        page_num = 1
        while True: # 页面循环
            url = "https://img.noy.asia/"+str(book_num)+"/"+str(page_num)+".webp"
            a = requests.get(url,headers=headers)
            if (len(a.content)<1100): # 是否404
                break
            else:
                with open(get_desktop()+"\\book_No."+str(book_num)+"\\"+str(page_num)+".webp","wb") as f:
                    f.write(a.content)
                print("├ Download next book page. No.",page_num,"(Book No.",book_num,")")
            page_num += 1
        book_num += 1

def download_book():
    book_num = input("请输入本子编号(如https://noy1.top/#/read/1145的本子编号为1145) >>")
    print("Download a new book. No.",book_num)
    os.chdir(get_desktop()) # 桌面路径
    os.makedirs("book_No."+str(book_num))
    page_num = 1
    while True: # 页面循环
        url = "https://img.noy.asia/"+str(book_num)+"/"+str(page_num)+".webp"
        a = requests.get(url,headers=headers) # 爬取页面
        if (len(a.content)<1100):
            break
        else:
            with open(get_desktop()+"\\book_No."+str(book_num)+"\\"+str(page_num)+".webp","wb") as f:
                f.write(a.content)
            print("├ Download next book page. No.",page_num,"(Book No.",book_num,")")
        page_num += 1

def download_STE_book(start,end):
    book_num = start
    for i in range(start,end+1,1):
        print("Download a new book. No.",book_num)
        os.chdir(get_desktop()) # 桌面路径
        os.makedirs("book_No."+str(book_num))
        page_num = 1
        while True: # 页面循环
            url = "https://img.noy.asia/"+str(book_num)+"/"+str(page_num)+".webp"
            a = requests.get(url,headers=headers)
            if (len(a.content)<1100): # 是否404
                break
            else:
                with open(get_desktop()+"\\book_No."+str(book_num)+"\\"+str(page_num)+".webp","wb") as f:
                    f.write(a.content)
                print("├ Download next book page. No.",page_num,"(Book No.",book_num,")")
            page_num += 1
        book_num += 1

def download_STE_book_input():
    inputstart=input("输入开始下载的本子编号(如https://noy1.top/#/read/1145的本子编号为1145) >>")
    inputend=input("输入结束下载的本子编号 >>")
    if (inputstart<inputend):
        print("要下载",(int(inputend)-int(inputstart)+1),"本本子("+inputend+"-"+inputstart+"="+str(int(inputend)-int(inputstart)+1)+") 确认请输入Y")
        inputstr=input(">>")
        if (inputstr=="Y"):
            download_STE_book(int(inputstart),int(inputend))
    elif (inputstart>inputend):
        print("要下载",(int(inputstart)-int(inputend)+1),"本本子("+inputstart+"-"+inputend+"="+str(int(inputend)-int(inputstart)+1)+") 确认请输入Y")
        inputstr=input(">>")
        if(inputstr=="Y"):
            download_STE_book(int(inputend),int(inputstart))

    else:
        print("ERROR!\n开始下载的编号等于结束下载的编号")

print("┌───────────────────────────────┐")
print("│       Noyacg本子下载器        │")
print("├───────────────────────────────┤")
print("│>1:下载全部本子                │")
print("├───────────────────────────────┤")
print("│>2:输入指定本子编号下载        │")
print("├───────────────────────────────┤")
print("│>3:指定下载范围                │")
print("├───────────────────────────────┤")
print("│>4:退出                        │")
print("└───────────────────────────────┘")
inputnum = input(">>")

if (inputnum=="1"):
    download_all_book() # 下载所有本子
elif (inputnum=="2"):
    download_book() # 下载指定本子
elif (inputnum=="3"):
    download_STE_book_input() # 指定下载范围的本子