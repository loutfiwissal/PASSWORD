# function to count the number of lowercase in the password
def NDCmin (P) :
    N=0
    for i in P :
        if i >= "a" and i <= "z" :
            N += 1
    return N


#function to count the number of uppercase in the password
def NDCmaj (P) :
    N=0
    for i in P :
        if i >= "A" and i <= "Z" :
            N += 1
    return N


#function to count the number of non-alphabetic characters in the password
def NDCALPH (P) :
    return len(password) - NDCmin(password) - NDCmaj(password)


#fuction to find the longest consecutive sequence of uppercase letters
def LongMaj (P) :
    max_langht2 = 0
    current_sequence2 = 0

    for i in range (len(P)):
        if P[i] >= "A" and P[i] <= "Z" :
            current_sequence2 += 1
        else :
            current_sequence2 = 0
        if max_langht2 < current_sequence2 :
            max_langht2 = current_sequence2
    return max_langht2


#fuction to find the longest consecutive sequence of lowercase letters
def LongMin (P) :
    min_langht1 = 0
    current_sequence1 = 0

    for i in range (len(P)):
        if P[i] >= "a" and P[i]<= "z" :
            current_sequence1 += 1
        else :
            current_sequence1 = 0
        if min_langht1 < current_sequence1 :
            min_langht1 = current_sequence1
    return min_langht1
    

#fuction to calculat the password scor 
def score (P) :
    NTotal = len(P)
    bonuse = (NTotal*4) + (NTotal - NDCmaj(P))*2 + (NTotal - NDCmin(P))*3 + NDCALPH (P) * 5
    malus = ( LongMaj(P) * 2 ) + (LongMin(P) * 2)
    
    return bonuse - malus

# Get user input for the password
password = input (" enter a password: ")

print("The number of characters in this password is:", len(password))
print("The number of lowercase characters in this password is:", NDCmin(password))
print("The number of uppercase characters in this password is:", NDCmaj(password))
print("The number of non-alphabetic characters in this password is:", NDCALPH(password))
print("The longest uppercase sequence is:", LongMaj(password))
print("The longest lowercase sequence is:", LongMin(password))


# Calculate and display the password score and strength assessment
print("The score is:", score(password))
if score(password) < 20:
    print("The password is very weak")
elif score(password) >= 20 and score(password) < 40 :
    print("The password is weak")
elif score(password) >= 40 and score(password) <= 80 :
    print("The password is strong")
else:
    print("The password is very strong")