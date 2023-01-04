import csv
import sys

if len(sys.argv) < 2:
    print("Usage: python account_transactions.py input_file output_file")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

#dictionary to store relevant monthly customer info including MinBalance, MaxBalance, and EndingBalance
customer_data = {}

#dictionary to store transactions for a given month for a given customer
transaction_data = {}

def read_transactions():
    with open(input_file, newline='') as csvfile:
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
            transaction_data[row[0]][month_key][day].append(int(row[2]))


    return

def store_customer_data():
    for customer in transaction_data:
        customer_data[customer] = {}
        for month in transaction_data[customer]:
            curr_balance = 0
            min_balance = 0
            max_balance = 0
            for i, day in enumerate(transaction_data[customer][month]):

                #ensures that for days with multiple transactions, credits are applied first, before debits
                trans_sorted = sorted(transaction_data[customer][month][day], reverse=True)
                if i == 0:
                    curr_balance += int(trans_sorted[0])

                    #min and max balance variables begin tracking after first transaction 
                    min_balance = int(trans_sorted[0])
                    max_balance = int(trans_sorted[0])

                    #process any remaining transactions for the first day 
                    for j in range(1, len(trans_sorted)):
                        curr_balance += int(trans_sorted[j])
                        min_balance = min(min_balance, curr_balance)
                        max_balance = max(max_balance, curr_balance)
                else:
                    #process all other days for current month/year
                    for j in range(0, len(trans_sorted)):
                        curr_balance += int(trans_sorted[j])
                        min_balance = min(min_balance, curr_balance)
                        max_balance = max(max_balance, curr_balance)

            customer_data[customer][month] = {"MinBalance": min_balance, "MaxBalance": max_balance, "EndingBalance": curr_balance}

    return

def create_output():
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        #iterate through each stored customer id
        for customer in customer_data:
            #iterate through customer's data for each month
            for month in customer_data[customer]:
                #write data for current month to output csv file
                writer.writerow([customer, str(month), customer_data[customer][month]["MinBalance"], customer_data[customer][month]["MaxBalance"], customer_data[customer][month]["EndingBalance"]])
    return


read_transactions()
store_customer_data()
create_output()
