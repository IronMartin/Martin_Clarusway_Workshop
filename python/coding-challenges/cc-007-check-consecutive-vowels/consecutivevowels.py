
text = (input("Please enter a string : ").lower())
vowels = "a,e,i,u,o" 
if len(text) <= 1:
    result = "Negative"
else:
    for i in range(len(text)-1):
        if text[i] in vowels and (text[i+1] in vowels):
            result = "Positive"
            break
        else:
            result = "Negative"
print(result)