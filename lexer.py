# Python Lexer created by Conner Forché for Concepts of Programming Languages Class at Seattle Pacific University 2017
import shlex


class LexicalAnalyzer:
    __new_string = ""
    __old_string = None

    def __init__(self, one_line):
        self.__old_string = one_line
    # takes a single lexeme and returns its token
    def sort_it_out(self, info):
        global tokens
        type = ""
        for i in range(0, len(info)):
            add_tokens = 0
            error = True
            temp = info[i]
            partial_string = ''
            if type == "INT":
                if temp[0].isdigit():
                    error = False
                    partial_string = "INT_CONST " + temp + "\n"
                    type = ""
            if type == "REAL":
                if temp[0].isdigit():
                    error = False
                    partial_string = "REAL_CONST " + temp + "\n"
                    type = ""
            if type == "STRING" or temp[0].islower() or temp[0] == " ":
                error = False
                partial_string = "QUOTE\n" + "STRING: " + temp + "\n" + "QUOTE\n"
                add_tokens = 2
                type = ""
            if temp[0].isupper():
                error = False
                partial_string = temp + "\n"
            if temp.endswith('#') or temp.endswith('%') or temp.endswith('$'):
                error = False
                add_tokens = 0
                if temp.endswith('#'):
                    type = "INT"
                if temp.endswith('%'):
                    type = "REAL"
                if temp.endswith('$'):
                    type = "STRING"
                partial_string = "ID " + temp[:-1] + " " + type + "\n"
            special_tokens = [";", "=", "+", "-", "*", "/", "^", "(", ")"]
            if temp[0] in special_tokens:
                error = False
                add_tokens = 0
                if temp[0] == "(":
                    partial_string = "LPAREN\n"
                if temp[0] == ")":
                    partial_string = "RPAREN\n"
                if temp[0] == ";":
                    partial_string = "SEMICOLON \n"
                if temp[0] == "=":
                    partial_string = "ASSIGN \n"
                if temp[0] == "+":
                    partial_string = "ADD \n"
                if temp[0] == "-":
                    partial_string = "SUBTRACT \n"
                if temp[0] == "*":
                    partial_string = "TIMES \n"
                if temp[0] == "/":
                    partial_string = "DIVIDE \n"
                if temp[0] == "^":
                    partial_string = "POWER \n"
            if error is False:
                self.__new_string += partial_string
                tokens += (1 + add_tokens)
            if error:
                self.__new_string += "Error: No token exists for this lexeme \n"
                add_tokens = 0
        return self.__new_string

    def lexer(self):
        data = shlex.split(self.__old_string)
        return self.sort_it_out(data)


file_given = input("Enter your files in this format: \"python lexer.py input.txt\"\n")
file_list = file_given.split()
file_given = file_list[len(file_list)-1]
file_out = file_given[:-3]
file_out = file_out + "out"
output_file = open(file_out, "wb")
tokens = 0
# Opens the test file and inputs line by line into lexer
print("Processing input file " + file_given)
with open(file_given) as test_file:
    for line in test_file:
        solve = LexicalAnalyzer(line)
        output_file.write(bytes(solve.lexer(), 'UTF-8'))
print(str(tokens) + " tokens produced")
print("Result in file " + file_out)
output_file.close()