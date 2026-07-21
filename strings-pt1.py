msg="welcome to Python 101: Strings"
    #0123456789
# new_msg={msg[-10],{msg[0:7],{msg[-5:-1]
tyler = (msg[8] + msg[12] + msg[2] + msg[1] + msg[-5]).title()

new_msg= f"{msg[-10]} {msg[0:7].title()} {msg[-5:-1].title()} {msg[8:10].title()} {tyler}"

print(new_msg)

print(new_msg[::-1])