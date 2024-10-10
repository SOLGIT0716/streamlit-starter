import streamlit as st
import folium
import requests
import numpy as np
import pandas as pd
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
st.header('서울시 따릉이:bike:를 이용한 최단경로 탐색 ')
BIKEdata = pd.read_csv('bike_usage_0.csv', encoding='CP949')
STATIONdata = pd.read_csv('stations.csv')
WEATHERdata = pd.read_csv('weather.csv')

start = st.text_input('출발지 좌표를 입력하세요 ex: (37.4648267,126.9571988)') #출발지 좌표 (ex 37.4648267,126.9571988)
end = st.text_input('도착지 좌표를 입력하세요 ex: (37.555946,126.9572317)') #도착지 좌표 (ex 37.555946,126.9572317)

if start and end:
    request = requests.get(f'https://www.google.co.kr/maps/dir/{start}/{end}')
    result= request.text.split("markers=")[1].split("&amp")[0].split("%7C")
    startxy=list(map(float,[result[0].split("%2C")[0],result[0].split("%2C")[1]]))
    endxy=list(map(float,[result[1].split("%2C")[0],result[1].split("%2C")[1]]))
    startpoint = np.array(startxy)
    endpoint = np.array(endxy)
    dataxy=STATIONdata.loc[:,['Latitude','Longitude']].values
    resultstartxy = (abs(dataxy-startpoint))
    #print(resultstartxy)
    STATIONdata['distancestart'] = (resultstartxy[:,0]**2+resultstartxy[:,1]**2)**(1/2)
    nearstart = STATIONdata['distancestart'].idxmin()
    nearstart2 = STATIONdata[['Latitude','Longitude']].iloc[nearstart].to_list()
    resultendxy = (abs(dataxy-endpoint))
    STATIONdata['distanceend'] = (resultendxy[:,0]**2+resultendxy[:,1]**2)**(1/2)
    nearend=STATIONdata['distanceend'].idxmin()
    nearend2 =STATIONdata[['Latitude','Longitude']].iloc[nearend].to_list()
    col1,col2=st.columns(2)

    with col1:
        st.write('출발지에서 가장 가까운 보관소',STATIONdata.iloc[nearstart])

    with col2:
        st.write('도착지에서 가장 가까운 보관소',STATIONdata.iloc[nearend])

    m = folium.Map(width=600, height=400, location= nearstart2, zoom_start=12)
    lines =[startxy,nearstart2,nearend2,endxy]
    folium.PolyLine(
        locations = lines,
        tooltip = 'PolyLine'
    ).add_to(m)
    for op in lines:
        if op == lines[0]:
        
            h = f'출발지: {start}'
        elif op == lines[1]:
            h = f"가까운 station:{STATIONdata['Station'].iloc[nearstart]}"
        elif op == lines[2]:
            h = f"도착지에서 가까운 station:{STATIONdata['Station'].iloc[nearend]}"
        else:
            h =f'도착지: {end}'
        folium.Marker(
            location = op,
            radius = 10,   
            popup= h,
            icon=folium.Icon(color='red',icon='star')
        


            ).add_to(m)


    map_button = st.button('지도로 최단경로 보기')
    if map_button:
        
        folium_static(m)