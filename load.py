import csv

def load_to_csv(clean_data, output_filename):
    headers = ["name", "price", "category"]
    with open(output_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(clean_data)

    print(f"Successfully loaded data to {output_filename}")