##############################################################         UI APP         ###########################################################################################


from Logic import get_response
from fastapi import FastAPI, Depends, HTTPException, status, Request, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
import uvicorn
import json
import re
import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse


load_dotenv()


app = FastAPI()

# Configure templates
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get_answer")
async def get_answer(request: Request, question: str = Form(...)):
    print(question)
    Answer= get_response(question)
    relevant_documents = Answer["source_documents"][0].page_content #"No information provided"
    answer = Answer['result']
    response_data = jsonable_encoder({"answer": answer, "relevant_documents": relevant_documents})
    print(answer)
    print(relevant_documents)
    res = JSONResponse(content=response_data)
    return res


if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=1973, reload=True)




