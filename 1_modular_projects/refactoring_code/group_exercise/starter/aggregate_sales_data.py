import csv

data = []


def perform_aggregation(keys, data, converter):
    """
    Performs a general calculation based on input data.
    :return: Dictionary containing key, and aggregation as value.
    """

    output = {}

    for row in data:
        product = row[keys[0]]
        aggregated_data = row[keys[1]]
        output[product] = output.get(product, 0) + converter(aggregated_data)

        if "sales" in keys:
            output[product] = round(output[product], 2)

    return output


def write_to_csv(path, data, headers):
    """Write data to CSV"""

    if not path:
        return None

    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for key, value in data.items():
            writer.writerow([key, value])


if __name__ == "__main__":

    with open("./sales_data_sample.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    amount_sales_per_product_type = perform_aggregation(["product_line", "quantity_ordered"], data, int)
    print(amount_sales_per_product_type)

    amount_revenue_per_product_type = perform_aggregation(["product_line", "sales"], data, float)
    print(amount_revenue_per_product_type)

    write_to_csv("./sales_per_product.csv", amount_sales_per_product_type, ["Product Type", "Amount Sales"])
    write_to_csv("./revenue_per_product.csv", amount_revenue_per_product_type, ["Product Type", "Amount Revenue"])
