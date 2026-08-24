# IoT Data Receiver

物联网数据接收服务，用于接收和查询传感器数据。

## 快速开始

1. 安装依赖：pip install -r requirements.txt
2. 启动服务：python app.py
3. 访问地址：http://127.0.0.1:5000

## 接口说明

POST /upload  → 上传数据
GET  /data    → 查询数据

## 技术栈

Flask + SQLAlchemy + SQLite