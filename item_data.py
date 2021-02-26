import re
import pyperclip

class item_data():

    def __init__(self, item_depth=1):
        super().__init__()
        self.item_depth=item_depth
        self.values = []
        self.mods = []
        #self.requirements = {}
        self.clipboard = pyperclip.paste()

    def process_item_data(self):
        s2 = self.clipboard.split("--------")[self.item_depth]
        s3 = s2.split("\r\n")[1:-1]

        for i in s3:
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
