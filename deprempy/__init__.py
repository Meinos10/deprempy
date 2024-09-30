# https://github.com/Meinos10/deprempy

# MIT License

__version__ = "0.0.9"


from requests import get as g
from bs4 import BeautifulSoup as bs
from pydantic import BaseModel

url = "http://www.koeri.boun.edu.tr/scripts/lst1.asp"


class DepremModel(BaseModel):
    tarih: str
    saat: str
    enlem: float
    boylam: float
    derinlik: float
    buyukluk: float
    yer: str
    tip: str

class Deprem:

    def __init__(self) -> None:
        self.r = g(url).text
        self.soup = bs(self.r, "html.parser")
        self.allstrs = self.soup.find("pre").text
        self.strs = self.allstrs.split("---------- --------  --------  -------   ----------    ------------    --------------                                  --------------")[1].strip().split("\n")

    def son_deprem(self):
        yer_ = ""
        tip_ = ""
        if self.strs[0].split()[9].replace("Ý", "I") == "Ilkesel":
            yer_ = self.strs[0].split()[8]
            tip_ = self.strs[0].split()[9].replace("Ý", "I")
        else:
            yer_ = self.strs[0].split()[8] + " " + self.strs[0].split()[9]
            t = len(self.strs[0].split())
            tip_ = self.strs[0].split()[t-1].replace("Ý", "I")
        tarih = self.strs[0].split()[0].split(".")
        sd = DepremModel(
            tarih=f"{tarih[2]}-{tarih[1]}-{tarih[0]}",
            saat=self.strs[0].split()[1],
            enlem=float(self.strs[0].split()[2]),
            boylam=float(self.strs[0].split()[3]),
            derinlik=float(self.strs[0].split()[4]),
            buyukluk=float(self.strs[0].split()[6]),
            yer=yer_,
            tip=tip_
        )
        return sd
    
    def tum_depremler(self, limit: int=100, buyukluk_limit: float=0.0):
        td = []
        for i in self.strs:
            if not self.strs.index(i)+1 > limit:
                yer = ""
                tip = ""
                if self.strs[0].split()[9].replace("Ý", "I") == "Ilkesel":
                    yer = self.strs[0].split()[8]
                    tip = self.strs[0].split()[9].replace("Ý", "I")
                else:
                    yer = self.strs[0].split()[8] + " " + self.strs[0].split()[9]
                    tip = self.strs[0].split()[10].replace("Ý", "I")
                if float(i.split()[6]) >= buyukluk_limit:
                    tarih = i.split()[0].split(".")
                    td.append(
                        DepremModel(
                            tarih=f"{tarih[2]}-{tarih[1]}-{tarih[0]}",
                            saat=i.split()[1],
                            enlem=float(i.split()[2]),
                            boylam=float(i.split()[3]),
                            derinlik=float(i.split()[4]),
                            buyukluk=float(i.split()[6]),
                            yer=yer,
                            tip=tip
                        )
                    )
        return td
    
    def son_24saat(self, limit: int=100, buyukluk_limit: float=0.0):
        s24 = []
        for i in self.strs:
            if not self.strs.index(i)+1 > limit:
                yer = ""
                tip = ""
                if self.strs[0].split()[9].replace("Ý", "I") == "Ilkesel":
                    yer = self.strs[0].split()[8]
                    tip = self.strs[0].split()[9].replace("Ý", "I")
                else:
                    yer = self.strs[0].split()[8] + " " + self.strs[0].split()[9]
                    tip = self.strs[0].split()[10].replace("Ý", "I")

                tarih = i.split()[0].split(".")
                tarih = f"{tarih[2]}-{tarih[1]}-{tarih[0]}"
                if tarih == self.son_deprem().tarih:
                    if float(i.split()[6]) >= buyukluk_limit:
                        s24.append(
                            DepremModel(
                                tarih=tarih,
                                saat=i.split()[1],
                                enlem=float(i.split()[2]),
                                boylam=float(i.split()[3]),
                                derinlik=float(i.split()[4]),
                                buyukluk=float(i.split()[6]),
                                yer=yer,
                                tip=tip
                            )
                        )

        return s24
    
    def son_1saat(self, limit: int=100, buyukluk_limit: float=0.0):
        s1 = []
        for i in self.strs:
            if not self.strs.index(i)+1 > limit:
                yer = ""
                tip = ""
                if self.strs[0].split()[9].replace("Ý", "I") == "Ilkesel":
                    yer = self.strs[0].split()[8]
                    tip = self.strs[0].split()[9].replace("Ý", "I")
                else:
                    yer = self.strs[0].split()[8] + " " + self.strs[0].split()[9]
                    tip = self.strs[0].split()[10].replace("Ý", "I")
                tarih = i.split()[0].split(".")
                tarih = f"{tarih[2]}-{tarih[1]}-{tarih[0]}"
                if tarih == self.son_deprem().tarih and i.split()[1].split(":")[0] == self.son_deprem().saat.split(":")[0]:
                    if float(i.split()[6]) >= buyukluk_limit:                  
                        s1.append(
                            DepremModel(
                                tarih=tarih,
                                saat=i.split()[1],
                                enlem=float(i.split()[2]),
                                boylam=float(i.split()[3]),
                                derinlik=float(i.split()[4]),
                                buyukluk=float(i.split()[6]),
                                yer=yer,
                                tip=tip
                            )
                        )
        return s1
    
