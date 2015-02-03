# -*- coding: utf-8 -*-
from bottle import *
from hashtagman import *
from hpics import *

version = "#HashtagMan v0.1.0a1"

@route('/')
def index() -> "string":

    if not request.cookies.tip:
        sol = li[randint(0, len(li)-1)]
        response.set_cookie("sol", sol)

        ## -1 what you actually want
        response.set_cookie("maxf", "8")
        response.set_cookie("curf", "0")
        response.set_cookie("tip", "")

        return version +": "+ \
            greeting()+"<br>"+\
            "<form action=\"/\" method=\"POST\">"+\
            "<input type=\"text\" name=\"ntip\" maxlength=\"1\">"+\
            "<input type=\"submit\" name=\"guess\" value=\"raten\"> <br />" +\
            pics[0]
    else:
        tip = request.cookies.tip
        sol = request.cookies.sol
        curf = request.cookies.curf
        maxf = request.cookies.maxf

        return "Welcome back!<br>"+\
            partSol(tip, sol) + "<br />" +\
            "Faults " + curf + " / " + str(int(maxf)+1) + ": " + falseChars(tip, sol) +\
            "<form action=\"/\" method=\"POST\">"+\
            "<input type=\"text\" name=\"ntip\" maxlength=\"1\">"+\
            "<input type=\"submit\" name=\"guess\" value=\"raten\"> <br />" +\
            pics[int(curf)]

@route('/', method='POST')
def do_index() -> "string":
    ntip = request.forms.get("ntip")
    ttip = request.cookies.tip
    if not ntip:
        return """
        <p>Please insert a letter. <br />
           <a href="http://localhost:8080">go back -></a>
           </p>
        """

    ntip = ntip.upper()
    if ntip.upper() in ttip:
        return """
        <p>Please do not insert the same letter. <br />
        <a href="http://localhost:8080">go back -></a>
        </p>
        """
    else:
        tip = ttip + ntip
        response.set_cookie("tip", tip)

    sol = request.cookies.sol
    curf = request.cookies.curf
    maxf = request.cookies.maxf

    if not rightChoice(tip, sol) and curf < maxf:
        if len(falseChars(ntip, sol)) > 0:
            curf = int(curf) + 1
            response.set_cookie("curf", str(curf))
            curf = str(curf)

        return partSol(tip, sol) + "<br />" +\
            "Faults " + curf + " / " + str(int(maxf)+1) + ": " + falseChars(tip, sol) +\
            "<form action=\"/\" method=\"POST\">"+\
            "<input type=\"text\" name=\"ntip\" maxlength=\"1\">"+\
            "<input type=\"submit\" name=\"guess\" value=\"raten\"> <br />" +\
            pics[int(curf)]
    else:
        response.set_cookie("tip", "", expires=0)
        response.set_cookie("sol", "", expires=0)
        response.set_cookie("curf", "", expires=0)
        response.set_cookie("maxf", "", expires=0)

        if (rightChoice(tip, sol) and curf < maxf):
            return '<p style="font-size:300px">勝ち</p><br />'
        else:
            return '<h1>負け・・・死んだ</h1>' + pics[int(maxf)]

run(host='localhost', port=8080)
