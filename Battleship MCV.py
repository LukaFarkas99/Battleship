import random

class Brod(object):
    #pravimo rjecnik za postavke i vrijednosti brodova
    __brodovi_info={
                "mali" : 2,
                "srednji": 3,
                "veliki": 4
                }
   # u initu primamo naziv broda i npr za kraj igre nam samo moze provjerit jesu svi postavljeni i potopljeni = TRUE
    def __init__(self,naziv,postavljen=False,potopljen=False):

        self.__naziv=naziv
        self.__postavljen=postavljen
        self.__potopljen=potopljen
        
    @property
    def naziv(self):
        return self.__naziv
    
    #vraca vrijednost iz rjecnika za određeni naziv(key) broda
    
    def vrijednost(self):
        return Brod.__brodovi_info.get(self.__naziv)
  
    @property
    def postavljen(self):
        return self.__postavljen
    
    @postavljen.setter
    def postavljen(self,value):
        self.__postavljen=value

    @property
    def potopljen(self):
        return self.__potopljen
    
    @potopljen.setter
    def potopljen(self,value):
        self.__potopljen=value
        
    def __repr__(self):
        return self.__class__.__name__ + ': %s, Postavljen: %s  Potopljen: %s' % (self.naziv, str( self.postavljen), str(self.potopljen))


class Igrac(object):
    def __init__(self,ime):
        self.__ime=ime
        self.__brodoviZaPostavljanje = [ ]
        self.__brodoviPotopljeni = [ ]
    
    @property
    def ime(self):
        return self.__ime
    
    @ime.setter
    def ime(self,value):
        self.__ime=value
    
    @property
    def brodoviZaPostavljanje(self):
        return self.__brodoviZaPostavljanje
    
    @brodoviZaPostavljanje.setter
    def brodoviZaPostavljanje(self,value):
        self.__brodoviZaPostavljanje = value

    def imaBrodovaZaPostavljanje(self):
        return len(self.__brodoviZaPostavljanje) > 0

    def __str__(self):
        return "Igrac " + self.ime

    def brodZaPostaviti(self, izbor):
        brod = self.__brodoviZaPostavljanje.pop(izbor)
        return brod

    #nisam siguran ovdje za  da li stavit value il nesto drugo, ali uglavnom prima naziv potopljenog broda
    def brodJePotopljen(self, naziv):
        self.__brodoviPotopljeni = naziv

    #nadodajem metodu za provjeru
    def brodoviSuPotopljeni(self):
        if len(self.__brodoviPotopljeni) == 3:
            return True
        else:
            return False
        
class Covjek(Igrac):

    def __init__(self,ime):
        self.ploca=["A1","B1","C1","D1","E1","A2","B2","C2","D2","E2","A3","B3","C3","D3","E3","A4","B4","C4","D4","E4","A5","B5","C5","D5","E5"]
        self.zauzeta_polja={} #tu ubacujemo polja na kojima su brodovi postavljeni
        self.brodoviZaPostavljanje = [ ]
        self.brodoviPotopljeni = [ ]
        super(Covjek,self).__init__(ime)
        
class Racunalo(Igrac):

    def __init__(self,ime):
        self.ploca=["A1","B1","C1","D1","E1","A2","B2","C2","D2","E2","A3","B3","C3","D3","E3","A4","B4","C4","D4","E4","A5","B5","C5","D5","E5"]
        self.zauzeta_polja=[]
        self.brodoviZaPostavljanje = {}
        self.brodoviPotopljeni = [ ]
        super(Racunalo,self).__init__(ime)

