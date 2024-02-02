
from fastapi import FastAPI, Request, Depends, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import multiprocessing as mp
import pyupbit
import datetime
import pandas as pd

app = FastAPI()


templates = Jinja2Templates(directory="./resources/templates")  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


major = pd.read_csv('src\main\python\static\메이저종목.csv')
major_list = major.market.to_list()
print(major_list)

if __name__ == "__main__":
    krw_tickers = pyupbit.get_tickers()
    print(krw_tickers)
    queue = mp.Queue()
    proc = mp.Process(
        target=pyupbit.WebSocketClient,
        args=('ticker', major_list, queue),
        daemon=True
    )
    proc.start()

    while True:
        data = queue.get()
        code = data['code']
        open = data['opening_price']
        high = data['high_price']
        low  = data['low_price']
        close = data['trade_price']
        ts = data['trade_timestamp']
        acc_volume = data['acc_trade_volume']
        acc_price = data['acc_trade_price']
        acc_ask_volume = data['acc_ask_volume']
        acc_bid_volume = data['acc_bid_volume']
        change_rate = data['signed_change_rate']

        dt = datetime.datetime.fromtimestamp(ts/1000)
        print(dt, code, open, high, low, close, acc_volume, acc_price, change_rate)


# cd src\main\python << 실행전 들어가야할 디렉토리 위치
# uvicorn main:app --reload  << (fastapi) 실행 시, 명령코드            

