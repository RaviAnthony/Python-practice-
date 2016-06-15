def chesse_and_crackers(chesse_count,boxes_of_crackers):
    print"amount of chesse:%d."%chesse_count
    print"number of boxes of crackers:%d." %boxes_of_crackers
    print"man thats enough for party"
    print"get a blanket \n"
    
print"we can just give the function number directly:"
chesse_and_crackers(40,50)

print" we can use variable from the script"
amount_chesse=20
amount_crackers=50
chesse_and_crackers(amount_chesse,amount_crackers)

print"we can do math inside to"
chesse_and_crackers(40+20,50+30)

print"we can combine two variable and math:"
chesse_and_crackers(amount_chesse+20,amount_crackers+10)
