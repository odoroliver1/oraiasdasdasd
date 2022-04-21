class Siugro:
    def __init__(self, egysor):
        darabok=egysor.replace(',','.').split("\t")
        self.nev=darabok[0]
        self.orszag=darabok[1]
        self.ugras1=float(darabok[2])
        self.ugras2=float(darabok[3])
        self.pont1=float(darabok[4])
        self.pont2=float(darabok[5])
        self.osszpontszam=self.pont1+self.pont2

f=open("siugras.txt", "r")
beolvas=f.readlines()
f.close()
siugrok=[]
for i in range(1,len(beolvas)):
    siugrok.append(Siugro(beolvas[i]))

print("A versenyen",len(siugrok),"-en indultak")
db_can=0
for item in siugrok:
    if item.orszag=="CAN":
        db_can+=1
print("A versenyen",db_can,"kanadai versenyző vett részt")
f=open("siugras.txt", "r")
minden=f.read()
f.close()
print(minden.count("CAN"))
orszagok=[]
for item in siugrok:
    if item.orszag not in orszagok:
        orszagok.append(item.orszag)
print("A versenyen" ,len(orszagok), "ország képviselői voltak jelen")
for item in siugrok:
    if item.nev=="AMMANN Simon":
        print("AMMANN Simon",item.orszag,"nemzetiségű")
        break
legnagyobb=siugrok[0].osszpontszam
neve=siugrok[0].nev
for item in siugrok:
    if item.osszpontszam>legnagyobb:
        legnagyobb=item.osszpontszam
        neve=item.nev
print("A versenyt a",neve,"nyerte, pontszáma:",legnagyobb)

       
