import json


def process_matches(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    total_coefficients = 0
    total_matches = 0
    betfair_commission = 1.025  # Betfair has commission 2,5% from profit of value bets

    for item in data:
        fields = item["fields"]
        result = fields["result"]
        coefficient = fields["coefficient"]

        if result == "+":
            total_coefficients += coefficient
            total_matches += 1
        else:
            total_matches += 1

    print(f"Sum of all value coefficients: {round(total_coefficients, 2)}")

    profit_with_commission_betfair = total_coefficients / betfair_commission

    print(f"Sum of all value coefficients with commission {round(profit_with_commission_betfair, 2)}")
    print(f"Count of all matches of our analysis: {total_matches}")

    profit = profit_with_commission_betfair - total_matches

    profitability = (profit / total_matches) * 100

    return round(profitability, 2)


json_file = 'fixed_data_of_bets_on_favorite.json'
result = process_matches(json_file)
print(f"Profitability: {result}%")
