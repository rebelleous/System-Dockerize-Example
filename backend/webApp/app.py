from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

#DEBUG MODE#########
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True




@app.route('/', methods=['POST', 'GET'])
def get_my_ip():

    x_forwarded_for = request.environ.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.environ.get('REMOTE_ADDR')
    
    return render_template('main.html', ip_address=ip)

#host='0.0.0.0', port=80
if __name__ == '__main__':
#Run the application
    app.run(host='0.0.0.0', port=80)