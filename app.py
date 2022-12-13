from flask import Flask, redirect, request, render_template
import requests
import os
import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/')
def index():
    text = None
    text = request.args.get('country')
    print(text)
    # countryName = data['country']
    corona_data = 'https://disease.sh/v3/covid-19/countries/' + text
    data = requests.get(corona_data).json()
    allData = {'cases': data['cases'], 'death': data['deaths'], 'recovered': data['recovered'],
               'active': data['active']}

    opData = list(allData.keys())
    values = list(allData.values())

    fig = plt.figure()

    plt.pie(values, labels=opData, autopct='%.2f')

    plt.title(text)
    fig.savefig('static/test.png')
    plt.close(fig)
    image_data = os.path.join('/static/', 'test.png')


    return render_template("index.html", image=image_data)

if __name__ == "__main__":
    app.run()

