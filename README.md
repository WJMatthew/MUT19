
# MUT Power Up Players and Their Eligible Teams
#### - Matt , last updated: Nov 9, 2018<br>




![png](https://github.com/WJMatthew/MUT19/blob/master/img/output_3_0.png)




![png](https://github.com/WJMatthew/MUT19/blob/master/img/output_4_0.png)




![png](https://github.com/WJMatthew/MUT19/blob/master/img/output_6_0.png)


### Biggest journeymen


<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>105</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>Legend PU</td>
      <td>NO,NYJ,TB,TEN,CIN,LAC,BAL</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Deion Sanders</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>ATL,SF,DAL,WAS,BAL</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Legend PU</td>
      <td>MIN,OAK,NE,TEN,SF</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Terell Owens</td>
      <td>WR</td>
      <td>HoF</td>
      <td>SF,PHI,DAL,BUF,CIN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>OAK,TB,BAL,NE,IND</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Michael Vick</td>
      <td>QB</td>
      <td>Legend PU</td>
      <td>ATL,PHI,NYJ,PIT</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Kevin Greene</td>
      <td>LOLB</td>
      <td>Legend PU</td>
      <td>LAR,PIT,CAR,SF</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Rod Woodson</td>
      <td>CB</td>
      <td>HoF</td>
      <td>PIT,SF,BAL,OAK</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>208</th>
      <td>Ty Law</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>NE,NYJ,KC,DEN</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
team_abbrevs = list(pal.keys())
team_list = []

players = players.dropna()

players.reset_index(drop=True, inplace=True)
small.reset_index(drop=True, inplace=True)

for team in team_abbrevs:
    current_team = players[ players[team]==1]
    indices = current_team.index.values
    team_list.append(small.iloc[indices])
```

# Team Lists
**---------------------------------------------------------------**

![Image](http://content.sportslogos.net/logos/7/167/thumbs/960.gif)

##  Philadelphia Eagles 


```python
i=0
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>84</th>
      <td>Michael Vick</td>
      <td>QB</td>
      <td>Legend PU</td>
      <td>ATL,PHI,NYJ,PIT</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Donovan McNabb</td>
      <td>QB</td>
      <td>Legend PU</td>
      <td>PHI,MIN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Brian Dawkins</td>
      <td>SS</td>
      <td>Legend PU</td>
      <td>PHI,DEN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Reggie White</td>
      <td>LE</td>
      <td>Legend PU</td>
      <td>PHI,GB,CAR</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Terell Owens</td>
      <td>WR</td>
      <td>HoF</td>
      <td>SF,PHI,DAL,BUF,CIN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Fletcher Cox</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>PHI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>151</th>
      <td>Zach Ertz</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>PHI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>152</th>
      <td>Brandon Graham</td>
      <td>LE</td>
      <td>Power Up</td>
      <td>PHI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>153</th>
      <td>Jordan Hicks</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>PHI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Lane Johnson</td>
      <td>RT</td>
      <td>Power Up</td>
      <td>PHI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>155</th>
      <td>Jason Kelce</td>
      <td>C</td>
      <td>Power Up</td>
      <td>PHI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Carson Wentz</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>PHI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Nigel Bradham</td>
      <td>LOLB</td>
      <td>Power Up</td>
      <td>PHI,BUF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>158</th>
      <td>Jason Peters</td>
      <td>LT</td>
      <td>Power Up</td>
      <td>PHI,BUF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Malcom Jenkins</td>
      <td>SS</td>
      <td>Power Up</td>
      <td>PHI,NO</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>205</th>
      <td>Alshon Jeffery</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>CHI,PHI</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>206</th>
      <td>Jevon Kearse</td>
      <td>LE</td>
      <td>Legend PU</td>
      <td>TEN,PHI</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/151/thumbs/y71myf8mlwlk8lbgagh3fd5e0.gif)

## New England Patriots


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>49</th>
      <td>Jabaal Sheard</td>
      <td>RE</td>
      <td>Power Up</td>
      <td>IND,CLE,NE</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Legend PU</td>
      <td>MIN,OAK,NE,TEN,SF</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>123</th>
      <td>David Andrews</td>
      <td>C</td>
      <td>Power Up</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>125</th>
      <td>James Develin</td>
      <td>FB</td>
      <td>Power Up</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Julian Edelman</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Rob Gronkowski</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>128</th>
      <td>Devin McCourty</td>
      <td>FS</td>
      <td>Power Up</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>129</th>
      <td>Dont'a Hightower</td>
      <td>LOLB</td>
      <td>Power Up</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Stephon Gilmore</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>NE,BUF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>OAK,TB,BAL,NE,IND</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>181</th>
      <td>Malcolm Butler</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>TEN,NE</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>196</th>
      <td>Willie McGinest</td>
      <td>ROLB</td>
      <td>Legend PU</td>
      <td>NE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>203</th>
      <td>Brandin Cooks</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>NO,NE,LAR</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>208</th>
      <td>Ty Law</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>NE,NYJ,KC,DEN</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/175/thumbs/907.gif)

## New Orleans Saints


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>42</th>
      <td>Jimmy Graham</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>GB,NO,SEA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>102</th>
      <td>La'Roi Glover</td>
      <td>DT</td>
      <td>Legend</td>
      <td>NO</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Willie Roaf</td>
      <td>LT</td>
      <td>Legend PU</td>
      <td>NO,KC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Ricky Williams</td>
      <td>HB</td>
      <td>Master</td>
      <td>NO,MIA,BAL</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>Legend PU</td>
      <td>NO,NYJ,TB,TEN,CIN,LAC,BAL</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>131</th>
      <td>Cameron Jordan</td>
      <td>LE</td>
      <td>Power Up</td>
      <td>NO</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>132</th>
      <td>Alvin Kamara</td>
      <td>HB</td>
      <td>Power Up</td>
      <td>NO</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>133</th>
      <td>Marson Lattimore</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>NO</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>134</th>
      <td>Ryan Ramczyk</td>
      <td>RT</td>
      <td>Power Up</td>
      <td>NO</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>135</th>
      <td>Michael Thomas</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>NO</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>136</th>
      <td>Drew Brees</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>NO,LAC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Demario Davis</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>NO,NYJ,CLE</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Malcom Jenkins</td>
      <td>SS</td>
      <td>Power Up</td>
      <td>PHI,NO</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>197</th>
      <td>Jeremy Shockey</td>
      <td>TE</td>
      <td>Legend PU</td>
      <td>NYG,NO,CAR</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>203</th>
      <td>Brandin Cooks</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>NO,NE,LAR</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/171/thumbs/dcy03myfhffbki5d7il3.gif)

