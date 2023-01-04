import csv
import sys

if len(sys.argv) < 2:
    print("Usage: python account_transactions.py input_file output_file")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

customer_data = {}

transaction_data = {}

# def read_transactions():
    

#     #read from input csv file
#     with open(input_file, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader)
#         for row in reader:
#             #checking if line is empty
#             if not row[0]:
#                 continue

#             parsed_row = row[1].split("/")
#             month_key = parsed_row[0] + "/" + parsed_row[2]

#             #checking if customer id has been seen before
#             if row[0] not in customer_data:
#                 # if not create new dictionary to store new customer's monthly transaction information
#                 customer_data[row[0]] = {}
#             #if customer has made transactions, check to see if any transactions for current month/year
#             if month_key not in customer_data[row[0]]:
#                 #if not begin tracking transaction data for current month/year
#                 customer_data[row[0]][month_key] = {"MinBalance": int(row[2]), "MaxBalance": int(row[2]), "Ending Balance": 0, "Transactions":{}}

#             #updating customer's monthly data based on current transaction
#             customer_data[row[0]][month_key]["Ending Balance"] += int(row[2])
#             customer_data[row[0]][month_key]["MinBalance"] = min(customer_data[row[0]][month_key]["MinBalance"], customer_data[row[0]][month_key]["Ending Balance"])
#             customer_data[row[0]][month_key]["MaxBalance"] = max(customer_data[row[0]][month_key]["MaxBalance"], customer_data[row[0]][month_key]["Ending Balance"])
    
#     #write to output csv file
#     with open(output_file, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)

#         #iterate through each stored customer id
#         for customer in customer_data:
#             #iterate through customer's data for each month
#             for month in customer_data[customer]:
#                 #write data for current month to output csv file
#                 writer.writerow([customer, str(month), customer_data[customer][month]["MinBalance"], customer_data[customer][month]["MaxBalance"], customer_data[customer][month]["Ending Balance"]])

#     return 

def read_transactions():
    with open(input_file, newlien='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            #checking if line is empty
            if not row[0]:
                continue
        parsed_row = row[1].split("/")
        month_key = parsed_row[0] + "/" + parsed_row[2]
        day = parsed_row[1]

        #checking if customer id has been seen before
        if row[0] not in transaction_data:
            #if not create new dictionary to store new customer's monthly transactions
            transaction_data[row[0]] = {}
        #check to see if there are any transactions for current month/year
        if month_key not in transaction_data[row[0]]:
            #if not begin tracking transaction data for current month/year
            transaction_data[row[0]][month_key] = {}
        #check to see if there are any transactions for current day
        if day not in transaction_data[row[0]][month_key]:
            #if not begin tracking transaction data for current day 
            transaction_data[row[0]][month_key][day] = []
        #add current transaction
        customer_data[row[0]][month_key][day].append(int(row[2]))

    return

def store_customer_data():
    return

def create_output():
    return


read_transactions()
