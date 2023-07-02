#-------------------------------------------------------#
#         Arthur Gama Jorge - RA: 23578 - 1 Info        #
#      Ion Mateus Nunes Oprea - RA: 23135 - 1 Info      #
#-------------------------------------------------------#

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QStatusBar,  QTableWidgetItem, QMessageBox
from PySide6.QtGui import QColor

from FrmReservas_ui import Ui_FrmReservas

from vetComputador import VetorComputador
from matReserva import MatrizReserva
from vetAlu import VetorAluno
from reserva import Reserva

        
class FormPrincipal(QMainWindow, Ui_FrmReservas):

    def __init__(self): 
        
        super().__init__()   # importa das classes ancestrais
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.show()
        
        self.btnAbrir.clicked.connect(self.Abrir)
        self.btnSalvar.clicked.connect(self.Salvar)
        
        #variaveis necessárias
        self.osComputadores = VetorComputador(50)
        self.osAlunos = VetorAluno(50)
        self.asReservas = MatrizReserva(50)
        
        self.matriz = [[]] #com ra ou nao
        
        self.qtosHorarios = 0
        self.qtosComputadores = 0
        
        self.nomesDosComputadores = []
        
        self.colunasNaoUtilizaveis = []
        
        self.grdReserva.cellDoubleClicked.connect(self.limparCelula)
        self.grdReserva.cellChanged.connect(self.testarRA)

        self.horarios = ["7:30", "8:15", "09:00", "10:00","10:45", "11:30", "13:30", "14:15", "15:00","16:00", "16:45","17:30","18:15","19:00", "19:45", "20:30", "21:15", "22:15"]
    
    
    def exibirMensagem(self, titulo : str, mensagem : str, icone) -> bool:     #MessageBox
        msgBox = QMessageBox()
        msgBox.setIcon(icone)
        msgBox.setText(mensagem)
        msgBox.setWindowTitle(titulo)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        return returnValue == QMessageBox.Ok
    
    def limparCelula(self,linha, coluna): #duplo clique limpa a celula
        self.grdReserva.item(linha, coluna).setText("")
        
    def testarRA(self, linha, coluna):
        raAtual = self.grdReserva.item(linha, coluna).text()
        if len(raAtual) >= 5 or len(raAtual) < 5 and len(raAtual) > 0:
            if not self.osAlunos.busca(raAtual):
                self.exibirMensagem("Atenção!", "RA digitado não existe", QMessageBox.Warning)
                self.grdReserva.item(linha, coluna).setText("")
                

    def Abrir(self):
        self.osComputadores.leituraDosDados('computadores.txt')
        self.osAlunos.leituraDosDados('alunos.txt')
        self.asReservas.leituraDosDados('reservas.txt')
        self.AdicionarColunas()
        self.CriarMatriz()
        self.PreencherMatriz()
        self.PreencherMalha()
        self.colunasNaoUtilizaveis = []
        
        for i in range(self.osComputadores.tamanho):  #verfica as colunas dos computadores não-usáveis
            if self.osComputadores.valorDe(i).PodeUsar == False:
                self.colunasNaoUtilizaveis += [i]
        
        for i in range(len(self.colunasNaoUtilizaveis)):   #muda a cor das colunas
            for linha in range(self.grdReserva.rowCount()):
                item = self.grdReserva.item(linha, self.colunasNaoUtilizaveis[i])
                item.setBackground(QColor("red"))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        
    
    def PreencherMatriz(self): #ler reserva e colocar na matriz os ras
        arqReserva = open('reservas.txt',"r")
        reservas = []
        horario = 0
        computador = ""
        
        podeRepetir = True
        while True and podeRepetir == True:  #cria o vetor de reservas
            umaReserva = Reserva()
            if not umaReserva.leuRegistro(arqReserva):
                podeRepetir = False
            if podeRepetir == True:
                reservas += [umaReserva]
    
        for i in range(0,len(reservas),1):    #preenche a matriz
            horario = int(reservas[i].Horario)
            computador = reservas[i].CodMicro
            ra = reservas[i].RA
            
            for j in range(self.osComputadores.tamanho):
                    if self.osComputadores.valorDe(j).CodMicro == computador:
                        coluna = j
              
            self.matriz[horario-1][coluna] = ra

        arqReserva.close()


    def AdicionarColunas(self):   #adiciona as colunas 
        self.grdReserva.setColumnCount(self.osComputadores.tamanho)
        nomesDasColunas = self.ObterNomeDosComputadores()
        self.grdReserva.setHorizontalHeaderLabels(nomesDasColunas)


    def ObterNomeDosComputadores(self):   #obtem o nome de todos os computadores
        self.nomesDosComputadores = []
        tamanho = self.osComputadores.tamanho
        for i in range(0,tamanho):
            computador = self.osComputadores.valorDe(i)
            self.nomesDosComputadores += [computador.CodMicro]
        return self.nomesDosComputadores


    def CriarMatriz(self): #criar matriz com espaços vazios
        self.qtosHorarios = len(self.horarios)
        self.qtosComputadores = len(self.nomesDosComputadores)
        self.matriz = [[""] * self.qtosComputadores for i in range(self.qtosHorarios)]
    
    def PreencherMalha(self):   #colocar os RAs na tabela
        matriz = self.matriz
        dadoAInserir = ""
        
        for i in range(0,self.qtosHorarios):
            for j in range(0,self.qtosComputadores):  
                dadoAInserir = QTableWidgetItem(str(matriz[i][j]))
                self.grdReserva.setItem(i, j, dadoAInserir)
        
        
    def Salvar(self): #salva as alterações
        umaReserva = Reserva()
        arquivoDeSaida = open("reservas.txt", "w")
        raAlunos = []
        
        for i in range(self.osAlunos.tamanho):  #ras dos alunos cadastrados
            raAlunos += [str(self.osAlunos.valorDe(i).ra)]
        
        for linha in range(len(self.horarios)):
            
            rasDaLinha = [] #para verificar repetição de RA

            for i in range(self.osComputadores.tamanho):
                valor = self.grdReserva.item(linha, i).text()
                if valor != "" and valor in raAlunos: # verifica se existe esse aluno
                    if i not in self.colunasNaoUtilizaveis:
                        rasDaLinha += [self.grdReserva.item(linha, i).text()]
                        
            inseriuUmaVez = False
                
            for coluna in range(self.osComputadores.tamanho):  
                valor = self.grdReserva.item(linha, coluna).text()
                if valor != "" and valor in raAlunos: # verifica se existe esse aluno
                    if coluna not in self.colunasNaoUtilizaveis: # verifivca se o computador esta util
                        
                        quantasVezes = 0 #verifica repetições
                        for i in range(len(rasDaLinha)):
                            if valor == rasDaLinha[i]:
                                quantasVezes += 1

                        if quantasVezes == 1 or inseriuUmaVez == False:
                            inseriuUmaVez = True
                            umaReserva.atribuirDados(self.osComputadores.valorDe(coluna).CodMicro,valor,linha+1) 
                            umaReserva.escreverRegistro(arquivoDeSaida)
                            
                        else:
                            self.exibirMensagem("Atenção!", "RA repetido na mesma linha", QMessageBox.Warning)
                       
        arquivoDeSaida.close()  #arquivo desorganizado
        
        #organiza o arquivo
        self.asReservas.leituraDosDados('reservas.txt')
        self.asReservas.ordenar()
        arquivoDeSaida = open("reservas.txt", "w")
                
        
        for i in range(0, self.asReservas.tamanho): #insere organizadamente
            self.ReservaAtual = self.asReservas.valorDe(i)
            umaReserva.atribuirDados(self.ReservaAtual.CodMicro, self.ReservaAtual.RA, self.ReservaAtual.Horario) 
            umaReserva.escreverRegistro(arquivoDeSaida)
            
        arquivoDeSaida.close()
    
