from flask import Flask, render_template_string
name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']


myobj = Flask(__name__)


@myobj.route('/')
def home():

    return render_template_string("""
    <html>
           <h1>
                Welcome {{name}}!
            </h1>
                <body>
                <a href='www.google.com'>not google</a>
                <ul>
                {% for i in city_name  %}
                <li>{{i}}</li>
                {% endfor %}
                </ul>
                
                </body>
                
                

    </html >""", city_name=city_names, name=name)
