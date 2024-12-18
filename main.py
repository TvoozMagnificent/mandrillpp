
from sys import argv as a

def indent(string): return '\n'.join('| ' + line for line in str(string).split('\n'))
lookup = {
    'neg': lambda a: -a,
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
    '%': lambda a, b: a % b,
    '<': lambda a, b: 1 if a < b else 0,
    '>': lambda a, b: 1 if a > b else 0,
    '==': lambda a, b: 1 if a == b else 0,
    '!=': lambda a, b: 1 if a != b else 0,
    '<=': lambda a, b: 1 if a <= b else 0,
    '>=': lambda a, b: 1 if a >= b else 0,
    '&&': lambda a, b: 1 if a and b else 0,
    '||': lambda a, b: 1 if a or b else 0,
    '!': lambda a, b: 1 if not a else 0,
    '?': lambda a, b, c: b if a else c,
}

class Token:
    def __init__(self, type, value=None): self.type = type; self.value = value
    def __repr__(self): return f'Token({self.type}, {self.value})'
    def __eq__(self, other): return self.type == other.type and self.value == other.value
class Tokenizer:
    def __init__(self, program): self.program = program; self.current = 0; self.tokens = []
    def get(self): character = self.program[self.current]; self.current += 1; return character
    def peek(self): return self.program[self.current] if self.current < len(self.program) else None
    def peek_next(self): return self.program[self.current+1] if self.current+1 < len(self.program) else None
    def consume(self, token):
        assert token == self.peek()
        return self.get()
    def get_token(self):
        current = self.peek()
        if current is None: return Token('EOF')
        if current in '+-' and self.peek_next() == current: return Token(self.consume(current) + self.consume(current))
        if current.isdigit(): return Token('nm', int(self.match('0123456789')))
        if current in 'abcdefghijklmnopqrstuvwxyz_': return Token('id', self.match('abcdefghijklmnopqrstuvwxyz_'))
        if current in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_': return Token('pr', self.match('ABCDEFGHIJKLMNOPQRSTUVWXYZ_'))
        if current in '+-*/%<=>!': return self.match_operator()
        if current in '(){}@?:;': return Token(self.consume(current))
        if current in '&|': return Token(self.consume(self.consume(current)) * 2)
        if current == '\\': self.get(); self.match_comment(); return self.get_token()
        if current == "'": self.get(); char = self.match_char(); self.consume("'"); return Token('nm', ord(char))
        self.get(); return self.get_token()
    def match(self, charset):
        match = ''
        while self.peek() in charset: match += self.get()
        return match
    def match_operator(self): base = self.get(); return Token(base + self.get() if self.peek() == '=' else base)
    def match_comment(self):
        while self.get() != '\\': pass
    def match_char(self):
        if self.peek() == '\\': self.get(); return {'n': '\n', '\\': '\\', "'": "'"}[self.get()]
        return self.get()
    def tokenize(self):
        while (token := self.get_token()).type != 'EOF': self.tokens.append(token)
        return self.tokens

class Block:
    def __init__(self, children): self.children = children
    def __repr__(self): return f'Block(\n{("," + chr(10)).join(indent(child) for child in self.children)}\n)'
    def execute(self, env):
        for child in self.children: child.execute(env)
class Assignment:
    def __init__(self, var, expression): self.var = var; self.expression = expression
    def __repr__(self): return f'Assignment(\n{indent(self.var)},\n{indent(self.expression)}\n)'
    def execute(self, env):
        l = self.var.name(env)
        if l == 'write': print(self.expression.evaluate(env), end=''); return
        if l == 'put': print(chr(self.expression.evaluate(env)), end=''); return
        env[l] = self.expression.evaluate(env)
class If:
    def __init__(self, condition, t, f): self.condition = condition; self.t = t; self.f = f;
    def __repr__(self): return f'If(\n{indent(self.condition)},\n{indent(self.t)},\n{indent(self.f)})'
    def execute(self, env): (self.t if self.condition.evaluate(env) != 0 else self.f).execute(env)
class While:
    def __init__(self, condition, block): self.condition = condition; self.block = block
    def __repr__(self): return f'While(\n{indent(self.condition)},\n{indent(self.block)})'
    def execute(self, env):
        while self.condition.evaluate(env) != 0: self.block.execute(env)
class Expr:
    def __init__(self, symb, *args): self.args = args; self.fn = lookup[symb] if symb in lookup else lambda: symb; self.symb = symb
    def __repr__(self): return f'Expr(\n{indent(self.symb)},\n{("," + chr(10)).join(indent(arg) for arg in self.args) if self.args else None}\n)'
    def evaluate(self, env): return self.fn(*(arg.evaluate(env) for arg in self.args))
class Ref:
    def __init__(self, var, id): self.var = var; self.id = id;
    def __repr__(self): return f'Ref(\n{indent(self.var)},\n{indent(self.id)}\n)'
    def evaluate(self, env): _ = self.name(env); return env[_] if _ in env else 0
    def name(self, env): return self.var.name(env) + '.' + str(self.id.evaluate(env))
