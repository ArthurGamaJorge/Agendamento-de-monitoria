#-------------------------------------------------------#
#         Arthur Gama Jorge - RA: 23578 - 1 Info        #
#      Ion Mateus Nunes Oprea - RA: 23135 - 1 Info      #
#-------------------------------------------------------#

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QStatusBar, QMessageBox, QMainWindow, QStatusBar,  QTableWidgetItem

from frmComputador_ui import Ui_FrmComputador
from computador import Computador
from vetComputador import VetorComputador
from matReserva import MatrizReserva
from vetorAbstrato import Situacao

class FormPrincipal(QMainWindow, Ui_FrmComputador):

    def __init__(self): 
        
        super().__init__() #classe ancestral
        self.setupUi(self) 
        self.statusBar = QStatusBar() 
        self.setStatusBar(self.statusBar)
        self.show()

        #eventos
        self.action_Inicio.triggered.connect(self.aoInicio)
        self.action_Anterior.triggered.connect(self.aoAnterior)
        self.action_Proximo.triggered.connect(self.aoProximo)
        self.action_Fim.triggered.connect(self.aoFim)
        
        self.action_Buscar.triggered.connect(self.buscarRegistro)
        self.action_Novo.triggered.connect(self.novoRegistro) 
        self.action_Editar.triggered.connect(self.editarRegistro) 
        self.action_Salvar.triggered.connect(self.salvarRegistro)
        self.action_Excluir.triggered.connect(self.excluirRegistro)
        self.action_Cancelar.triggered.connect(self.cancelarAcao)
        self.action_Sair.triggered.connect(self.sairDoPrograma)
        
        self.btnConfirmarProcura.clicked.connect(self.testarComputador)
        
        self.abas.currentChanged.connect(self.mudarAba)
        
        self.rbPorCodigo.toggled.connect(self.OrdenarPor)
        self.rbPorDescricao.toggled.connect(self.OrdenarPor)
        self.rbPorCondicao.toggled.connect(self.OrdenarPor)
        
        #variaveis
        self.osComputadores = VetorComputador(50)
        self.osComputadores.leituraDosDados('computadores.txt')
        
        self.asReservas = MatrizReserva(50)
        self.asReservas.leituraDosDados('reservas.txt')

        self.atualizarTela()    # exibirá o 1o registro da tabela (registroAtual = 0)
    
    def exibirMensagem(self, titulo : str, mensagem : str, icone) -> bool:     #MessageBox
        msgBox = QMessageBox()
        msgBox.setIcon(icone)
        msgBox.setText(mensagem)
        msgBox.setWindowTitle(titulo)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        return returnValue == QMessageBox.Ok
    
    def OrdenarPor(self):
        self.grdComputador.setRowCount(self.numeroTotalLinhas) 

        if self.rbPorCodigo.isChecked():
            self.osComputadores.ordenar()
        elif self.rbPorDescricao.isChecked():
            self.osComputadores.ordenarPorDescricao()
        elif self.rbPorCondicao.isChecked():
            self.osComputadores.ordenarPorCondicao()
            
        self.mudarAba() 


    def aoInicio(self): 
        self.osComputadores.irAoInicio() 
        self.atualizarTela() 
    
    def aoAnterior(self): 
        self.osComputadores.irAoAnterior() 
        self.atualizarTela() 
        
    def aoProximo(self): 
        self.osComputadores.irAoProximo() 
        self.atualizarTela() 
        
    def aoFim(self): 
        self.osComputadores.irAoFim() 
        self.atualizarTela()
        
    def atualizarTela(self): 
        if self.osComputadores.tamanho > 0: # há dados para exibir 
            oComputador = self.osComputadores.valorDe(self.osComputadores.posicaoAtual) 
            self.edCodComputador.setText(oComputador.CodMicro)  # dispara textChanged
            self.edDescricao.setText(oComputador.Descricao) # vamos procurar o código do curso nos itens do combobox
            self.osComputadores.ordenar()
            if oComputador.PodeUsar:
                self.chkUso.setChecked(True)
            else:
                self.chkUso.setChecked(False)
            self.edDescricao.setReadOnly(True)
            self.edCodComputador.setReadOnly(True)
            self.btnConfirmarProcura.setEnabled(False)
            self.chkUso.setEnabled(False)
                
        else: 
            self.limparTela() # tabela de dados está vazia 
        
        self.statusBar.showMessage(f"Registro "+\
            f"{self.osComputadores.posicaoAtual+1}/{self.osComputadores.tamanho}") 

        self.testarBotoes() 
        self.osComputadores.ordenar()
        
    def testarBotoes(self): 
        self.action_Inicio.setEnabled(True) 
        self.action_Anterior.setEnabled(True) 
        self.action_Proximo.setEnabled(True) 
        self.action_Fim.setEnabled(True) 
        
        if self.osComputadores.estaNoInicio: 
            self.action_Inicio.setEnabled(False) 
            self.action_Anterior.setEnabled(False) 
            
        if self.osComputadores.estaNoFim: 
            self.action_Proximo.setEnabled(False) 
            self.action_Fim.setEnabled(False)

    def limparTela(self): 
        self.edCodComputador.setText("") 
        self.edDescricao.setText("") 
        self.chkUso.setChecked(False)
    
    def sairDoPrograma(self):
        self.close()
        
    def closeEvent(self, event):
        self.osComputadores.gravarDados('computadores.txt')
        self.asReservas.gravarDados('reservas.txt')

    def buscarRegistro(self):
        self.limparTela()
        self.edCodComputador.setReadOnly(False)
        self.edCodComputador.setFocus()
        self.statusBar.showMessage("Digite o código do computador que busca")
        self.osComputadores.situacao = Situacao.buscando      # modo de busca
        self.btnConfirmarProcura.setEnabled(True)

    def novoRegistro(self):
        # limpamos os campos de tela para iniciar o modo de inclusão
        self.btnConfirmarProcura.setEnabled(False)
        self.limparTela()
        self.edCodComputador.setReadOnly(False)     # permite digitação nesse controle  
        self.edDescricao.setReadOnly(False)
        self.chkUso.setEnabled(True)
        self.statusBar.showMessage("Digite os dados acima")
        self.edCodComputador.setFocus()             # põe o cursor no line edit de RA 
        # modo de operação do programa = modo de inclusão
        self.osComputadores.situacao = Situacao.incluindo  
            
    def editarRegistro(self):
        self.btnConfirmarProcura.setEnabled(False)
        self.osComputadores.situacao = Situacao.editando  # programa entra em modo de edição
        self.edCodComputador.setReadOnly(True)     # não permite alterar (digitar) esse controle
        self.chkUso.setEnabled(True)
        self.edDescricao.setReadOnly(False)
        self.edDescricao.setFocus()          # coloca cursor nesse controle
        self.statusBar.showMessage("Altere os dados acima e pressione [Salvar]")
    
    def salvarRegistro(self):
        if self.chkUso.isChecked():
            PodeUsar = True
        else:
            PodeUsar = False
        if self.osComputadores.situacao == Situacao.incluindo:   # está no modo de inclusão
            computadorProcurado = self.edCodComputador.text()
            if self.osComputadores.busca(computadorProcurado) : 
                self.exibirMensagem("ATENÇÃO!", "Computador já existe!",  QMessageBox.Warning)
                self.osComputadores.situacao = Situacao.navegando
                self.atualizarTela()        # restaura dados anteriores
            else:
                novoComputador = Computador()
                novoComputador.atribuirDados(self.edCodComputador.text(), self.edDescricao.text(), PodeUsar)
                self.osComputadores.incluirEm(novoComputador, self.osComputadores.posicaoAtual)
                self.osComputadores.posicaoAtual = self.osComputadores.posicaoAtual
                self.atualizarTela()
        elif self.osComputadores.situacao == Situacao.editando: 
            computadorEditado = Computador()
            computadorEditado.atribuirDados(self.edCodComputador.text(), self.edDescricao.text(), PodeUsar)
            self.osComputadores._dados[self.osComputadores.posicaoAtual] = computadorEditado
                
        self.osComputadores.situacao  = Situacao.navegando   # e - terminou a inclusão/edição
        self.atualizarTela()
                
    def excluirRegistro(self):
        self.osComputadores.situacao  = Situacao.excluindo
        if self.exibirMensagem("Atenção!", 
                               "Deseja realmente excluir esse registro?", 
                               QMessageBox.Warning):
            computadorExcluido = self.osComputadores.valorDe(self.osComputadores.posicaoAtual)
            
            for i in range(0, self.asReservas.tamanho):
                if i < self.asReservas.tamanho:
                    ReservaAtual = self.asReservas.valorDe(i)
                    if ReservaAtual.CodMicro == computadorExcluido.CodMicro:
                        self.asReservas.excluir(i)          
                        
            self.osComputadores.excluir(self.osComputadores.posicaoAtual)
            if self.osComputadores.posicaoAtual >= self.osComputadores.tamanho :
                self.osComputadores.irAoFim()
            self.atualizarTela()
        self.osComputadores.situacao  = Situacao.navegando   # terminou a exclusão
        

    def cancelarAcao(self):
        self.osComputadores.situacao = Situacao.navegando
        self.atualizarTela()

    def testarComputador(self):     
        computadorProcurado = self.edCodComputador.text()
        if self.osComputadores.situacao == Situacao.incluindo or \
            self.osComputadores.situacao == Situacao.buscando:
            if self.osComputadores.busca(computadorProcurado) :  
                if self.osComputadores.situacao == Situacao.incluindo:
                    self.exibirMensagem("ATENÇÃO!", "esse computador já existe!", 
                                        QMessageBox.Warning)
                    self.osComputadores.situacao = Situacao.navegando
                    self.atualizarTela()       
                else:
                    self.osComputadores.posicaoAtual = self.osComputadores.posicaoAtual 
                    self.atualizarTela()             
            else:
                if self.osComputadores.situacao == Situacao.incluindo:
                    self.edDescricao.setFocus()
                    self.statusBar.showMessage(f"Digite os demais dados")
                else:
                    self.exibirMensagem("ATENÇÂO!","código de computador não encontrado.", QMessageBox.Information)
                    self.atualizarTela()

    def mudarAba(self):
        if self.abas.currentIndex() == 1:
            try:
                i2=0
                for i in range(0, self.osComputadores.tamanho): # Consegue o tamanho de linhas do grid de listagem de computadores
                    if not self.asReservas.busca(self.osComputadores.valorDe(i).CodMicro):
                        i2+= 1 # Soma 
                        
                numerodeLinhasReserva = self.asReservas.tamanho
                self.numeroTotalLinhas = i2 + numerodeLinhasReserva # Soma a quantidade de linhas do arquivos reservas com a de computadores não reservados
                horarios = ["7:30", "8:15", "09:00", "10:00","10:45", "11:30", "13:30", "14:15", "15:00","16:00", "16:45","17:30","18:15","19:00", "19:45", "20:30", "21:15", "22:15"]
                # Vetor com horários formatados para melhor visualização
                
                self.grdComputador.setRowCount(self.numeroTotalLinhas) # ajusta o número de linhas do grid

                indice = 0
                indice2 = 0
                while indice < self.numeroTotalLinhas:
                    quantosItens = 0
                    item_ra = QTableWidgetItem("-")          # Padrão
                    item_horario = QTableWidgetItem("-")
                    
                    computadorAtual = self.osComputadores.valorDe(indice2)
                    indice2 += 1
                    if computadorAtual.PodeUsar:
                        item_podeUsar = "Sim"
                    else:
                        item_podeUsar = "Não"
                    item_horarioAnt = ""
                    i3=0
                    for i in range(0, numerodeLinhasReserva):
                        if self.asReservas.busca(computadorAtual.CodMicro): # Caso o computador tenha sido reservado
                            reservaAtual = self.asReservas.valorDe(i)
                            if reservaAtual.CodMicro == computadorAtual.CodMicro:
                                item_ra = QTableWidgetItem(reservaAtual.RA)
                                item_horario = QTableWidgetItem(f"{horarios[reservaAtual.Horario-1]}") # Atribui os valores a item da tabela
                            else: # Se o computador for reservado mas a reserva atual não for a dele, impede o registro na tabela
                                item_horarioAnt = item_horario
                            
                        else: # Caso o computador não tenha sido reservado ele é colocado na tabela na primeira vez
                            i3 += 1
                        quantosItens += 1
                                
                        for ind in range(0, quantosItens):
                            if item_horario != item_horarioAnt and i3 < 2: # Caso o computador não for reservado ele só aparece uma vez através do contador i3
                                self.grdComputador.setItem(indice, 0, QTableWidgetItem(computadorAtual.CodMicro))       # linha índice, coluna 
                                self.grdComputador.setItem(indice, 1, QTableWidgetItem(computadorAtual.Descricao))     
                                self.grdComputador.setItem(indice, 2, QTableWidgetItem(item_podeUsar))    
                                self.grdComputador.setItem(indice, 3, item_ra)    
                                self.grdComputador.setItem(indice, 4, item_horario)   
                                indice += 1
                                item_horarioAnt = item_horario # Impede repetição de registro
                    
                self.grdComputador.resizeColumnsToContents()  # redimensiona largura das colunas
                self.grdComputador.resizeRowsToContents()     # redimensiona altura das linhas
                self.statusBar.showMessage("Listagem")
                    
            except Exception as erro:   # em caso de erro
                if hasattr(erro, 'message'):
                    mensagem = erro.message 
                else: 
                    mensagem = erro.args[1] 
                self.statusBar.showMessage(mensagem) 
        else:   
            self.rbPorCodigo.setChecked(True) # Ao mudar para a aba 1, deixa o radio de ordenar por código checado