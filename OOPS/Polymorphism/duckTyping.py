# print(1+2)

# print("1"+"2") #print function behaving differently with different kind of arguments

# print(len("python"))
# print(len(["a","b","c"])) 

# # Dynamic  typing 

# def square(x):
#     return x*x

# print(square(5))

# Static typing --> You have to defin the data types before using



class StripeProcessor:
    def process_payment(self, amount):
        print(f"Charging ${amount} via Stripe credit card gateway.")


class PayPalProcessor:
    def process_payment(self, amount):
        print(f"Redirecting to PayPal. Charging ${amount} from user balance.")


class CryptoProcessor:
    def process_payment(self, amount):
        print(f"Verifying blockchain transaction for ${amount} in Bitcoin.")


class Checkout:
    def __init__(self, processor):
        self.processor = processor

    def complete_order(self, total_amount):
        print("Initializing checkout...")
        self.processor.process_payment(total_amount)
        print("Order placed successfully!\n")


# 1. User chooses Stripe
stripe_checkout = Checkout(StripeProcessor())
stripe_checkout.complete_order(49.99)

# 2. User chooses PayPal
paypal_checkout = Checkout(PayPalProcessor())
paypal_checkout.complete_order(15.50)

# 3. User chooses Bitcoin
crypto_checkout = Checkout(CryptoProcessor())
crypto_checkout.complete_order(1200.00)
