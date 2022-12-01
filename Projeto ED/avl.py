# http://10.0.61.81:9000/
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    Árvore AVL em Python
    
    Copyright (c) 2009 Vindemiatrix Almuredin.
    É dada permissão para copiar, distribuir e/ou modificar este documento
    sob os termos da Licença de Documentação FAIL,
    Versão 97.545.668.112.666.002 Build 69 Release 42;
    Uma cópia da licença talvez esteja inclusa na seção entitulada
    "Licença de Documentação FAIL".
"""

class No:
    def __init__(self, data):
        self.data = data
        self.setaFilhos(None, None)

    def setaFilhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def balanco(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def rotacaoEsquerda(self):
        self.data, self.direita.data = self.direita.data, self.data
        t1 = self.esquerda #T1
        t2 = self.direita.esquerda
        t3 = self.direita.direita
        self.setaFilhos(esquerda=self.direita, direita=t3)
        self.esquerda.setaFilhos(t1, t2)

    def rotacaoDireita(self):
        self.data, self.esquerda.data = self.esquerda.data, self.data
        t3 = self.direita 
        t1 = self.esquerda.esquerda
        t2 = self.esquerda.direita
        self.setaFilhos(t1, self.esquerda)
        self.direita.setaFilhos(t2, t3)

    def rotacaoEsquerdaDireita(self):
        self.esquerda.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self.direita.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.esquerda.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.direita.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def insere(self, data):
        if data <= self.data:
            if not self.esquerda:
                self.esquerda = No(data)
            else:
                self.esquerda.insere(data)
        else:
            if not self.direita:
                self.direita = No(data)
            else:
                self.direita.insere(data)
        self.executaBalanco()

    def imprimeArvore(self, indent = 0):
        if self.esquerda:
            self.esquerda.imprimeArvore(indent + 2)
        print(" " * indent + str(self.data))
        if self.direita:
            self.direita.imprimeArvore(indent + 2)