## Green Bay Packers


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12</th>
      <td>Micah Hyde</td>
      <td>SS</td>
      <td>Power Up</td>
      <td>BUF,GB</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Davante Adams</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>GB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>David Bakhtiari</td>
      <td>LT</td>
      <td>Power Up</td>
      <td>GB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Kenny Clark</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>GB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Aaron Rodgers</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>GB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Ha Ha Clinton-Dix</td>
      <td>FS</td>
      <td>Power Up</td>
      <td>GB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Jimmy Graham</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>GB,NO,SEA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Casey Hayward</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>LAC,GB</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Josh Sitton</td>
      <td>LG</td>
      <td>Power Up</td>
      <td>MIA,GB,CHI</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Ted Hendricks</td>
      <td>LOLB</td>
      <td>Legend PU</td>
      <td>IND,GB,OAK</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Reggie White</td>
      <td>LE</td>
      <td>Legend PU</td>
      <td>PHI,GB,CAR</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/172/thumbs/17227042013.gif)

## Minnesota Vikings


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>76</th>
      <td>Anthony Barr</td>
      <td>ROLB</td>
      <td>Power Up</td>
      <td>MIN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Stefon Diggs</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>MIN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Everson Griffen</td>
      <td>RE</td>
      <td>Power Up</td>
      <td>MIN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Xavier Rhodes</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>MIN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Harrison Smith</td>
      <td>FS</td>
      <td>Power Up</td>
      <td>MIN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Adam Thielen</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>MIN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Linval Joseph</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>MIN,NYG</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Legend PU</td>
      <td>MIN,OAK,NE,TEN,SF</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>101</th>
      <td>John Randle</td>
      <td>DT</td>
      <td>Legend PU</td>
      <td>MIN,SEA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Donovan McNabb</td>
      <td>QB</td>
      <td>Legend PU</td>
      <td>PHI,MIN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Steve Hutchinson</td>
      <td>LG</td>
      <td>Legend PU</td>
      <td>SEA,MIN,TEN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>189</th>
      <td>Randall McDaniel</td>
      <td>LG</td>
      <td>Legend</td>
      <td>MIN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>191</th>
      <td>Paul Krause</td>
      <td>FS</td>
      <td>Legend PU</td>
      <td>WAS,MIN</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/168/thumbs/im5xz2q9bjbg44xep08bf5czq.gif)

