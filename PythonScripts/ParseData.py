import csv
import numpy as np
import collections


class ParseData:
    def __init__(self, path):
        """
        This class is to parse csv document and put it into python data structures that is ready to be used, remove
         duplicates, and check NA value at the same time.
        :param path: path to the csv file.
        """
        file_obj = open(path, 'r')
        reader = csv.reader(file_obj)

        self.raw_data = []

        for row in reader:
            self.raw_data.append(tuple(row))

        self.title = self.raw_data[0]

        self.raw_data = set(self.raw_data[1:])

        self.data_body = []

        for data in self.raw_data:
            data_list = list(data)
            for i in range(len(data_list)):
                if (isinstance(data_list[i], float) or isinstance(data_list[i], int)) and np.isnan(data_list[i]):
                    break
                elif i == len(data_list) - 1:
                    self.data_body.append(data_list)

        self.table = collections.defaultdict(list)

        for i in range(len(self.title)):
            for j in range(len(self.data_body)):
                self.table[self.title[i]].append(self.data_body[j][i])
