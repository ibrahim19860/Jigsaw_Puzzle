import random 
import numpy as np
import streamlit as st 
import pandas as pd
from PIL import Image
image = np.asarray(Image.open("bird.jpeg"))
    # print(image.shape)
st.image(image)
if not st.session_state.get("opened", False):
    curr_height=0 
    curr_width = 0 
    divided_width = image.shape[0]//4 
    divided_height = image.shape[1]//4
    black = np.asarray(Image.open("black.png"))[curr_width:curr_width+int(divided_height)]
    # print(image.shape)
    parts = [[] for _ in range(4)]
    for i in range(4):
        curr_width=0
        for j in range(4):
            parts[i].append(image[curr_width:curr_width+divided_width, curr_height:curr_height+divided_height])
            # print("Height" , curr_height, curr_height+divided_height, "Width", curr_width, curr_width+divided_width)
            curr_width+=divided_width
        curr_height+=divided_height 
    st.session_state["opened"]=True
    st.session_state["parts"]=parts 
    st.session_state["black"]=black
new_columns = st.columns(4)
with new_columns[0]:    
    button1 = st.button("Down")
with new_columns[1]:
    button2 = st.button("up")
with new_columns[2]:
    button3 = st.button("Left")
with new_columns[3]:
    button4 = st.button("Right")
columns = st.columns(4)
if st.session_state["parts"]:
    parts = st.session_state["parts"]

    new_parts = []
    for i in parts: 
        new_parts.extend(i)
    hm = {}
    x = 1
    for i in range(4):
        for j in range(4):
            hm[x]=parts[i][j]
            x+=1 
    #removing last part

for key in ['w','a','s','d']:
    st.session_state[key]=key
original = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
if not st.session_state.get("loaded", False):
    new = original.copy()
    for x in new: 
        random.shuffle(x)
    random.shuffle(new)
    st.session_state["new"]=new
    st.session_state["loaded"]=True
   

def printarr(new):
    for i in new:
        for j in i:
            print("%4d" %j , end = ' ')
        print('\n')
# for i in range(4):
#     for j in range(4):
#         curr = st.session_state["new"][i][j]
#         with columns[i]:
#             if curr in hm:
#                 st.image(hm[curr],use_column_width=True)



# function for moving the images
def move(curr_i, curr_j, playermove):
    if playermove=='s':
        if(curr_i+1==4):
            st.warning("wrong move")
            
            
        else:
            st.session_state["new"][curr_i][curr_j], st.session_state["new"][curr_i+1][curr_j] = st.session_state["new"][curr_i+1][curr_j], st.session_state["new"][curr_i][curr_j]
            curr_i += 1
    if playermove=='w':
        if(curr_i-1<0):
            st.warning("wrong move")
            
        else:
            st.session_state["new"][curr_i][curr_j], st.session_state["new"][curr_i-1][curr_j] = st.session_state["new"][curr_i-1][curr_j], st.session_state["new"][curr_i][curr_j]
            curr_i-=1
    if playermove=='d':
        if(curr_j-1<0):
            st.warning("wrong move")
            
        else:
            st.session_state["new"][curr_i][curr_j-1], st.session_state["new"][curr_i][curr_j] = st.session_state["new"][curr_i][curr_j], st.session_state["new"][curr_i][curr_j-1]
            curr_j -=1 
    if playermove=='a':
        if(curr_j+1==4):
            st.warning("wrong move")

        else:
            st.session_state["new"][curr_i][curr_j+1], st.session_state["new"][curr_i][curr_j] = st.session_state["new"][curr_i][curr_j], st.session_state["new"][curr_i][curr_j+1]
            curr_j +=1 
    return curr_i, curr_j
curr_i = 0 
curr_j = 0 
for i in range(4):
    for j in range(4):
        if st.session_state["new"][i][j]==0:
            curr_i=i 
            curr_j=j
st.session_state['game_started']=True
if "curr_i" not in st.session_state:
    st.session_state["curr_i"]=curr_i 
if "curr_j" not in st.session_state:
    st.session_state["curr_j"]=curr_j
# while st.session_state['new']!=original:
    # printarr(new)
# st.write(st.session_state["new"])
curr_i, curr_j = st.session_state["curr_i"], st.session_state["curr_j"]

# print(st.session_state["new"])
# curr_i, curr_j = move(curr_i, curr_j, input_move)
if button1:
    curr_i, curr_j = move(curr_i, curr_j, 'w')
if button2:
    curr_i, curr_j = move(curr_i, curr_j, 's')
if button3:
    curr_i, curr_j = move(curr_i, curr_j, 'a')
if button4:
    curr_i, curr_j = move(curr_i, curr_j, 'd')
st.session_state["curr_i"], st.session_state["curr_j"] = curr_i, curr_j
print(st.session_state["curr_i"], st.session_state["curr_j"])
print(st.session_state["new"], end='\n')
x = 0

if st.session_state["new"]==original:
    st.success("You Win!")
for i in range(4):
    for j in range(4):
        curr = st.session_state["new"][i][j]
        with columns[j]:
            if curr in hm:
                st.image(hm[curr], use_column_width=True)
            else:
                st.image(st.session_state["black"])
                st.image(st.session_state["black"])
                st.image(st.session_state["black"])
x+=1
columns.clear()
# for i in range(4):
#     for j in range(4):
#         curr = new[i][j]
#         with columns[i]:
#             if curr in hm: