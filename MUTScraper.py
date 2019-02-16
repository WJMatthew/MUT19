from bs4 import BeautifulSoup
import pandas as pd
import requests
import warnings;
warnings.simplefilter('ignore')
import time
import re

#   Classes:
#       - Player: object to store data for mut card
#
#       - PlayerHandler: class to compile and work with player objects
#
#
prefix = 'https://www.muthead.com'


class Player:

    def __init__(self, link):
        self.stat_dict = {}
        self.trait_dict = {}
        self.name = ' '.join(link.split('-')[1:])
        self.link = link
        self.full_link = prefix + link  # + f'/upgrades?from={upgrade_number}'
        self.price = '0K'
        self.price_diff = '0%'
        self.traits_correct = 0
        self.ovr = 0
        self.position = '-'
        self.program = '-'
        self.first_name = ''
        self.last_name = ''
        self.team = '-'
        self.height_wt = ''
        self.cap_hit = 0
        self.attrib_dict = {}

    def get_ratings(self):
        response = requests.get(self.full_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.soup = soup

        self.get_player_ratings()
        self.get_player_traits()

        if len(self.trait_dict.keys()) == 10: self.traits_correct = 1
        self.get_price(self.soup)
        self.set_values(self.soup)
        self.set_attrib_dict()

    def summary(self):
        print(self.name, ' - ', self.price, ' - ', self.traits_correct)

    def get_price(self, soup):
        try:
            self.price = soup.find_all('span', class_='item-price')[1].contents[0]
            self.price_diff = soup.find_all('span', class_='item-price')[1].contents[1]
        except:
            pass

    def get_player_ratings(self):
        stat_vals = self.soup.find_all('span', class_='stat')  # name also stat-abbreviation
        stat_abbrevs = self.soup.find_all('span', class_='stat-abbreviation')
        [self.stat_dict.update({stat_abbrev.string: stat_val.string})
         for stat_abbrev, stat_val in zip(stat_abbrevs, stat_vals)];

    def get_player_traits(self):
        traits = self.soup.find('ul', class_='player-traits-list').contents

        for trait in traits:
            if trait != '\n':
                try:
                    trait_key = str(trait).split('>')[2].rstrip('</span')
                    trait_val = str(trait).split('>')[3].rstrip('</li').strip()
                    self.trait_dict.update({trait_key: trait_val})
                except:
                    pass

    def set_attrib_dict(self):
        self.attrib_dict.update({'HtWt': self.height_wt})
        self.attrib_dict.update({'OVR': self.ovr})
        self.attrib_dict.update({'Team': self.team})
        self.attrib_dict.update({'Position': self.position})

    def set_values(self, soup):
        try:
            self.ovr = int(soup.find('span', class_='overall').string)
            self.position = soup.find('span', class_='position').string
            self.program = soup.find('div', class_='program-name').string
            self.first_name = soup.find('span', class_='first-name').string
            self.last_name = soup.find('span', class_='last-name').string
            self.team = soup.find('span', class_='team').string
            self.height_wt = soup.find('span', class_='height-weight').string
            self.cap_hit = int(soup.find('span', class_='cap-hit').string)
            self.name = self.first_name + " " + self.last_name
        except:
            pass

    def get_stats_df(self):
        return pd.DataFrame({self.name: self.stat_dict}).T

    def get_traits_df(self):
        return pd.DataFrame({self.name: self.trait_dict}).T

    def get_attribs_df(self):
        return pd.DataFrame({self.name: self.attrib_dict}).T


pos_dict = {'WR': 8, 'RB': 2, 'QB': 1, 'FB': 4, 'BACKS': 6, 'TE': 16, 'OL': 992, 'DB': 458752, 'LB': 57344,
            'DL': 7168, 'ST': 1572864}

print('Available Positions:', [pos for pos in pos_dict.keys()])


class PlayerHandler:

    def __init__(self, position, min_ovr, date):
        self.player_list = []
        self.MIN_OVR = 90
        self.player_links = []
        self.player_df = pd.DataFrame
        self.position = position
        self.min_ovr = min_ovr
        self.date = date
        self.n_pages = 0
        self.print_first_page_link()

    def handle_players(self, pages):
        self.n_pages = pages
        self.get_player_links()
        self.make_player_list()
        self.make_dataframe()
        self.parse_height_and_weight()
        self.save_dataframe()

    def get_player_links(self):
        links = []

        i = 0

        if self.position not in pos_dict.keys():
            print('Position not programmed in yet!')
            return

        while i < self.n_pages:

            try:
                url = f'https://www.muthead.com/19/players?filter-market=3&filter-ovr-min={self.min_ovr}\
                        &filter-position={pos_dict.get(self.position)}&page={i}'
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'lxml')

                for link in soup.findAll('a', attrs={'href': re.compile("19/players/")}):
                    links.append(link.get('href'))
                i += 1

            except:
                print(f'breaking... {len(links)} links gathered.')
                break

        self.player_links = [s for s in links if 'prices' not in s]
        print(f' {len(self.player_links)} player links gathered.')

    def make_player_list(self):

        for player_link in self.player_links:
            p = Player(player_link)
            self.player_list.append(p)

        for player in self.player_list:
            player.get_ratings()
            time.sleep(2)

    def make_dataframe(self):
        stat_list = []
        trait_list = []
        attrib_list = []

        for player in self.player_list:
            stat_list.append(player.get_stats_df())
            trait_list.append(player.get_traits_df())
            attrib_list.append(player.get_attribs_df())

        player_stats = pd.concat(stat_list)
        player_traits = pd.concat(trait_list)
        player_attribs = pd.concat(attrib_list)

        for _ in player_stats.columns:
            player_stats[_] = player_stats[_].fillna(0).astype(int)

        self.player_df = pd.concat([player_stats, player_traits, player_attribs], axis=1)

    def parse_height_and_weight(self):
        # Parsing Height and Weight
        try:
            htwt = self.player_df['HtWt'].str.split('Wt: ')
            ht = htwt.map(lambda x: x[0])
            wt = htwt.map(lambda x: x[1])

            ht2 = ht.str.lstrip('Ht: ').str.rstrip('" ').str.split("' ")
            self.player_df['Ht'] = ht2.map(lambda x: int(x[0]) * 12 + int(x[1].strip()))
            self.player_df['Wt'] = wt.astype(int)
            self.player_df['OVR'] = self.player_df['OVR'].astype(int)
        except:
            pass

    def save_dataframe(self):
        self.player_df.to_csv(f'csv/mut_{self.position}s_{self.min_ovr}plus_{self.date}.csv')


    def print_first_page_link(self):
        url = f'https://www.muthead.com/19/players?filter-market=3&filter-ovr-min={self.min_ovr}&filter-position={pos_dict.get(self.position)}&page=1'
        print('Retrieve the number of pages...')
        print(url)
