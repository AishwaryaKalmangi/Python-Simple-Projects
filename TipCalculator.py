bill = float(input('Enter a bill amount in $\t'))
print(bill)
tip = int(input('Enter tip in, 10, 20? $\t'))
print(tip)
person = int(input('Enter the amount of people to split\t'))
print(person)
tip_as_percent = tip / 100
totaltip = bill * tip_as_percent
totalbill = totaltip + bill
finalBill = totalbill / person
bill_per_person=round(finalBill,1)
print(bill_per_person)