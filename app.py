from flask import Flask, request, make_response  # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/hello', methods=['GET','POST']) #curl -X POST http://127.0.0.1:5555/hello sul terminale
def hello():
    if request.method == 'GET':
        return "You made a GET request\n"
    elif request.method == 'POST':
        return "You made a POST request\n"
    else:
        return "You will never see this message\n"

@app.route('/hello2') #curl -I http://127.0.0.1:5555/hello2 sul terminale, sul browser il link farà partire un download
def hello2():
    response = make_response('Hello World\n')
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream' #si può mettere anche text/plain al posto di application/octet-stream 
    return response

@app.route('/greet/<name>')
def greeting(name):
    return f"Hello {name}"

@app.route('/add/<number1>/<number2>') #si può anche utilizzare <int:number1> e  <int:number2>
def add(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    return f'{number1} + {number2} = {number1 + number2}'

@app.route('/handle_url_params')
def handle_url_params():
    #return str(request.args) #http://127.0.0.1:5555/handle_url_params?name=Mike&greeting=Hello
    
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args['name']
        return f'{greeting}, {name}'
    else:
        return "Some parameters are missing"

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port =5555, debug=True)