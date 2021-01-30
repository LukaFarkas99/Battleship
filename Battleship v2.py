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
        self.__brodoviPotopljeni.append(naziv)

    #nadodajem metodu za provjeru
    def brodoviSuPotopljeni(self):
        return len(self.__brodoviPotopljeni)
        
class Covjek(Igrac):

    def __init__(self,ime):
        self.ploca=["A1","B1","C1","D1","E1","A2","B2","C2","D2","E2","A3","B3","C3","D3","E3","A4","B4","C4","D4","E4","A5","B5","C5","D5","E5"]
        self.zauzeta_polja={} #tu ubacujemo polja na kojima su brodovi postavljeni
        self.brodoviZaPostavljanje = [ ]
        self.brodoviPotopljeni = [ ]
        super(Covjek,self).__init__(ime)
        
class Racunalo(Igrac):

    def __init__(self):
        self.ploca=["A1","B1","C1","D1","E1","A2","B2","C2","D2","E2","A3","B3","C3","D3","E3","A4","B4","C4","D4","E4","A5","B5","C5","D5","E5"]
        self.zauzeta_polja=[]
        self.brodoviZaPostavljanje = []
        self.brodoviPotopljeni = [ ]
        super(Racunalo,self).__init__('GLaDOS')

class Prikaz(object):

    def __init__(self): 
        pass
    def prikaziPocetakIgre(self):
        print("#"*50)
        print("#"*19 +" BATTLESHIP " + "#"*19)
        print("#"*50)

    def unesiIgraca(self):
        while True:
            ime = input("Unesi igraca ")
            if ime.strip():
                print("#"*50+"\n\n")
                return ime
                
    def ispis_ploce(self,ploca):
        br=0
        s=""
        print("\n")
        for i in ploca:
            br+=1
            s+="\t" +i#[0:2]
            if(br%5==0):
                print(s+"\n")
                s=""

    def ispis_gadjanja(self,ploca,igrac,gadjanaPolja,pogodjenaPolja):
        br=0
        s=""
        print("Ploča gadjanja od "+igrac.ime+"\n")
        for i in ploca:
            br+=1
            if (i + "m" in pogodjenaPolja) or (i +"s" in pogodjenaPolja) or (i+"v" in pogodjenaPolja):
                s+="\t" +"X"
            elif (i in gadjanaPolja):
                s+="\t" +"~"
            else:
                s+="\t" +i#[0:2]
            if(br%5==0):
                print(s+"\n")
                s=""

    def prikaziPocetakPoteza(self,igrac):
        print("*"*10)
        print("Na potezu je " +  igrac.ime)

    def proglasenjePobjednika(self,ime):
        print("*"*50)
        print("*"*16+ "Pobjednik je " + ime + "!" + "*"*16)
        print("*"*50)

    

