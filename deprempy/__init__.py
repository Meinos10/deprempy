# https://github.com/Meinos10/deprempy

# MIT License

__version__ = "0.0.1"


from requests import get as g
from bs4 import BeautifulSoup as bs

url = "http://www.koeri.boun.edu.tr/scripts/lst4.asp"

class Deprem:

    def __init__(self) -> None:
        self.r = g(url).text
        self.soup = bs(self.r, "html.parser")
        self.allstrs = self.soup.find("pre").text
        self.strs = self.allstrs.split("---------- --------  --------  -------   ----------    ------------    --------------                                  --------------")[1].strip().split("\n")

    def son_deprem(self):
        sd = {
            "tarih": self.strs[0].split()[0],
            "saat": self.strs[0].split()[1],
            "enlem": self.strs[0].split()[2],
            "boylam": self.strs[0].split()[3],
            "derinlik": self.strs[0].split()[4],
            "buyukluk": self.strs[0].split()[6],
            "yer": self.strs[0].split()[8],
            "tip": self.strs[0].split()[9].replace("Ý", "I")
        }
        return sd
    
    def tum_depremler(self, limit: int=100):
        td = []
        for i in self.strs:
            if not self.strs.index(i)+1 > limit:
                td.append({
                    "tarih": i.split()[0],
                    "saat": i.split()[1],
                    "enlem": i.split()[2],
                    "boylam": i.split()[3],
                    "derinlik": i.split()[4],
                    "buyukluk": i.split()[6],
                    "yer": i.split()[8],
                    "tip": i.split()[9].replace("Ý", "I")
                })
        return td
    
    def son_24saat(self, limit: int=100):
        s24 = []
        for i in self.strs:
            if not self.strs.index(i)+1 > limit:
                if i.split()[0] == self.son_deprem()["tarih"]:
                    s24.append({
                        "tarih": i.split()[0],
                        "saat": i.split()[1],
                        "enlem": i.split()[2],
                        "boylam": i.split()[3],
                        "derinlik": i.split()[4],
                        "buyukluk": i.split()[6],
                        "yer": i.split()[8],
                        "tip": i.split()[9].replace("Ý", "I")
                    })
        return s24
    
    def son_1saat(self, limit: int=100):
        s1 = []
        for i in self.strs:
            if not self.strs.index(i)+1 > limit:
                if i.split()[0] == self.son_deprem()["tarih"] and i.split()[1].split(":")[0] == self.son_deprem()["saat"].split(":")[0]:
                    s1.append({
                        "tarih": i.split()[0],
                        "saat": i.split()[1],
                        "enlem": i.split()[2],
                        "boylam": i.split()[3],
                        "derinlik": i.split()[4],
                        "buyukluk": i.split()[6],
                        "yer": i.split()[8],
                        "tip": i.split()[9].replace("Ý", "I")
                    })
        return s1
    
