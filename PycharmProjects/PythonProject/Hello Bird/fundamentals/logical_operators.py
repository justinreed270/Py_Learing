# Logical pperators
# AND: both
# OR: at lease one tru
# NOT:


has_good_credit=True
has_high_income=True
has_criminal_record=False

if has_good_credit and has_high_income:
    print("Get that loan.")
if has_good_credit or has_high_income:
    print("Hmm, give him the loan.")
if has_good_credit and not has_criminal_record:
    print("Nothing to see here, Boss. He gets the loan.")
