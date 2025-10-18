

expected_title = "Dashboard"
actual_title = input("Enter actual title: ").strip()
if expected_title.lower() == actual_title.lower():
    print("✅ Test Passed – Title matches")
elif expected_title != actual_title:
    print("❌Test Failed – Title does not matches")