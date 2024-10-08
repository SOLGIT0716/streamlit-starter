import streamlit as st
import random
import datetime
import numpy as np


button = st.button('로또를 생성해주세요')

if button:
    st.write('1. 행운의 번호:',np.array(random.sample(range(1,45),6)))
    st.write('2. 행운의 번호:',np.random.randint(low=1,high=45,size=6).tolist())
    st.write('3. 행운의 번호:',random.sample(range(1,45),6))
    st.write('4. 행운의 번호:',random.sample(range(1,45),6))
    st.write('5. 행운의 번호:',random.sample(range(1,45),6))