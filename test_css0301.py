import os
from bs4 import BeautifulSoup
import pytest

def test_gazd_osztalyu_elemek_elrejtve_html():
    if not os.path.exists('index.html'):
        pytest.skip("index.html fájl nem található, a tesztelés kihagyva.")

    with open('index.html', 'r', encoding='utf-8') as f:
        html_tartalom = f.read()

    soup = BeautifulSoup(html_tartalom, 'html.parser')

    for elem in soup.find_all(class_='gazd'):
        # Ellenőrizzük, hogy az elem rendelkezik-e style attribútummal, mielőtt ellenőrizzük az értékét.
        if elem.has_attr('style'):
            assert 'visibility: hidden;' in elem['style'], f"A(z) {elem.text} elem nincs elrejtve a HTML-ben!"
        else:
            # Ha nincs style attribútum, akkor a teszt meghiúsul, mert az elem nincs elrejtve.
            assert False, f"A(z) {elem.text} elemen nincs style attribútum!"


def test_gazd_osztalyu_elemek_elrejtve_css():
    if not os.path.exists('style.css'):
        pytest.skip("style.css fájl nem található, a tesztelés kihagyva.")

    with open('style.css', 'r', encoding='utf-8') as f:
        css_tartalom = f.read()

    # Pontosabb ellenőrzés a CSS szabályra.
    assert ".gazd {\n    visibility: hidden;\n}" in css_tartalom, "A .gazd stílus nem található vagy nem megfelelő a style.css fájlban!"


def test_gazd_osztalyu_elemek_helye_megmarad():
    if not os.path.exists('index.html'):
        pytest.skip("index.html fájl nem található, a tesztelés kihagyva.")

    with open('index.html', 'r', encoding='utf-8') as f:
        html_tartalom = f.read()

    soup = BeautifulSoup(html_tartalom, 'html.parser')

    gazd_elemek = soup.find_all(class_='gazd')
    assert len(gazd_elemek) == 2, "Nem található meg mindkét 'gazd' osztályú elem!"

if __name__ == '__main__':
    pytest.main()