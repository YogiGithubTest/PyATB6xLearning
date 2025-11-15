# An API sometimes fails due to network delays.
#
# Write a program to retry the API call 3 times until the response code becomes 200.
#
# If it still fails after 3 tries, print a failure message.
# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.
# Expected Output Example:
# Attempt 1: Response 500
# Attempt 2: Response 200
# ✅ Test Passed
import random


def response():
    return random.choice([300,200,500])
Attempt = 1
MAx_Attempt = 3

while Attempt<=MAx_Attempt:
    if response() == 200:
        print(f"You got it! {response()}")
        print("✅ Passed API Request")
        break
    else:
        Attempt = Attempt + 1
if response!=200:
    print("❌ Test Failed after 3 attempts.")