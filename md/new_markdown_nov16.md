<h1>MUT Power Up Players and Their Eligible Teams</h1>
<h4>- Matt , last updated: Nov 16, 2018</h4>
<p><code>python
%matplotlib inline
import pandas as pd
from PowerUpAnalyzer import PowerUpAnalyzer
import matplotlib.pyplot as plt
%load_ext autoreload
%autoreload 2</code></p>
<p>```python
date = 'nov16'</p>
<p>pa = PowerUpAnalyzer(date)
```</p>
<p><img alt="png" src="output_2_0.png"></p>
<p><img alt="png" src="output_2_1.png"></p>
<p><img alt="png" src="output_2_2.png"></p>
<p><img alt="png" src="output_2_3.png"></p>
<p><code>python
pa.player_data['Type'].value_counts()</code></p>
<pre><code>Power Up     155
Legend PU     38
HoF            5
Captain        4
Master         2
Name: Type, dtype: int64
</code></pre>
<h3>Biggest journeymen</h3>
<p><code>python
team_list = pa.get_team_list()</code></p>
<h1>Team Lists</h1>
<p><strong>---------------------------------------------------------------</strong></p>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/167/thumbs/960.gif"></p>
<h2>Philadelphia Eagles</h2>
<p><code>python
i=0
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  84
  Michael Vick
  QB
  Legend PU
  ATL,PHI,NYJ,PIT
  4


  107
  Donovan McNabb
  QB
  Legend PU
  PHI,MIN
  2


  108
  Brian Dawkins
  SS
  Legend PU
  PHI,DEN
  2


  109
  Reggie White
  LE
  Legend PU
  PHI,GB,CAR
  3


  113
  Terell Owens
  WR
  HoF
  SF,PHI,DAL,BUF,CIN
  5


  146
  Fletcher Cox
  DT
  Power Up
  PHI
  1


  147
  Zach Ertz
  TE
  Power Up
  PHI
  1


  148
  Brandon Graham
  LE
  Power Up
  PHI
  1


  149
  Jordan Hicks
  MLB
  Power Up
  PHI
  1


  150
  Lane Johnson
  RT
  Power Up
  PHI
  1


  151
  Jason Kelce
  C
  Power Up
  PHI
  1


  152
  Carson Wentz
  QB
  Power Up
  PHI
  1


  153
  Nigel Bradham
  LOLB
  Power Up
  PHI,BUF
  2


  154
  Jason Peters
  LT
  Power Up
  PHI,BUF
  2


  155
  Malcom Jenkins
  SS
  Power Up
  PHI,NO
  2


  197
  Alshon Jeffery
  WR
  Power Up
  CHI,PHI
  2


  198
  Jevon Kearse
  LE
  Legend PU
  TEN,PHI
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/151/thumbs/y71myf8mlwlk8lbgagh3fd5e0.gif"></p>
<h2>New England Patriots</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  49
  Jabaal Sheard
  RE
  Power Up
  IND,CLE,NE
  3


  99
  Randy Moss
  WR
  Legend PU
  MIN,OAK,NE,TEN,SF
  5


  119
  David Andrews
  C
  Power Up
  NE
  1


  120
  Tom Brady
  QB
  Power Up
  NE
  1


  121
  James Develin
  FB
  Power Up
  NE
  1


  122
  Julian Edelman
  WR
  Power Up
  NE
  1


  123
  Rob Gronkowski
  TE
  Power Up
  NE
  1


  124
  Devin McCourty
  FS
  Power Up
  NE
  1


  125
  Dont'a Hightower
  LOLB
  Power Up
  NE
  1


  126
  Stephon Gilmore
  CB
  Power Up
  NE,BUF
  2


  145
  Rashaan Melvin
  CB
  Power Up
  OAK,TB,BAL,NE,IND
  5


  177
  Malcolm Butler
  CB
  Power Up
  TEN,NE
  2


  188
  Willie McGinest
  ROLB
  Legend PU
  NE
  1


  195
  Brandin Cooks
  WR
  Power Up
  NO,NE,LAR
  3


  200
  Ty Law
  CB
  Legend PU
  NE,NYJ,KC,DEN
  4
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/175/thumbs/907.gif"></p>
<h2>New Orleans Saints</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  42
  Jimmy Graham
  TE
  Power Up
  GB,NO,SEA
  3


  101
  Willie Roaf
  LT
  Legend PU
  NO,KC
  2


  102
  Ricky Williams
  HB
  Master
  NO,MIA,BAL
  3


  103
  Lorenzo Neal
  FB
  Legend PU
  NO,NYJ,TB,TEN,CIN,LAC,BAL
  7


  127
  Cameron Jordan
  LE
  Power Up
  NO
  1


  128
  Alvin Kamara
  HB
  Power Up
  NO
  1


  129
  Marson Lattimore
  CB
  Power Up
  NO
  1


  130
  Ryan Ramczyk
  RT
  Power Up
  NO
  1


  131
  Michael Thomas
  WR
  Power Up
  NO
  1


  132
  Drew Brees
  QB
  Power Up
  NO,LAC
  2


  133
  Demario Davis
  MLB
  Power Up
  NO,NYJ,CLE
  3


  155
  Malcom Jenkins
  SS
  Power Up
  PHI,NO
  2


  189
  Jeremy Shockey
  TE
  Legend PU
  NYG,NO,CAR
  3


  195
  Brandin Cooks
  WR
  Power Up
  NO,NE,LAR
  3
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/171/thumbs/dcy03myfhffbki5d7il3.gif"></p>
<h2>Green Bay Packers</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  12
  Micah Hyde
  SS
  Power Up
  BUF,GB
  2


  37
  Davante Adams
  WR
  Power Up
  GB
  1


  38
  David Bakhtiari
  LT
  Power Up
  GB
  1


  39
  Kenny Clark
  DT
  Power Up
  GB
  1


  40
  Aaron Rodgers
  QB
  Power Up
  GB
  1


  41
  Ha Ha Clinton-Dix
  FS
  Power Up
  GB
  1


  42
  Jimmy Graham
  TE
  Power Up
  GB,NO,SEA
  3


  68
  Casey Hayward
  CB
  Power Up
  LAC,GB
  2


  75
  Josh Sitton
  LG
  Power Up
  MIA,GB,CHI
  3


  95
  Ted Hendricks
  LOLB
  Legend PU
  IND,GB,OAK
  3


  109
  Reggie White
  LE
  Legend PU
  PHI,GB,CAR
  3
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/172/thumbs/17227042013.gif"></p>
<h2>Minnesota Vikings</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  76
  Anthony Barr
  ROLB
  Power Up
  MIN
  1


  77
  Stefon Diggs
  WR
  Power Up
  MIN
  1


  78
  Everson Griffen
  RE
  Power Up
  MIN
  1


  79
  Xavier Rhodes
  CB
  Power Up
  MIN
  1


  80
  Harrison Smith
  FS
  Power Up
  MIN
  1


  81
  Adam Thielen
  WR
  Power Up
  MIN
  1


  82
  Linval Joseph
  DT
  Power Up
  MIN,NYG
  2


  99
  Randy Moss
  WR
  Legend PU
  MIN,OAK,NE,TEN,SF
  5


  100
  John Randle
  DT
  Legend PU
  MIN,SEA
  2


  107
  Donovan McNabb
  QB
  Legend PU
  PHI,MIN
  2


  111
  Steve Hutchinson
  LG
  Legend PU
  SEA,MIN,TEN
  3


  186
  Paul Krause
  FS
  Legend PU
  WAS,MIN
  2


  203
  Alan Page
  DT
  Legend PU
  MIN,CHI
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/168/thumbs/im5xz2q9bjbg44xep08bf5czq.gif"></p>
<h2>Washington Redskins</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  85
  Deion Sanders
  CB
  Legend PU
  ATL,SF,DAL,WAS,BAL
  5


  88
  Bruce Smith
  RE
  Legend PU
  BUF,WAS
  2


  117
  Sean Taylor
  FS
  Legend PU
  WAS
  1


  118
  Champ Bailey
  CB
  Legend PU
  WAS,DEN
  2


  179
  Ryan Kerrigan
  LOLB
  Power Up
  WAS
  1


  180
  Jordan Reed
  TE
  Power Up
  WAS
  1


  181
  Brandon Scherff
  RG
  Power Up
  WAS
  1


  182
  Trent Williams
  LT
  Power Up
  WAS
  1


  183
  Zach Brown
  MLB
  Power Up
  WAS,TEN,BUF
  3


  186
  Paul Krause
  FS
  Legend PU
  WAS,MIN
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/160/thumbs/1053.gif"></p>
<h2>Tennessee Titans</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  99
  Randy Moss
  WR
  Legend PU
  MIN,OAK,NE,TEN,SF
  5


  103
  Lorenzo Neal
  FB
  Legend PU
  NO,NYJ,TB,TEN,CIN,LAC,BAL
  7


  111
  Steve Hutchinson
  LG
  Legend PU
  SEA,MIN,TEN
  3


  116
  Eddie George
  HB
  Legend PU
  TEN
  1


  174
  Kevin Byard
  FS
  Power Up
  TEN
  1


  175
  Jurell Casey
  RE
  Power Up
  TEN
  1


  176
  Taylor Lewan
  LT
  Power Up
  TEN
  1


  177
  Malcolm Butler
  CB
  Power Up
  TEN,NE
  2


  178
  Delanie Walker
  TE
  Power Up
  TEN,SF
  2


  183
  Zach Brown
  MLB
  Power Up
  WAS,TEN,BUF
  3


  198
  Jevon Kearse
  LE
  Legend PU
  TEN,PHI
  2


  202
  Bruce Matthews
  C
  Legend PU
  TEN
  1
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/176/thumbs/17636702014.gif"></p>
<h2>Tampa Bay Buccaneers</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  103
  Lorenzo Neal
  FB
  Legend PU
  NO,NYJ,TB,TEN,CIN,LAC,BAL
  7


  106
  Tim Brown
  WR
  Legend PU
  OAK,TB
  2


  114
  Derrick Brooks
  ROLB
  Legend PU
  TB
  1


  115
  Steve Young
  QB
  Legend PU
  TB,SF
  2


  145
  Rashaan Melvin
  CB
  Power Up
  OAK,TB,BAL,NE,IND
  5


  169
  Lavonte David
  ROLB
  Power Up
  TB
  1


  170
  Demar Dotson
  RT
  Power Up
  TB
  1


  171
  Mike Evans
  WR
  Power Up
  TB
  1


  172
  Gerald McCoy
  DT
  Power Up
  TB
  1


  173
  Brent Grimes
  CB
  Power Up
  TB,ATL,MIA
  3


  184
  Ronde Barber
  CB
  Legend PU
  TB
  1
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/180/thumbs/pfiobtreaq7j0pzvadktsc6jv.gif"></p>
<h2>Seattle Seahawks</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  36
  Golden Tate III
  WR
  Power Up
  DET,SEA
  2


  42
  Jimmy Graham
  TE
  Power Up
  GB,NO,SEA
  3


  100
  John Randle
  DT
  Legend PU
  MIN,SEA
  2


  111
  Steve Hutchinson
  LG
  Legend PU
  SEA,MIN,TEN
  3


  112
  Jerry Rice
  WR
  Captain
  SF,OAK,SEA
  3


  162
  Doug Baldwin
  WR
  Power Up
  SEA
  1


  163
  Kam Chancellor
  SS
  Power Up
  SEA
  1


  164
  Earl Thomas III
  FS
  Power Up
  SEA
  1


  165
  Bobby Wagner
  MLB
  Power Up
  SEA
  1


  166
  Russell Wilson
  QB
  Power Up
  SEA
  1


  168
  Richard Sherman
  CB
  Power Up
  SF,SEA
  2


  187
  Franco Harris
  FB
  Legend PU
  PIT,SEA
  2


  190
  Marshawn Lynch
  HB
  Power Up
  OAK,BUF,SEA
  3
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/6446/thumbs/644624152017.gif"></p>
<h2>Los Angeles Chargers</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  63
  Keenan Allan
  WR
  Power Up
  LAC
  1


  64
  Joey Bosa
  LE
  Power Up
  LAC
  1


  65
  Melvin Gordon
  HB
  Power Up
  LAC
  1


  66
  Hunter Henry
  TE
  Power Up
  LAC
  1


  67
  Melvin Ingram
  RE
  Power Up
  LAC
  1


  68
  Casey Hayward
  CB
  Power Up
  LAC,GB
  2


  103
  Lorenzo Neal
  FB
  Legend PU
  NO,NYJ,TB,TEN,CIN,LAC,BAL
  7


  132
  Drew Brees
  QB
  Power Up
  NO,LAC
  2


  201
  LaDainian Tomlinson
  HB
  Legend PU
  LAC,NYJ
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/173/thumbs/299.gif"></p>
<h2>Atlanta Falcons</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  3
  Devonta Freeman
  HB
  Power Up
  ATL
  1


  4
  Deion Jones
  MLB
  Power Up
  ATL
  1


  5
  Julio Jones
  WR
  Power Up
  ATL
  1


  6
  Matt Ryan
  QB
  Power Up
  ATL
  1


  7
  Desmond Trufant
  CB
  Power Up
  ATL
  1


  8
  Alex Mack
  C
  Power Up
  ATL,CLE
  2


  84
  Michael Vick
  QB
  Legend PU
  ATL,PHI,NYJ,PIT
  4


  85
  Deion Sanders
  CB
  Legend PU
  ATL,SF,DAL,WAS,BAL
  5


  96
  Tony Gonzalez
  TE
  Legend PU
  KC,ATL
  2


  173
  Brent Grimes
  CB
  Power Up
  TB,ATL,MIA
  3


  192
  Dontari Poe
  DT
  Power Up
  KC,ATL,CAR
  3
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/153/thumbs/318.gif"></p>
<h2>Baltimore Ravens</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  9
  Jimmy Smith
  CB
  Power Up
  BAL
  1


  10
  Terrell Suggs
  ROLB
  Power Up
  BAL
  1


  11
  Marshal Yanda
  RG
  Power Up
  BAL
  1


  85
  Deion Sanders
  CB
  Legend PU
  ATL,SF,DAL,WAS,BAL
  5


  86
  Ray Lewis
  MLB
  Captain
  BAL
  1


  87
  Jonathan Ogden
  LT
  Legend PU
  BAL
  1


  93
  Shannon Sharpe
  TE
  Captain
  DEN,BAL
  2


  102
  Ricky Williams
  HB
  Master
  NO,MIA,BAL
  3


  103
  Lorenzo Neal
  FB
  Legend PU
  NO,NYJ,TB,TEN,CIN,LAC,BAL
  7


  110
  Rod Woodson
  CB
  HoF
  PIT,SF,BAL,OAK
  4


  143
  Kelechi Osemele
  LG
  Power Up
  OAK,BAL
  2


  145
  Rashaan Melvin
  CB
  Power Up
  OAK,TB,BAL,NE,IND
  5


  167
  Kyle Juszczyk
  FB
  Power Up
  SF,BAL
  2


  199
  Willie Anderson
  RT
  Legend PU
  CIN,BAL
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/5941/thumbs/594179532017.gif"></p>
<h2>Los Angeles Rams</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  69
  Aaron Donald
  DT
  Power Up
  LAR
  1


  70
  Todd Gurley II
  HB
  Power Up
  LAR
  1


  71
  Lamarcus Joyner
  FS
  Power Up
  LAR
  1


  72
  Ndamukong Suh
  DT
  Power Up
  LAR,DET,MIA
  3


  73
  Marcus Peters
  CB
  Power Up
  LAR,KC
  2


  83
  Aeneas Williams
  CB
  Legend PU
  ARI,LAR
  2


  97
  Kevin Greene
  LOLB
  Legend PU
  LAR,PIT,CAR,SF
  4


  136
  Janoris Jenkins
  CB
  Power Up
  NYG,LAR
  2


  139
  Trumaine Johnson
  CB
  Power Up
  NYJ,LAR
  2


  195
  Brandin Cooks
  WR
  Power Up
  NO,NE,LAR
  3
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/162/thumbs/857.gif"></p>
<h2>Kansas City Chiefs</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  57
  Eric Berry
  SS
  Power Up
  KC
  1


  58
  Tyreek Hill
  WR
  Power Up
  KC
  1


  59
  Justin Houston
  LOLB
  Power Up
  KC
  1


  60
  Kareen Hunt
  HB
  Power Up
  KC
  1


  61
  Travis Kelce
  TE
  Power Up
  KC
  1


  62
  Patrick Mahomes
  QB
  Power Up
  KC
  1


  73
  Marcus Peters
  CB
  Power Up
  LAR,KC
  2


  96
  Tony Gonzalez
  TE
  Legend PU
  KC,ATL
  2


  101
  Willie Roaf
  LT
  Legend PU
  NO,KC
  2


  144
  Rodney Hudson
  C
  Power Up
  OAK,KC
  2


  192
  Dontari Poe
  DT
  Power Up
  KC,ATL,CAR
  3


  200
  Ty Law
  CB
  Legend PU
  NE,NYJ,KC,DEN
  4
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/152/thumbs/v7tehkwthrwefgounvi7znf5k.gif"></p>
<h2>Boo York Jets</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  84
  Michael Vick
  QB
  Legend PU
  ATL,PHI,NYJ,PIT
  4


  103
  Lorenzo Neal
  FB
  Legend PU
  NO,NYJ,TB,TEN,CIN,LAC,BAL
  7


  133
  Demario Davis
  MLB
  Power Up
  NO,NYJ,CLE
  3


  137
  Damon Harrison Sr
  DT
  Power Up
  NYG,NYJ
  2


  138
  Jamal Adams
  SS
  Power Up
  NYJ
  1


  139
  Trumaine Johnson
  CB
  Power Up
  NYJ,LAR
  2


  200
  Ty Law
  CB
  Legend PU
  NE,NYJ,KC,DEN
  4


  201
  LaDainian Tomlinson
  HB
  Legend PU
  LAC,NYJ
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/159/thumbs/15988562013.gif"></p>
<h2>Jacksonville Jaguars</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  50
  Leonard Fournette
  HB
  Power Up
  JAX
  1


  51
  Myles Jack
  LOLB
  Power Up
  JAX
  1


  52
  Jalen Ramsey
  CB
  Power Up
  JAX
  1


  53
  Telvin Smith
  ROLB
  Power Up
  JAX
  1


  54
  Calais Campbell
  LE
  Power Up
  JAX,ARI
  2


  55
  Andrew Norwell
  LG
  Power Up
  JAX,CAR
  2


  56
  AJ Bouye
  CB
  Power Up
  JAX,HOU
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/163/thumbs/g9mgk6x3ge26t44cccm9oq1vl.gif"></p>
<h2>Oakland Raiders</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  95
  Ted Hendricks
  LOLB
  Legend PU
  IND,GB,OAK
  3


  99
  Randy Moss
  WR
  Legend PU
  MIN,OAK,NE,TEN,SF
  5


  106
  Tim Brown
  WR
  Legend PU
  OAK,TB
  2


  110
  Rod Woodson
  CB
  HoF
  PIT,SF,BAL,OAK
  4


  112
  Jerry Rice
  WR
  Captain
  SF,OAK,SEA
  3


  140
  Amari Cooper
  WR
  Power Up
  OAK
  1


  141
  Khalil Mack
  LE
  Power Up
  CHI,OAK
  2


  142
  Derek Carr
  QB
  Power Up
  OAK
  1


  143
  Kelechi Osemele
  LG
  Power Up
  OAK,BAL
  2


  144
  Rodney Hudson
  C
  Power Up
  OAK,KC
  2


  145
  Rashaan Melvin
  CB
  Power Up
  OAK,TB,BAL,NE,IND
  5


  190
  Marshawn Lynch
  HB
  Power Up
  OAK,BUF,SEA
  3
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/149/thumbs/n0fd1z6xmhigb0eej3323ebwq.gif"></p>
<h2>Buffalo Bills</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  12
  Micah Hyde
  SS
  Power Up
  BUF,GB
  2


  88
  Bruce Smith
  RE
  Legend PU
  BUF,WAS
  2


  113
  Terell Owens
  WR
  HoF
  SF,PHI,DAL,BUF,CIN
  5


  126
  Stephon Gilmore
  CB
  Power Up
  NE,BUF
  2


  153
  Nigel Bradham
  LOLB
  Power Up
  PHI,BUF
  2


  154
  Jason Peters
  LT
  Power Up
  PHI,BUF
  2


  183
  Zach Brown
  MLB
  Power Up
  WAS,TEN,BUF
  3


  190
  Marshawn Lynch
  HB
  Power Up
  OAK,BUF,SEA
  3
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/174/thumbs/f1wggq2k8ql88fe33jzhw641u.gif"></p>
<h2>Carolina Panthers</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  13
  Luke Kuechly
  MLB
  Power Up
  CAR
  1


  14
  Cam Newton
  QB
  Power Up
  CAR
  1


  15
  Kawann Short
  DT
  Power Up
  CAR
  1


  16
  Daryl Williams
  RT
  Power Up
  CAR
  1


  17
  Greg Olsen
  TE
  Power Up
  CAR,CHI
  2


  55
  Andrew Norwell
  LG
  Power Up
  JAX,CAR
  2


  97
  Kevin Greene
  LOLB
  Legend PU
  LAR,PIT,CAR,SF
  4


  109
  Reggie White
  LE
  Legend PU
  PHI,GB,CAR
  3


  189
  Jeremy Shockey
  TE
  Legend PU
  NYG,NO,CAR
  3


  192
  Dontari Poe
  DT
  Power Up
  KC,ATL,CAR
  3


  194
  Christian McCaffrey
  HB
  Power Up
  CAR
  1
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/155/thumbs/15578552015.gif"></p>
<h2>Cleveland Browns</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  8
  Alex Mack
  C
  Power Up
  ATL,CLE
  2


  23
  Joel Bitonio
  LG
  Power Up
  CLE
  1


  24
  Kevin Zeitler
  RG
  Power Up
  CLE,CIN
  2


  25
  Jarvis Landry
  WR
  Power Up
  CLE,MIA
  2


  49
  Jabaal Sheard
  RE
  Power Up
  IND,CLE,NE
  3


  133
  Demario Davis
  MLB
  Power Up
  NO,NYJ,CLE
  3
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/156/thumbs/970.gif"></p>
<h2>Pittsburgh Steelers</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  84
  Michael Vick
  QB
  Legend PU
  ATL,PHI,NYJ,PIT
  4


  97
  Kevin Greene
  LOLB
  Legend PU
  LAR,PIT,CAR,SF
  4


  110
  Rod Woodson
  CB
  HoF
  PIT,SF,BAL,OAK
  4


  156
  Ryan Shazier
  MLB
  Master
  PIT
  1


  157
  Le'Veon Bell
  HB
  Power Up
  PIT
  1


  158
  Antonio Brown
  WR
  Power Up
  PIT
  1


  159
  David DeCastro
  RG
  Power Up
  PIT
  1


  160
  Marcus Gilbert
  RT
  Power Up
  PIT
  1


  161
  Ben Roethlisberger
  QB
  Power Up
  PIT
  1


  185
  Dermontti Dawson
  C
  Legend PU
  PIT
  1


  187
  Franco Harris
  FB
  Legend PU
  PIT,SEA
  2


  193
  Emmanuel Sanders
  WR
  Power Up
  DEN,PIT
  2


  196
  T.J. Watt
  ROLB
  Power Up
  PIT
  1
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/166/thumbs/919.gif"></p>
<h2>New York Giants</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  82
  Linval Joseph
  DT
  Power Up
  MIN,NYG
  2


  104
  Michael Strahan
  LE
  Captain
  NYG
  1


  105
  Lawrence Taylor
  ROLB
  Legend PU
  NYG
  1


  134
  Odell Beckham Jr
  WR
  Power Up
  NYG
  1


  135
  Landon Collins
  SS
  Power Up
  NYG
  1


  136
  Janoris Jenkins
  CB
  Power Up
  NYG,LAR
  2


  137
  Damon Harrison Sr
  DT
  Power Up
  NYG,NYJ
  2


  189
  Jeremy Shockey
  TE
  Legend PU
  NYG,NO,CAR
  3
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/179/thumbs/17994552009.gif"></p>
<h2>San Francisco 49ers</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  85
  Deion Sanders
  CB
  Legend PU
  ATL,SF,DAL,WAS,BAL
  5


  91
  Larry Allen
  RG
  Legend PU
  DAL,SF
  2


  97
  Kevin Greene
  LOLB
  Legend PU
  LAR,PIT,CAR,SF
  4


  99
  Randy Moss
  WR
  Legend PU
  MIN,OAK,NE,TEN,SF
  5


  110
  Rod Woodson
  CB
  HoF
  PIT,SF,BAL,OAK
  4


  112
  Jerry Rice
  WR
  Captain
  SF,OAK,SEA
  3


  113
  Terell Owens
  WR
  HoF
  SF,PHI,DAL,BUF,CIN
  5


  115
  Steve Young
  QB
  Legend PU
  TB,SF
  2


  167
  Kyle Juszczyk
  FB
  Power Up
  SF,BAL
  2


  168
  Richard Sherman
  CB
  Power Up
  SF,SEA
  2


  178
  Delanie Walker
  TE
  Power Up
  TEN,SF
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/169/thumbs/364.gif"></p>
<h2>Chicago Bears</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  17
  Greg Olsen
  TE
  Power Up
  CAR,CHI
  2


  18
  Adrian Amos
  SS
  Power Up
  CHI
  1


  19
  Jordan Howard
  HB
  Power Up
  CHI
  1


  20
  Danny Trevathan
  MLB
  Power Up
  CHI,DEN
  2


  75
  Josh Sitton
  LG
  Power Up
  MIA,GB,CHI
  3


  89
  Brian Urlacher
  MLB
  HoF
  CHI
  1


  141
  Khalil Mack
  LE
  Power Up
  CHI,OAK
  2


  197
  Alshon Jeffery
  WR
  Power Up
  CHI,PHI
  2


  203
  Alan Page
  DT
  Legend PU
  MIN,CHI
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/165/thumbs/406.gif"></p>
<h2>Dallas Cowboys</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  26
  Ezekiel Elliot
  HB
  Power Up
  DAL
  1


  27
  Travis Frederick
  C
  Power Up
  DAL
  1


  28
  Sean Lee
  ROLB
  Power Up
  DAL
  1


  29
  Zack Martin
  RG
  Power Up
  DAL
  1


  30
  Tyron Smith
  LT
  Power Up
  DAL
  1


  85
  Deion Sanders
  CB
  Legend PU
  ATL,SF,DAL,WAS,BAL
  5


  90
  DeMarcus Ware
  LOLB
  Legend PU
  DAL,DEN
  2


  91
  Larry Allen
  RG
  Legend PU
  DAL,SF
  2


  113
  Terell Owens
  WR
  HoF
  SF,PHI,DAL,BUF,CIN
  5


  191
  Demarcus Lawrence
  LE
  Power Up
  DAL
  1
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/150/thumbs/15073062018.gif"></p>
<h2>Miami Dolphins</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  25
  Jarvis Landry
  WR
  Power Up
  CLE,MIA
  2


  72
  Ndamukong Suh
  DT
  Power Up
  LAR,DET,MIA
  3


  74
  Reshad Jones
  SS
  Power Up
  MIA
  1


  75
  Josh Sitton
  LG
  Power Up
  MIA,GB,CHI
  3


  98
  Dan Marino
  QB
  HoF
  MIA
  1


  102
  Ricky Williams
  HB
  Master
  NO,MIA,BAL
  3


  173
  Brent Grimes
  CB
  Power Up
  TB,ATL,MIA
  3
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/161/thumbs/9ebzja2zfeigaziee8y605aqp.gif"></p>
<h2>Denver Broncos</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  20
  Danny Trevathan
  MLB
  Power Up
  CHI,DEN
  2


  31
  Chris Harris Jr
  CB
  Power Up
  DEN
  1


  32
  Von Miller
  LOLB
  Power Up
  DEN
  1


  33
  Demaryius Thomas
  WR
  Power Up
  DEN
  1


  90
  DeMarcus Ware
  LOLB
  Legend PU
  DAL,DEN
  2


  92
  Terrell Davis
  HB
  HoF
  DEN
  1


  93
  Shannon Sharpe
  TE
  Captain
  DEN,BAL
  2


  108
  Brian Dawkins
  SS
  Legend PU
  PHI,DEN
  2


  118
  Champ Bailey
  CB
  Legend PU
  WAS,DEN
  2


  193
  Emmanuel Sanders
  WR
  Power Up
  DEN,PIT
  2


  200
  Ty Law
  CB
  Legend PU
  NE,NYJ,KC,DEN
  4
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/157/thumbs/570.gif"></p>
<h2>Houston Texans</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  43
  Jadeveon Clowney
  ROLB
  Power Up
  HOU
  1


  44
  DeAndre Hopkins
  WR
  Power Up
  HOU
  1


  45
  JJ Watt
  LE
  Power Up
  HOU
  1


  46
  Tyrann Mathieu
  FS
  Power Up
  HOU,ARI
  2


  56
  AJ Bouye
  CB
  Power Up
  JAX,HOU
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/177/thumbs/kwth8f1cfa2sch5xhjjfaof90.gif"></p>
<h2>Arizona Cardinals</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  0
  Larry Fitzgerald
  WR
  Power Up
  ARI
  1


  1
  David Johnson
  HB
  Power Up
  ARI
  1


  2
  Patrick Peterson
  CB
  Power Up
  ARI
  1


  46
  Tyrann Mathieu
  FS
  Power Up
  HOU,ARI
  2


  54
  Calais Campbell
  LE
  Power Up
  JAX,ARI
  2


  83
  Aeneas Williams
  CB
  Legend PU
  ARI,LAR
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/154/thumbs/403.gif"></p>
<h2>Cincinnati Bengals</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  21
  Geno Atkins
  DT
  Power Up
  CIN
  1


  22
  AJ Green
  WR
  Power Up
  CIN
  1


  24
  Kevin Zeitler
  RG
  Power Up
  CLE,CIN
  2


  103
  Lorenzo Neal
  FB
  Legend PU
  NO,NYJ,TB,TEN,CIN,LAC,BAL
  7


  113
  Terell Owens
  WR
  HoF
  SF,PHI,DAL,BUF,CIN
  5


  199
  Willie Anderson
  RT
  Legend PU
  CIN,BAL
  2
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/170/thumbs/17013982017.gif"></p>
<h2>Detroit Lions</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  34
  Darius Slay Jr
  CB
  Power Up
  DET
  1


  35
  Matthew Stafford
  QB
  Power Up
  DET
  1


  36
  Golden Tate III
  WR
  Power Up
  DET,SEA
  2


  72
  Ndamukong Suh
  DT
  Power Up
  LAR,DET,MIA
  3


  94
  Barry Sanders
  HB
  Legend PU
  DET
  1
</code></pre>
<p><img alt="Image" src="http://content.sportslogos.net/logos/7/158/thumbs/593.gif"></p>
<h2>Indianapolis Colts</h2>
<p><code>python
i+=1
team_list[i]</code></p>
<pre><code>.dataframe tbody tr th:only-of-type {
    vertical-align: middle;
}

.dataframe tbody tr th {
    vertical-align: top;
}

.dataframe thead th {
    text-align: right;
}





  Name
  Position
  Type
  All Teams
  numTeams




  47
  TY Hilton
  WR
  Power Up
  IND
  1


  48
  Andrew Luck
  QB
  Power Up
  IND
  1


  49
  Jabaal Sheard
  RE
  Power Up
  IND,CLE,NE
  3


  95
  Ted Hendricks
  LOLB
  Legend PU
  IND,GB,OAK
  3


  145
  Rashaan Melvin
  CB
  Power Up
  OAK,TB,BAL,NE,IND
  5
</code></pre>