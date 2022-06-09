import streamlit as st
import requests
def dib(body, number, name, addr):
    box = body.container()
    col1, col2 = box.columns([1, 4])
    col1.write(number)
    up = col2.container()
    down = col2.container()
    up.write(name)
    down.write(addr)
def di(body, re):
    body.write(f'{re["total"]}개가 검색되었습니다.')
    fl = re['list']
    for i in range(len(fl)):
        info = fl[i]
        number = i + 1
        name = info['name']
        addr = info['addr']
        dib(body, number, name, addr)
def search(sc):
    url = 'https://floating-harbor-78336.herokuapp.com/fastfood'
    params = {'searchKeyword': sc}
    response = requests.get(url, params=params)
    return response.json()


head = st.container()
body = st.container()
foot = st.container()
pre_sc = ''
sc = head.text_input('음식점', placeholder='내용을 입력하시오')
Button = head.button('SEARCH')
if Button or sc != pre_sc:
    re = search(sc)
    di(body, re)
    pre_sc = sc