class Igra():

    gadjanaPolja1 = [] #za covjeka
    gadjanaPolja2 = [] #za racunalo
    mali_r = 0 #ovo brojim 'HP' od brodova racunala
    srednji_r = 0
    veliki_r = 0
    mali_c = 0 # za 'HP' broda od covjeka
    srednji_c = 0
    veliki_c = 0
    pogodjenaPoljaC = [] #polja sto je pogodio covjek
    pogodjenaPoljaR = [] #sto je pogodilo racunalo
    default_ploca = ["A1","B1","C1","D1","E1","A2","B2","C2","D2","E2","A3","B3","C3","D3","E3","A4","B4","C4","D4","E4","A5","B5","C5","D5","E5"]

    def __init__(self,prikaz=None,brod=None):
        self.prikaz=prikaz
        self.brod=brod
        self.__igraci=[]

    #samo treba nadodati metodu za unosenje imena za covjeka u prikaz
    def unosIgraca(self):
        ime = self.prikaz.unesiIgraca()
        self.__igraci.append(Covjek(ime))
        self.__igraci.append(Racunalo())
    
    
    @property
    def igracPrvi(self):
        return self.__igraci[0]
    
    @property
    def igracDrugi(self):
        return self.__igraci[1]

    def postavljanje_brodova(self):
        igracPrvi.brodoviZaPostavljanje=(mali.naziv+str(mali.vrijednost()),srednji.naziv+str(srednji.vrijednost()),veliki.naziv+str(veliki.vrijednost()))
        igracDrugi.brodoviZaPostavljanje=(mali.naziv+str(mali.vrijednost()),srednji.naziv+str(srednji.vrijednost()),veliki.naziv+str(veliki.vrijednost()))
        
        print("\n\nPostavi ove brodove na svoju ploču!!!\n")
        for i in self.igracPrvi.brodoviZaPostavljanje:
            print(i[0:-1]+" brod zauzima " +i[-1]+" polja")
            
        print('''Brodove postavi na način da uneseš početno polje npr [a5]
a zatim odaberi smjer u kojem želiš postaviti brod
[w-gore, s-dolje, d-desno, a-lijevo]''' )

  
    def postavljanje_malog_broda(self):
        while(1):
            m_brod=input("Unesi 2 polja odvojena zarezom npr: >>A1,A2<< ili >>a1,b1<< pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude uzlazan kao u primjeru!!\n")
            unos=False
            while(unos==False):
                try:
                    if (type(m_brod[0])is str and type(int(m_brod[1]))is int and type(m_brod[3])is str and type(int(m_brod[4]))is int):
                        unos=True
                except:
                      m_brod=input("Unesi 2 polja odvojena zarezom npr: >>A1,A2<< ili >>a1,b1<< pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude uzlazan kao u primjeru!!\n")
           

            while(1):
                if(len(m_brod)==5):
                    if(m_brod[2]==','):
                        break
                print("Popravi unos")
                m_brod=input("Unesi 2 polja odvojena zarezom npr >>A1,A2<< ili >>a1,b1<< i pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude uzlazan kao u primjeru!!\n")
            m_brod=m_brod.upper()
            m=m_brod.split(',')
            prvo_p=m[0]
            drugo_p=m[1]
            p=ord(prvo_p[0])
            pp=int(prvo_p[1])
            d=ord(drugo_p[0])
            dp=int(drugo_p[1])
            #print(p,d)
            #print(pp,dp)
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
            if el not in self.igracPrvi.zauzeta_polja.keys():
                self.igracPrvi.zauzeta_polja[el]=1
                #print(el)
                
        #for i,j in self.covjek.zauzeta_polja.items():
            #print(i,j)
        br=0
        for i in self.igracPrvi.ploca:
            for j in m:
                if i==j:
                    self.igracPrvi.ploca[br]=i+"m"
            br+=1
            
    def postavljanje_srednjeg_broda(self):
        while(1):
            s_brod=input("Unesi 3 polja odvojena zarezom npr: >>A1,A2,A3<< ili >>a1,b1,c1<< pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude uzlazan kao u primjeru!!\n")
            unos=False
            while(unos==False):
                try:
                    if (type(s_brod[0])is str and type(int(s_brod[1]))is int and type(s_brod[3])is str and type(int(s_brod[4]))is int and type(s_brod[6])is str and type(int(s_brod[7])) is int):
                        unos=True
                except:
                    s_brod=input("Unesi 3 polja odvojena zarezom npr: >>A1,A2,A3<< ili >>a1,b1,c1<< pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude uzlazan kao u primjeru!!\n")
           
            while(1):
                if(len(s_brod)==8):
                    if(s_brod[2]==',' and s_brod[5]==',' ):
                        s_brod=s_brod.upper()
                        s=s_brod.split(',')
                        br=0 
                        b=0
                        for el in s:
                            if el not in self.igracPrvi.zauzeta_polja.keys():
                                b+=1
                                self.igracPrvi.zauzeta_polja[el]=1
                                #print("Nije zauzet: "+ el)
                                if (b==3):
                                    break
                                    
                            
                            else:
                                br+=1
                        if (b==3):
                            br=3
                            
                        for i in range(3-br):
                            a=list(self.igracPrvi.zauzeta_polja.keys())[-1]
                            #print("obrisano je "+str(a))
                            self.igracPrvi.zauzeta_polja.pop(a)
                        if(len(self.igracPrvi.zauzeta_polja)==5):
                            break
                for i,j in self.igracPrvi.zauzeta_polja.items():
                    print(i,j)            
                print("Popravi unos")
                s_brod=input("Unesi 3 polja odvojena zarezom npr >>A1,A2,A3<< ili >>a1,b1,c1<< i pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude uzlazan kao u primjeru!!\n")
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
            #print(p,d,t)
            #print(pp,dp,tp)
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
        for i in self.igracPrvi.ploca:
            for j in s:
                if i==j:
                    self.igracPrvi.ploca[br]=i+"s"
            br+=1
        self.prikaz.ispis_ploce(self.igracPrvi.ploca)
        
    def postavljanje_velikog_broda(self):
        while(1):
            
            unos=False
            v_brod=input("Unesi 4 polja odvojena zarezom npr: >>A1,A2,A3,A4<< ili >>a1,b1,c1,d1<< pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude uzlazan kao u primjeru!!\n")
            while(unos==False):
                try:
                    if (type(v_brod[0])is str and type(int(v_brod[1]))is int and type(v_brod[3])is str and type(int(v_brod[4]))is int and type(v_brod[6])is str and type(int(v_brod[7])) is int and type(v_brod[9])is str and type(int(v_brod[10])) is int):
                        unos=True
                except:
                     v_brod=input("Unesi 4 polja odvojena zarezom npr: >>A1,A2,A3,A4<< ili >>a1,b1,c1,d1<< pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude uzlazan kao u primjeru!!\n")
           
            while(1):
                if(len(v_brod)==11):
                    if(v_brod[2]==',' and v_brod[5]==',' and v_brod[8]==','):
                        v_brod=v_brod.upper()
                        v=v_brod.split(',')
                        br=0 
                        b=0
                        for el in v:
                            if el not in self.igracPrvi.zauzeta_polja.keys():
                                b+=1
                                self.igracPrvi.zauzeta_polja[el]=1
                                #print("Nije zauzet: "+el)
                                if (b==4):
                                    break
                                    
                            
                            else:
                                br+=1
                        if (b==4):
                            br=4
                            
                        for i in range(4-br):
                            a=list(self.igracPrvi.zauzeta_polja.keys())[-1]
                            #print("obrisano je "+str(a))
                            self.igracPrvi.zauzeta_polja.pop(a)
                        if(len(self.igracPrvi.zauzeta_polja)==9):
                            break
                #for i,j in self.covjek.zauzeta_polja.items():
                    #print(i,j)
                print("Popravi unos")
                v_brod=input("Unesi 4 polja odvojena zarezom npr >>A1,A2,A3,A4<< ili >>a1,b1,c1,d1<< i pazi da brod bude postavljen vertikalno ili horizontalno i da poredak polja bude uzlazan kao u primjeru!!\n")
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
            #print(p,d,t,c)
            #print(pp,dp,tp,cp)
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
        for i in self.igracPrvi.ploca:
            for j in v:
                if i==j:
                    self.igracPrvi.ploca[br]+="v"
            br+=1
        self.prikaz.ispis_ploce(self.igracPrvi.ploca)

