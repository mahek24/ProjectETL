import json

class User:
    def __init__(self, user_id, name, email, age, signup_date, bank_balance, debt):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.age = age
        self.signup_date = signup_date
        self.bank_balance = bank_balance
        self.debt = debt

    def email_current_balance(self):
        # Simulate sending an email
        print(f"Simulating email to {self.email} with current balance: {self.bank_balance}")

    @staticmethod
    def sort_users(users_list):
        # Bubble sort algorithm to sort users by their names
        n = len(users_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if users_list[j].name > users_list[j+1].name:
                    users_list[j], users_list[j+1] = users_list[j+1], users_list[j]
        return users_list

def load_users_from_json(user_file, bank_file):
    # Load user data
    with open(user_file, 'r') as file:
        users_data = [json.loads(line) for line in file if line.strip()]
    
    # Load bank account data
    with open(bank_file, 'r') as file:
        bank_accounts_data = [json.loads(line) for line in file if line.strip()]
    
    # Create a dictionary for quick lookup of bank accounts by user_id
    bank_accounts_dict = {account['user_id']: account for account in bank_accounts_data}
    
    # Merge user data with bank account data
    users = []
    for user_data in users_data:
        user_id = user_data['user_id']
        bank_account = bank_accounts_dict.get(user_id, {'balance': 0, 'debt': 0})
        user_instance = User(
            user_id=user_data['user_id'],
            name=user_data['name'],
            email=user_data['email'],
            age=user_data['age'],
            signup_date=user_data['signup_date'],
            bank_balance=bank_account['balance'],
            debt=bank_account['debt']
        )
        users.append(user_instance)
    
    return users

# Load users from the JSON files
user_instances = load_users_from_json('filtered_users.json', 'transformed_bank_accounts.json')

# Sort users
sorted_users = User.sort_users(user_instances)

# Print sorted users
for user in sorted_users:
    print(f"Name: {user.name}, Balance: {user.bank_balance}")

# Simulate sending email notifications
for user in sorted_users:
    user.email_current_balance()
