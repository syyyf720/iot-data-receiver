# app.py
from flask import Flask, request, jsonify,render_template
from models import SensorData
from config import Session

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    temp = request.json.get('temperature')
    humi = request.json.get('humidity')
    localtion = request.json.get('location')
    
    session = Session()
    data = SensorData(temperature=temp, humidity=humi, location=localtion)
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
        'localtion': d.location
    } for d in all_data])

@app.route('/api/chart_data')
def chart_data():
    session = Session()
    all_data = session.query(SensorData).order_by(SensorData.id).all()
    session.close()
    temp_data = [{'id':d.id,'value':d.temperature} for d in all_data]
    humi_data = [{'id':d.id,'value':d.humidity} for d in all_data]
    return jsonify({'temp' : temp_data,'humi' : humi_data})

@app.route('/chart')
def chart_page():
    return render_template('chart.html')



if __name__ == '__main__':
    app.run(debug=True)