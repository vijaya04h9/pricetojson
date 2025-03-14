import csv
import json

# Read the CSV file and process data
csv_file = r"C:\Users\91966\Downloads\Book2.csv"  # Change this to your actual file name
json_file = "output.json"

data = []

with open(csv_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Extracting details from product columns
        product1_details = row["product1"].split('_')
        product2_details = row["product2"].split('_')
        
        product1_price = float(product1_details[1])
        product1_line = int(product1_details[2])
        
        product2_price = float(product2_details[1])
        product2_line = int(product2_details[2])
        
        # Construct the JSON structure
        entry = {
            "ID": row["ID"],
            "First Name": row["First Name"],
            "Last Name": row["Last Name"],
            "Age": row["Age"],
            "Gender": row["Gender"],
            "Email": row["Email"],
            "Phone Number": row["Phone Number"],
            "Address": row["Address"],
            "City": row["City"],
            "Country": row["Country"],
            "Items": [
                {"Item": "Product 1", "Price": product1_price, "Line": product1_line},
                {"Item": "Product 2", "Price": product2_price, "Line": product2_line}
            ]
        }
        
        data.append(entry)

# Write to JSON file
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print(f"CSV converted to JSON successfully! Output file: {json_file}")
