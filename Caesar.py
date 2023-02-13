def Caesar(Plain,Key): 
    A=[] 
    for i in range(len(Plain)):
        for j in range (26):
            if(Plain[i]==Rule[j]):
                Cal=(j+Key)%26
                A.append(Rule[Cal])
                print(Rule[Cal],end='')
                break
    return A   
Rule='abcdefghijklmnopqrstuvwxyz'
Plain=input("Enter Your Plain Text :")
Key=int(input("Enter the Key Value :"))
Plain=Plain.lower()
print("Caser Encrypted Text is:",end='')
Encry=Caesar(Plain,Key)
print("\nDecrypted Text is :",end='')
Plain=Caesar(Encry,-Key)