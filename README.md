# Hyperia - zadanie na pozíciu `Python developer`


> __Zadanie__: Vytvor jednoduchú web-scrape cli appku, ktorá zozbiera údaje z danej stránky a vypíše na výstup/do súboru v JSON formáte. Viac [info](https://lnk.sk/rlz6).

<br>

## Ako spustiť?
Aplikácia využíva moduly jazyka python, kt. sú dostupné v súbore `requirements.txt`. Ich inštaláciu možno realizovať príkazom: 

`pip install -r requirements.txt`

## Návod na použitie
Cieľom vývoja aplikácie bolo osvojiť si zručnosti v oblasti web-scrappingu s využitím (pre mňa nového) modulu BeautifulSoap. Aplikácia nemá poriešené zlé vstupy od uživateľa a preto prosím dodržujte následovnú syntax:

`py cli.py [scrape arg] [json result arg]`

_scrape args_:  

    1) '-s' [job_position]    ->  scrape particular job position  
    2) '-sa'                  ->  scrape all job position  

_json result arg_:

    1) '-j'                   ->  print JSON file w jobs positions  
    2) '-jo' [filename.json]  ->  create and fill in JSON file w jobs positions


Príklad:


Vypíše informácie o prac. pozícii leadgen-php-developer na štandardný výstup:  
`py cli.py -s leadgen-php-developer -j`

Vypíše informácie o všetkých prac. pozíciach na štandardný výstup:  
`py cli.py -sa -j`


Vypíše informácie o prac. pozícii leadgen-php-developer do súboru out.json:  
`py cli.py -s leadgen-php-developer -jo out.json`


Vypíše informácie o všetkých prac. pozíciach do súboru out.json:  
`py cli.py -sa -jo out.json`







