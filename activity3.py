print("Enter the marks obtained in 4 subjects :")
maths = int(input("maths: "))
english = int(input("english: "))
science = int(input("science:" ))
socialstudies = int(input("socialstudies: "))

sum = maths+english+science+socialstudies
print("sum of maths,english,science and socialstudies =", sum )
perc = (sum/400)*100
print(end="Percentage mark =")
print(perc)