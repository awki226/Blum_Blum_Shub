# Blum-Blum-Shub pseudo
# use python3 BBS.py to run

#finds Frequency of a substring
def Frequency(string, substring): 
    count = 0
    begin = 0
    while begin < len(string): 
        flag = string.find(substring, begin) 
        if flag != -1: 
            begin = flag + 1 
            count += 1
        else: 
            return count

def main():
    x = [] #holds the values before mod 2
    y = [] #holds the lsb
    p = 1000003
    q = 2001911
    m = p * q
    seed = 5 # btw 1-10
    zeroavg = 0
    zeros = 0
    onesavg = 0
    lsb = "" #least sig bit of the BBS
    print ('p = ', p )
    print ('q = ', q )
    print ('m = ', m )
    print ('seed = ', seed)
    
    #intializing x0
    x.append(seed * seed % m)
    y.append(x[0] % 2)
    
    for i in range(100000):
        x.append(x[i-1] * x[i-1] % m) #(x-1)^2 mod m
        y.append(x[i] % 2)
        lsb += str(y[i])
        #print(y[i])
    
    for j in range (0, 99000): #looks through the 10000 bits section
        
        zeroavg += lsb.count("0",j, j +1000)
        zeros += lsb.count("0000",j,j+10000)
        
        onesavg += lsb.count("1",j, j +1000)
    print('The avg number of zeros is: ', zeroavg/100000)
    print('The avg number of ones is:  ', onesavg/100000)
    
    #Finding the frequencies of the substrings 
    
    print('Frequency of 0000: ' , Frequency(lsb,"0000"))
    print('Frequency of 0001: ' , Frequency(lsb,"0001"))
    print('Frequency of 0010: ' , Frequency(lsb,"0010"))
    print('Frequency of 0011: ' , Frequency(lsb,"0011"))
    print('Frequency of 0100: ' , Frequency(lsb,"0100"))
    print('Frequency of 0101: ' , Frequency(lsb,"0101"))
    print('Frequency of 0110: ' , Frequency(lsb,"0110"))
    print('Frequency of 0111: ' , Frequency(lsb,"0111"))
    print('Frequency of 1000: ' , Frequency(lsb,"1000"))
    print('Frequency of 1001: ' , Frequency(lsb,"1001"))
    print('Frequency of 1010: ' , Frequency(lsb,"1010"))
    print('Frequency of 1011: ' , Frequency(lsb,"1011"))
    print('Frequency of 1100: ' , Frequency(lsb,"1100"))
    print('Frequency of 1101: ' , Frequency(lsb,"1101"))
    print('Frequency of 1110: ' , Frequency(lsb,"1110"))
    print('Frequency of 1111: ' , Frequency(lsb,"1111"))
    
    
    
main()
