class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]

    def factor(self):
        if self.token.type == "INT" or self.token.type == "FLOAT":
            return self.token
        elif self.token.value == "(":
            self.move()
            expression = self.expression()
            return expression
        
    def term(self):
        left_node = self.factor()
        self.move()
        output = left_node
        while self.token.value in "*/":
            operator = self.token
            self.move()
            right_node = self.factor()
            self.move()

            output = [left_node, operator, right_node]

        return output
    
    def expression(self):
        # 3 + 4 + 5
        left_node = self.term()
        output = left_node
        while self.token.value in "+-":
            operator = self.token
            self.move()
            right_node = self.term()
            output = [output, operator, right_node]

        return output
        
    def parse(self):
        return self.expression()

    def move(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]