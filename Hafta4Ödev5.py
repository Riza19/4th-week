football_players=open("futbolcular.txt","r")
letters=football_players.read()
new_file=open("Newfutbolcular.txt","w")
source="şçöğüıŞÇÖĞÜİ"
target="scoguiSCOGUI"
translate_chart=str.maketrans(source,target)
print(letters.translate(translate_chart))
new_file.write(letters.translate(translate_chart))
new_file.close()
print("Letter transforming is done!")
