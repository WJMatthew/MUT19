
# MUT Power Up players and their eligible teams (scraped from FootballDB)
#### - Matt , last updated: August 29, 2018<br>

- Added Sept. 1 legends


```python
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('csv/powerup_data_aug18.csv')
data.set_value(5, 'Ind', 1) # - added Ted
data.set_value(5, 'Bal', 0)
data.drop('Unnamed: 0', axis=1, inplace=True)
numeric_data = data.select_dtypes(include=['int64', 'float64']).drop('OVR', axis=1)
numeric_data.sum().sort_values(ascending=False)
teams = numeric_data.columns
```


```python
def insert_player(name, pos, pos2, teams, data):
    data = data.append({'Name': name, 'POS':pos, 'POS2':pos2}, ignore_index=True).fillna(0)
    
    for team in teams:
        data.set_value(len(data)-1, team, 1)
        
    return data
```


```python
# Updates
data = insert_player('Aeneas Williams', 'CB', 'DB', ['Ari', 'RAMS'], data)
data = insert_player('Tony Gonzalez', 'TE', 'TE', ['KC', 'Atl'], data)
data = insert_player('Barry Sanders', 'RB', 'RB', ['Det'], data)
data = insert_player('Brian Dawkins', 'FS', 'DB', ['Phi', 'Den'], data)
```


```python
data.tail()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>OVR</th>
      <th>POS</th>
      <th>PS4</th>
      <th>firstName</th>
      <th>lastName</th>
      <th>POS2</th>
      <th>Player</th>
      <th>Pos</th>
      <th>College</th>
      <th>...</th>
      <th>Phi</th>
      <th>Pit</th>
      <th>SF</th>
      <th>Sea</th>
      <th>TB</th>
      <th>Ten</th>
      <th>Was</th>
      <th>RAMS</th>
      <th>CHARGERS</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>165</th>
      <td>Michael Strahan</td>
      <td>0.0</td>
      <td>LE</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>166</th>
      <td>Aeneas Williams</td>
      <td>0.0</td>
      <td>CB</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>DB</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>167</th>
      <td>Tony Gonzalez</td>
      <td>0.0</td>
      <td>TE</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>TE</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Barry Sanders</td>
      <td>0.0</td>
      <td>RB</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>RB</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>169</th>
      <td>Brian Dawkins</td>
      <td>0.0</td>
      <td>FS</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>DB</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 44 columns</p>
</div>




```python
# Number of teams per power up player
data['numTeams'].value_counts().sort_values(ascending=False)
```




    1.0    114
    2.0     35
    3.0     10
    0.0      4
    4.0      3
    5.0      2
    6.0      1
    7.0      1
    Name: numTeams, dtype: int64




```python
a = numeric_data.sum().sort_values(ascending=False)[1:]

pal = {'Phi':'xkcd:green', 'NE': 'darkblue', 'NO':'gold', 'GB':'green',
       'Min':'xkcd:purple', 'Was':'maroon', 'Ten': 'cyan', 'TB':'xkcd:crimson',
       'Sea':'chartreuse', 'CHARGERS':'xkcd:azure', 'Atl':'xkcd:red',
       'Bal':'indigo', 'RAMS':'xkcd:khaki', 'KC':'red', 'NYJ': 'darkgreen',
       'Jax':'xkcd:darkgreen', 'Oak':'grey', 'Buf':'xkcd:blue', 'Car':'aqua',
       'Cle':'chocolate', 'Pit':'yellow', 'NYG':'blue', 'SF':'xkcd:gold',
       'Chi':'xkcd:orange', 'Dal':'xkcd:darkblue', 'Mia':'xkcd:aqua',
       'Den':'xkcd:orangered', 'Hou':'xkcd:navy', 'Ari':'xkcd:red',
       'Cin':'xkcd:orange', 'Det':'xkcd:lightblue', 'Ind':'xkcd:azure'}
```


```python
sns.set_style("whitegrid")

plt.figure(figsize=(15, 10))
ax = sns.barplot(x=a.values, y=a.index, palette=pal)
for p in ax.patches:
    if np.isnan(p.get_width()):
        gh = 0.0
    else:
        gh = np.round(p.get_width(), 2)
                
    ax.annotate(int(gh), (np.round(gh+0.15, 3), p.get_y()+0.5))