## Washington Redskins


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>85</th>
      <td>Deion Sanders</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>ATL,SF,DAL,WAS,BAL</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Bruce Smith</td>
      <td>RE</td>
      <td>Legend PU</td>
      <td>BUF,WAS</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>121</th>
      <td>Sean Taylor</td>
      <td>FS</td>
      <td>Legend PU</td>
      <td>WAS</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>122</th>
      <td>Champ Bailey</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>WAS,DEN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>183</th>
      <td>Ryan Kerrigan</td>
      <td>LOLB</td>
      <td>Power Up</td>
      <td>WAS</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>184</th>
      <td>Jordan Reed</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>WAS</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>185</th>
      <td>Brandon Scherff</td>
      <td>RG</td>
      <td>Power Up</td>
      <td>WAS</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Trent Williams</td>
      <td>LT</td>
      <td>Power Up</td>
      <td>WAS</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Zach Brown</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>WAS,TEN,BUF</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>191</th>
      <td>Paul Krause</td>
      <td>FS</td>
      <td>Legend PU</td>
      <td>WAS,MIN</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/160/thumbs/1053.gif)

## Tennessee Titans


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>100</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Legend PU</td>
      <td>MIN,OAK,NE,TEN,SF</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>Legend PU</td>
      <td>NO,NYJ,TB,TEN,CIN,LAC,BAL</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Steve Hutchinson</td>
      <td>LG</td>
      <td>Legend PU</td>
      <td>SEA,MIN,TEN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Eddie George</td>
      <td>HB</td>
      <td>Legend PU</td>
      <td>TEN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>178</th>
      <td>Kevin Byard</td>
      <td>FS</td>
      <td>Power Up</td>
      <td>TEN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>179</th>
      <td>Jurell Casey</td>
      <td>RE</td>
      <td>Power Up</td>
      <td>TEN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>180</th>
      <td>Taylor Lewan</td>
      <td>LT</td>
      <td>Power Up</td>
      <td>TEN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>181</th>
      <td>Malcolm Butler</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>TEN,NE</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>182</th>
      <td>Delanie Walker</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>TEN,SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Zach Brown</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>WAS,TEN,BUF</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>206</th>
      <td>Jevon Kearse</td>
      <td>LE</td>
      <td>Legend PU</td>
      <td>TEN,PHI</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/176/thumbs/17636702014.gif)

## Tampa Bay Buccaneers


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>105</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>Legend PU</td>
      <td>NO,NYJ,TB,TEN,CIN,LAC,BAL</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Tim Brown</td>
      <td>WR</td>
      <td>Legend PU</td>
      <td>OAK,TB</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>118</th>
      <td>Derrick Brooks</td>
      <td>ROLB</td>
      <td>Legend PU</td>
      <td>TB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>119</th>
      <td>Steve Young</td>
      <td>QB</td>
      <td>Legend PU</td>
      <td>TB,SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>OAK,TB,BAL,NE,IND</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>173</th>
      <td>Lavonte David</td>
      <td>ROLB</td>
      <td>Power Up</td>
      <td>TB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>174</th>
      <td>Demar Dotson</td>
      <td>RT</td>
      <td>Power Up</td>
      <td>TB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Mike Evans</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>TB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>176</th>
      <td>Gerald McCoy</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>TB</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Brent Grimes</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>TB,ATL,MIA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>188</th>
      <td>Ronde Barber</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>TB</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/180/thumbs/pfiobtreaq7j0pzvadktsc6jv.gif)

## Seattle Seahawks


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>36</th>
      <td>Golden Tate III</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>DET,SEA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Jimmy Graham</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>GB,NO,SEA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>101</th>
      <td>John Randle</td>
      <td>DT</td>
      <td>Legend PU</td>
      <td>MIN,SEA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Steve Hutchinson</td>
      <td>LG</td>
      <td>Legend PU</td>
      <td>SEA,MIN,TEN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Jerry Rice</td>
      <td>WR</td>
      <td>Captain</td>
      <td>SF,OAK,SEA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>166</th>
      <td>Doug Baldwin</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>SEA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>167</th>
      <td>Kam Chancellor</td>
      <td>SS</td>
      <td>Power Up</td>
      <td>SEA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Earl Thomas III</td>
      <td>FS</td>
      <td>Power Up</td>
      <td>SEA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>169</th>
      <td>Bobby Wagner</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>SEA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>170</th>
      <td>Russell Wilson</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>SEA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>172</th>
      <td>Richard Sherman</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>SF,SEA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>192</th>
      <td>Franco Harris</td>
      <td>FB</td>
      <td>Legend PU</td>
      <td>PIT,SEA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>198</th>
      <td>Marshawn Lynch</td>
      <td>RB</td>
      <td>Power Up</td>
      <td>OAK,BUF,SEA</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/6446/thumbs/644624152017.gif)

