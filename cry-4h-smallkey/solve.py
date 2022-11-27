def int_to_str(a):
    res = ""
    while a > 0:
        res =  chr(a%256) + res # chr() - функция, сопоставляющая числу символ из таблицы ASCII
        a = a // 256
    return res 

def find_invpow(x,n):# можно отыскать на просторах интернета 
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

def Discriminant(a,b):
    D = b**2 - 4*a
    sqrt_D = find_invpow(D,2)
    return sqrt_D,D


enc_flag = 102475614332391158696292668196677454327575013110816235691433575169808787996308419611246869307143895936906425853672255268421034524411417182626002685228545126
a = 9034793510905756932433184816289116901151996037480760280519980068848096171863474584355252956304710637
# x^2 + a*x + (k - y) = 0

for k in range(1,10**5):
    sqrt_D , D = Discriminant(k - enc_flag,a)
    if D == sqrt_D**2 :
        print("key = ",k)
        flag_int = (sqrt_D - a) // 2
        print("flag: "+ int_to_str(flag_int))
        break
