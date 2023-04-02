import json


def fix_json_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    fixed_data = []
    for item in data:
        fixed_item = {
            "model": item["model"],
            "pk": item["pk"],
            "fields": {
                "match": item["match"],
                "coefficient": item["coefficient"],
                "result": item["result"]
            }
        }
        fixed_data.append(fixed_item)

    with open(output_file, 'w') as f:
        json.dump(fixed_data, f, ensure_ascii=False, indent=2)


input_file = 'data_of_bets_on_favorite.json'
output_file = 'fixed_data_of_bets_on_favorite.json'
fix_json_data(input_file, output_file)
