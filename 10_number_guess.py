import streamlit as st
import random

st.title(':game_dice: 숫자 추측 게임 :game_dice:')

if 'answer' not in st.session_state:
    st.session_state.answer = random.randrange(1,101)

numb = st.number_input(label='1부터 100 사이의 무작위 정수를 선택하세요',min_value=0,max_value=100)

guess = st.button('추측하기')
restart = st.button('게임 재시작')
if guess:
    if numb < st.session_state.answer:
        st.write('너무 낮습니다! 다시 시도하세요.')
    elif numb > st.session_state.answer:
        st.write('너무 높습니다! 다시 시도하세요.')
    else :
        st.success('축하합니다! 정답은 {}입니다'.format(numb))



if restart:
    st.session_state.answer = random.randrange(1,101)
