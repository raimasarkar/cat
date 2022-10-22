import streamlit as st
import pandas as pd 
import numpy as np
import time
from datetime import datetime

from bokeh.plotting import figure
from PIL import Image

st.markdown('<style>description{color: grey;}</style>',unsafe_allow_html=True)
st.title('✨BE MEOWSOME✨')
st.markdown("<description>Cat is a domestic species of small carnivorous mammal. It is the only domesticated species in the family Felidae and is commonly referred to as the domestic cat or house cat to distinguish it from the wild members of the family.</description>",unsafe_allow_html=True)
st.sidebar.title('FACTS ABOUT KITTIES')
st.sidebar.button("🐈‍⬛")
st.sidebar.title('Daily sleep: 12 – 16 hours')
st.sidebar.title('Mass: 4 – 5 kg')
st.sidebar.title('Speed: 48 km/h')
st.sidebar.title('Lifespan: 12 – 18 years')
st.sidebar.title('Height: 23 – 25 cm')
st.sidebar.title('Scientific name: Felis catus')

image = Image.open('C:\\Users\\raima\\Downloads\\cat-1.jpg')
st.image(image,caption='One cat just leads to another.')




st.subheader('🥣Feeding Guidelines🥣')

l=[['1-2 Kg','15-30 G'],['2-3 Kg','30-45 G'],['3-4 Kg','45-60 G'],['4-5 Kg','60-80 G']]
df=pd.DataFrame(l,columns=['BODY WEIGHT','FEEDING AMOUNT/DAY'],index=['','','',''])
st.table(df)

image = Image.open('C:\\Users\\raima\\Downloads\\cat-2.jpg')
st.image(image,caption='We recommend feeding them atleast once in 3 hours if its still a baby.')

st.subheader('Should I get a Cat?')
if st.button('Yes'):
    st.write('Good Job')
else:
    st.write('Why Not?')

agree = st.checkbox('I agree cats are amazing!')

if agree:
    st.write('Great!')

agre = st.checkbox('Would you adopt a cat?')

if agre:
    st.write('Pawsome!')


genre = st.radio(
    "Infos about different breeds of cats:",
    ('Siberian cat', 'Persian cat', 'British Shorthair'))

if genre == 'Siberian cat':
    st.write('The Siberian is a centuries-old landrace of domestic cat in Russia and recently developed as a formal breed with standards promulgated the world over since the late 1980s. Siberians vary from medium to medium-large in size.')
    image = Image.open('C:\\Users\\raima\\Downloads\\cat3.jpg')
    st.image(image)


if genre == 'Persian cat':
    st.write('The Persian cat, also known as the Persian longhair, is a long-haired breed of cat characterized by a round face and short muzzle. The first documented ancestors of Persian cats were imported into Italy from Persia around 1620.')
    image = Image.open('C:\\Users\\raima\\Downloads\\cat4.jpg')
    st.image(image)

if genre == 'British Shorthair':
    st.write('The British Shorthair is the pedigreed version of the traditional British domestic cat, with a distinctively stocky body, dense coat, and broad face. The most familiar colour variant is the "British Blue", with a solid grey-blue coat, orange eyes, and a medium-sized tail.')
    image = Image.open('C:\\Users\\raima\\Downloads\\cat5.jpg')
    st.image(image)



age = st.slider('How many cats you want to adopt?', 0, 25)
st.write("I want ", age, ' cats')



st.subheader('Cat Lovers Through The Years')


x = [2000, 2005, 2010, 2020, 2022]
y = [3000, 2000, 5000, 4000, 7000]

p = figure(
    title='no of cat owners:',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Cat Owners', line_width=2)

st.bokeh_chart(p, use_container_width=True)

rat = st.slider('Do you love cats?', 0, 10, 5)
st.write("I would rate it a", rat)

if(rat==10):
    st.success('Congratulations!You are officially a Cat Guru now!', icon="✅")
    