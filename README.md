# Automated report
## Om projektet
Detta är en fördjupning inom Data Science med fokus på automatiserad rapportgenerering med Python.    
Syftet är att bygga en återanvändbar lösning som kan läsa in webbtrafik- och marknadsföringsdata, rensa och validera datan, beräkna KPI och skapa visualiseringar.    Resultaten används sedan för att automatiskt generera en rapport i HTML- och PDF-format.     
En viktig del av projektet är att samma kod ska kunna användas när ny data kommer in, utan att pythonkoden behöver ändras.    
Projektet fokuserar framför allt på hur **Jinja2** kan användas för att skapa en dynamisk HTML-rapport och hur **WeasyPrint** kan användas för att omvandla HTML-rapporten till PDF. 


## Projektstruktur och moduler
```
automated_report/ 
│ 
├── src/ 
│   └── report_tools/ 
│       ├── __init__.py 
│       ├── main.py 
│       ├── config.py 
│       ├── loading.py 
│       ├── cleaning.py 
│       ├── validation.py 
│       ├── analysis.py 
│       ├── visualization.py 
│       └── output.py 
│ 
├── data/ 
│   └── web_traffic_marketing_data_2026.csv 
│ 
├── output/ 
│   └── charts/ 
│ 
├── templates/ 
│   ├── base.html 
│   └── report.html 
│   
├── tests/ 
│   ├── test_analysis.py 
│   ├── test_cleaning.py 
│   └── test_validation.py 
│ 
├── automated_report.pdf 
├── presentation.pptx 
├── README.md 
└── pyproject.toml
```
### Projektets moduler

Projektet är uppdelat i flera moduler med tydliga ansvarsområden:

- `__init__.py` – definierar paketet och dess publika API.
- `main.py` – innehåller programmets huvudflöde och kopplar ihop projektets olika delar.
- `config.py` – samlar projektets konfiguration och sökvägar.
- `loading.py` – läser in webbtrafikdata från CSV-filen.
- `cleaning.py` – rensar och omvandlar data till rätt format.
- `validation.py` – validerar den rensade datan och kontrollerar att den uppfyller projektets krav.
- `analysis.py` – beräknar KPI och sammanställer data för rapporten.
- `visualization.py` – skapar visualiseringarna som används i rapporten.
- `output.py` – hanterar sparning av genererade rapporter.

## Data 
Projektet använder en CSV-fil med webbtrafik- och marknadsföringsdata. 

Datasetet innehåller bland annat information om:
- datum
- trafikkälla/kanal
- enhet
- sessioner
- användare
- sidvisningar
- bounce rate
- genomsnittlig sessionstid
- konverteringar
- intäkter
- marknadsföringskostnad

Datasetet har tagits fram specifikt för projektet och används för att demonstrera hela flödet från rådata till färdig rapport.

## Installation
### Beroenden
Projektet använder Python och följande huvudsakliga bibliotek:
- pandas - datainläsning och databearbetning
- matplotlib - visualiseringar
- seaborn - styling av visualiseringar
- Jinja2 - generering av HTML-rapport
- WeasyPrint - kovertering från HTML till PDF
- pytest - tester

Projektets beroenden finns även definierade i ```pyproject.toml```


### Installera projektet
Skapa en virtuell miljö:   
python -m venv .venv

Aktivera den i PowerShell:   
.venv\Scripts\Activate.ps1

Installera projektet och dess beroenden:   
pip install -e .  

## Så kör du programmet
När den virtuella miljön är aktiverad kan programmet köras genom projektets huvudmodul:

python -m report_tools

Programmet genomför då hela arbetsflödet:

```
Läs in data   
    ↓    
Rensa data     
    ↓    
Validera data    
    ↓     
Beräkna KPI:er     
    ↓     
Skapa visualiseringar     
    ↓     
Generera HTML-rapport     
    ↓     
Skapa PDF-rapport
```   
När programmet körs används samma kod även om innehållet i datasetet har förändrats.

## Rapporten
Programmet genererar en rapport i både HTML- och PDF-format.   

Rapporten innehållet bland annat:
- Övergripande KPI
- KPI uppdelade efter kanal
- KPI uppdelade efter enhet 
- Intäkter i förhållande till marknadsföringskostnad
- ROAS per kanal
- Intäktsutveckling över tid

HTML-rapporten byggs med hjälp av **Jinja2**. 

Projektet använder två HTML-mallar:   
- ```base.html``` - innehåller rapportens gemensamma struktur och CSS.
- ```report.html``` - innehåller det specifika rapportinnehållet och återanvänder strukturen från ```base.html``` genom template inheritance.   

Den färdiga HTML-rapporten konverteras sedan till PDF med **WeasyPrint**. 

Genererade rapporter sparas i ```output/``` och får dagens datum i filnamnet för att göra der möjligt att spara flera rapportversioner. 

## Tester

Projektet innehåller tester skrivna med **pytest**. 

Tester finns för:
- ```analysis.py``` - test av KPI-beräkningar och analysfunktioner. 
- ```cleaning.py``` - test av datarensning och datatyper. 
- ```validation.py```- test av valideringsregler och gränsfall. 

Testerna kan köras från projektets rotmapp med:    
pytest 

## Möjliga vidareutvecklingar 

Den nuvarande lösningen kräver att CSV-filen uppdateras manuellt innan en ny rapport genereras. 

En möjlig vidareutveckling är därför att:
- hämta data automatiskt från ett API eller en databas
- automatiskt identifiera den senaste datafilen
- schemalägga rapportgenereringen
- utöka rapporten med fler KPI och analyser
- skapa en mer interaktiv version av rapporten

På så sätt skulle hela processen kunna automatiseras från datainsamling till färdig rapport. 