ax.set_title('Number of Power Up Players Eligible for Each Team');
```


![png](output_7_0.png)



```python
data.to_csv('powerup_sep1.csv')
small_data = data[['Name','POS','Teams', 'numTeams']]
small_data.to_csv('small_powerup_data.csv')
```

### Biggest journeymen


```python
small_data['Teams'] = small_data['Teams'].str.replace(',', ', ')
small_data['Teams'] = small_data['Teams'].str.replace('NFLEHam', ' ')
small_data[ small_data['numTeams'] >= 4].sort_values('numTeams', ascending=False)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>NO, NYJ, TB, Ten, Cin, SD, Bal</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Min, Oak, NE, Min, Ten, SF</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>TB, Bal, NE, Ind, Oak</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Terrell Owens</td>
      <td>WR</td>
      <td>SF,  Phi,  Dal,  Buf,  Cin</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Michael Vick</td>
      <td>QB</td>
      <td>Atl, Phi, NYJ, Pit</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Demario Davis</td>
      <td>MLB</td>
      <td>NYJ, Cle, NYJ, NO</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Rod Woodson</td>
      <td>CB</td>
      <td>Pit,  SF,  Bal,  Oak</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
team_abbrevs = list(pal.keys())
team_list = []

data.reset_index(drop=True, inplace=True)
small_data.reset_index(drop=True, inplace=True)

for team in team_abbrevs:
    current_team = data[ data[team]==1]
    indices = current_team.index.values
    team_list.append(small_data.iloc[indices])
