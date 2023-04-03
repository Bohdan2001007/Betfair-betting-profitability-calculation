import json


class MatchProcessor:
    def __init__(self, json_file):
        self.json_file = json_file
        self.total_coefficients = 0
        self.total_matches = 0
        self.betfair_commission = 1.025  # Betfair has commission 2.5% from profit of value bets

    def process_matches(self):
        with open(self.json_file, 'r') as f:
            data = json.load(f)

        for item in data:
            fields = item["fields"]
            result = fields["result"]
            coefficient = fields["coefficient"]

            if result == "+":
                self.total_coefficients += coefficient

            self.total_matches += 1

        return self.calculate_profitability()

    def calculate_profitability(self):
        print(f"Sum of all value coefficients: {round(self.total_coefficients, 2)}")

        profit_with_commission_betfair = self.total_coefficients / self.betfair_commission

        print(f"Sum of all value coefficients with commission {round(profit_with_commission_betfair, 2)}")
        print(f"Count of all matches of our analysis: {self.total_matches}")

        profit = profit_with_commission_betfair - self.total_matches

        profitability = (profit / self.total_matches) * 100

        print(f"Profitability: {round(profitability, 2)}%")


json_file = 'fixed_data_of_1:1_scores.json'
match_processor = MatchProcessor(json_file)
match_processor.process_matches()
