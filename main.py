@@ -1,23 +1,33 @@
import sys


class Umjunsik:
    def __init__(self):
        self.data = [0]*256

    def toNumber(self, code):
        return eval('*'.join(list(map(lambda cmd:str((self.data[cmd.count('어')-1] if cmd.count('어') else 0) + cmd.count('.') - cmd.count(',')), code.split(' ')))))

    def type(self, code):
        if '멸치' in code: return 'IF'
        if '훈' in code: return 'MOVE'
        if '화이팅!' in code: return 'END'
        if '희' in code and '?' in code: return 'INPUT'
        if '희' in code and '!' in code: return 'PRINT'
        if '희' in code and 'ㅋ' in code: return 'PRINTASCII'
        if '김' in code: return 'DEF'
    @staticmethod
    def type(code):
        if '멸치' in code:
            return 'IF'
        if '훈' in code:
            return 'MOVE'
        if '화이팅!' in code:
            return 'END'
        if '희' in code and '?' in code:
            return 'INPUT'
        if '희' in code and '!' in code:
            return 'PRINT'
        if '희' in code and 'ㅋ' in code:
            return 'PRINTASCII'
        if '김' in code:
            return 'DEF'

    def compileLine(self, code):
        if code == '': return None
        if code == '':
            return None
        TYPE = self.type(code)

        if TYPE == 'DEF':
@@ -35,7 +45,8 @@ def compileLine(self, code):
            print(chr(value) if value else '\n', end='')
        elif TYPE == 'IF':
            cond, cmd = code.replace('멸치', '').split('?')
            if self.toNumber(cond) == 0: return cmd
            if self.toNumber(cond) == 0:
                return cmd
        elif TYPE == 'MOVE':
            return self.toNumber(code.replace('훈', ''))

@@ -44,7 +55,7 @@ def compile(self, code, check=True, errors=100000):
        recode = ''
        spliter = '\n' if '\n' in code else '~'
        code = code.rstrip().split(spliter)
        if check and (code[0].replace(" ","") != '어떻게' or code[-1] != '이 사람이름이냐!' or not code[0].startswith('어떻게') ) :
        if check and (code[0].replace(" ","") != '어떻게' or code[-1] != '이 사람이름이냐ㅋㅋ' or not code[0].startswith('어떻게')):
            raise SyntaxError('어떻게 이게 훈행이냐!')
        index = 0
        error = 0
@@ -55,11 +66,12 @@ def compile(self, code, check=True, errors=100000):
            if jun:
                jun = False
                code[index] = recode
            if isinstance(res, int): index = res-2
            if isinstance(res, int):
                index = res-2
            if isinstance(res, str):
                recode = code[index]
                code[index] = res
                index -=1
                index -= 1
                jun = True

            index += 1
            error += 1
            if error == errors:
                raise RecursionError(str(errorline+1) + '번째 줄에서 무한 루프가 감지되었습니다.')
    def compilePath(self, path):
        with open(path) as file:
            code = ''.join(file.readlines())
            self.compile(code)