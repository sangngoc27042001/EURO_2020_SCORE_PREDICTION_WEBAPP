from flask import Flask, render_template, request
import Model
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', css="../static/style.css", country=Model.Country, predict=False)

@app.route("/predict",methods=['POST', 'GET'])
def predict():
    time = request.form['time']
    team1 = request.form['team1'].strip()
    team2 = request.form['team2'].strip()
    print(team2)
    result=Model.predict(time, team1, team2)
    return render_template('index.html', css="../static/style.css",
     country=Model.Country, predict=True, 
     team1=Model.manage(team1), team2=Model.manage(team2), 
     score1=result['score'][0],
     score2=result['score'][1] 
     )
if __name__=="__main__":
    app.run(debug=True)