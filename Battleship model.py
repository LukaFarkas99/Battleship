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

    def __init__(self, ime):
        self.__ime = ime
        self.__brodoviZaPostavljanje = [ ]
        self.__brodoviPotopljeni = [ ]

    @property
    def ime(self):
        return self.__ime

    @property
    def brodoviZaPostavljanje(self):
        return self.__brodoviZaPostavljanje
    @brodoviZaPostavljanje.setter
    def brodoviZaPostavljanje(self,value):
        self.__brodoviZaPostavljanje = value

    def imaBrodovaZaPostavljanje(self):
        return len(self.__brodoviZaPostavljanje) > 0

    def __str__(self):
        return "Igrac " + self.__ime

    def brodZaPostaviti(self, izbor):
        brod = self.__brodoviZaPostavljanje.pop(izbor)
        return brod

    #nisam siguran ovdje za  da li stavit value il nesto drugo, ali uglavnom prima naziv potopljenog broda
    def brodJePotopljen(self, naziv):
        self.__brodoviPotopljeni = naziv

 class Covjek(Igrac):

    def __init__(self, ime):
        super(Covjek, self).__init__(ime)

class Racunalo(Igrac):

    def __init__(self):
        super(Racunalo, self).__init__('GLaDOS')
        
class PrikazIgre(object):

    def prikaziPocetakIgre(self):
        print("#"*50)
        print("#"*20 +"BATTLESHIP" + "#"*20)
        print("#"*50)

    def unesiIgraca(self):
        while True:
            ime = input("Unesi igraca ")
            if ime.strip():
                print("#"*50)
                return ime.strip()
