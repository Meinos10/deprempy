# [deprempy](https://pypi.org/project/deprempy/)

Kandilli Rasathanesi araciligi ile elde edilen deprem sinyallerini kullanarak depremleri gosteren bir Python kutuphanesidir.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -U deprempy
```

## Usage

```python
from deprempy import Deprem

deprem = Deprem()



deprem.son_deprem()

"""
{
    'tarih': '2023.04.19', 
    'saat': '14:45:23', 
    'enlem': '37.8543', 
    'boylam': '36.5763', 
    'derinlik': '12.1', 
    'buyukluk': '2.5', 
    'yer': 'CEVREPINAR-(KAHRAMANMARAS)', 
    'tip': 'Ilksel'
}
"""

deprem.son_1saat(2)

"""
[
    {
        'tarih': '2023.04.19', 
        'saat': '14:45:23', 
        'enlem': '37.8543', 
        'boylam': '36.5763', 
        'derinlik': '12.1', 
        'buyukluk': '2.5', 
        'yer': 'CEVREPINAR-(KAHRAMANMARAS)', 
        'tip': 'Ilksel'
    }, 
    {
        'tarih': '2023.04.19', 
        'saat': '14:28:29', 
        'enlem': '37.4822', 
        'boylam': '35.2963', 
        'derinlik': '7.7', 
        'buyukluk': '2.0', 
        'yer': 'MADENLI-ALADAG', 
        'tip': '(ADANA)'
    }
]
"""

deprem.son_24saat(2)

"""
[
    {
        'tarih': '2023.04.19', 
        'saat': '14:45:23', 
        'enlem': '37.8543', 
        'boylam': '36.5763', 
        'derinlik': '12.1', 
        'buyukluk': '2.5', 
        'yer': 'CEVREPINAR-(KAHRAMANMARAS)',
        'tip': 'Ilksel'
    }, 
    {
        'tarih': '2023.04.19', 
        'saat': '14:28:29', 
        'enlem': '37.4822', 
        'boylam': '35.2963', 
        'derinlik': '7.7', 
        'buyukluk': '2.0', 
        'yer': 'MADENLI-ALADAG', 
        'tip': '(ADANA)'
    }
]
"""

deprem.tum_depremler(2)

"""
[
    {
        'tarih': '2023.04.19', 
        'saat': '14:45:23', 
        'enlem': '37.8543', 
        'boylam': '36.5763', 
        'derinlik': '12.1', 
        'buyukluk': '2.5', 
        'yer': 'CEVREPINAR-(KAHRAMANMARAS)',
        'tip': 'Ilksel'
    }, 
    {
        'tarih': '2023.04.19', 
        'saat': '14:28:29', 
        'enlem': '37.4822', 
        'boylam': '35.2963', 
        'derinlik': '7.7', 
        'buyukluk': '2.0', 
        'yer': 'MADENLI-ALADAG', 
        'tip': '(ADANA)'
    }
]
"""
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

[Telegram](https://t.me/ReWoxi) - [Github](https://github.com/Meinos10)
