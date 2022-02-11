import chunk
import json
import time
from fastapi import FastAPI, UploadFile
import pandas as pd
from fastapi.middleware.gzip import GZipMiddleware


app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/uploadFile/{appName}")
def readExcel(file: UploadFile, appName,skipRows: int):
    start = time.time()
    excelFile = pd.ExcelFile(file.file.read())
    excel_data_df = pd.DataFrame()
    print(excelFile.sheet_names)
    excel_data_df = excel_data_df.append(pd.read_excel(excelFile,skiprows=skipRows))
    end = time.time()
    print(end - start)
    return json.loads(excel_data_df.to_json(orient='index'))
