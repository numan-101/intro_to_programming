# comparison operators and nested conditions

has_high_income = True
has_good_credit = False
has_criminal_record = True

if not has_criminal_record:
    if has_high_income and has_good_credit:
        print("Eligible for loan")
    elif has_high_income or has_good_credit:
        print("Eligible for small loan")
else:
    print("loan denied, criminal record found")
