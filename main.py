# lexer file lexer/program.txt
# lexer dir lexer/Tests
# parser file parser_expression/program.txt
# parser dir parser_expression/Tests
import sys  # чтение консоли
import os  # работа с путями к файлам\папкам
from lexer.lexer import Lexer
from error import CompilerError
from parser_expression.parser_expression import ParserExpression

console = sys.argv[1:]
type_analize = ''
type_read = ''
path = ''

for el in console:
    if el == 'lexer' or el == 'parser':
        type_analize = el
    elif el == 'file' or el == 'dir':
        type_read = el
    elif os.path.isfile(el) or os.path.isdir(el):
        path = el

if type_analize == 'lexer':
    if type_read == 'file':
        if os.path.isfile(path):
            try:
                lexer = Lexer(path)
                lexem = lexer.next_lexem()
                if not lexem.is_end():
                    print(lexem.to_string())

                while not lexem.is_end():
                    lexem = lexer.next_lexem()
                    if not lexem.is_end():
                        print(lexem.to_string())
            except CompilerError as error:
                print(error)

    if type_read == 'dir':
        if os.path.isdir(path):
            count_all = 0
            count_passed = 0
            for file in os.listdir(path):
                if file.endswith('(code).txt'):
                    count_all += 1
                    abspath = path + '/' + file
                    output = abspath.replace('(code)', '(output)')
                    answer = abspath.replace('(code)', '')
                    file_output = open(output, 'w+')
                    file_output.seek(0)
                    file_answer = open(answer, 'r').read()
                    try:
                        lexer = Lexer(abspath)
                        lexem = lexer.next_lexem()
                        if not lexem.is_end():
                            file_output.write(lexem.to_string())

                        while not lexem.is_end():
                            lexem = lexer.next_lexem()
                            if not lexem.is_end():
                                file_output.write('\n' + lexem.to_string())

                    except CompilerError as error:
                        if file_output.tell() != 0:
                            file_output.write('\n' + str(error))
                        else:
                            file_output.write(str(error))

                    finally:
                        file_output.close()
                        file_output = open(output, 'r').read()
                        if file_output != file_answer:
                            print(f'{file} - не пройден')
                        else:
                            print(f'{file} - пройден')
                            count_passed += 1

if type_analize == 'parser':
    if type_read == 'file':
        if os.path.isfile(path):
            try:
                lexer = Lexer(path)
                lexer.next_lexem()
                parser = ParserExpression(lexer).expr()
                print(parser.to_string())
            except CompilerError as error:
                print(error)

    elif type_read == 'dir':
        if os.path.isdir(path):
            count_all = 0
            count_passed = 0
            for file in os.listdir(path):
                if file.endswith('(code).txt'):
                    count_all += 1
                    abspath = path + '/' + file
                    output = abspath.replace('(code)', '(output)')
                    answer = abspath.replace('(code)', '')
                    file_output = open(output, 'w+')
                    file_output.seek(0)
                    file_answer = open(answer, 'r').read()
                    try:
                        lexer = Lexer(abspath)
                        lexer.next_lexem()
                        parser = ParserExpression(lexer).expr()
                        file_output.write(parser.to_string())

                    except CompilerError as error:
                        file_output.write(str(error))

                    finally:
                        file_output.close()
                        file_output = open(output, 'r').read()
                        if file_output != file_answer:
                            print(f'{file} - не пройден')
                        else:
                            print(f'{file} - пройден')
                            count_passed += 1
