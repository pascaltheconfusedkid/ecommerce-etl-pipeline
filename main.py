from extract import extract_products
from transform import transform_products
from load import load_to_csv

raw_data = extract_products()
clean_data = transform_products(raw_data)
load_to_csv(clean_data, "products.csv")