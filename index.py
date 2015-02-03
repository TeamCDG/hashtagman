from bottle import *
from hashtagman import *

#@route('/hello/<name>')
#def index(name):
#    return template('<b>Hello {{name}}</b>!', name=name)

sol = li[randint(0, len(li)-1)]
maxf = 10
curf = 0
tip = ""

@route('/')
def index():
    global tip
    global curf
    global maxf
    global sol

    if(request.query.get("tip") == None):
        sol = li[randint(0, len(li)-1)]

        maxf = 10
        curf = 0
        tip = ""

        return "#HashtagMan v0.0.1 alpha 2: "+greeting()+"<br>"+"<form action=\"/\" method=\"POST\">"+"<input type=\"text\" name=\"tip\" maxlength=\"1\">"+"<input type=\"submit\" name=\"baum\" value=\"baum\">"
    else:
        tip = request.query.get("tip") + request.query.get("ntip").upper()

        if(request.query.get("ntip").upper() == None):
            pass


        if(not rightChoice(tip, sol) and curf < maxf):
            return "<form action=\"/\" method=\"POST\">"+"<input type=\"hidden\" name=\"tip\" value=\""+tip+"\">"+"<input type=\"text\" name=\"ntip\" maxlength=\"1\">"+"<input type=\"submit\" name=\"baum\" value=\"baum\">"
        else:
            pass

@route('/doof')
def doof():
    return "du bist doof"

run(host='localhost', port=8080)
