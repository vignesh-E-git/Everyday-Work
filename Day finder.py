# DATE = 15.12.2025
# zeller congurency -> h = ( q + 13(m+1)/5 + k + k/4 + j/4 + 5j ) % 7

date = int(input("enter the date  "))
print("type 123 for month")
month = int(input("enter the month  "))
year = int(input("enter the year  "))

q = date
m = month
j = year // 100 # first two digits in year
k = year % 100 # last two digit (remainder)

h = ( q + (13*(m+1))//5 + k + k//4 + j//4 + 5*j ) % 7
days = ["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
print(days[h])