class Var:
    text = ''
    def __init__(self, name): self._ = name
    def __repr__(self): return f'Var({self._})'
    def evaluate(self, env):
        if self._ == 'read':
            try:
                while not Var.text: Var.text = input()
            except: return 0
            assert Var.text[0] in '-1234567890'
            k = 1
            while k < len(Var.text) and Var.text[k] in '1234567890': k += 1
            num = int(Var.text[:k])
            Var.text = Var.text[k:]
            if Var.text and Var.text[0] == ' ': Var.text = Var.text[1:]
            return num
        if self._ == 'get':
            try:
                while not Var.text: Var.text = input()
            except: return 0
            num = ord(Var.text[0])
            Var.text = Var.text[1:]
            return num
        return env[self._] if self._ in env else 0
    def name(self, env): return self._
class Parser:
    def __init__(self, tokens): self.tokens = tokens; self.current = 0; self.pr = {}
    def get(self): token = self.tokens[self.current]; self.current += 1; return token
    def peek(self): return self.tokens[self.current] if self.current < len(self.tokens) else Token('EOF', None)
    def peeknext(self): return self.tokens[self.current+1] if self.current+1 < len(self.tokens) else Token('EOF', None)
    def consume(self, token): assert token == self.peek(); return self.get()
    def parse(self):
        while self.peek().type != 'EOF': self.parse_procedure()
        return self.pr
    def parse_procedure(self):
        name = self.peek();
        if name.type == 'pr' and self.peeknext().type == ':': self.get(); self.consume(Token(':')); self.pr[name.value] = self.parse_stmt()
        else: self.pr['MAIN'] = self.parse_block()
    def parse_block(self):
        children = []
        while self.peek().type not in ['}', 'EOF']: children.append(self.parse_stmt())
        if self.peek().type == '}': self.consume(Token('}'))
        return Block(children)
    def parse_stmt(self):
        current = self.peek()
        if current.type == 'pr': self.get(); self.consume(Token(';')); return self.pr[current.value]
        if current.type == '{': self.get(); return self.parse_block()
        assert current.type == 'id'
        if current.value == 'if':
            self.get(); self.consume(Token('(')); cond = self.parse_expr(); self.consume(Token(')')); t = self.parse_stmt(); f=Block([])
            if self.peek().value == 'else': self.consume(Token('id', 'else')); f = self.parse_stmt()
            return If(cond, t, f)
        if current.value == 'while':
            self.get(); self.consume(Token('(')); c = self.parse_expr(); self.consume(Token(')')); block = self.parse_stmt(); return While(c, block)
        current = self.parse_ref()
        next = self.get()
        if next.type == '=': expr = self.parse_expr(); self.consume(Token(';')); return Assignment(current, expr)
        if next.type in ['++', '--']: self.consume(Token(';')); return Assignment(current, Expr(next.type[0], current, Expr(1)))
        assert next.type[1] == '=' and next.type[0] in '+-*/%'
        expr = self.parse_expr(); self.consume(Token(';')); return Assignment(current, Expr(next.type[0], current, expr))
    def parse_expr(self):
        return self.parse_cond()
    def parse_cond(self):
        r = self.parse_or()
        if self.peek().type == '?':
            self.consume(Token('?')); t = self.parse_cond(); self.consume(Token(':')); f = self.parse_cond(); r = Expr('?', r, t, f)
        return r
    def parse_or(self):
        r = self.parse_and()
        if self.peek().type == '||': return Expr(self.get().type, r, self.parse_or())
        return r
    def parse_and(self):
        r = self.parse_ncomp()
        if self.peek().type == '&&': return Expr(self.get().type, r, self.parse_and())
        return r
    def parse_ncomp(self):
        if self.peek().type == '!': return Expr(self.get().type, self.parse_ncomp())
        return self.parse_comp()
    def parse_comp(self):
        r = self.parse_am()
        if self.peek().type in ['<', '>', '<=', '>=', '==', '!=']: r = Expr(self.get().type, r, self.parse_am())
        return r
    def parse_am(self):
        r = self.parse_md()
        while self.peek().type in ['+', '-']: r = Expr(self.get().type, r, self.parse_md())
        return r
    def parse_md(self):
        r = self.parse_pref()
        while self.peek().type in ['*', '/', '%']: r = Expr(self.get().type, r, self.parse_pref())
        return r
    def parse_pref(self):
        if self.peek().type == 'nm': return Expr(self.get().value)
        if self.peek().type == '(': self.consume(Token('(')); expr = self.parse_expr(); self.consume(Token(')')); return expr
        return self.parse_ref()
    def parse_patom(self):
        if self.peek().type == 'nm': return Expr(self.get().value)
        if self.peek().type == '(': self.consume(Token('(')); expr = self.parse_expr(); self.consume(Token(')')); return expr
        return self.parse_atom()
    def parse_ref(self):
        r = self.parse_atom()
        while self.peek().type == '@': self.consume(Token('@')); r = Ref(r, self.parse_patom())
        return r
    def parse_atom(self): var = self.get(); assert var.type == 'id'; return Var(var.value)

with open(a[1]) as f: program = f.read()
tokens = Tokenizer(program).tokenize()
tree = Parser(tokens).parse()
env = {}
tree['MAIN'].execute(env)
