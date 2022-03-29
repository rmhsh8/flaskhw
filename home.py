from flask import Flask
import jinja2

app = Flask(__name__)
app.config['DEBUG'] =True

name = 'Lisa'
city_names = ["Paris", "London", "Rome", "Tahiti"]

@app.route('/')
def main():
    return '''
<html>
    </head>
    <body>
        <h1>Welcome ''' + name + ''' </h1>
        <p>
            <a href = "https://www.google.com/" > not google</a>
            <ul>
                <li> ''' + city_names[0] + ''' </li>
                <li> ''' + city_names[1] + ''' </li>
                <li> ''' + city_names[2] + ''' </li>
                <li> ''' + city_names[3] + ''' </li>
                 </ul>
        </p>
    </body>
</html> 
'''
app.run()
