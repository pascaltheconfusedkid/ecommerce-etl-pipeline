def transform_products(raw_data):
    clean_data_list = []
    
    for product in raw_data:
        clean_data = {
            "name": product.get("title", ""),
            "price": product.get("price", 0),
            "category": product.get("category", "")
        }
        clean_data_list.append(clean_data)
    return clean_data_list