## Los Angeles Chargers


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>63</th>
      <td>Keenan Allan</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>LAC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Joey Bosa</td>
      <td>LE</td>
      <td>Power Up</td>
      <td>LAC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Melvin Gordon</td>
      <td>HB</td>
      <td>Power Up</td>
      <td>LAC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Hunter Henry</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>LAC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Melvin Ingram</td>
      <td>RE</td>
      <td>Power Up</td>
      <td>LAC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Casey Hayward</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>LAC,GB</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>Legend PU</td>
      <td>NO,NYJ,TB,TEN,CIN,LAC,BAL</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>136</th>
      <td>Drew Brees</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>NO,LAC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>209</th>
      <td>LaDainian Tomlinson</td>
      <td>RB</td>
      <td>Legend PU</td>
      <td>LAC,NYJ</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/173/thumbs/299.gif)

## Atlanta Falcons


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Devonta Freeman</td>
      <td>HB</td>
      <td>Power Up</td>
      <td>ATL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Deion Jones</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>ATL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Julio Jones</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>ATL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Matt Ryan</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>ATL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Desmond Trufant</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>ATL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Alex Mack</td>
      <td>C</td>
      <td>Power Up</td>
      <td>ATL,CLE</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Michael Vick</td>
      <td>QB</td>
      <td>Legend PU</td>
      <td>ATL,PHI,NYJ,PIT</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Deion Sanders</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>ATL,SF,DAL,WAS,BAL</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Tony Gonzalez</td>
      <td>TE</td>
      <td>Legend PU</td>
      <td>KC,ATL</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Brent Grimes</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>TB,ATL,MIA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>200</th>
      <td>Dontari Poe</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>KC,ATL,CAR</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/153/thumbs/318.gif)

## Baltimore Ravens


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9</th>
      <td>Jimmy Smith</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>BAL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Terrell Suggs</td>
      <td>ROLB</td>
      <td>Power Up</td>
      <td>BAL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Marshal Yanda</td>
      <td>RG</td>
      <td>Power Up</td>
      <td>BAL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Deion Sanders</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>ATL,SF,DAL,WAS,BAL</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Ray Lewis</td>
      <td>MLB</td>
      <td>Captain</td>
      <td>BAL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Jonathan Ogden</td>
      <td>LT</td>
      <td>Legend PU</td>
      <td>BAL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Shannon Sharpe</td>
      <td>TE</td>
      <td>Captain</td>
      <td>DEN,BAL</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Ricky Williams</td>
      <td>HB</td>
      <td>Master</td>
      <td>NO,MIA,BAL</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>Legend PU</td>
      <td>NO,NYJ,TB,TEN,CIN,LAC,BAL</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Rod Woodson</td>
      <td>CB</td>
      <td>HoF</td>
      <td>PIT,SF,BAL,OAK</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>147</th>
      <td>Kelechi Osemele</td>
      <td>LG</td>
      <td>Power Up</td>
      <td>OAK,BAL</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>OAK,TB,BAL,NE,IND</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>171</th>
      <td>Kyle Juszczyk</td>
      <td>FB</td>
      <td>Power Up</td>
      <td>SF,BAL</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>207</th>
      <td>Willie Anderson</td>
      <td>RT</td>
      <td>Legend PU</td>
      <td>CIN,BAL</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/5941/thumbs/594179532017.gif)

## Los Angeles Rams


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>69</th>
      <td>Aaron Donald</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>LAR</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Todd Gurley II</td>
      <td>HB</td>
      <td>Power Up</td>
      <td>LAR</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Lamarcus Joyner</td>
      <td>FS</td>
      <td>Power Up</td>
      <td>LAR</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Ndamukong Suh</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>LAR,DET,MIA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Marcus Peters</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>LAR,KC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Aeneas Williams</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>ARI,LAR</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Kevin Greene</td>
      <td>LOLB</td>
      <td>Legend PU</td>
      <td>LAR,PIT,CAR,SF</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>140</th>
      <td>Janoris Jenkins</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>NYG,LAR</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>143</th>
      <td>Trumaine Johnson</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>NYJ,LAR</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>203</th>
      <td>Brandin Cooks</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>NO,NE,LAR</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/162/thumbs/857.gif)