```

## Team Lists

![Image](http://content.sportslogos.net/logos/7/167/thumbs/960.gif)


```python
i=0
team_list[i]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Michael Vick</td>
      <td>QB</td>
      <td>Atl, Phi, NYJ, Pit</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Reggie White</td>
      <td>LE</td>
      <td>Phi, GB, Car</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Nigel Bradham</td>
      <td>LOLB</td>
      <td>Buf, Phi</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Fletcher Cox</td>
      <td>DT</td>
      <td>Phi</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zach Ertz</td>
      <td>TE</td>
      <td>Phi</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Brandon Graham</td>
      <td>LE</td>
      <td>Phi</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Jordan Hicks</td>
      <td>MLB</td>
      <td>Phi</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Malcolm Jenkins</td>
      <td>SS</td>
      <td>NO, Phi</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Lane Johnson</td>
      <td>RT</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Jason Kelce</td>
      <td>C</td>
      <td>Phi</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Jason Peters</td>
      <td>LT</td>
      <td>Buf, , Phi</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Carson Wentz</td>
      <td>QB</td>
      <td>Phi</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Terrell Owens</td>
      <td>WR</td>
      <td>SF,  Phi,  Dal,  Buf,  Cin</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>169</th>
      <td>Brian Dawkins</td>
      <td>FS</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/151/thumbs/y71myf8mlwlk8lbgagh3fd5e0.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    NE





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Min, Oak, NE, Min, Ten, SF</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>David Andrews</td>
      <td>C</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Malcolm Butler</td>
      <td>CB</td>
      <td>NE, Ten</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>James Develin</td>
      <td>FB</td>
      <td>, NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Julian Edelman</td>
      <td>WR</td>
      <td>, NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Stephon Gilmore</td>
      <td>CB</td>
      <td>Buf, NE</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Rob Gronkowski</td>
      <td>TE</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Devin McCourty</td>
      <td>FS</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>TB, Bal, NE, Ind, Oak</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Jabaal Sheard</td>
      <td>RE</td>
      <td>Cle, NE, Ind</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/175/thumbs/907.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    NO





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>NO, NYJ, TB, Ten, Cin, SD, Bal</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Willie Roaf</td>
      <td>LT</td>
      <td>NO, KC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Drew Brees</td>
      <td>QB</td>
      <td>SD, NO</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Demario Davis</td>
      <td>MLB</td>
      <td>NYJ, Cle, NYJ, NO</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Jimmy Graham</td>
      <td>TE</td>
      <td>NO, Sea, GB</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Malcolm Jenkins</td>
      <td>SS</td>
      <td>NO, Phi</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>90</th>
      <td>Cameron Jordan</td>
      <td>LE</td>
      <td>NO</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Alvin Kamara</td>
      <td>HB</td>
      <td>NO</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Marshon Lattimore</td>
      <td>CB</td>
      <td>NO</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>119</th>
      <td>Ryan Ramczyk</td>
      <td>RT</td>
      <td>NO</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>143</th>
      <td>Michael Thomas</td>
      <td>WR</td>
      <td>NO</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/171/thumbs/dcy03myfhffbki5d7il3.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    GB





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Reggie White</td>
      <td>LE</td>
      <td>Phi, GB, Car</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Ted Hendricks</td>
      <td>LOLB</td>
      <td>Bal, GB, Oak, LAR</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Davante Adams</td>
      <td>WR</td>
      <td>GB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>David Bakhtiari</td>
      <td>LT</td>
      <td>GB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Kenny Clark</td>
      <td>DT</td>
      <td>GB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Jimmy Graham</td>
      <td>TE</td>
      <td>NO, Sea, GB</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Casey Hayward</td>
      <td>CB</td>
      <td>GB, SD, LAC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Micah Hyde</td>
      <td>SS</td>
      <td>GB, Buf</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Aaron Rodgers</td>
      <td>QB</td>
      <td>GB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Josh Sitton</td>
      <td>LG</td>
      <td>GB, Chi, Mia</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/172/thumbs/17227042013.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Min





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>Steve Hutchinson</td>
      <td>LG</td>
      <td>Sea, Min, Ten</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Anthony Barr</td>
      <td>ROLB</td>
      <td>Min</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Stefon Diggs</td>
      <td>WR</td>
      <td>Min</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Everson Griffen</td>
      <td>RE</td>
      <td>Min</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Linval Joseph</td>
      <td>DT</td>
      <td>NYG, Min</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>122</th>
      <td>Xavier Rhodes</td>
      <td>CB</td>
      <td>Min</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>132</th>
      <td>Harrison Smith</td>
      <td>FS</td>
      <td>Min</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>140</th>
      <td>Adam Thielen</td>
      <td>WR</td>
      <td>Min</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/168/thumbs/im5xz2q9bjbg44xep08bf5czq.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Was





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Champ Bailey</td>
      <td>CB</td>
      <td>Was, Den</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bruce Smith</td>
      <td>RE</td>
      <td>Buf, Was</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Sean Taylor</td>
      <td>FS</td>
      <td>Was</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Zach Brown</td>
      <td>MLB</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Ryan Kerrigan</td>
      <td>LOLB</td>
      <td>Was</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>121</th>
      <td>Jordan Reed</td>
      <td>TE</td>
      <td>Was</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Brandon Scherff</td>
      <td>RG</td>
      <td>Was</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>151</th>
      <td>Trent Williams</td>
      <td>LT</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/160/thumbs/1053.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Ten





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Min, Oak, NE, Min, Ten, SF</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Steve Hutchinson</td>
      <td>LG</td>
      <td>Sea, Min, Ten</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>NO, NYJ, TB, Ten, Cin, SD, Bal</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Zach Brown</td>
      <td>MLB</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Malcolm Butler</td>
      <td>CB</td>
      <td>NE, Ten</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Kevin Byard</td>
      <td>FS</td>
      <td>Ten</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jurrell Casey</td>
      <td>RE</td>
      <td>Ten</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>102</th>
      <td>Taylor Lewan</td>
      <td>LT</td>
      <td>Ten</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>147</th>
      <td>Delanie Walker</td>
      <td>TE</td>
      <td>SF, Ten</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/176/thumbs/17636702014.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    TB





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>Derrick Brooks</td>
      <td>ROLB</td>
      <td>TB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>NO, NYJ, TB, Ten, Cin, SD, Bal</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Steve Young</td>
      <td>QB</td>
      <td>TB, SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Lavonte David</td>
      <td>ROLB</td>
      <td>TB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Demar Dotson</td>
      <td>RT</td>
      <td>, TB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Mike Evans</td>
      <td>WR</td>
      <td>TB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Brent Grimes</td>
      <td>CB</td>
      <td>Atl, Mia, TB,</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Gerald McCoy</td>
      <td>DT</td>
      <td>TB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>TB, Bal, NE, Ind, Oak</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>161</th>
      <td>Tim Brown</td>
      <td>WR</td>
      <td>Oak,  TB</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/180/thumbs/pfiobtreaq7j0pzvadktsc6jv.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Sea





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>Steve Hutchinson</td>
      <td>LG</td>
      <td>Sea, Min, Ten</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Doug Baldwin</td>
      <td>WR</td>
      <td>Sea</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Kam Chancellor</td>
      <td>SS</td>
      <td>Sea</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Jimmy Graham</td>
      <td>TE</td>
      <td>NO, Sea, GB</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>128</th>
      <td>Richard Sherman</td>
      <td>CB</td>
      <td>Sea, SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>139</th>
      <td>Golden Tate III</td>
      <td>WR</td>
      <td>0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>142</th>
      <td>Earl Thomas III</td>
      <td>FS</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>146</th>
      <td>Bobby Wagner</td>
      <td>MLB</td>
      <td>Sea</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>152</th>
      <td>Russell Wilson</td>
      <td>QB</td>
      <td>Sea</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>163</th>
      <td>Jerry Rice</td>
      <td>WR</td>
      <td>SF,  Oak,  Sea</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/6446/thumbs/644624152017.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    CHARGERS





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>NO, NYJ, TB, Ten, Cin, SD, Bal</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Keenan Allen</td>
      <td>WR</td>
      <td>SD, LAC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Joey Bosa</td>
      <td>LE</td>
      <td>SD, LAC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Drew Brees</td>
      <td>QB</td>
      <td>SD, NO</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Melvin Gordon</td>
      <td>HB</td>
      <td>SD, LAC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Casey Hayward</td>
      <td>CB</td>
      <td>GB, SD, LAC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Hunter Henry</td>
      <td>TE</td>
      <td>SD, LAC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Melvin Ingram</td>
      <td>RE</td>
      <td>SD, LAC</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/173/thumbs/299.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Atl





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Michael Vick</td>
      <td>QB</td>
      <td>Atl, Phi, NYJ, Pit</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Devonta Freeman</td>
      <td>HB</td>
      <td>Atl</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Brent Grimes</td>
      <td>CB</td>
      <td>Atl, Mia, TB,</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Deion Jones</td>
      <td>MLB</td>
      <td>Atl</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Julio Jones</td>
      <td>WR</td>
      <td>Atl</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Alex Mack</td>
      <td>C</td>
      <td>Cle, Atl</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>125</th>
      <td>Matt Ryan</td>
      <td>QB</td>
      <td>Atl</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Desmond Trufant</td>
      <td>CB</td>
      <td>Atl</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>167</th>
      <td>Tony Gonzalez</td>
      <td>TE</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/153/thumbs/318.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Bal





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>NO, NYJ, TB, Ten, Cin, SD, Bal</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Kyle Juszczyk</td>
      <td>FB</td>
      <td>Bal, SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>TB, Bal, NE, Ind, Oak</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Kelechi Osemele</td>
      <td>LG</td>
      <td>Bal, Oak</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>133</th>
      <td>Jimmy Smith</td>
      <td>CB</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Terrell Suggs</td>
      <td>ROLB</td>
      <td>Bal</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>153</th>
      <td>Marshal Yanda</td>
      <td>RG</td>
      <td>Bal</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Rod Woodson</td>
      <td>CB</td>
      <td>Pit,  SF,  Bal,  Oak</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>162</th>
      <td>Ray Lewis</td>
      <td>MLB</td>
      <td>Bal</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>164</th>
      <td>Shannon Sharpe</td>
      <td>TE</td>
      <td>Den,  Bal</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/5941/thumbs/594179532017.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    RAMS





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>47</th>
      <td>Aaron Donald</td>
      <td>RE</td>
      <td>Stl, LA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Todd Gurley II</td>
      <td>HB</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Janoris Jenkins</td>
      <td>CB</td>
      <td>Stl, NYG</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Trumaine Johnson</td>
      <td>CB</td>
      <td>0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Lamarcus Joyner</td>
      <td>FS</td>
      <td>Stl, LA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Marcus Peters</td>
      <td>CB</td>
      <td>KC, LA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>138</th>
      <td>Ndamukong Suh</td>
      <td>DT</td>
      <td>Det, Mia, LA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>166</th>
      <td>Aeneas Williams</td>
      <td>CB</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/162/thumbs/857.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    KC





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Willie Roaf</td>
      <td>LT</td>
      <td>NO, KC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Eric Berry</td>
      <td>SS</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Tyreek Hill</td>
      <td>WR</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Justin Houston</td>
      <td>LOLB</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Rodney Hudson</td>
      <td>C</td>
      <td>KC, Oak</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Kareem Hunt</td>
      <td>HB</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Travis Kelce</td>
      <td>TE</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Marcus Peters</td>
      <td>CB</td>
      <td>KC, LA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>167</th>
      <td>Tony Gonzalez</td>
      <td>TE</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/152/thumbs/v7tehkwthrwefgounvi7znf5k.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    NYJ





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Michael Vick</td>
      <td>QB</td>
      <td>Atl, Phi, NYJ, Pit</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>NO, NYJ, TB, Ten, Cin, SD, Bal</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Jamal Adams</td>
      <td>SS</td>
      <td>NYJ</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Damon Harrison Sr</td>
      <td>DT</td>
      <td>0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Trumaine Johnson</td>
      <td>CB</td>
      <td>0</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/159/thumbs/15988562013.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Jax





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>26</th>
      <td>A.J. Bouye</td>
      <td>CB</td>
      <td>Hou, Jax</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Calais Campbell</td>
      <td>LE</td>
      <td>Ari, Jax</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Leonard Fournette</td>
      <td>HB</td>
      <td>Jax</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Myles Jack</td>
      <td>LOLB</td>
      <td>Jax</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Andrew Norwell</td>
      <td>LG</td>
      <td>Car, Jax</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Jalen Ramsey</td>
      <td>CB</td>
      <td>Jax</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>134</th>
      <td>Telvin Smith</td>
      <td>ROLB</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/163/thumbs/g9mgk6x3ge26t44cccm9oq1vl.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Oak





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Min, Oak, NE, Min, Ten, SF</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Ted Hendricks</td>
      <td>LOLB</td>
      <td>Bal, GB, Oak, LAR</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Amari Cooper</td>
      <td>WR</td>
      <td>Oak</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Rodney Hudson</td>
      <td>C</td>
      <td>KC, Oak</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Khalil Mack</td>
      <td>LE</td>
      <td>Oak</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>TB, Bal, NE, Ind, Oak</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Kelechi Osemele</td>
      <td>LG</td>
      <td>Bal, Oak</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Rod Woodson</td>
      <td>CB</td>
      <td>Pit,  SF,  Bal,  Oak</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>161</th>
      <td>Tim Brown</td>
      <td>WR</td>
      <td>Oak,  TB</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>163</th>
      <td>Jerry Rice</td>
      <td>WR</td>
      <td>SF,  Oak,  Sea</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/149/thumbs/n0fd1z6xmhigb0eej3323ebwq.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Buf





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9</th>
      <td>Bruce Smith</td>
      <td>RE</td>
      <td>Buf, Was</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Nigel Bradham</td>
      <td>LOLB</td>
      <td>Buf, Phi</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Zach Brown</td>
      <td>MLB</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Stephon Gilmore</td>
      <td>CB</td>
      <td>Buf, NE</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Micah Hyde</td>
      <td>SS</td>
      <td>GB, Buf</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Jason Peters</td>
      <td>LT</td>
      <td>Buf, , Phi</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Terrell Owens</td>
      <td>WR</td>
      <td>SF,  Phi,  Dal,  Buf,  Cin</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/174/thumbs/f1wggq2k8ql88fe33jzhw641u.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Car





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Reggie White</td>
      <td>LE</td>
      <td>Phi, GB, Car</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Luke Kuechly</td>
      <td>MLB</td>
      <td>Car</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Cam Newton</td>
      <td>QB</td>
      <td>Car</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Andrew Norwell</td>
      <td>LG</td>
      <td>Car, Jax</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Greg Olsen</td>
      <td>TE</td>
      <td>Chi, Car</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>129</th>
      <td>Kawann Short</td>
      <td>DT</td>
      <td>Car</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Daryl Williams</td>
      <td>RT</td>
      <td>Car</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/155/thumbs/15578552015.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Cle





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>Joel Bitonio</td>
      <td>LG</td>
      <td>Cle</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Demario Davis</td>
      <td>MLB</td>
      <td>NYJ, Cle, NYJ, NO</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Jarvis Landry</td>
      <td>WR</td>
      <td>Mia, Cle</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Alex Mack</td>
      <td>C</td>
      <td>Cle, Atl</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Jabaal Sheard</td>
      <td>RE</td>
      <td>Cle, NE, Ind</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Kevin Zeitler</td>
      <td>RG</td>
      <td>Cin, Cle</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/156/thumbs/970.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Pit





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Michael Vick</td>
      <td>QB</td>
      <td>Atl, Phi, NYJ, Pit</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Le'Veon Bell</td>
      <td>HB</td>
      <td>Pit</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Antonio Brown</td>
      <td>WR</td>
      <td>Pit</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>David DeCastro</td>
      <td>RG</td>
      <td>Pit</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Marcus Gilbert</td>
      <td>RT</td>
      <td>Pit</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Ben Roethlisberger</td>
      <td>QB</td>
      <td>Pit</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Rod Woodson</td>
      <td>CB</td>
      <td>Pit,  SF,  Bal,  Oak</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/166/thumbs/919.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    NYG





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21</th>
      <td>Odell Beckham Jr</td>
      <td>WR</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Landon Collins</td>
      <td>SS</td>
      <td>NYG</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Damon Harrison Sr</td>
      <td>DT</td>
      <td>0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Janoris Jenkins</td>
      <td>CB</td>
      <td>Stl, NYG</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Linval Joseph</td>
      <td>DT</td>
      <td>NYG, Min</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>165</th>
      <td>Michael Strahan</td>
      <td>LE</td>
      <td>NYG</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/179/thumbs/17994552009.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    SF





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Min, Oak, NE, Min, Ten, SF</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Steve Young</td>
      <td>QB</td>
      <td>TB, SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Kyle Juszczyk</td>
      <td>FB</td>
      <td>Bal, SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>128</th>
      <td>Richard Sherman</td>
      <td>CB</td>
      <td>Sea, SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>147</th>
      <td>Delanie Walker</td>
      <td>TE</td>
      <td>SF, Ten</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Terrell Owens</td>
      <td>WR</td>
      <td>SF,  Phi,  Dal,  Buf,  Cin</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Rod Woodson</td>
      <td>CB</td>
      <td>Pit,  SF,  Bal,  Oak</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>163</th>
      <td>Jerry Rice</td>
      <td>WR</td>
      <td>SF,  Oak,  Sea</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/169/thumbs/364.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Chi





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>Adrian Amos</td>
      <td>SS</td>
      <td>Chi</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Jordan Howard</td>
      <td>HB</td>
      <td>Chi</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Greg Olsen</td>
      <td>TE</td>
      <td>Chi, Car</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Josh Sitton</td>
      <td>LG</td>
      <td>GB, Chi, Mia</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>144</th>
      <td>Danny Trevathan</td>
      <td>MLB</td>
      <td>Den, Chi</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>158</th>
      <td>Brian Urlacher</td>
      <td>MLB</td>
      <td>Chi</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/165/thumbs/406.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Dal





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>Ezekiel Elliott</td>
      <td>HB</td>
      <td>Dal</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Travis Frederick</td>
      <td>C</td>
      <td>Dal</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>101</th>
      <td>Sean Lee</td>
      <td>ROLB</td>
      <td>, Dal</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Zack Martin</td>
      <td>RG</td>
      <td>Dal</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>135</th>
      <td>Tyron Smith</td>
      <td>LT</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Terrell Owens</td>
      <td>WR</td>
      <td>SF,  Phi,  Dal,  Buf,  Cin</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>160</th>
      <td>Demarcus Ware</td>
      <td>ROLB</td>
      <td>Dal,  Den</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/150/thumbs/15073062018.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Mia





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>64</th>
      <td>Brent Grimes</td>
      <td>CB</td>
      <td>Atl, Mia, TB,</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Reshad Jones</td>
      <td>SS</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Jarvis Landry</td>
      <td>WR</td>
      <td>Mia, Cle</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Josh Sitton</td>
      <td>LG</td>
      <td>GB, Chi, Mia</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>138</th>
      <td>Ndamukong Suh</td>
      <td>DT</td>
      <td>Det, Mia, LA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Dan Marino</td>
      <td>QB</td>
      <td>Mia</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/161/thumbs/9ebzja2zfeigaziee8y605aqp.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Den





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Champ Bailey</td>
      <td>CB</td>
      <td>Was, Den</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Chris Harris Jr</td>
      <td>CB</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Von Miller</td>
      <td>LOLB</td>
      <td>Den</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>141</th>
      <td>Demaryius Thomas</td>
      <td>WR</td>
      <td>Den</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>144</th>
      <td>Danny Trevathan</td>
      <td>MLB</td>
      <td>Den, Chi</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>155</th>
      <td>Terrell Davis</td>
      <td>RB</td>
      <td>Den</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>160</th>
      <td>Demarcus Ware</td>
      <td>ROLB</td>
      <td>Dal,  Den</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>164</th>
      <td>Shannon Sharpe</td>
      <td>TE</td>
      <td>Den,  Bal</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>169</th>
      <td>Brian Dawkins</td>
      <td>FS</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/157/thumbs/570.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Hou





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>26</th>
      <td>A.J. Bouye</td>
      <td>CB</td>
      <td>Hou, Jax</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Jadeveon Clowney</td>
      <td>ROLB</td>
      <td>Hou</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>74</th>
      <td>DeAndre Hopkins</td>
      <td>WR</td>
      <td>Hou</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Tyrann Mathieu</td>
      <td>FS</td>
      <td>Ari, Hou</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>148</th>
      <td>J.J. Watt</td>
      <td>LE</td>
      <td>Hou</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/177/thumbs/kwth8f1cfa2sch5xhjjfaof90.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Ari





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Calais Campbell</td>
      <td>LE</td>
      <td>Ari, Jax</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Larry Fitzgerald</td>
      <td>WR</td>
      <td>Ari</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>84</th>
      <td>David Johnson</td>
      <td>HB</td>
      <td>Ari</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Tyrann Mathieu</td>
      <td>FS</td>
      <td>Ari, Hou</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>118</th>
      <td>Patrick Peterson</td>
      <td>CB</td>
      <td>Ari</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>166</th>
      <td>Aeneas Williams</td>
      <td>CB</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/154/thumbs/403.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Cin





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>NO, NYJ, TB, Ten, Cin, SD, Bal</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Geno Atkins</td>
      <td>DT</td>
      <td>Cin</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>62</th>
      <td>A.J. Green</td>
      <td>WR</td>
      <td>Cin</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Kevin Zeitler</td>
      <td>RG</td>
      <td>Cin, Cle</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Terrell Owens</td>
      <td>WR</td>
      <td>SF,  Phi,  Dal,  Buf,  Cin</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/170/thumbs/17013982017.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Det





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>131</th>
      <td>Darius Slay Jr</td>
      <td>CB</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>136</th>
      <td>Matthew Stafford</td>
      <td>QB</td>
      <td>Det</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>138</th>
      <td>Ndamukong Suh</td>
      <td>DT</td>
      <td>Det, Mia, LA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>139</th>
      <td>Golden Tate III</td>
      <td>WR</td>
      <td>0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Barry Sanders</td>
      <td>RB</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/158/thumbs/593.gif)


```python
i+=1
print(team_abbrevs[i])
team_list[i]
```

    Ind





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>POS</th>
      <th>Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Ted Hendricks</td>
      <td>LOLB</td>
      <td>Bal, GB, Oak, LAR</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>73</th>
      <td>T.Y. Hilton</td>
      <td>WR</td>
      <td>Ind</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Andrew Luck</td>
      <td>QB</td>
      <td>, Ind</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>TB, Bal, NE, Ind, Oak</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Jabaal Sheard</td>
      <td>RE</td>
      <td>Cle, NE, Ind</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>


