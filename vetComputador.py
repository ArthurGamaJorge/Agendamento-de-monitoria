#-------------------------------------------------------#
#         Arthur Gama Jorge - RA: 23578 - 1 Info        #
#      Ion Mateus Nunes Oprea - RA: 23135 - 1 Info      #
#-------------------------------------------------------#

from vetorAbstrato import VetorDados
from computador import Computador

class VetorComputador(VetorDados):       # VetorAluno é uma herança de VetorDados

    def __init__(self, tamanhoFisico : int):
        super().__init__(tamanhoFisico, Computador)
        
        #ordenar
    def ordenar(self):
        for lento in range(0, self._qtosDados, 1):
            for rapido in range(lento+1, self._qtosDados, 1):
                if self._dados[lento].CodMicro > self._dados[rapido].CodMicro:
                    self.trocar(lento, rapido)
                    
    def ordenarPorDescricao(self):
        for lento in range(0, self._qtosDados, 1):
            for rapido in range(lento+1, self._qtosDados, 1):
                if self._dados[lento].Descricao > self._dados[rapido].Descricao:
                    self.trocar(lento, rapido)
                    
    def ordenarPorCondicao(self):
        for lento in range(0, self._qtosDados, 1):
            for rapido in range(lento+1, self._qtosDados, 1):
                if self._dados[lento].PodeUsar < self._dados[rapido].PodeUsar:
                    self.trocar(lento, rapido) 
                elif self._dados[lento].PodeUsar == self._dados[rapido].PodeUsar: # Se houver condições iguais
                    if self._dados[lento].CodMicro > self._dados[rapido].CodMicro: # Ordena por código de computador 
                        self.trocar(lento, rapido)    

    def busca(self, codigoProcurado) -> bool: #buscar por RA
        achou = False
        inicio = 0
        fim = self._qtosDados - 1
        while not achou and inicio <= fim:
            self._posicaoAtual = (inicio + fim) // 2     # posição média do trecho em pesquisa
            if self._dados[self._posicaoAtual].CodMicro == codigoProcurado:
                achou = True
            elif codigoProcurado < self._dados[self._posicaoAtual].CodMicro:
                fim = self._posicaoAtual - 1
            else:
                inicio = self._posicaoAtual + 1
                
        if not achou:   # vamos indicar onde deveria estar para manter ordenado
            self._posicaoAtual = inicio     # posição onde deveria estar ou ser incluído
              
        return achou