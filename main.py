from flask import Flask, render_template, request
import geocoder

app = Flask(__name__)
data = []

def get_coords(ip):
    g = geocoder.ip(ip)
    if g.ok:
        return g.latlng
    else: return 'Error'

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/ip", methods=['POST'])
def ip():
    global data
    data.append(request.json['ip'])
    nodupe = []
    [nodupe.append(val) for val in data if val not in nodupe]
    file = open('data.txt', 'w')
    for ip in nodupe:
        file.write(f"{ip} : {get_coords(ip)}")
    file.close()
    return 'hi'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True, use_reloader=False)