#postavljanej brodova za racunalo


    def postavljanje_malog_broda_racunalo(self):
        while(1):
            k=random.randint(65,69)         
            p=chr(k)                        #A/B/C/D/E     
            pp=random.randint(1,5)          #1/2/3/4/5
            smjer=random.randint(0,1)  
            if (smjer==1):                  #postavlja se horizontalno
                if( p>='A' and p <='D'):
                    d=k+1
                    d=chr(d)
                else:
                    d=k-1
                    d=chr(d)
                dp=pp
            else:                           #postavlja se vertikalno 
                if(pp>=1 and pp<5):
                    dp=pp+1
                else:
                    dp=pp-1
                d=p 
            #x[3:6] = [''.join(x[3:6])] primjer
                
            break
            
        self.igracDrugi.zauzeta_polja+=(str(p)+str(pp))+(str(d)+str(dp))
        self.igracDrugi.zauzeta_polja[0:2]=[''.join(self.igracDrugi.zauzeta_polja[0:2])]
        self.igracDrugi.zauzeta_polja[1:]=[''.join(self.igracDrugi.zauzeta_polja[1:])]    
        #print(self.racunalo.zauzeta_polja)
        br=0
        for i in self.igracDrugi.ploca:
            for j in self.igracDrugi.zauzeta_polja:
                if i==j:
                    self.igracDrugi.ploca[br]+="m"
            br+=1
        #self.prikaz.ispis_ploce(self.racunalo.ploca)
        print("\n!!!\tPC je postavio mali brod\t!!!\n")

    def postavljanje_srednjeg_broda_racunalo(self):

        ponovi=True
        while(ponovi):
            k=random.randint(65,69)         
            p=chr(k)                             
            pp=random.randint(1,5)          
            smjer=random.randint(0,1)  
            if (smjer==1):                  
                if( p>='A' and p <='C'):
                    d=k+1
                    d=chr(d)
                    t=k+2
                    t=chr(t)
                else:
                    d=k-1
                    d=chr(d)
                    t=k-2
                    t=chr(t)
                dp=pp
                tp=pp
            else:                           
                if(pp >= 1 and pp < 4):
                    dp=pp+1
                    tp=pp+2
                else:
                    dp=pp-1
                    tp=pp-2
                d=p
                t=p
            self.igracDrugi.zauzeta_polja+=(str(p)+str(pp))+(str(d)+str(dp))+(str(t)+str(tp))
            self.igracDrugi.zauzeta_polja[2:4]=[''.join(self.igracDrugi.zauzeta_polja[2:4])]
            self.igracDrugi.zauzeta_polja[3:5]=[''.join(self.igracDrugi.zauzeta_polja[3:5])]
            self.igracDrugi.zauzeta_polja[4:]=[''.join(self.igracDrugi.zauzeta_polja[4:])] 

            #print(self.racunalo.zauzeta_polja)
                
            ponovi=False
            for i in self.igracDrugi.zauzeta_polja[0:2]:
                for j in self.igracDrugi.zauzeta_polja[2:]:
                    #print(i+j)
                    if (i==j):
                        del self.igracDrugi.zauzeta_polja[2:]
                        ponovi=True
                        break
               
            
        
                                             
        br=0
        for i in self.igracDrugi.ploca:
            for j in self.igracDrugi.zauzeta_polja:
                if i==j:
                    self.igracDrugi.ploca[br]+="s"
            br+=1
        #self.prikaz.ispis_ploce(self.racunalo.ploca)
        print("\n!!!\tPC je postavio srednji brod\t!!!\n")
            

    def postavljanje_velikog_broda_racunalo(self):
        ponovi=True
        neispravan_unos=False
        while(ponovi):
            strana=random.randint(0,1)
            if (strana==0):  #lijevo
                k=random.randint(65,66)
            else:
                k=random.randint(68,69)
            #k=random.randint(65,69) # bug za 67     
            p=chr(k)
            
            pp=random.randint(1,5) #bug za 3         
            smjer=random.randint(0,1)
            if (k==67):
                smjer = 0
                
            if (pp==3):
                smjer = 1
                
            
            if (smjer==1):
                
                if (p =='A' or p== 'B'):
                    d=k+1
                    d=chr(d)
                    t=k+2
                    t=chr(t)
                    c=k+3
                    c=chr(c)
                    dp=pp
                    tp=pp
                    cp=pp
                elif(p=='D' or p=='E'):
                    d=k-1
                    d=chr(d)
                    t=k-2
                    t=chr(t)
                    c=k-3
                    c=chr(c)
                    dp=pp
                    tp=pp
                    cp=pp
                else:
                    if(pp==1  or pp==2):
                        dp=pp+1
                        tp=pp+2
                        cp=pp+3
                    elif(pp==4 or pp==5):
                        dp=pp-1
                        tp=pp-2
                        cp=pp-3
                    d=p
                    t=p
                    c=p
                    
                
            else:
                if(pp==1  or pp==2):
                    dp=pp+1
                    tp=pp+2
                    cp=pp+3
                elif(pp==4 or pp==5):
                    dp=pp-1
                    tp=pp-2
                    cp=pp-3
                else:
                    neispravan_unos=True                 
                d=p
                t=p
                c=p
                
            if (k==67 and pp==3):
                ponovi=True
                neispravan_unos==True
                
            if (neispravan_unos==False):
                self.igracDrugi.zauzeta_polja+=(str(p)+str(pp))+(str(d)+str(dp))+(str(t)+str(tp)+(str(c)+str(cp)))
                self.igracDrugi.zauzeta_polja[5:7]=[''.join(self.igracDrugi.zauzeta_polja[5:7])]
                self.igracDrugi.zauzeta_polja[6:8]=[''.join(self.igracDrugi.zauzeta_polja[6:8])]
                self.igracDrugi.zauzeta_polja[7:9]=[''.join(self.igracDrugi.zauzeta_polja[7:9])]
                self.igracDrugi.zauzeta_polja[8:]=[''.join(self.igracDrugi.zauzeta_polja[8:])]

                #print(self.racunalo.zauzeta_polja)
                
                ponovi=False
            for i in self.igracDrugi.zauzeta_polja[0:5]:
                for j in self.igracDrugi.zauzeta_polja[5:]:
                    #print(i+j)
                    if (i==j):
                        del self.igracDrugi.zauzeta_polja[5:]
                        ponovi=True
                        break
                    
                    
            
                
        
        br=0
        for i in self.igracDrugi.ploca:
            for j in self.igracDrugi.zauzeta_polja:
                if i==j:
                    self.igracDrugi.ploca[br]+="v"
            br+=1
        #self.prikaz.ispis_ploce(self.racunalo.ploca)
        print("\n!!!\tPC je postavio veliki brod\t!!!\n")

   
    def igranje(self):
        self.prikaz.prikaziPocetakIgre()
        self.unosIgraca()
        self.prikaz.ispis_ploce(self.igracPrvi.ploca)
        #self.postavljanje_brodova()
        self.postavljanje_malog_broda()
        self.postavljanje_srednjeg_broda()
        self.postavljanje_velikog_broda()
        self.postavljanje_malog_broda_racunalo()
        self.postavljanje_srednjeg_broda_racunalo()
        self.postavljanje_velikog_broda_racunalo()
        while True:
            if self.igracPrvi.brodoviSuPotopljeni()  == 3 or self.igracDrugi.brodoviSuPotopljeni()  == 3:
                break
            self.gadjanjeBrodova() 
        self.prikaz.proglasenjePobjednika(self.provjeraPobjednika())


    
    def gadjanjeBrodova(self):
    
        for igrac in self.__igraci:
            if type(igrac) == Covjek:
                shot_c=1
                if self.igracPrvi.brodoviSuPotopljeni() != 3 and self.igracDrugi.brodoviSuPotopljeni() != 3:
                    self.prikaz.prikaziPocetakPoteza(igrac)
                    self.prikaz.ispis_ploce(igrac.ploca)
                    self.prikaz.ispis_gadjanja(self.default_ploca,self.igracPrvi,self.gadjanaPolja1,self.pogodjenaPoljaC)
                while shot_c == 1 and self.igracPrvi.brodoviSuPotopljeni() != 3 and self.igracDrugi.brodoviSuPotopljeni() != 3:
                    polje = input("Unesite polje za gadjati:")
                    polje=polje.upper()
                    while polje not in self.default_ploca:
                            polje = input("\nPRAVILNO unesite polje za gadjati:")
                            polje=polje.upper()
                    while polje in self.gadjanaPolja1:
                        polje = input("\nVec ste to polje gadjali! Unesite neko drugo polje:")
                        polje=polje.upper()
                    self.gadjanaPolja1.append(polje)
                    poljeFC = [ string for string in self.igracDrugi.ploca if polje in string ]
                    for ele in poljeFC:
                        if 'm' in ele:
                            print('Pogodili ste mali brod racunala.')
                            self.pogodjenaPoljaC.append(ele)
                            self.mali_r+=1
                            if self.mali_r ==2: 
                                print('!!!\tPotopili ste mali brod racunala\t!!!')
                                self.igracDrugi.brodJePotopljen('mali')
                            self.prikaz.ispis_gadjanja(self.default_ploca,self.igracPrvi,self.gadjanaPolja1,self.pogodjenaPoljaC)
                        elif 's' in ele:
                            print('Pogodili ste srednji brod racunala.')
                            self.pogodjenaPoljaC.append(ele)
                            self.srednji_r+=1
                            if self.srednji_r ==3:
                                print('!!!\tPotopili ste srednji brod racunala\t!!!!')
                                self.igracDrugi.brodJePotopljen('srednji')
                            self.prikaz.ispis_gadjanja(self.default_ploca,self.igracPrvi,self.gadjanaPolja1,self.pogodjenaPoljaC)
                        elif 'v' in ele:
                            print('Pogodili ste veliki brod racunala.')
                            self.pogodjenaPoljaC.append(ele)
                            self.veliki_r+=1
                            if self.veliki_r ==4:
                                print('!!!\tPotopili ste veliki brod racunala\t!!!')
                                self.igracDrugi.brodJePotopljen('veliki')
                            self.prikaz.ispis_gadjanja(self.default_ploca,self.igracPrvi,self.gadjanaPolja1,self.pogodjenaPoljaC)
                        else:
                            print('Nazalost, promasili ste!')
                            shot_c = 0
                            break

            else:
                shot_r = 1
                if self.igracPrvi.brodoviSuPotopljeni() != 3 and self.igracDrugi.brodoviSuPotopljeni() != 3:
                    self.prikaz.prikaziPocetakPoteza(igrac)
                while shot_r == 1 and self.igracPrvi.brodoviSuPotopljeni() != 3 and self.igracDrugi.brodoviSuPotopljeni() != 3:
                    polje = random.choice(self.igracPrvi.ploca)
                    while polje in self.gadjanaPolja2:
                            polje = random.choice(self.igracPrvi.ploca)
                    self.gadjanaPolja2.append(polje)
                    poljeFR = [ string for string in self.igracPrvi.ploca if polje in string ]
                    for ele in poljeFR:
                        if 'm' in ele:
                            print(igrac.ime+' je pogodilo vas mali brod.')
                            self.pogodjenaPoljaR.append(ele)
                            self.mali_c+=1
                            if self.mali_c ==2:
                                print(igrac.ime+' je potopio vas mali brod!')
                                self.igracPrvi.brodJePotopljen('mali')
                        elif 's' in ele:
                            print(igrac.ime+' je pogodio vas srednji brod.')
                            self.pogodjenaPoljaR.append(ele)
                            self.srednji_c+=1
                            if self.srednji_c ==3:
                                print(igrac.ime+' je potopio vas srednji brod!')
                                self.igracPrvi.brodJePotopljen('srednji')
                        elif 'v' in ele:
                            print(igrac.ime+' je pogodio vas veliki brod.')
                            self.pogodjenaPoljaR.append(ele)
                            self.veliki_c+=1
                            if self.veliki_c ==4:
                                print(igrac.ime+' je potopio vas veliki brod!')
                                self.igracPrvi.brodJePotopljen('veliki')
                        else:
                            print(igrac.ime + ' je promasio!')
                            self.prikaz.ispis_gadjanja(self.default_ploca,self.igracDrugi,self.gadjanaPolja2,self.pogodjenaPoljaR)
                            shot_r = 0
                            break
                    


    def provjeraPobjednika(self):
        if self.igracPrvi.brodoviSuPotopljeni() == 3:
            return self.igracDrugi.ime
        if self.igracDrugi.brodoviSuPotopljeni() == 3:
            return self.igracPrvi.ime
        
        
                    
#instanciranje brodova
def main():
    mali=Brod("mali")
    srednji=Brod("srednji")
    veliki=Brod("veliki")

    p=Prikaz()
    i=Igra(p)
    i.igranje()

main()
