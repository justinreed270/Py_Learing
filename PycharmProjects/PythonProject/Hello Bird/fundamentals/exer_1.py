name="John Smith"
age=20
is_new_patient=True

def is_new():
    if is_new_patient==True:
        return "new"
    if is_new_patient == False:
        return "prior"
def sign_up():
    var1=is_new()
    patient_age = str(age)
    print(name + " is a " + var1 + " patient" + " and is " + patient_age + " years old.")
sign_up()
