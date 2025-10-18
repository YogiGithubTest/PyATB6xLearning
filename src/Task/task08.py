# You want to check whether a web page loads within 3 seconds (performance test condition).
#
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

load_time = float(input("Enter load time: "))
if load_time <= 4.2:
    print("⚠️ Page load too slow")
else:
    print("Page loading is ok ✅")