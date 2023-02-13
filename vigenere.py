def Caesar(Plain,Key,T): 
    A=''
    for i in range(len(Plain)):
        P=-1
        K=-1
        for j in range (26):
            if(Plain[i]==Rule[j]):
                P=j
            if(Key[i]==Rule[j]):
                K=j
            if(P!=-1 and K!=-1):
                break
        if(T==0):
            Cal=(P+K+T)%26
        else:
            Cal=(P-K+T)%26
        A+=Rule[Cal]
    print(A)
    return A   

if __name__ == "__main__":
    Rule='abcdefghijklmnopqrstuvwxyz'
    Plain=input("Enter Your Plain Text :")
    Key=input("Enter the Key Value :")
    Plain=Plain.lower()
    k=0
    while(True):
        if(len(Plain)>len(Key)):
            L=len(Plain)-len(Key)
            if(k<len(Key)):
                Key+=Key[k]
                k+=1
        else:
            break       
    print("Key",Key)
    print("Caser Encrypted Text is:",end='')
    Encry=Caesar(Plain,Key,0)
    print("\nDecrypted Text is :",end='')
    Plain=Caesar(Encry,Key,26)