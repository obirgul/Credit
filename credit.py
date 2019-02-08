from prettytable import PrettyTable

credit = int(input("Ne kadar credit kullandınız = "))
interest = float(input("Aylık interest oranı : "))
length = int(input("Kaç ayda ödemek istiyorsunuz : "))

pmt = credit / (1 - (1 / ((1 + (interest / 100)) ** length))) * (interest / 100)
cost = pmt * length
total_interest = cost - credit
print(cost)
print(total_interest)
last_cost = credit

t = PrettyTable(['Kalan Para','Aylık taksit','Ödenen para','ödenen interest'])

for i in range(1, length + 1):
    last_interest = last_cost * interest / 100
    paid_cost = pmt - last_interest
    last_cost = last_cost - paid_cost

    t.add_row([round(last_cost, 1), round(pmt, 1), round(last_interest, 1), round(paid_cost, 1)])

print(t)
