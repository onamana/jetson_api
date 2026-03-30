# 스마트폰에서 받은 JSON 데이터가 규격에 맞는지 검사
# app/models.py에는 DB 구조가 존재하고, schemas.py에는 통신 규격이 존재하는 것

from pydantic import BaseModel
from typing import List, Optional

# 젯슨 등록용
class JetsonCreate(BaseModel):
    jetson_wp: str
    jetson_loc: str
    status: bool = True
    ip_addr: str
    port: int

class JetsonResponse(JetsonCreate):
    jetson_id: int
    class Config:
        from_attributes = True

# 센서 등록용
class SensorCreate(BaseModel):
    sensor_type: str
    sen_name: str
    status: str
    jetson_id: int

class SensorResponse(SensorCreate):
    sen_id: int
    class Config:
        from_attributes = True

# 카메라 등록용
class CameraCreate(BaseModel):
    sensor_type: str = "CAM"
    sen_name: str
    status: str
    jetson_id: int
    ip_address: str
    camera_id: str
    camera_pw: str

# 위험 정보 알림용 (내부 모듈 -> API 서버)
class HazardAlert(BaseModel):
    sen_id: int
    jetson_id: int
    risk_level: str
    detail: str