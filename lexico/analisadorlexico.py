#import ply as lex
from ply import lex
import re
import codecs
import os
import sys

tokens = ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
          'ODD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE',
          'LPARENT', 'RPARENT', 'COMMA', 'SEMMICOLOM',
          'DOT', 'UPDATE'
]
reservadas = {
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'while': 'WHILE',
    'do': 'DO',
    'call': 'CALL',
    'int': 'INT',
    'procedure': 'PROCEDURE',
    'out': 'OUT',
    'in': 'IN',
    'else': 'ELSE'
}

tokens = tokens + list(reservadas.values())

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*' #ANALIZAR
t_DIVIDE = r'/' #ANALIZAR
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';' #ANALIZAR
t_DOT = r'\.'
t_UPDATE = r':='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print('Caracter ilegal {}'.format(t.value[0]))
    t.lexer.skip(1)

def buscarFicheiros(diretorio):
    ficheiros = []
    numArquivo = ''
    resposta = False
    cont = 1

    for base, dirs, files in os.walk(diretorio):
        ficheiros.append(files)

    for file in files:
        print('{}. {}'.format(cont, file))
        cont += 1

    while resposta == False:
        numArquivo = input('\nNúmero de teste: ')
        for file in files:
            if file == files[int(numArquivo) - 1]:
                resposta = True
                break
    print('O escolhido "{}" \n'.format((files[int(numArquivo) - 1])))

    return (files[int(numArquivo) - 1])

diretorio = 'teste/'
arquivo = buscarFicheiros(diretorio)
teste = diretorio+arquivo


fp = codecs.open(teste, 'r', 'utf-8')
cadena = fp.read()
fp.close()

analisador = lex.lex()

analisador.input(cadena)

while True:
    tok = analisador.token()
    if not tok:
        break
    #print(tok)
    print('{:12}{:^12}{:^12}{:^12}'.format(tok.type, tok.value, tok.lineno, tok.lexpos))