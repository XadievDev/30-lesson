#XadievDev
#30-lesson.Vorislik va Polimorfizm

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"Passport:{self.passport},{self.tyil}-yil."
        return info
    
    def get_age(self,yil):
        """Shaxs yoshi"""
        age = yil - self.tyil
        return age


inson = Shaxs('Amirbek','Xadiev','FB00011122',2006)

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil,fanlar):
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = fanlar
    
    def get_id(self):
        """Talaba idraqamini qaytaradi"""
        return self.idraqam

    def get_bosqich(self):
        """Talaba bosqichini qaytaradi"""
        return self.bosqich

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"Passport:'{self.passport}',{self.tyil}-yil.ID raqam:'{self.idraqam}'"
        return info
    
    def fanga_yozil(self,):



class Manzil():
    """Manzilni saqlash uchun klass"""
    def __init__(self,uy,kocha,shahar,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.shahar = shahar
        self.viloyat = viloyat

    def get_manzil(self):
        manzil = f"{self.uy}-uy.{self.kocha.title()} ko'cha. {self.shahar.title()} shahar.{self.viloyat.title()} viloyati."
        return manzil
    
talaba1_manzil = Manzil(43,'osiyo','kogon','buxoro')
talaba1 = Talaba('Alisher','Xadiev','FF123456',1998,'N00000001',talaba1_manzil)


class Fanlar():
    def __init__(self,math,bio,art,prog,eng):
        self.math = math
        self.bio = bio
        self.art = art
        self.prog = prog
        self.eng = eng
    

