from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/functions')
def functions():
	return render_template('functions.html')

@app.route('/odl')
def odl():
	return render_template('odl.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/blacklist', methods=['POST'])
def blacklist():
	print request.form['ip']
	requests.put('54.174.114.150:8083/vtn-webapi/dataflows?&switch_id=' + request.form['ip'] + '&port_name=s1-eth1&controller_id=odc&srcmacaddr=de3d.7dec.e4d2&no_vlan_id=true')
	return 'Submitted IP ' + request.form['ip'];

if __name__ == '__main__':
	app.run('0.0.0.0', 5000, True)
