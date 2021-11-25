class Customer:

    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount


def transfer(sender: Customer, receiver: Customer, amount: int):
    try:
        if isinstance(sender, Customer) and isinstance(receiver, Customer):
            sender.amount -= amount
            receiver.amount += amount
        else:
            return 'Type Error: sender and receiver are supposed to be Customer instance'
        print(f'{sender.name} sent {amount} to {receiver.name}')
        new_balance = f"Sender's balance = {sender.amount}, Receiver's balance = {receiver.amount}"
    except TypeError as e:
        return 'amount arg is supposed to be an Integer.'
    return new_balance


class Buyer:
    pass


# a = Customer('Mr. A', 1000)
a = Buyer()
b = Customer('Mr. B', 100)


if __name__ == '__main__':
    print(transfer(a, b, 50))
