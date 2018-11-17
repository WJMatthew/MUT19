import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("husl")

'''
class: PowerUpAnalyzer
attributes: - date (str) :
            - player_data (DataFrame) : 
            - 

'''


class PowerUpAnalyzer:

    def __init__(self, date):
        self.date = date
        self.player_data = pd.read_csv('csv/mut_powerups.csv').drop('Unnamed: 0', axis=1)
        self.numeric_data = pd.DataFrame
        self.obj_data = pd.DataFrame
        self.small_data = pd.DataFrame
        self.team_palette = {}
        self.team_list = []
        data = self.player_data
        data = self.clean_data(data)
        data = self.gather_dummies(data)
        self.player_data = self.convert_datatypes(data)
        self.save_file()
        self.set_palette()
        self.minimize_data()
        self.make_plots()
        self.place_into_teams()

    def clean_data(self, data):
        unwanted = ['Legend', 'Legend Ltd']
        data['Type'] = data['Type'].str.strip()
        data = data[~data['Type'].str.strip().isin(unwanted)]
        data['Position'] = data['Position'].str.replace('RB', 'HB').str.upper()
        return data

    def gather_dummies(self, data):
        df = pd.concat( [data, data['All Teams'].str.replace(',', '|').str.get_dummies()], axis=1)
        return df

    def convert_datatypes(self, data):
        self.numeric_data = data.select_dtypes(include=[float, int])
        self.obj_data = data.select_dtypes(exclude=[float, int])
        self.numeric_data['numTeams'] = self.numeric_data.sum(axis=1).astype(int)
        return pd.concat([self.obj_data, self.numeric_data[self.numeric_data['numTeams'] != 0]], axis=1)

    def save_file(self):
        self.player_data.to_csv(f'csv/mut_powerups_{self.date}.csv')

    def make_plots(self):
        self.make_plot1()
        self.make_plot2()
        self.make_plot3()
        self.make_main_plot()

    def make_plot1(self):
        plt.figure(figsize=(13, 7))
        sns.countplot(self.player_data['Position']);
        plt.title('Number of Power-Up Players by Position');
        plt.savefig('img/pu_by_position.png')

    def make_plot2(self):
        # Number of teams per power up player
        plt.figure(figsize=(10, 5))
        sns.countplot(self.player_data['numTeams']);
        plt.title('Power-Up Players Binned by Number of Teams Played For');
        plt.savefig('img/pu_by_numteams.png')

    def make_plot3(self):
        # Number of players per program
        plt.figure(figsize=(10, 5))
        sns.countplot(self.player_data['Type']);
        plt.title('Power-Up Players by Program');
        plt.savefig('img/pu_by_program.png')

    def set_palette(self):
        self.team_palette = {'PHI': 'xkcd:green', 'NE': 'darkblue', 'NO': 'gold', 'GB': 'green', 'MIN': 'xkcd:purple',
                             'WAS': 'maroon', 'TEN': 'cyan', 'TB': 'xkcd:crimson', 'SEA': 'chartreuse',
                             'LAC': 'xkcd:azure', 'ATL': 'xkcd:red', 'BAL': 'indigo', 'LAR': 'xkcd:khaki',
                             'KC': 'red', 'NYJ': 'darkgreen', 'JAX': 'xkcd:darkgreen', 'OAK': 'grey',
                             'BUF': 'xkcd:blue', 'CAR': 'aqua', 'CLE': 'chocolate', 'PIT': 'xkcd:yellow', 'NYG': 'blue',
                             'SF': 'xkcd:gold', 'CHI': 'xkcd:orange', 'DAL': 'xkcd:darkblue', 'MIA': 'xkcd:aqua',
                             'DEN': 'xkcd:orangered', 'HOU': 'xkcd:navy', 'ARI': 'xkcd:red', 'CIN': 'xkcd:orange',
                             'DET': 'xkcd:lightblue', 'IND': 'xkcd:azure'}

    def make_main_plot(self):
        a = self.numeric_data.sum().sort_values(ascending=False)[1:]
        plt.figure(figsize=(15, 10))
        ax = sns.barplot(x=a.values, y=a.index, palette=self.team_palette)
        for p in ax.patches:
            if np.isnan(p.get_width()):
                gh = 0.0
            else:
                gh = np.round(p.get_width(), 2)

            ax.annotate(int(gh), (np.round(gh + 0.15, 3), p.get_y() + 0.5))
        ax.set_title('Number of Power Up Players Eligible for Each Team');
        plt.savefig('img/num_per_team.png')

    def minimize_data(self):
        small = pd.concat([self.obj_data[['Name', 'Position', 'Type', 'All Teams']],
                           self.player_data['numTeams']], axis=1)
        small['All Teams'] = small['All Teams'].str.lstrip(',')
        small[small['numTeams'] >= 4].sort_values('numTeams', ascending=False)
        self.small_data = small[small['Type'] != 'Legend']

    def place_into_teams(self):
        team_abbrevs = list(self.team_palette.keys())
        players = self.player_data.dropna()
        players.reset_index(drop=True, inplace=True)
        self.small_data.reset_index(drop=True, inplace=True)

        for team in team_abbrevs:
            current_team = players[players[team] == 1]
            indices = current_team.index.values
            self.team_list.append(self.small_data.iloc[indices])

    def get_team_list(self):
        return self.team_list


class MarkdownHtmlCleaner:

    def __init__(self, date):
        self.date = date
        self.path = f'md/powerup_analysis_{date}/powerup_analysis_{date}.md'
        self.clean_to_markdown()

    def clean_to_markdown(self):
        with open(self.path, 'r') as f:
            s = f.read()
            s = s.replace('<style></style>', ' ')
            with open(f'md/new_markdown_{self.date}.md', 'w') as f2:
                f2.write(s)

    def clean_to_html(self):
        with open(self.path, 'r') as f:
            s = f.read()

