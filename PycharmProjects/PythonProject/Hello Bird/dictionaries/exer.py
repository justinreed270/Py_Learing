
#ask for "phone: "
# translates into words
#output: "One Two Three Four"

phone=input("phone: ")

dic_num_words={
    "0": "Zero",
    '1': "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Sever",
    "8": "Eight",
    "9": "Nine"
}

output = ""
for ch in phone:
    output+= dic_num_words.get(ch,"!") + " "

print(output)
