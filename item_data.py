import re
import pyperclip

class item_data():

    def __init__(self, item_int=4):
        super().__init__()
        self.item_int=item_int
        self.values = []
        self.mods = []
        #self.requirements = {}
        self.clipboard = pyperclip.paste()

    def process_item_data(self):
        s2 = self.clipboard.split("--------")[self.item_int]
        s3 = s2.split("\r\n")[1:-1]

        for i in s3:
            i.split()
            tmp = [s.replace('%','') for s in re.split("[\+\-]",i)]
            tmp = list(filter(None,tmp))
            #print(tmp)
            self.values.append([int(s) for s in tmp[0].split() if s.isdigit()])
            self.mods.append([s for s in tmp[0].split() if not s.isdigit()])
