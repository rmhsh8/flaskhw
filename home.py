from flask import Flask

app = Flask(__name__)

name = 'Lisa'
city_names = ["Paris", "London", "Rome", "Tahiti"]

@app.route('/')
def home():
    return '''
<html>
    </head>
    <body>
        <h1>Welcome ''' + name + ''' ! </h1>
        <p>
            <a href = "www.google.com" > not google </a>
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
#app.run()
#Worked with Jaskaran Singh, Chris Nicholson, and Minh Bui