# app.py
from flask import Flask, request, jsonify
from models import SensorData
from config import Session

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    temp = request.json.get('temperature')
    humi = request.json.get('humidity')
    locals = request.json.get('location')
    
    session = Session()
    data = SensorData(temperature=temp, humidity=humi, location=locals)
    session.add(data)
    session.commit()
    session.close()
    
    return jsonify({'states': '接收成功'})

@app.route('/data')
def get_data():
    session = Session()
    all_data = session.query(SensorData).filter(SensorData.temperature > 20.0).all()
    session.close()
    
    return jsonify([{
        'id': d.id,
        'temp': d.temperature,
        'humi': d.humidity,
        'locals': d.location
    } for d in all_data])

if __name__ == '__main__':
    app.run(debug=True)