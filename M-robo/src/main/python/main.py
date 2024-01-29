from fastapi import FastAPI, Request, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import os
import pandas as pd
import requests
from typing import List, Optional

app = FastAPI()

# 템플릿 디렉토리 설정
templates = Jinja2Templates(directory="./resources/templates")  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def root():
    price_list = []
    price_list2 = []
    price_list3 = []
    total_price2 = []
    

    major = pd.read_csv('static/메이저종목.csv')    # 메이저 종목 pandas 데이터 프레임형식으로 불러오기
    info = pd.read_csv('static/현재가필드명.csv')   # 현재가필드명 pandas 데이터 프레임형식으로 불러오기
    major_list = major.market.to_list()            # 메이저 종목의 종목명 리스트로 변환

    info_keys = []
    info_values = []
    for i in range(len(info.필드.to_list())):       
        info_keys.append(info.필드.to_list()[i])
        info_values.append(info.설명.to_list()[i])
    info_total = dict(zip(info_keys, info_values))  # 현재가필드명 딕셔너리(Map)로 재생성
    print(info_total)

    major_coin_list = []

    for major in major_list:
        url = "https://api.upbit.com/v1/ticker"     # 업비트 API 현재가 연결
        headers = {"accept": "application/json"}
        querystring = {"markets": major}
        response = requests.get(url, headers=headers, params=querystring)
        major_coin_list.append(response.json())     # 업비트 API 실시간 현재가 데이터(딕셔너리/맵)  major_coin_list 리스트에 업로드

    info_coin_total= []

    for major_coin_data in major_coin_list: 
        major_data = major_coin_data[0]     
        
        coin_values = []  # Clear the list for each major coin data
        for key in info_total.keys():               
            coin_values.append(major_data[key])     
        info_coin_total.append(dict(zip(info_values, coin_values)))     # 업비트 API 현재가필드명정보 한국어를 key값으로, 현재가API데이터 값을 value값으로 딕셔너리(맵) 생성 
    
    
    # HTML 템플릿에 데이터를 전달하여 렌더링
    # return templates.TemplateResponse("main.html", {"request": request, "result": info_coin_total})
    return JSONResponse(content=info_coin_total)    #  필드명+현재가APIdate 딕셔너리인 info_coin_total JSON형식으로 전달


# cd M-robo\src\main\python << 실행전 들어가야할 디렉토리 위치
# uvicorn main:app --reload  << (fastapi) 실행 시, 명령코드

#  D:\Programs\aiproject\workspace-sts\M-robo\src\main\python