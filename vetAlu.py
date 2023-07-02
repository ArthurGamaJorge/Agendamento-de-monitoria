#-------------------------------------------------------#
#         Arthur Gama Jorge - RA: 23578 - 1 Info        #
#      Ion Mateus Nunes Oprea - RA: 23135 - 1 Info      #
#-------------------------------------------------------#

from vetorAbstrato import VetorDados
from alu import Aluno
from PySide6.QtWidgets import QTableView

class VetorAluno(VetorDados):       # VetorAluno é uma herança de VetorDados

    def __init__(self, tamanhoFisico : int):
        super().__init__(tamanhoFisico, Aluno)
        
    def ordenar(self):   #ordenar
        for lento in range(0, self._qtosDados, 1):
            for rapido in range(lento+1, self._qtosDados, 1):
                if self._dados[lento].ra > self._dados[rapido].ra:
                    self.trocar(lento, rapido)
                    
    def ordenarPorNome(self):
        for lento in range(0, self._qtosDados, 1):
            for rapido in range(lento+1, self._qtosDados, 1):
                if self._dados[lento].nome > self._dados[rapido].nome:
                    self.trocar(lento, rapido)
                    
    def ordenarPorCurso(self):
        for lento in range(0, self._qtosDados, 1):
            for rapido in range(lento+1, self._qtosDados, 1):
                if self._dados[lento].curso > self._dados[rapido].curso:
                    self.trocar(lento, rapido) 
                elif self._dados[lento].curso == self._dados[rapido].curso: # cursos iguais
                    if self._dados[lento].nome > self._dados[rapido].nome:  # ordena por nome
                        self.trocar(lento, rapido)    

    def busca(self, codigoProcurado) -> bool: #busca por RA
        achou = False
        inicio = 0
        fim = self._qtosDados - 1
        while not achou and inicio <= fim:
            self._posicaoAtual = (inicio + fim) // 2     # posição média do trecho em pesquisa
            if self._dados[self._posicaoAtual].ra == codigoProcurado:
                achou = True
            elif codigoProcurado < self._dados[self._posicaoAtual].ra:
                fim = self._posicaoAtual - 1
            else:
                inicio = self._posicaoAtual + 1
                
        if not achou:   # vamos indicar onde deveria estar para manter ordenado
            self._posicaoAtual = inicio     # posição onde deveria estar ou ser incluído
              
        return achou
    