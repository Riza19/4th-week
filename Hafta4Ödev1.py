something=input("Write down whatever you want in letters, please")
something=something.replace("i","İ").replace("ı","I").replace("ç","Ç").replace("ş","Ş").replace("ğ","Ğ").replace("ö","Ö").upper()
print(something)

