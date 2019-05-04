#coding UTF-8
#author PE

import base64
open_icon = open("5.ico","rb")
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = "img = '%s'" % b64str
f = open("5.py","w+")
f.write(write_data)
f.close()