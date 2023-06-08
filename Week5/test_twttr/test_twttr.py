from twttr import shorten

def test_normal():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('Duck') == 'Dck'
    assert shorten('Elon') == 'ln'

def test_withoutVowel():
    assert shorten('Crypt') == 'Crypt'
    assert shorten('Fly') == 'Fly'
    assert shorten('Myths') == 'Myths'

def test_casesensitivity():
    assert shorten('MytHs') == 'MytHs'
    assert shorten('elOn') == 'ln'
    assert shorten('DUCK') == 'DCK'

def test_extraCharacters():
    assert shorten('Myt,Hs') == 'Myt,Hs'
    assert shorten('el0n') == 'l0n'
    assert shorten('DUCK!!!') == 'DCK!!!'