## Kansas City Chiefs


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>57</th>
      <td>Eric Berry</td>
      <td>SS</td>
      <td>Power Up</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Tyreek Hill</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Justin Houston</td>
      <td>LOLB</td>
      <td>Power Up</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Kareen Hunt</td>
      <td>HB</td>
      <td>Power Up</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Travis Kelce</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Patrick Mahomes</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>KC</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Marcus Peters</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>LAR,KC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>97</th>
      <td>Tony Gonzalez</td>
      <td>TE</td>
      <td>Legend PU</td>
      <td>KC,ATL</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Willie Roaf</td>
      <td>LT</td>
      <td>Legend PU</td>
      <td>NO,KC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>148</th>
      <td>Rodney Hudson</td>
      <td>C</td>
      <td>Power Up</td>
      <td>OAK,KC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>200</th>
      <td>Dontari Poe</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>KC,ATL,CAR</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>208</th>
      <td>Ty Law</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>NE,NYJ,KC,DEN</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/152/thumbs/v7tehkwthrwefgounvi7znf5k.gif)

## Boo York Jets


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>84</th>
      <td>Michael Vick</td>
      <td>QB</td>
      <td>Legend PU</td>
      <td>ATL,PHI,NYJ,PIT</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>Legend PU</td>
      <td>NO,NYJ,TB,TEN,CIN,LAC,BAL</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>108</th>
      <td>Kevin Mawae</td>
      <td>C</td>
      <td>Legend Ltd</td>
      <td>NYJ</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Demario Davis</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>NO,NYJ,CLE</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>141</th>
      <td>Damon Harrison Sr</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>NYG,NYJ</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>142</th>
      <td>Jamal Adams</td>
      <td>SS</td>
      <td>Power Up</td>
      <td>NYJ</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>143</th>
      <td>Trumaine Johnson</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>NYJ,LAR</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>208</th>
      <td>Ty Law</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>NE,NYJ,KC,DEN</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>209</th>
      <td>LaDainian Tomlinson</td>
      <td>RB</td>
      <td>Legend PU</td>
      <td>LAC,NYJ</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



