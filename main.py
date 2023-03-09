# Function to calculate monthly mortgage payment
def calculate_mortgage():
    loan_amount = float(input("Enter the loan amount: "))  # get loan amount from user
    annual_interest_rate_input = input(
        "Enter the annual interest rate (as a decimal or percentage): "
    )
    # get annual interest rate from user as decimal or percentage
    annual_interest_rate = (
        float(annual_interest_rate_input.strip("%")) / 100
        if "%" in annual_interest_rate_input
        else float(annual_interest_rate_input) / 100
    )
    # convert percentage to decimal if necessary
    loan_term_years = float(
        input("Enter the loan term in years: ")
    )  # get loan term from user
    number_of_payments = (
        loan_term_years * 12
    )  # calculate number of payments based on loan term
    monthly_interest_rate = annual_interest_rate / 12  # calculate monthly interest rate
    payment = (
        loan_amount
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
        / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    )
    # calculate monthly payment based on loan amount, interest rate, and number of payments
    payment = round(payment, 2)  # round payment to 2 decimal places
    print(f"The monthly mortgage payment is: ${payment:.2f}")  # print payment result


# Function to calculate compound interest
def calculate_compound_interest():
    principal = float(
        input("Enter the principal amount: ")
    )  # get principal amount from user
    interest_rate_input = input(
        "Enter the annual interest rate (as a decimal or percentage): "
    )
    # get annual interest rate from user as decimal or percentage
    interest_rate = (
        float(interest_rate_input.strip("%")) / 100
        if "%" in interest_rate_input
        else float(interest_rate_input)
    )
    # convert percentage to decimal if necessary
    compound_frequency = float(
        input("Enter the number of times the interest is compounded per year: ")
    )  # get compound frequency from user
    time_period = float(
        input("Enter the time period in years: ")
    )  # get time period from user
    amount = principal * (
        (1 + (interest_rate / compound_frequency)) ** (compound_frequency * time_period)
    )
    # calculate amount based on principal, interest rate, compound frequency, and time period
    amount = round(amount, 2)  # round amount to 2 decimal places
    print(
        f"The amount after {time_period:.2f} years is: ${amount:.2f}"
    )  # print amount result


# Main function to run program
def main():
    print("Welcome to the Loan Calculator!")
    while True:
        print("1. Calculate Monthly Mortgage Payment")
        print("2. Calculate Compound Interest")
        choice = input("Enter your choice (1 or 2): ")  # get user choice
        if choice == "1":
            calculate_mortgage()  # run monthly mortgage payment calculation function
            break
        elif choice == "2":
            calculate_compound_interest()  # run compound interest calculation function
            break
        else:
            print(
                "Invalid choice. Please select either 1 or 2."
            )  # prompt user for valid choice


if __name__ == "__main__":
    main()  # run main function
