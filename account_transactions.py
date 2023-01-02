import csv
import sys

if len(sys.argv) < 2:
    print("Usage: python account_transactions.py input_file output_file")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

customer_data = {}

def read_transactions():
    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if not row[0]:
                continue

            parsed_row = row[1].split("/")
            month_key = parsed_row[0] + "/" + parsed_row[2]

            #checking if customer id has been seen before
            if row[0] not in customer_data:
                # if not create new dictionary to store new customer's monthly transaction information
                customer_data[row[0]] = {}
            #if customer has made transactions, check to see if any transactions for current month/year
            if month_key not in customer_data[row[0]]:
                #if not begin tracking transaction data for current month/year
                customer_data[row[0]][month_key] = {"MinBalance": int(row[2]), "MaxBalance": int(row[2]), "Ending Balance": 0}

            customer_data[row[0]][month_key]["Ending Balance"] += int(row[2])
            customer_data[row[0]][month_key]["MinBalance"] = min(customer_data[row[0]][month_key]["MinBalance"], customer_data[row[0]][month_key]["Ending Balance"])
            customer_data[row[0]][month_key]["MaxBalance"] = max(customer_data[row[0]][month_key]["MaxBalance"], customer_data[row[0]][month_key]["Ending Balance"])
    

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for customer in customer_data:
            for month in customer_data[customer]:
                print([customer, month, customer_data[customer][month][0], customer_data[customer][month][1], customer_data[customer][month][2]])
                writer.writerow([customer, month, customer_data[customer][month][0], customer_data[customer][month][1], customer_data[customer][month][2]])

    return 

read_transactions()
