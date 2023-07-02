#-------------------------------------------------------#
#         Arthur Gama Jorge - RA: 23578 - 1 Info        #
#      Ion Mateus Nunes Oprea - RA: 23135 - 1 Info      #
#-------------------------------------------------------#

#importar bibliotecas necessáriac
import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar

from menuPrincipal_ui import Ui_MainWindow

from manAluno import FormPrincipal as manAluno
from manComputador import FormPrincipal as manComputador
from manReserva import FormPrincipal as manReserva

class FormPrincipal(QMainWindow, Ui_MainWindow):  

    def __init__(self): 
        
        super().__init__() #importa das classes ancestrais
        self.setupUi(self) 
        self.statusBar = QStatusBar() 
        self.setStatusBar(self.statusBar)
        self.show()

        self.actionSair.triggered.connect(self.Sair)
        self.actionAlunos.triggered.connect(self.Alunos)
        self.actionComputadores.triggered.connect(self.Computadores)
        self.actionQuadro_de_reservas.triggered.connect(self.QuadroDeReservas)
        
    
    def Sair(self): #fecha o programa
        self.close()
        
    
    def Alunos(self): #abre a janela de mautenção dos alunos
        self.Aluno = manAluno()
        self.Aluno.show()
        
        
    def Computadores(self): #abre a janela de mautenção dos computadores
        self.Computador = manComputador()
        self.Computador.show()
    
    
    def QuadroDeReservas(self): #abre o quadro de reservas
        self.Reservas = manReserva()
        self.Reservas.show()

   
if __name__ == "__main__":
    aplicacao = QApplication(sys.argv) 
    try:
        janela = FormPrincipal() 
        aplicacao.exec() 
        
    except Exception as erro: 
        if hasattr(erro, 'message'): 
            mensagem = erro.message 
        else: 
            mensagem = erro.args[0]
        print(mensagem)
    