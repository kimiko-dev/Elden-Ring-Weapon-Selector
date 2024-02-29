import pandas as pd
import pandasql as pdsql

class WeaponQuery():

    def __init__(self):

        self.full_data = pd.read_csv('Elden_Ring_Weapons.csv')
