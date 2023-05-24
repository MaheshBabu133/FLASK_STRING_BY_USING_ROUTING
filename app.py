from doctest import debug
from webbrowser import BackgroundBrowser
from flask import Flask

FAI=Flask(__name__)

@FAI.route('/Greeshma')
def Greeshma():
    return "<marquee><h1>Greeshma mam is my trainer<h1></marquee>"

@FAI.route('/Renu')
def Renu():
    return "<center><h1>Renu is very good girl</h1></center>"


@FAI.route('/Sonu')
def Sonu():
    return "<center><h1>Sonu is very good girl</h1></center>"


if __name__=='__main__':
    FAI.run(debug=True)
