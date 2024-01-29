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
    

    major = pd.read_csv('static/메이저종목.csv')
    info = pd.read_csv('static/현재가필드명.csv')
    major_list = major.market.to_list()

    info_keys = []
    info_values = []
    for i in range(len(info.필드.to_list())):
        info_keys.append(info.필드.to_list()[i])
        info_values.append(info.설명.to_list()[i])
    info_total = dict(zip(info_keys, info_values))

    major_coin_list = []

    for major in major_list:
        url = "https://api.upbit.com/v1/ticker"
        headers = {"accept": "application/json"}
        querystring = {"markets": major}
        response = requests.get(url, headers=headers, params=querystring)
        major_coin_list.append(response.json())

    info_coin_total= []

    for major_coin_data in major_coin_list:
        major_data = major_coin_data[0]
        
        coin_values = []  # Clear the list for each major coin data
        for key in info_total.keys():
            coin_values.append(major_data[key])
        info_coin_total.append(dict(zip(info_values, coin_values)))
    
    
    # HTML 템플릿에 데이터를 전달하여 렌더링
    # return templates.TemplateResponse("main.html", {"request": request, "result": info_coin_total})
    return JSONResponse(content=info_coin_total)


# cd src\main\python << 실행전 들어가야할 디렉토리 위치
# uvicorn main:app --reload  << (fastapi) 실행 시, 명령코드

#  D:\Programs\aiproject\workspace-sts\M-robo\src\main\python