import re
from typing import List, Dict

#Whitespace
def whiteSpaceTokenizer(text: str) -> List[str]:
    return text.split()

#Regular expression
def regexTokenizer(text: str) -> List[str]:

    tokenPatterns = [
        r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', 
        r'\b\d{4}-\d{2}-\d{2}\b',         
        r'\b\d+\b',                       
        r'\b\w+\b',                       
        r'[.,!?;]',                       
    ]
    
    combinedPattern = '|'.join(tokenPatterns)
    
    tokens = re.findall(combinedPattern, text)
    
    return tokens

def tokenizeText(text: str) -> Dict[str, List[str]]:

    whiteSpaceTokens = whiteSpaceTokenizer(text)
    
    regexTokens = regexTokenizer(text)
    
    tokens = {
        'whiteSpaceTokens': whiteSpaceTokens,
        'regexTokens': regexTokens,
    }
    
    return tokens

sampleText = "Hej n.azywam sie we]soly romek! mam na przedmiesciu domek 2 3 4 5 a w nim wode prad i gaz zaspiewam wam jeszcze raz! : D"
    
tokens = tokenizeText(sampleText)
print("White Space Tokenizer Output:")
print(tokens['whiteSpaceTokens'])
print("")
print("Regex Tokenizer Output:")
print(tokens['regexTokens'])


#Przepraszam za bardzo prostą formę zadania ale nie miałem w ostatnich tygodniach wiele czasu a nie chciałem nie wysyłać zadania.
#Pozdrawiam

