import random
Bal = 25000
print("Welcome to Shopping site Discount on Amazon 15%, Flipkart 10%, Myntra 20%")
Pro = ["Shirt","Mobile","Pen","Pant"]
pin = 12345
a = input("Please select Product")
Proval=int(input("Enter Amount"))

if a==Pro[0] or a==Pro[1] or a==Pro[2] or Pant[3]:
    M = input("select site")
    A=
    if M == "Amazon" or M == "Flipkart" or M == "Myntra":
        b = int(input("Please enter you pin"))
        if b == pin:
            OTP = random.randrange(1000, 5000)
            print(OTP)
            if int(input("enter your otp"))==OTP:
                if Bal>Proval:
                    D = (Bal - Proval)
                    print("your remaining Balc", D)
                else:
                    print("Insufficient Fund")
            else:
                print("invalid OTP")
        else:
            print(" Incorrect PIN ")
