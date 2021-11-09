import tkinter as tk  #引入tkinter模块
from googletrans import Translator   #pip install googletrans==4.0.0-rc1

#https://blog.csdn.net/Mountain_Zhou_only
#设置Google翻译服务地址
translator = Translator(service_urls=["translate.google.cn"])

window = tk.Tk()
window.title('论文整段翻译')
window.minsize(500,500)
 
#点击按钮后执行的函数
def changeString():
    text_output.delete('1.0','end')
    index=1
    string_input=""
    #把输入到文本框里面的整段论文拼接起来
    while True:
        if text_input.get(str(index)+'.0',str(index)+'.end')==text_input.get('end'):
            break
        else:
            if string_input=="":
                string_input=text_input.get(str(index)+'.0',str(index)+'.end')
            else:
                string_input =string_input+' '+text_input.get(str(index)+'.0',str(index)+'.end')
            index=index+1
            
    #处理好之后调用googletrans翻译整段英文论文
    print(string_input)
    string_output = translator.translate(text=string_input, dest='zh-CN')
    text_output.insert("insert",string_output.text)

#创建文本输入框和按钮
text_input  = tk.Text(window, width=100, height=24) #100的意思是100个平均字符的宽度，height设置为24行
text_output = tk.Text(window, width=100, height=24)
button = tk.Button(window,text="翻译",command=changeString,padx=32,pady=4,bd=4)

 
#把Text组件和按钮放在窗口上，然后让窗口打开，并处理在窗口内发生的所有事件；
text_input.pack()
text_output.pack()
button.pack()
window.mainloop()
