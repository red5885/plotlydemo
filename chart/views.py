from flask import render_template, jsonify

def test_chart():
    return render_template('chart.html')

def fetch_chart():
    return render_template('datafetch.html')

def get_data():
    data = {
        'x': [1,2,3,4,5],
        'y1': [1,2,4,8,16],
        'y2': [1,2,3,5,8]
    }
    return jsonify(data)