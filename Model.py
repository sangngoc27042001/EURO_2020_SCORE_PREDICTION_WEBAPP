import numpy as np
import pandas as pd
import math
import pickle
Country=['Belgium',
 'France',
 'England',
 'Portugal',
 'Spain',
 'Italy',
 'Croatia',
 'Denmark',
 'Germany',
 'Netherlands',
 'Switzerland',
 'Wales',
 'Poland',
 'Sweden',
 'Austria',
 'Ukraine',
 'Serbia',
 'Turkey',
 'Slovakia',
 'Romania',
 'Russia',
 'Hungary',
 'Republic of Ireland',
 'Czech Republic',
 'Norway',
 'Northern Ireland',
 'Iceland',
 'Scotland',
 'Greece',
 'Finland',
 'Bosnia-Herzegovina',
 'Slovenia',
 'Montenegro',
 'North Macedonia',
 'Albania',
 'Bulgaria',
 'Israel',
 'Belarus',
 'Georgia',
 'Luxembourg',
 'Armenia',
 'Cyprus',
 'Faroe Islands',
 'Azerbaijan',
 'Estonia',
 'Kosovo',
 'Kazakhstan',
 'Lithuania',
 'Latvia',
 'Andorra',
 'Malta',
 'Moldova',
 'Liechtenstein',
 'Gibraltar',
 'San Marino']
Country.sort()
with open('weights.pkl', "rb") as f:
        unpickler = pickle.Unpickler(f)
        w = unpickler.load()
        
weights=w[0]
basis=w[1]

data=pd.read_csv('data.csv')
data2=pd.read_csv('data2.csv')
def manage(country):
    for c in Country:
        if country == c.split(" ")[0]:
            return c

def return_rank(country):
    country=manage(country)
    return data[data.country==country].reset_index()['rank'][0]
def return_point(country):
    country=manage(country)
    return data[data.country==country].reset_index()['points'][0]

X=data2[['time','rank_1','rank_2','point_1','point_2']]
y=data2[['y_1','y_2']]
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X)

scaler_y = MinMaxScaler()
scaler_y.fit(y)

def predict(time, team1, team2):
    X=np.array([[time, return_rank(team1),return_rank(team2),return_point(team1),return_point(team2)]])
    yy=np.dot(scaler.transform(X), weights) +basis
    y_predict=scaler_y.inverse_transform(yy)
    winner=(yy.argmax()==0)
    if winner:
        winner=team1
    else:
        winner=team2
    return{
        'score':[[round(x) for x in y] for y in y_predict][0],
        'winner':winner
    }

