# Alien-Invaders
Gra Inwazja Obcych opracowana w PyGame
## Setup
Aby uruchomić projekt, wykonaj poniższe polecenia:

```
$ git clone https://github.com/Lioheart/Alien-Invaders.git
$ cd Alien-Invaders
# pip install virtualenv
$ python -m venv venv
$ virtualenv venv
$ source venv/bin/activate              - Linux and Mac
# Set-ExecutionPolicy RemoteSigned      - Windows
$ venv\Scripts\activate                 - Windows
# Set-ExecutionPolicy Restricted        - Windows
$ pip install -r requirements.txt
```

## Użycie
Uruchom program za pomocą komendy: `python alien_invasion.py` 

## Plik wykonywalny .exe
Aby ręcznie utworzyć plik .exe, należy doinstalować pakiet cx_Freeze, a następnie zbudować paczkę:
```
$ pip install cx-Freeze
$ python setup.py build
```
Można także pobrać gotową paczkę [tutaj](https://github.com/Lioheart/Alien-Invaders/releases/latest).
