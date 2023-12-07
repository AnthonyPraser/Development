def get_balances(transactions):
    output = {}

    for t in transactions:
        if t['id'] in output.keys():
            if t['type'] == 'deposit':
                output[t['id']] += t['amount']
            else:
                output[t['id']] -= t['amount']
        else:
            if t['type'] == 'deposit':
                output[t['id']] = t['amount']
            else:
                output[t['id']] = -t['amount']
    return output

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'c', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]

print(get_balances(transactions))













































































