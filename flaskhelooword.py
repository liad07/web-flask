import webbrowser
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">' \
           '  <script>function liad(){ window.alert("hello word") }</script>' \
           '<button  type="button" onclick="liad()" class="btn btn-outline-primary">hello word</button>'
webbrowser.open("http://192.168.1.194/")
app.run(host='0.0.0.0', port=80)
