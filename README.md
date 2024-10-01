# [deprempy](https://pypi.org/project/deprempy/)

Kandilli Rasathanesi araciligi ile elde edilen deprem sinyallerini kullanarak depremleri gosteren bir Python kutuphanesidir.

</br>

![PyPI](https://img.shields.io/pypi/v/deprempy?color=yellow&logo=python&logoColor=cyan&style=for-the-badge)
</br>

![PyPI - Downloads](https://img.shields.io/pypi/dm/deprempy?label=%C4%B0nd%C4%B0rme&logo=python&style=for-the-badge)
</br>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -U deprempy
```

## Usage

```python
from deprempy import Deprem

deprem = Deprem()



d = deprem.son_deprem()

"""
tarih: d.tarih
saat: d.saat
enlem: d.enlem
boylam: d.boylam
derinlik: d.derinlik
buyukluk: d.buyukluk
yer: d.yer
tip: d.tip

"""

d = deprem.son_1saat(limit=2, buyukluk_limit=1.0)

"""
[
    DepremModel(
        tarih: d.tarih
        saat: d.saat
        enlem: d.enlem
        boylam: d.boylam
        derinlik: d.derinlik
        buyukluk: d.buyukluk
        yer: d.yer
        tip: d.tip
    ),
    DepremModel(
        tarih: d.tarih
        saat: d.saat
        enlem: d.enlem
        boylam: d.boylam
        derinlik: d.derinlik
        buyukluk: d.buyukluk
        yer: d.yer
        tip: d.tip
    )
]
"""

d = deprem.son_24saat(limit=2, buyukluk_limit=1.0)

"""
[
    DepremModel(
        tarih: d.tarih
        saat: d.saat
        enlem: d.enlem
        boylam: d.boylam
        derinlik: d.derinlik
        buyukluk: d.buyukluk
        yer: d.yer
        tip: d.tip
    ),
    DepremModel(
        tarih: d.tarih
        saat: d.saat
        enlem: d.enlem
        boylam: d.boylam
        derinlik: d.derinlik
        buyukluk: d.buyukluk
        yer: d.yer
        tip: d.tip
    )
]
"""

d = deprem.tum_depremler(limit=2, buyukluk_limit=1.0)

"""
[
    DepremModel(
        tarih: d.tarih
        saat: d.saat
        enlem: d.enlem
        boylam: d.boylam
        derinlik: d.derinlik
        buyukluk: d.buyukluk
        yer: d.yer
        tip: d.tip
    ),
    DepremModel(
        tarih: d.tarih
        saat: d.saat
        enlem: d.enlem
        boylam: d.boylam
        derinlik: d.derinlik
        buyukluk: d.buyukluk
        yer: d.yer
        tip: d.tip
    )
]
"""
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

[Telegram](https://t.me/ReWoxi) - [Github](https://github.com/Meinos10)
