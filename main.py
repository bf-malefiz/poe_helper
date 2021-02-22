import pyperclip

#pyperclip.copy('Hello, world!')

def get_item_clipboard():
    s = pyperclip.paste()
    s2 = s.split("--------")[1]
    s3 = s2.split("\r\n")[1:-1]
    s4 = [i.split("%") for i in s3]

    for count,value in enumerate(s4):
        s4[count][0] = int(s4[count][0])

    print(type(s4[0][0]))

get_item_clipboard()