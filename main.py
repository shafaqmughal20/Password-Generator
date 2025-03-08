import streamlit as st
import random
import string

def Password (len, data, spe) :
    character = string.ascii_letters

    if data :
        character += string.digits

    if spe :
        character += string.punctuation

    return ''.join(random.choice(character) for i in range(len))

st.subheader('🔐 Password Generator ')

len = st.slider('Select The Length :', min_value=8 , max_value=20 , value=10)

data = st.checkbox('Include Digits')

spe = st.checkbox('Include Special Characters')


if st.button('Generate Password') :
    use = Password(len , data , spe)

    st.write(f'Generated Password : {use}')


    st.write('Build With 💖 By Saad Qureshi !!!')