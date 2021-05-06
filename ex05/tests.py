# -*- coding: utf-8 -*-

from elem import Text
from elements import *

def check_text():
  print(str(Html( [Head(), Body()])))

def full_test():
    print(str(Html([
        Head(Title(Text("\"Hello ground!\""))),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"})
        ])])))

def html_test():
    assert((str(Html())) == """<html></html>""")
    assert((str(Html(attr={'lang': 'en'}))) == """<html lang="en"></html>""")
    print("Html Test : OK.")

def test():
    html_test()
    full_test()
    check_text()


if __name__ == '__main__':
    try:
        test()
        print('Tests succeeded!')
    except AssertionError as e:
        print(e)
        print('Tests failed!')