import pandas as pd


class MergeData:
    def __init__(self, table1, table2):
        self.df1 = pd.DataFrame(table1)
        self.df2 = pd.DataFrame(table2)

        self.df3 = pd.merge(self.df1, self.df2)



