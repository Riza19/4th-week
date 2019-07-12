request=input("Write whatever you want:")
capital_letter="ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
lower_case="abcçdefgğhıijklmnoöprsştuüvyz"
number="0123456789"

repetition=0
repetition1=0
repetition2=0
repetition3=0
for i in request:
    if i in lower_case:
        repetition+=1
    elif i in capital_letter:
        repetition1+=1
    elif i in number:
        repetition3+=1
    elif i not in capital_letter and lower_case and number:
        repetition2+=1
print("{} times you used lowers case".format(repetition))
print("{} times you used capital letter".format(repetition1))
print("{} times you used special character".format(repetition2))
print("{} times you used number".format(repetition3))
