football_players=open("futbolcular.txt","r")
names=football_players.readlines()
new=open("NewFile.txt","w")
capital_letter="AEIİOÖUÜ"
for i in names:
    if i[0] in capital_letter:
        new.write(i)
new.close()
print("Futbolcular ilgili dosyalara transfer edildi.")


