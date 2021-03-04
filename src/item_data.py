import re
import pyperclip
from operator import add
from functools import reduce

class item_data():

    def __init__(self):
        super().__init__()
        self.values = []
        self.mods = []
        self.clipboard = pyperclip.paste()

    def process_item_data(self):
        s2 = self.clipboard.split("--------")
        s3 = [s.split("\r\n")[1:-1] for s in s2[:-1]]
        s4 = None
        try:
            s4 = reduce(add, s3)
            for i in s4:
                tmp = [s.replace('%','') for s in i.split()]
                tmp_values = []
                tmp_mods = []
                for s in tmp:
                    r_values = re.findall(r"[-+]?\d*\.\d+|\d+", s)
                    if r_values:
                        tmp_values.append(float(r_values[0]))
                    r_mods = re.findall(r"\b[^\d\W]+\b", s)
                    if r_mods:
                        tmp_mods.append(r_mods[0])
                self.values.append(tmp_values)
                self.mods.append(tmp_mods)


        except TypeError:
            pass