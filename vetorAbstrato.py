#-------------------------------------------------------#
#         Arthur Gama Jorge - RA: 23578 - 1 Info        #
#      Ion Mateus Nunes Oprea - RA: 23135 - 1 Info      #
#-------------------------------------------------------#

from PySide6.QtWidgets import QListView, QTableView, QTextEdit, QComboBox, QListWidgetItem
from abc import ABCMeta, abstractmethod
from enum import Enum

class Situacao(Enum): 
    # atribui valores de 0 a 4 para os itens 
    navegando, incluindo, editando, buscando, excluindo = range(0, 5)

class VetorDados:   # é a classe abstrata ancestral (superior) das classes derivadas
    
    def __init__(self, tamanhoFisico : int, Classe):
        self._dados = [None]*tamanhoFisico   # vetor sem objetos instanciados
        self._qtosDados = 0                  # tamanho lógico, nenhuma usada
        self._posicaoAtual = 0               # índice do elemento visitado
        self._situacao = Situacao.navegando  # o que o programa faz agora
        self._Classe = Classe                # classe específica que será mantida no vetor

    @property 
    def tamanho(self): 
        return self._qtosDados 
    
    @property 
    def posicaoAtual(self): 
        return self._posicaoAtual 
    
    @posicaoAtual.setter 
    def posicaoAtual(self, novoValor): 
        if novoValor < 0 or novoValor >= self._qtosDados: 
            raise IndexError("Posição inválida para acesso a dados.") 
        self._posicaoAtual = novoValor
        
    @property 
    def situacao(self): 
        return self._situacao 
    
    @situacao.setter
    def situacao(self, novoValor): 
        if type(novoValor) is Situacao: 
            self._situacao = novoValor 
        else: 
            raise Exception("Situação inválida!")
        
    @property 
    def estaVazio(self) -> bool: 
        return self._qtosDados == 0
    
    @property 
    def estaNoInicio(self) ->bool: 
        return self._posicaoAtual == 0 
    
    @property 
    def estaNoFim(self) -> bool: 
        return self._posicaoAtual >= self._qtosDados - 1 
    
    def irAoInicio(self): 
        self._posicaoAtual = 0   # índice do primeiro 
        
    def irAoFim(self): 
        self._posicaoAtual = self._qtosDados - 1   # índice do último 
        
    def irAoAnterior(self): 
        if not self.estaNoInicio: 
            self._posicaoAtual -= 1   # retrocede índice 
            
    def irAoProximo(self): 
        if not self.estaNoFim: 
            self._posicaoAtual += 1   # avança índice
    
    def leituraDosDados(self, nomeArquivo): 
        arqDados = open(nomeArquivo, "r") 
        self._qtosDados = 0 
        haRegistros = True 
        while haRegistros: 
            dadoLido = self._Classe()   # cria (instancia) objeto da classe específica
            haRegistros = dadoLido.leuRegistro(arqDados) 
            if haRegistros: 
                self.incluirNoFinal(dadoLido) 
        
        arqDados.close()   

    def gravarDados(self, nomeArquivo):
        arqDados = open(nomeArquivo, "w")    # "w" --> arquivo para escrita é limpo
        
        for indice in range(0, self._qtosDados, 1):
            self._dados[indice].escreverRegistro(arqDados)
            
        arqDados.close()  # nunca esqueça de fechar os arquivos após usar 

    def incluirNoFinal(self, novoDado): 
        if self._qtosDados >= len(self._dados):     # vetor cheio
            raise Exception("Área de armazenamento cheia!")
        
        self._dados[self._qtosDados] = novoDado  # guarda novo registro no fim do vetor
        self._qtosDados += 1                     # temos um registro a mais 
                                                 # (tamanho lógico é incrementado)

    def incluirEm(self, novoValor, posicaoDeInclusao: int): 
        if self._qtosDados >= len(self._dados): 
            raise IndexError("Espaço de armazenamento insuficente!"); 
        indice = self._qtosDados 
        while indice > posicaoDeInclusao: 
            self._dados[indice] = self._dados[indice - 1] 
            indice -= 1 
        
        self._dados[posicaoDeInclusao] = novoValor 
        self._qtosDados += 1
    
    def excluir(self, posicao : int): 
        if posicao < 0 or posicao >= self._qtosDados :
            raise IndexError("Posição inválida para acesso aos dados!")
        
        self._qtosDados -= 1
        for indice in range(posicao, self._qtosDados, 1): 
            self._dados[indice] = self._dados[indice+1]

        self._dados[self._qtosDados] = None
        
    def valorDe(self, indice : int): 
        if indice >= 0 and indice < self._qtosDados: 
            return self._dados[indice] 
        
        raise IndexError("Índice inválido!") 
    
    def alterar(self, posicao : int, novoDado ): 
        if posicao >= 0 and posicao < self._qtosDados: 
            self._dados[posicao] = novoDado 
        
        raise IndexError("Posição inválida para alteração!") 
    
    def trocar(self, origem, destino):
        aux = self._dados[origem]
        self._dados[origem] = self._dados[destino]
        self._dados[destino] = aux
    
    def exibir(self): 
        for indice in range(0, self._qtosDados,1): 
            print(self._dados[indice]) 
            
    def exibirLista(self, lista : QListView): 
        lista.removeRows(0, lista.rowCount())   # limpa os itens desse controle
        for indice in range(0, self._qtosDados,1): 
            item = QListWidgetItem(self._dados[indice])
            lista.addItem(item) 
                
    def exibirCombo(self, lista : QComboBox): 
        lista.clear() 
        for indice in range(0, self._qtosDados,1): 
            lista.addItem(self._dados[indice])

    def exibirTexto(self, texto : QTextEdit): 
        pass

    @abstractmethod     # deverá ser implementado em uma classe derivada
    def ordenar(self):
        pass

    @abstractmethod     # deverá ser implementado em uma classe derivada
    def busca(self, codigoProcurado) -> bool:
        pass
    
    @abstractmethod     # deverá ser implementado em uma classe derivada
    def exibirGrade(self, grade: QTableView): 
        pass 


