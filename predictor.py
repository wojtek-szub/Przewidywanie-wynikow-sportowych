import pickle
import pandas as pd
import matplotlib.pyplot as plt

with open("model.pkl","rb") as f:
    grid=pickle.load(f)
model=grid.best_estimator_

data=pd.read_csv("data.csv")
ranking=pd.read_csv("rating.csv")

def get_stats(home_team, away_team):
    line = pd.DataFrame()
    line['HomeTeam'] = [home_team]
    line['AwayTeam'] = [away_team]
    x = ranking.loc[ranking['Team'] == home_team,"Rating"]
    line['HELO'] = x.iloc[0]
    y = ranking.loc[ranking['Team'] == away_team,"Rating"]
    line['AELO'] = y.iloc[0]

    # line dla hometeam
    df = data[(data['HomeTeam'] == home_team) | (data['AwayTeam'] == home_team)]
    df = df.tail(1)
    df = df.reset_index()
    if df['HomeTeam'][0] == home_team:
        line['HTHG3'] = (3 * df['HTHG3'][0] + df['FTHG'])/4
        line['HTHGL3'] = (3 * df['HTHGL3'] + df['FTAG'][0])/4
        line['HTHG20'] = (20 * df['HTHG20'] + df['FTHG'][0])/21
        line['HTHGL20'] = (20 * df['HTHGL20'] + df['FTAG'][0])/21
        if df['FTR'][0] == 2:
            line['HW20'] = (20 * df['HW20'][0]+1)/21
            line['HL20'] = (20*df['HL20'][0])/21
            line['HW3'] = (3 * df['HW3'][0]+1)/4
            line['HL3'] = (3*df['HL3'][0])/4
        if df['FTR'][0] == 0:
            line['HW20'] = (20 * df['HW20'][0])/21
            line['HL20'] = (20*df['HL20'][0]+1)/21
            line['HW3'] = (3 * df['HW3'][0])/4
            line['HL3'] = (3*df['HL3'][0]+1)/4
        if df['FTR'][0] == 1:
            line['HW20'] = (20 * df['HW20'][0])/21
            line['HL20'] = (20*df['HL20'][0])/21
            line['HW3'] = (3 * df['HW3'][0])/4
            line['HL3'] = (3*df['HL3'][0])/4
        line['HTAG'] = df['HTAG'][0]
        line['HTAG5'] = df['HTAG5'][0]
        line['HTAGL'] = df['HTAGL'][0]
        line['HTAGL3'] = df['HTAGL3'][0]
        line['HTAW'] = df['HTAW'][0]
        line['HTAW3'] = df['HTAW3'][0]
        line['HTAL'] = df['HTAL'][0]
        line['HTAL3'] = df['HTAL3'][0]
    else:
        line['HTAG'] = (20 * df['ATAG20'] + df['FTAG'][0])/21
        line['HTAG5'] = (3 * df['ATAG3'] + df['FTAG'][0])/4
        line['HTAGL'] = (20 * df['ATAGL20'] + df['FTHG'][0])/21
        line['HTAGL3'] = (3 * df['ATAGL3'][0] + df['FTHG'][0])/4
        if df['FTR'][0] == 2:
            line['HTAW'] = (20 * df['AW20'][0])/21
            line['HTAL'] = (20*df['AL20'][0]+1)/21
            line['HTAW3'] = (3 * df['AW3'][0])/4
            line['HTAL3'] = (3*df['AL3'][0]+1)/4
        if df['FTR'][0] == 0:
            line['HTAW'] = (20 * df['AW20'][0]+1)/21
            line['HTAL'] = (20*df['AL20'][0])/21
            line['HTAW3'] = (3 * df['AW3'][0]+1)/4
            line['HTAL3'] = (3*df['AL3'][0])/4
        if df['FTR'][0] == 1:
            line['HTAW'] = (20 * df['AW20'][0])/21
            line['HTAL'] = (20*df['AL20'][0])/21
            line['HTAW3'] = (3 * df['AW3'][0])/4
            line['HTAL3'] = (3*df['AL3'][0])/4
        line['HTHG20'] = df['ATHG'][0]
        line['HTHG3'] = df['ATHG3'][0]
        line['HTHGL20'] = df['ATHGL'][0]
        line['HTHGL3'] = df['ATHGL3'][0]
        line['HW20'] = df['ATHW'][0]
        line['HW3'] = df['ATHW3'][0]
        line['HL20'] = df['ATHL'][0]
        line['HL3'] = df['ATHL3'][0]
    # line dla awayteam
    df = data[(data['HomeTeam']==away_team) | (data['AwayTeam'] == away_team)]
    df = df.tail(1)
    df = df.reset_index()
    if df['HomeTeam'][0] == away_team:
        line['ATHG'] = (20 * df['HTHG20'] + df['FTHG'][0])/21
        line['ATHG3'] = (3 * df['HTHG3'] + df['FTHG'][0])/4
        line['ATHGL'] = (20 * df['HTHGL20'] + df['FTAG'][0])/21
        line['ATHGL3'] = (3 * df['HTHGL3'] + df['FTAG'][0])/4
        if df['FTR'][0] == 2:
            line['ATHW'] = (20 * df['HW20'][0]+1)/21
            line['ATHL'] = (20*df['HL20'][0])/21
            line['ATHW3'] = (3 * df['HW3'][0]+1)/4
            line['ATHL3'] = (3*df['HL3'][0])/4
        if df['FTR'][0] == 0:
            line['ATHW'] = (20 * df['HW20'][0])/21
            line['ATHL'] = (20*df['HL20'][0]+1)/21
            line['ATHW3'] = (3 * df['HW3'][0])/4
            line['ATHL3'] = (3*df['HL3'][0]+1)/4
        if df['FTR'][0] == 1:
            line['ATHW'] = (20 * df['HW20'][0])/21
            line['ATHL'] = (20*df['HL20'][0])/21
            line['ATHW3'] = (3 * df['HW3'][0])/4
            line['ATHL3'] = (3*df['HL3'][0])/4
        line['ATAG20'] = df['HTAG'][0]
        line['ATAG3'] = df['HTAG5'][0]
        line['ATAGL20'] = df['HTAGL'][0]
        line['ATAGL3'] = df['HTAGL3'][0]
        line['AW20a'] =df['HTAW'][0]
        line['AW20'] = df['HTAW'][0]
        line['AW3'] = df['HTAW3'][0]
        line['AL20'] = df['HTAL'][0]
        line['AL3'] = df['HTAL3'][0]
    else:
        line['ATAG20'] = (20 * df['ATAG20'] + df['FTAG'][0])/21
        line['ATAG3'] = (3 * df['ATAG3'] + df['FTAG'][0])/4
        line['ATAGL20'] = (20 * df['ATAGL20'] + df['FTHG'][0])/21
        line['ATAGL3'] = (3 * df['ATAGL3'] + df['FTHG'][0])/4
        if df['FTR'][0] == 2:
            line['AW20a']=(20*df['AW20a'])/21
            line['AW20'] = (20 * df['AW20'][0])/21
            line['AL20'] = (20*df['AL20'][0]+1)/21
            line['AW3'] = (3 * df['AW3'][0])/4
            line['AL3'] = (3*df['AL3'][0]+1)/4
        if df['FTR'][0] == 0:
            line['AW20a']=(20*df['AW20a']+1)/21
            line['AW20'] = (20 * df['AW20'][0]+1)/21
            line['AL20'] = (20*df['AL20'][0])/21
            line['AW3'] = (3 * df['AW3'][0]+1)/4
            line['AL3'] = (3*df['AL3'][0])/4
        if df['FTR'][0] == 1:
            line['AW20a']=(20*df['AW20a'][0])/21
            line['AW20'] = (20 * df['AW20'][0])/21
            line['AL20'] = (20*df['AL20'][0])/21
            line['AW3'] = (3 * df['AW3'][0])/4
            line['AL3'] = (3*df['AL3'][0])/4
        line['ATHG'] = df['ATHG'][0]
        line['ATHG3'] = df['ATHG3'][0]
        line['ATHGL'] = df['ATHGL'][0]
        line['ATHGL3'] = df['ATHGL3'][0]
        line['ATHW'] = df['ATHW'][0]
        line['ATHW3'] = df['ATHW3'][0]
        line['ATHL'] = df['ATHL'][0]
        line['ATHL3'] = df['ATHL3'][0]
    
    kolejnosc = ['HomeTeam', 'AwayTeam','HELO', 'AELO',
       'HTHG3', 'HTHGL3', 'ATAG3', 'ATAGL3', 'HTHG20', 'HTHGL20', 'ATAG20',
       'ATAGL20', 'AW20a','HW20', 'HL20', 'AW20', 'AL20', 'HW3', 'HL3', 'AW3',
       'AL3', 'HTAG', 'HTAG5', 'HTAW', 'HTAL', 'HTAW3', 'HTAL3', 'HTAGL',
       'HTAGL3', 'ATHG', 'ATHG3', 'ATHW', 'ATHW3', 'ATHL', 'ATHL3', 'ATHGL',
       'ATHGL3']
    line = line[kolejnosc]
    return line

def predykcja(home_team, away_team):

    line = get_stats(home_team, away_team)
    predict = model.predict(line)[0]
    proba = model.predict_proba(line)[0]
    
    if predict == 2:
        print("wygra",home_team,"z prawdoppodobienstwem", round(proba[2],2))
    elif predict == 1:
        print("bedzie remis z prawdopodobienstwem ", round(proba[1],2))
    else:
        print("wygra",away_team,"z prawdoppodobienstwem", round(proba[0],2))

    labels = [away_team, 'Remis',home_team]
    colors = ['red', 'orange', 'green']

    plt.figure(figsize=(7,7), facecolor='white')

    wedges, texts, autotexts = plt.pie(
        proba,
        labels=labels,
        autopct='%1.1f%%',
        startangle=150,
        colors=colors,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2},
        textprops={'fontsize': 14, 'color': 'black'}
    )
    plt.title('Rozklad prawdopodobienstwa wyniku meczu', fontsize=16, fontweight='bold')
    plt.show()
    return