class Prikaz(object):

    def __init__(self,red): #red = tko baca
        self.red=red

    def prikaziPocetakIgre(self):
        print("#"*50)
        print("#"*19 +" BATTLESHIP " + "#"*19)
        print("#"*50)

    def unesiIgraca(self):
        while True:
            ime = input("Unesi igraca ")
            if ime.strip():
                print("#"*50+"\n\n}")
                return ime
                
    def ispis_ploce(self,ploca):
        br=0
        s=""
        print("Ploča od "+self.red+"\n")
        for i in ploca:
            br+=1
            s+="\t" +i#[0:2]
            if(br%5==0):
                print(s+"\n")
                s=""

    #samo treba dodati neki ispis tko je pobijedio           
    #def proglasenjePobjednika(self,ime):

    

class Igra():

    gadjanaPolja1 = [] #za covjeka
    gadjanaPolja2 = [] #za racunalo
    mali_r = 0 #ovo brojim 'HP' od brodova racunala
    srednji_r = 0
    veliki_r = 0
    mali_c = 0 # za 'HP' broda od covjeka
    srednji_c = 0
    veliki_c = 0
    iskoristeni_brojevi = []

    def __init__(self,prikaz=None,covjek=None,racunalo=None,brod=None):
        self.prikaz=prikaz
        self.covjek=covjek
        self.racunalo=racunalo
        self.brod=brod
        self.igraci=[]

    #samo treba nadodati metodu za unosenje imena za covjeka u prikaz
    def unosIgraca(self):
        #ime = self.Prikaz.unesiIgraca()
        self.igraci.append(self.covjek)
        self.igraci.append(self.racunalo)
    
    
    @property
    def igracPrvi(self):
        return self.igraci[0]
    
    @property
    def igracDrugi(self):
        return self.igraci[1]

    def postavljanje_brodova(self):
        c.brodoviZaPostavljanje=(mali.naziv+str(mali.vrijednost()),srednji.naziv+str(srednji.vrijednost()),veliki.naziv+str(veliki.vrijednost()))
        r.brodoviZaPostavljanje=(mali.naziv+str(mali.vrijednost()),srednji.naziv+str(srednji.vrijednost()),veliki.naziv+str(veliki.vrijednost()))
        
        print("\n\nPostavi ove brodove na svoju ploču!!!\n")
        for i in self.covjek.brodoviZaPostavljanje:
            print(i[0:-1]+" brod zauzima " +i[-1]+" polja")
            
        print('''Brodove postavi na način da uneseš početno polje npr [a5]
a zatim odaberi smjer u kojem želiš postaviti brod
[w-gore, s-dolje, d-desno, a-lijevo]''' )

  
    def postavljanje_malog_broda(self):
        while(1):
            m_brod=input("Unesi 2 polja odvojena zarezom npr: >>A1,A2<< ili >>a1,b1<< pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude izlazan kao u primjeru!!\n")
            while(1):
                if(len(m_brod)==5):
                    if(m_brod[2]==','):
                        break
                print("Popravi unos")
                m_brod=input("Unesi 2 polja odvojena zarezom npr >>A1,A2<< ili >>a1,b1<< i pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude izlazan kao u primjeru!!\n")
            m_brod=m_brod.upper()
            m=m_brod.split(',')
            prvo_p=m[0]
            drugo_p=m[1]
            p=ord(prvo_p[0])
            pp=int(prvo_p[1])
            d=ord(drugo_p[0])
            dp=int(drugo_p[1])
            print(p,d)
            print(pp,dp)
            if(pp>=1 and dp >=1 and pp<=5 and dp<=5 and pp==dp):
                if(p>=65 and d>=65 and p<=69 and d<=69 and((d+1)==p or (d-1)==p)):
                   print("Ispravno")
                   break
                else:
                    print("Neispravno postavljanje brodova\n")
            else:
                if(pp>=1 and dp >=1 and pp<=5 and dp<=5 and pp!=dp and p==d and((dp+1==pp)or(dp-1==pp))):
                    print("ispravno")
                    break
                else:
                    print("Neispravno postavljanje brodova\n")
                    
        for el in m:
            if el not in self.covjek.zauzeta_polja.keys():
                self.covjek.zauzeta_polja[el]=1
                print(el)
                
        for i,j in self.covjek.zauzeta_polja.items():
            print(i,j)
        br=0
        for i in self.covjek.ploca:
            for j in m:
                if i==j:
                    self.covjek.ploca[br]=i+"m"
            br+=1
            
    def postavljanje_srednjeg_broda(self):
        while(1):
            s_brod=input("Unesi 3 polja odvojena zarezom npr: >>A1,A2,A3<< ili >>a1,b1,c1<< pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude izlazan kao u primjeru!!\n")
            while(1):
                if(len(s_brod)==8):
                    if(s_brod[2]==',' and s_brod[5]==',' ):
                        s_brod=s_brod.upper()
                        s=s_brod.split(',')
                        br=0 
                        b=0
                        for el in s:
                            if el not in self.covjek.zauzeta_polja.keys():
                                b+=1
                                self.covjek.zauzeta_polja[el]=1
                                print("Nije zauzet: "+ el)
                                if (b==3):
                                    break
                                    
                            
                            else:
                                br+=1
                        if (b==3):
                            br=3
                            
                        for i in range(3-br):
                            a=list(self.covjek.zauzeta_polja.keys())[-1]
                            print("obrisano je "+str(a))
                            self.covjek.zauzeta_polja.pop(a)
                        if(len(self.covjek.zauzeta_polja)==5):
                            break
                for i,j in self.covjek.zauzeta_polja.items():
                    print(i,j)            
                print("Popravi unos")
                s_brod=input("Unesi 3 polja odvojena zarezom npr >>A1,A2,A3<< ili >>a1,b1,c1<< i pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude izlazan kao u primjeru!!\n")
            s_brod=s_brod.upper()
            s=s_brod.split(',')
            prvo_p=s[0]
            drugo_p=s[1]
            trece_p=s[2]
            p=ord(prvo_p[0])#slovo/stupac
            pp=int(prvo_p[1])#broj/red
            d=ord(drugo_p[0])
            dp=int(drugo_p[1])
            t=ord(trece_p[0])
            tp=int(trece_p[1])
            print(p,d,t)
            print(pp,dp,tp)
            if(pp>=1 and dp >=1 and pp<=5 and dp<=5 and pp==dp and tp>=1 and tp<=5 and tp==pp):
                if(p>=65 and d>=65 and p<=69 and d<=69 and t>=65 and t<=69 and ((d+1)==p or (d-1)==p) and ((t+2)==p or (t-2)==p)):
                   print("Ispravno\n")
                   break
                else:
                    print("Neispravno postavljanje brodova\n")
            else:
                if(pp>=1 and dp >=1 and pp<=5 and dp<=5 and tp>=1 and tp<=5 and pp!=dp and pp!=tp and p==d and p==t and((dp+1)==pp or(dp-1)==pp)and((tp+2)==pp or(tp-2)==pp)):
                    print("ispravno")
                    break
                else:
                    print("Neispravno postavljanje brodova\n")
        
        
        br=0
        for i in self.covjek.ploca:
            for j in s:
                if i==j:
                    self.covjek.ploca[br]=i+"s"
            br+=1
        self.prikaz.ispis_ploce(self.covjek.ploca)
        
    def postavljanje_velikog_broda(self):
        while(1):
            v_brod=input("Unesi 4 polja odvojena zarezom npr: >>A1,A2,A3,A4<< ili >>a1,b1,c1,d1<< pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude izlazan kao u primjeru!!\n")
            while(1):
                if(len(v_brod)==11):
                    if(v_brod[2]==',' and v_brod[5]==',' and v_brod[8]==','):
                        v_brod=v_brod.upper()
                        v=v_brod.split(',')
                        br=0 
                        b=0
                        for el in v:
                            if el not in self.covjek.zauzeta_polja.keys():
                                b+=1
                                self.covjek.zauzeta_polja[el]=1
                                print("Nije zauzet: "+el)
                                if (b==4):
                                    break
                                    
                            
                            else:
                                br+=1
                        if (b==4):
                            br=4
                            
                        for i in range(4-br):
                            a=list(self.covjek.zauzeta_polja.keys())[-1]
                            print("obrisano je "+str(a))
                            self.covjek.zauzeta_polja.pop(a)
                        if(len(self.covjek.zauzeta_polja)==9):
                            break
                for i,j in self.covjek.zauzeta_polja.items():
                    print(i,j)
                print("Popravi unos")
                v_brod=input("Unesi 4 polja odvojena zarezom npr >>A1,A2,A3,A4<< ili >>a1,b1,c1,d1<< i pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude izlazan kao u primjeru!!\n")
            v_brod=v_brod.upper()
            v=v_brod.split(',')
            prvo_p=v[0]
            drugo_p=v[1]
            trece_p=v[2]
            cetvrto_p=v[3]
            p=ord(prvo_p[0])
            pp=int(prvo_p[1])
            d=ord(drugo_p[0])
            dp=int(drugo_p[1])
            t=ord(trece_p[0])
            tp=int(trece_p[1])
            c=ord(cetvrto_p[0])
            cp=int(cetvrto_p[1])
            print(p,d,t,c)
            print(pp,dp,tp,cp)
            if(pp>=1 and dp >=1 and pp<=5 and dp<=5 and pp==dp and tp>=1 and tp<=5 and tp==pp and cp>=1 and cp >=1 and cp==pp):
                if(p>=65 and d>=65 and p<=69 and d<=69 and t>=65 and t<=69 and c>=65 and c<=69 and ((d+1)==p or (d-1)==p) and ((t+2)==p or (t-2)==p) and ((c+3)==p or(c-3)==p)):
                   print("Ispravno\n")
                   break
                else:
                    print("Neispravno postavljanje brodova\n")
            else:
                if(pp>=1 and dp >=1 and pp<=5 and dp<=5 and tp>=1 and tp<=5 and cp>=1 and cp<=5 and pp!=dp and pp!=tp and pp!=cp and p==d and p==t and p==c and((dp+1==pp)or(dp-1==pp))and((tp+2==pp)or(tp-2==pp))and((cp+3==pp)or(cp-3==pp))):
                    print("ispravno")
                    break
                else:
                    print("Neispravno postavljanje brodova\n")

        br=0
        for i in self.covjek.ploca:
            for j in v:
                if i==j:
                    self.covjek.ploca[br]+="v"
            br+=1
        self.prikaz.ispis_ploce(self.covjek.ploca)
    def igranje(self):
        #self.prikaz.prikaziPocetakIgre()
        #self.postavljanje_brodova()
        self.postavljanje_malog_broda()
        self.postavljanje_srednjeg_broda()
        self.postavljanje_velikog_broda()
        self.unosIgraca()
        
        #dio za gadjanje sto ce se vrtiti nonstop dokle netko ne "pobijedi"
        while True:
            self.gadjanjeBrodova()
            a = self.igracPrvi.brodoviSuPotopljeni() 
            b = self.igracDrugi.brodoviSuPotopljeni()
            if a == True or b == True:
                break
            
        pobjednik = self.provjeraPobjednika()
        Prikaz.proglasenjePobjednika(pobjednik)


    
    def gadjanjeBrodova(self):
        #u prikazu bi kao trebalo napisati ciji je potez cisto tekstualno nesto
        #Prikaz.prikaziPocetakPoteza(self.igracPrvi.ime)
        
        for igrac in self.igraci:
            if type(igrac) == Covjek:
                #ispisati plocu za gadjati da se otprilike vidi kako izgleda
                #Prikaz.ispis_ploce(igrac.ploca) 
                print('Zasad gadjana polja su')
                for ele in self.gadjanaPolja1:
                    print(ele)
                #idemo bez provjere za unos polja zasad
                polje = input("Unesi polje za gadjati: ")
                self.gadjanaPolja1.append(polje)
                poljeF = [ string for string in self.igracDrugi.ploca if polje in self.igracDrugi.ploca ]
                #sada provjerava jel pogodjeno il promaseno
                for ele in poljeF:
                    if 'm' in ele:
                        print('Pogodjen je mali brod racunala')
                        self.mali_r+=1
                        if self.mali_r ==2: #cisto gledamo da je dva puta pogodio malog na ploci
                            print('Potopljen je mali brod racunala')
                            igrac.brodJePotopljen('mali')
                    elif 's' in ele:
                        print('Pogodjen je srednji brod racunala')
                        self.srednji_r+=1
                        if self.srednji_r ==3:
                            print('Potopljen je srednji brod racunala')
                            igrac.brodJePotopljen('srednji')
                    elif 'v' in ele:
                        print('Pogodjen je veliki brod racunala')
                        self.veliki_r+=1
                        if self.veliki_r ==4:
                            print('Potopljen je veliki brod racunala')
                            igrac.brodJePotopljen('veliki')
                            
                    else:
                        print('Promasaj! Na redu je racunalo')
                        self.igraci = self.igraci[::-1]
                        break
            else:
                #za racunalo neka bude bilo cisto random od 0 pa do 25, odnosno 24, ili sa len ploce
                #samo treba pripaziti da se ne ponovi polje koje je vec gadjano
                broj = random.randrange(0,24)
                while True:
                    if broj in self.iskoristeni_brojevi:
                        broj = random.randrange(0,24)
                    else:
                        self.iskoristeni_brojevi.append(broj)
                        break
                
                polje = igrac.ploca[broj]
                self.gadjanaPolja2.append(polje)
                poljeF = [ string for string in self.igracPrvi.ploca if polje in string ]
                #sada provjerava jel pogodjeno il promaseno
                for ele in poljeF:
                    if 'm' in ele:
                        print('Pogodjen je mali brod racunala')
                        self.mali_c+=1
                        if self.mali_c ==2:
                            print('Potopljen je mali brod racunala')
                            igrac.brodJePotopljen('mali')
                    elif 's' in ele:
                        print('Pogodjen je srednji brod racunala')
                        self.srednji_c+=1
                        if self.srednji_c ==3:
                            print('Potopljen je srednji brod racunala')
                            igrac.brodJePotopljen('srednji')
                    elif 'v' in ele:
                        print('Pogodjen je veliki brod racunala')
                        self.veliki_c+=1
                        if self.veliki_c ==4:
                            print('Potopljen je veliki brod racunala')
                            igrac.brodJePotopljen('veliki')
                            
                    else:
                        print('Racunalo je promasilo! Vas je red.')
                        self.igraci = self.igraci[::-1]
                        break

        #isto tako za kraj poteza kao za pocetak
        #Prikaz.prikaziKrajPoteza(self.igracPrvi.ime)

    def provjeraPobjednika():
        if self.igracPrvi.brodoviSuPotopljeni() == 1:
            return self.igracDrugi.ime
        else:
            return self.igracPrvi.ime
        
        
                    
#instanciranje brodova
    
mali=Brod("mali")
srednji=Brod("srednji")
veliki=Brod("veliki")
c=Covjek("Luka")
r=Racunalo("PC")
'''
c.brodoviZaPostavljanje=(mali.naziv+str(mali.vrijednost()),srednji.naziv+str(srednji.vrijednost()),veliki.naziv+str(veliki.vrijednost()))
r.brodoviZaPostavljanje=(mali.naziv+str(mali.vrijednost()),srednji.naziv+str(srednji.vrijednost()),veliki.naziv+str(veliki.vrijednost()))
'''
p=Prikaz(c.ime)
p.ispis_ploce(c.ploca)
i=Igra(p,c,r)
i.igranje()

