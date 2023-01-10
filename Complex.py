import os
os.system('cls')
class Complex:
    def __init__(self,re,im):
        self.__re = re
        self.__im = im
    def get_re(self):
        return self.__re
    def set_re(self,valeur):
        self.__re=valeur
    def get_im(self):
        return self.__im
    def set_im(self,valeur):
        self.im=valeur
    Re=property(get_re,set_re)
    Im=property(get_im,set_im)
    def __str__(self):
        if self.__re == 0:
            s = "%.2fi"%(self.__im)
        elif self.__im == 0:
            s = "%.2f"%(self.__re)
        elif self.__im >self.__re:
            s = "%.2f - %.2fi"%(self.__re,self.__im)
        else:
            s = "%.2f + %.2fi"%(self.__re,self.__im)
        return s
    def __add__(self,z):
        re=self.__re+z.__re
        im=self.__im+z.__im
        c=complex(re,im)
        return c
    def __sup__(self,z):
        re=self.__re+z.__re
        im=self.__im+z.__im
        c=complex(re,im)
        return c
    def __mul__(self,z):
        re=self.__re+z.__re
        im=self.__im+z.__im
        c=complex(re,im)
        return c
    def __div__(self,z):
        re=self.__re+z.__re
        im=self.__im+z.__im
        c=complex(re,im)
        return c
c1 = Complex(7,5)
c2 = Complex(-2,5)
print(c1)