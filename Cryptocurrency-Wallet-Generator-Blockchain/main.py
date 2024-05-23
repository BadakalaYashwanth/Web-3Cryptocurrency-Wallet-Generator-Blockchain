# main.py

from blockchain import Blockchain
from wallet import Wallet
from transaction import Transaction

def main():
    blockchain = Blockchain()
    wallet = Wallet()

    print("Welcome to the Cryptocurrency Wallet Generator and Blockchain!")
    print("Your new wallet address:", wallet.get_address())

    while True:
        print("\nMenu:")
        print("1. Create a new transaction")
        print("2. Mine a new block")
        print("3. Display the blockchain")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sender = wallet.get_address()
            recipient = input("Enter recipient address: ")
            amount = float(input("Enter amount: "))
            transaction = {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
            signature = wallet.sign_transaction(transaction)
            blockchain.new_transaction(sender, recipient, amount)
            print(f"Transaction created and signed: {transaction} with signature: {signature}")

        elif choice == '2':
            last_proof = blockchain.last_block['proof']
            proof = blockchain.proof_of_work(last_proof)
            blockchain.new_block(proof)
            print("New block mined!")

        elif choice == '3':
            print("Blockchain:")
            for block in blockchain.chain:
                print(block)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
