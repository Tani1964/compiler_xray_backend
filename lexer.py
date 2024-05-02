from tokens import Integer, Float, Operator

# create variableName = value

class Lexer:
    digits = set(["1","2","3","4","5","6","7","8","9"])
    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    operations = set(["/","*","-","+","(",")", "="])
    stopwords = [" "]
    keywords = set("create")

    def __init__(self, text):
        print(text)
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None

    # scanning is taking point
    def tokenize(self):
        # print(type(self.idx), type(len(self.text)))
        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extract_number()
            elif self.char in Lexer.operations:
                self.token = Operator(self.char)
                self.move()
            elif self.char in Lexer.stopwords:
                self.move()
                continue
            elif self.char in Lexer.letters:
                word = self.extract_word()
                
                if word in Lexer.keywords:
                    self.token =  Declaration(word)
                else: 
                    self.token = Variable(word)
                
                
            self.tokens.append(self.token)
        return self.tokens

    def extract_number(self):
        number = ""
        isFloat = False
        while (self.char in Lexer.digits or self.char == ".") and (self.idx < len(self.text)):
            if self.char == ".":
                isFloat = True
            number += self.char
            self.move()
        return Integer(number) if not isFloat else Float(number) 

    def extract_word(self):
        word = ""
        while self.char in Lexer.letters and self.idx < len(self.text):
            word += self.char
            self.move()
        
        return word
            

    def move(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]




# Lexer = Lexer("5 + 3")
# Lexer.tokenize()