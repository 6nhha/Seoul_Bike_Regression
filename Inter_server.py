from fastapi import FastAPI, Request,Body,Form
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.staticfiles import StaticFiles
from Seoul_Bike_model import common_fun
import requests
app = FastAPI()
#이미지등 직접 접근 수신방법
app.mount("/assets",
          StaticFiles(directory="./static"),
          name="assets")
templates = Jinja2Templates(directory="./")
@app.get("/")
def root(request:Request):
    return (templates.TemplateResponse(request,"index.html"))

@app.post("/anal_data")
def anal_data(data:dict):#(데이터변수:타입)
    #print(data)
    res = common_fun(data["user_data"], data["user_sub"])
    return int(res)


# @app.get("/")
# def main():#기본 리턴이 json 데이터
#     return {"message":"thank you sur!!!"}
# @app.get("/index")
# def index_page(request:Request):#(변수:타입형태)
#     return (templates.
#             TemplateResponse("index.html",
#                              {"request":request,
#                               "name":"홍길동"}))
# #get방식의 요청 1.
# @app.get("/test/api")
# def receive_data(name:str,age:int):
#     print(name,age)
#     return {"name_val":name,"age_val":age}
# #post 방식의 요청 2.
# @app.post("/test/api_1")
# def receive_api1(name:str=Body(...),age:int=Body(...)):
#     print(name,age)
#     return {"datas":f"{name},{age}"}
# # form 데이터 요청응답 3.
# @app.post("/test/api_2")
# def receive_form(myname:str=Form(...),
#                  myage:int=Form(...)):
#     print(myname,myage)
#     return {"form":f"{myname},{myage}"}


uvicorn.run(app,host="127.0.0.1",port=8000)

