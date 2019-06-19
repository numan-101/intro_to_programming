# credit evaluation
# no input
has_good_credit = False
price = 1000000
down_pmt = 0

if has_good_credit:
    down_pmt = price * 0.1
else:
    down_pmt = price * 0.2

print(f"Down payment: ${down_pmt}")