![Image](http://content.sportslogos.net/logos/7/159/thumbs/15988562013.gif)

## Jacksonville Jaguars


```python
i+=1
team_list[i]
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>Leonard Fournette</td>
      <td>HB</td>
      <td>Power Up</td>
      <td>JAX</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Myles Jack</td>
      <td>LOLB</td>
      <td>Power Up</td>
      <td>JAX</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Jalen Ramsey</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>JAX</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Telvin Smith</td>
      <td>ROLB</td>
      <td>Power Up</td>
      <td>JAX</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Calais Campbell</td>
      <td>LE</td>
      <td>Power Up</td>
      <td>JAX,ARI</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Andrew Norwell</td>
      <td>LG</td>
      <td>Power Up</td>
      <td>JAX,CAR</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>AJ Bouye</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>JAX,HOU</td>
      <td>2.0</td>
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

    OAK





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>96</th>
      <td>Ted Hendricks</td>
      <td>LOLB</td>
      <td>Legend PU</td>
      <td>IND,GB,OAK</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Legend PU</td>
      <td>MIN,OAK,NE,TEN,SF</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Howie Long</td>
      <td>RT</td>
      <td>Legend Ltd</td>
      <td>OAK</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Tim Brown</td>
      <td>WR</td>
      <td>Legend PU</td>
      <td>OAK,TB</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Rod Woodson</td>
      <td>CB</td>
      <td>HoF</td>
      <td>PIT,SF,BAL,OAK</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Jerry Rice</td>
      <td>WR</td>
      <td>Captain</td>
      <td>SF,OAK,SEA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>144</th>
      <td>Amari Cooper</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>OAK</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Khalil Mack</td>
      <td>LE</td>
      <td>Power Up</td>
      <td>CHI,OAK</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>146</th>
      <td>Derek Carr</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>OAK</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>147</th>
      <td>Kelechi Osemele</td>
      <td>LG</td>
      <td>Power Up</td>
      <td>OAK,BAL</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>148</th>
      <td>Rodney Hudson</td>
      <td>C</td>
      <td>Power Up</td>
      <td>OAK,KC</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>OAK,TB,BAL,NE,IND</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>198</th>
      <td>Marshawn Lynch</td>
      <td>RB</td>
      <td>Power Up</td>
      <td>OAK,BUF,SEA</td>
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

    BUF





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12</th>
      <td>Micah Hyde</td>
      <td>SS</td>
      <td>Power Up</td>
      <td>BUF,GB</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Bruce Smith</td>
      <td>RE</td>
      <td>Legend PU</td>
      <td>BUF,WAS</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Terell Owens</td>
      <td>WR</td>
      <td>HoF</td>
      <td>SF,PHI,DAL,BUF,CIN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>130</th>
      <td>Stephon Gilmore</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>NE,BUF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Nigel Bradham</td>
      <td>LOLB</td>
      <td>Power Up</td>
      <td>PHI,BUF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>158</th>
      <td>Jason Peters</td>
      <td>LT</td>
      <td>Power Up</td>
      <td>PHI,BUF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Zach Brown</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>WAS,TEN,BUF</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>198</th>
      <td>Marshawn Lynch</td>
      <td>RB</td>
      <td>Power Up</td>
      <td>OAK,BUF,SEA</td>
      <td>3.0</td>
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

    CAR





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13</th>
      <td>Luke Kuechly</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>CAR</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Cam Newton</td>
      <td>Qb</td>
      <td>Power Up</td>
      <td>CAR</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Kawann Short</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>CAR</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Daryl Williams</td>
      <td>RT</td>
      <td>Power Up</td>
      <td>CAR</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Greg Olsen</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>CAR,CHI</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Andrew Norwell</td>
      <td>LG</td>
      <td>Power Up</td>
      <td>JAX,CAR</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Kevin Greene</td>
      <td>LOLB</td>
      <td>Legend PU</td>
      <td>LAR,PIT,CAR,SF</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Reggie White</td>
      <td>LE</td>
      <td>Legend PU</td>
      <td>PHI,GB,CAR</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>197</th>
      <td>Jeremy Shockey</td>
      <td>TE</td>
      <td>Legend PU</td>
      <td>NYG,NO,CAR</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>200</th>
      <td>Dontari Poe</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>KC,ATL,CAR</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>202</th>
      <td>Christian McCaffrey</td>
      <td>RB</td>
      <td>Power Up</td>
      <td>CAR</td>
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

    CLE





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Alex Mack</td>
      <td>C</td>
      <td>Power Up</td>
      <td>ATL,CLE</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Joel Bitonio</td>
      <td>LG</td>
      <td>Power Up</td>
      <td>CLE</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Kevin Zeitler</td>
      <td>RG</td>
      <td>Power Up</td>
      <td>CLE,CIN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Jarvis Landry</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>CLE,MIA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Jabaal Sheard</td>
      <td>RE</td>
      <td>Power Up</td>
      <td>IND,CLE,NE</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Demario Davis</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>NO,NYJ,CLE</td>
      <td>3.0</td>
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

    PIT





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>84</th>
      <td>Michael Vick</td>
      <td>QB</td>
      <td>Legend PU</td>
      <td>ATL,PHI,NYJ,PIT</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Kevin Greene</td>
      <td>LOLB</td>
      <td>Legend PU</td>
      <td>LAR,PIT,CAR,SF</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Rod Woodson</td>
      <td>CB</td>
      <td>HoF</td>
      <td>PIT,SF,BAL,OAK</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>160</th>
      <td>Ryan Shazier</td>
      <td>MLB</td>
      <td>Master</td>
      <td>PIT</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>161</th>
      <td>Le'Veon Bell</td>
      <td>HB</td>
      <td>Power Up</td>
      <td>PIT</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>162</th>
      <td>Antonio Brown</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>PIT</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>163</th>
      <td>David DeCastro</td>
      <td>RG</td>
      <td>Power Up</td>
      <td>PIT</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>164</th>
      <td>Marcus Gilbert</td>
      <td>RT</td>
      <td>Power Up</td>
      <td>PIT</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>165</th>
      <td>Ben Roethlisberger</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>PIT</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>190</th>
      <td>Dermontti Dawson</td>
      <td>C</td>
      <td>Legend PU</td>
      <td>PIT</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>192</th>
      <td>Franco Harris</td>
      <td>FB</td>
      <td>Legend PU</td>
      <td>PIT,SEA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>194</th>
      <td>Mean Joe Greene</td>
      <td>DT</td>
      <td>NG</td>
      <td>PIT</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>201</th>
      <td>Emmanuel Sanders</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>DEN,PIT</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>204</th>
      <td>T.J. Watt</td>
      <td>ROLB</td>
      <td>Power Up</td>
      <td>PIT</td>
      <td>1.0</td>
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

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>82</th>
      <td>Linval Joseph</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>MIN,NYG</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Michael Strahan</td>
      <td>LE</td>
      <td>Captain</td>
      <td>NYG</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Lawrence Taylor</td>
      <td>ROLB</td>
      <td>Legend PU</td>
      <td>NYG</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>138</th>
      <td>Odell Beckham Jr</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>NYG</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>139</th>
      <td>Landon Collins</td>
      <td>SS</td>
      <td>Power Up</td>
      <td>NYG</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>140</th>
      <td>Janoris Jenkins</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>NYG,LAR</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>141</th>
      <td>Damon Harrison Sr</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>NYG,NYJ</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>197</th>
      <td>Jeremy Shockey</td>
      <td>TE</td>
      <td>Legend PU</td>
      <td>NYG,NO,CAR</td>
      <td>3.0</td>
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

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>85</th>
      <td>Deion Sanders</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>ATL,SF,DAL,WAS,BAL</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Larry Allen</td>
      <td>RG</td>
      <td>Legend PU</td>
      <td>DAL,SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Kevin Greene</td>
      <td>LOLB</td>
      <td>Legend PU</td>
      <td>LAR,PIT,CAR,SF</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Randy Moss</td>
      <td>WR</td>
      <td>Legend PU</td>
      <td>MIN,OAK,NE,TEN,SF</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Rod Woodson</td>
      <td>CB</td>
      <td>HoF</td>
      <td>PIT,SF,BAL,OAK</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Jerry Rice</td>
      <td>WR</td>
      <td>Captain</td>
      <td>SF,OAK,SEA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Terell Owens</td>
      <td>WR</td>
      <td>HoF</td>
      <td>SF,PHI,DAL,BUF,CIN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>119</th>
      <td>Steve Young</td>
      <td>QB</td>
      <td>Legend PU</td>
      <td>TB,SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>171</th>
      <td>Kyle Juszczyk</td>
      <td>FB</td>
      <td>Power Up</td>
      <td>SF,BAL</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>172</th>
      <td>Richard Sherman</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>SF,SEA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>182</th>
      <td>Delanie Walker</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>TEN,SF</td>
      <td>2.0</td>
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

    CHI





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>17</th>
      <td>Greg Olsen</td>
      <td>TE</td>
      <td>Power Up</td>
      <td>CAR,CHI</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Adrian Amos</td>
      <td>SS</td>
      <td>Power Up</td>
      <td>CHI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Jordan Howard</td>
      <td>HB</td>
      <td>Power Up</td>
      <td>CHI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Danny Trevathan</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>CHI,DEN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Josh Sitton</td>
      <td>LG</td>
      <td>Power Up</td>
      <td>MIA,GB,CHI</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Brian Urlacher</td>
      <td>MLB</td>
      <td>HoF</td>
      <td>CHI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Khalil Mack</td>
      <td>LE</td>
      <td>Power Up</td>
      <td>CHI,OAK</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>205</th>
      <td>Alshon Jeffery</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>CHI,PHI</td>
      <td>2.0</td>
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

    DAL





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>26</th>
      <td>Ezekiel Elliot</td>
      <td>HB</td>
      <td>Power Up</td>
      <td>DAL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Travis Frederick</td>
      <td>C</td>
      <td>Power Up</td>
      <td>DAL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Sean Lee</td>
      <td>ROLB</td>
      <td>Power Up</td>
      <td>DAL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Zack Martin</td>
      <td>RG</td>
      <td>Power Up</td>
      <td>DAL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Tyron Smith</td>
      <td>LT</td>
      <td>Power Up</td>
      <td>DAL</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Deion Sanders</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>ATL,SF,DAL,WAS,BAL</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>90</th>
      <td>DeMarcus Ware</td>
      <td>LOLB</td>
      <td>Legend PU</td>
      <td>DAL,DEN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Larry Allen</td>
      <td>RG</td>
      <td>Legend PU</td>
      <td>DAL,SF</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Terell Owens</td>
      <td>WR</td>
      <td>HoF</td>
      <td>SF,PHI,DAL,BUF,CIN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>199</th>
      <td>Demarcus Lawrence</td>
      <td>LE</td>
      <td>Power Up</td>
      <td>DAL</td>
      <td>1.0</td>
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

    MIA





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>25</th>
      <td>Jarvis Landry</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>CLE,MIA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Ndamukong Suh</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>LAR,DET,MIA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Reshad Jones</td>
      <td>SS</td>
      <td>Power Up</td>
      <td>MIA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Josh Sitton</td>
      <td>LG</td>
      <td>Power Up</td>
      <td>MIA,GB,CHI</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>99</th>
      <td>Dan Marino</td>
      <td>QB</td>
      <td>HoF</td>
      <td>MIA</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Ricky Williams</td>
      <td>HB</td>
      <td>Master</td>
      <td>NO,MIA,BAL</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Brent Grimes</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>TB,ATL,MIA</td>
      <td>3.0</td>
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

    DEN





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20</th>
      <td>Danny Trevathan</td>
      <td>MLB</td>
      <td>Power Up</td>
      <td>CHI,DEN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Chris Harris Jr</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>DEN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Von Miller</td>
      <td>LOLB</td>
      <td>Power Up</td>
      <td>DEN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Demaryius Thomas</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>DEN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>90</th>
      <td>DeMarcus Ware</td>
      <td>LOLB</td>
      <td>Legend PU</td>
      <td>DAL,DEN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Terrell Davis</td>
      <td>HB</td>
      <td>HoF</td>
      <td>DEN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>Steve Atwater</td>
      <td>SS</td>
      <td>Legend</td>
      <td>DEN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Shannon Sharpe</td>
      <td>TE</td>
      <td>Captain</td>
      <td>DEN,BAL</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Brian Dawkins</td>
      <td>SS</td>
      <td>Legend PU</td>
      <td>PHI,DEN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>122</th>
      <td>Champ Bailey</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>WAS,DEN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>201</th>
      <td>Emmanuel Sanders</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>DEN,PIT</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>208</th>
      <td>Ty Law</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>NE,NYJ,KC,DEN</td>
      <td>4.0</td>
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

    HOU





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>43</th>
      <td>Jadeveon Clowney</td>
      <td>ROLB</td>
      <td>Power Up</td>
      <td>HOU</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>DeAndre Hopkins</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>HOU</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>JJ Watt</td>
      <td>LE</td>
      <td>Power Up</td>
      <td>HOU</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Tyrann Mathieu</td>
      <td>FS</td>
      <td>Power Up</td>
      <td>HOU,ARI</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>AJ Bouye</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>JAX,HOU</td>
      <td>2.0</td>
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

    ARI





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Larry Fitzgerald</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>ARI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>David Johnson</td>
      <td>HB</td>
      <td>Power Up</td>
      <td>ARI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Patrick Peterson</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>ARI</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Tyrann Mathieu</td>
      <td>FS</td>
      <td>Power Up</td>
      <td>HOU,ARI</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Calais Campbell</td>
      <td>LE</td>
      <td>Power Up</td>
      <td>JAX,ARI</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Aeneas Williams</td>
      <td>CB</td>
      <td>Legend PU</td>
      <td>ARI,LAR</td>
      <td>2.0</td>
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

    CIN





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21</th>
      <td>Geno Atkins</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>CIN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>AJ Green</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>CIN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Kevin Zeitler</td>
      <td>RG</td>
      <td>Power Up</td>
      <td>CLE,CIN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>105</th>
      <td>Lorenzo Neal</td>
      <td>FB</td>
      <td>Legend PU</td>
      <td>NO,NYJ,TB,TEN,CIN,LAC,BAL</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Terell Owens</td>
      <td>WR</td>
      <td>HoF</td>
      <td>SF,PHI,DAL,BUF,CIN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>193</th>
      <td>Anthony Munoz</td>
      <td>LT</td>
      <td>Legend</td>
      <td>CIN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>207</th>
      <td>Willie Anderson</td>
      <td>RT</td>
      <td>Legend PU</td>
      <td>CIN,BAL</td>
      <td>2.0</td>
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

    DET





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Darius Slay Jr</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>DET</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Matthew Stafford</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>DET</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Golden Tate III</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>DET,SEA</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Ndamukong Suh</td>
      <td>DT</td>
      <td>Power Up</td>
      <td>LAR,DET,MIA</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Barry Sanders</td>
      <td>HB</td>
      <td>Legend PU</td>
      <td>DET</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>195</th>
      <td>Calvin Johnson</td>
      <td>WR</td>
      <td>MF</td>
      <td>DET</td>
      <td>1.0</td>
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

    IND





<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Type</th>
      <th>All Teams</th>
      <th>numTeams</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>47</th>
      <td>TY Hilton</td>
      <td>WR</td>
      <td>Power Up</td>
      <td>IND</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Andrew Luck</td>
      <td>QB</td>
      <td>Power Up</td>
      <td>IND</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Jabaal Sheard</td>
      <td>RE</td>
      <td>Power Up</td>
      <td>IND,CLE,NE</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Ted Hendricks</td>
      <td>LOLB</td>
      <td>Legend PU</td>
      <td>IND,GB,OAK</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Rashaan Melvin</td>
      <td>CB</td>
      <td>Power Up</td>
      <td>OAK,TB,BAL,NE,IND</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>


