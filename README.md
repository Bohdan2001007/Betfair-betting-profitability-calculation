# Betfair-betting-profitability-calculation

Hello! This Python project demonstrates the profitability of two types of bets:

1. Betting on a correct score of 1:1
2. Betting on the win of the favorite team against an outsider

Over a certain period, I collected coefficient data and conducted statistical analysis of positive (represented by "+" in the JSON file) and negative (represented by "-" in the JSON file) outcomes. This analysis allows us to understand the potential profitability of these betting strategies.

# Consider the example of the match Napoli-Milan

In this case, a coefficient of 7.2 is available for us, since the coefficients are higher (for example, 7.4) are in the auction:

![File1](/static/File1.png)

In this case, a coefficient of 2.02 is available to us

![File2](/static/File2.png)

# Created tables

As the "result" field is obligatory, I must fill them not knowing the result, because let's imagine that Napoli won 2:1 and fill tables

![File3](/static/File3.png)

We add "F" before the home team if it is a favorite or add "F" after the guest team if it is a favorite

![File4](/static/File4.png)

# Installation

Python3 must be already installed

- git clone https://github.com/Bohdan2001007/Betfair-betting-profitability-calculation.git
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py migrate

# Profitability of bet on correct score 1:1

- cd analysis_score_bet
- python profitability.py

![File5](/static/File5.png)

# Profitability of bet on win of favorite team against outsider

- cd bet_on_favorite
- python profitability.py

![File6](/static/File6.png)

# Secret information

You need to create a .env file to store the secret key in the format SECRET_KEY="".
