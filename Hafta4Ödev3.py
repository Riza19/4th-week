

text=input("Type whatever you want:")
sum_digit = 0
for x in text:
        if x.isdigit() == True:
            z = int(x)
            sum_digit += z
print(sum_digit)


