# bmi_api.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义输入数据模型
class BMIRequest(BaseModel):
    height: float  # 单位：米
    weight: float  # 单位：公斤

# 计算 BMI 函数
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    status = "正常"
    if bmi < 18.5:
        status = "偏瘦"
    elif 18.5 <= bmi < 24.9:
        status = "正常"
    elif 25 <= bmi < 29.9:
        status = "超重"
    else:
        status = "肥胖"
    return round(bmi, 2), status

# 设置 API 路由
@app.post("/predict_bmi")
def predict_bmi(data: BMIRequest):
    bmi, status = calculate_bmi(data.height, data.weight)
    return {
        "BMI值": bmi,
        "状态": status
    }
