#-------------------------------------------------------#
#         Arthur Gama Jorge - RA: 23578 - 1 Info        #
#      Ion Mateus Nunes Oprea - RA: 23135 - 1 Info      #
#-------------------------------------------------------#

# importações
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QMainWindow, QStatusBar,  QTableWidgetItem

from FrmAluno_ui import Ui_FrmAluno
from vetAlu import VetorAluno
from alu import Aluno
from vetorAbstrato import Situacao
from vetAlu import VetorAluno
from matReserva import MatrizReserva

class FormPrincipal(QMainWindow, Ui_FrmAluno):

    def __init__(self): 
        
        super().__init__() 
        self.setupUi(self) 
        self.statusBar = QStatusBar() 
        self.setStatusBar(self.statusBar)
        self.show()
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
        
        self.edRA.textChanged.connect(self.testarRA)  # testa se o RA em digitação existe
        
        self.abas.currentChanged.connect(self.mudarAba)
        
        self.rbPorNome.toggled.connect(self.OrdenarPor)
        self.rbPorRA.toggled.connect(self.OrdenarPor)
        self.rbPorCurso.toggled.connect(self.OrdenarPor)
        
        self.osAlunos = VetorAluno(50)
        self.osAlunos.leituraDosDados('alunos.txt')
        
        self.asReservas = MatrizReserva(50)
        self.asReservas.leituraDosDados('reservas.txt')
        
        self.preencherComboCursos()

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
        numeroDeLinhas = self.osAlunos.tamanho 
        self.grdAluno.setRowCount(numeroDeLinhas) # Coloca o número de linhas como o qtosDados de Alunos

        if self.rbPorNome.isChecked(): # Verifica se o radio de ordenar por nome está ativado
            self.osAlunos.ordenarPorNome() # Ordena por nome
        elif self.rbPorRA.isChecked():
            self.osAlunos.ordenar()
        elif self.rbPorCurso.isChecked():
            self.osAlunos.ordenarPorCurso()
            
        self.mudarAba() # Atualiza a tela com a ordenação


    def preencherComboCursos(self): # Preenche o combo com base nas linhas do cursos.txt
        arquivo = open("cursos.txt", "r") 
        linha = "1" 
        while linha != "": 
            linha = arquivo.readline() 
            if linha != "": 
                saida = linha[0:2]+" - "+linha[2:].strip() 
                self.cbxCurso.addItem(saida) 
        arquivo.close()

    def aoInicio(self): 
        self.osAlunos.irAoInicio() 
        self.atualizarTela() 
    
    def aoAnterior(self): 
        self.osAlunos.irAoAnterior() 
        self.atualizarTela() 
        
    def aoProximo(self): 
        self.osAlunos.irAoProximo() 
        self.atualizarTela() 
        
    def aoFim(self): 
        self.osAlunos.irAoFim() 
        self.atualizarTela()
        
    def atualizarTela(self): 
        if self.osAlunos.tamanho > 0: # há dados para exibir 
            oAluno = self.osAlunos.valorDe(self.osAlunos.posicaoAtual) 
            self.edRA.setText(oAluno.ra)  # dispara textChanged
            self.edNome.setText(oAluno.nome) # vamos procurar o código do curso nos itens do combobox
            posicao = -1 
            for indice in range(0, self.cbxCurso.count(), 1): 
                if oAluno.curso in self.cbxCurso.itemText(indice): 
                    posicao = indice 
                    break 
            self.edRA.setReadOnly(True)
            self.edNome.setReadOnly(True)
            self.cbxCurso.setEnabled(False)
            
            self.cbxCurso.setCurrentIndex(posicao) 
        else: 
            self.limparTela() # tabela de dados está vazia 
        
        self.statusBar.showMessage(f"Registro "+\
            f"{self.osAlunos.posicaoAtual+1}/{self.osAlunos.tamanho}") 

        self.testarBotoes() 
        self.osAlunos.ordenar()
        
        
    def testarBotoes(self): # Tira destaque de botões que não podem ser usados
        self.action_Inicio.setEnabled(True) 
        self.action_Anterior.setEnabled(True) 
        self.action_Proximo.setEnabled(True) 
        self.action_Fim.setEnabled(True) 
        
        if self.osAlunos.estaNoInicio: 
            self.action_Inicio.setEnabled(False) 
            self.action_Anterior.setEnabled(False) 
            
        if self.osAlunos.estaNoFim: 
            self.action_Proximo.setEnabled(False) 
            self.action_Fim.setEnabled(False)

    def limparTela(self):  # volta os valores para o padrão
        self.edRA.setText("") 
        self.edNome.setText("") 
        self.cbxCurso.setCurrentIndex(-1)
    
    def sairDoPrograma(self):
        self.close()
        
    def closeEvent(self, event):
        self.osAlunos.gravarDados('alunos.txt')
        self.asReservas.gravarDados('reservas.txt')

    def buscarRegistro(self):
        self.limparTela()
        self.edRA.setReadOnly(False)
        self.edRA.setFocus() # Coloca o foco no line edit de RA
        self.statusBar.showMessage("Digite o RA do(a) aluno(a) que busca")
        self.osAlunos.situacao = Situacao.buscando      # modo de busca

    def novoRegistro(self):
        # limpamos os campos de tela para iniciar o modo de inclusão
        self.limparTela()
        self.edRA.setReadOnly(False)     # permite digitação nesse controle  
        self.edNome.setReadOnly(False)
        self.cbxCurso.setEnabled(True)
        self.statusBar.showMessage("Digite os dados acima")
        self.edRA.setFocus()             # põe o cursor no line edit de RA 
        # modo de operação do programa = modo de inclusão
        self.osAlunos.situacao = Situacao.incluindo  
            
    def editarRegistro(self):
        self.osAlunos.situacao = Situacao.editando  # programa entra em modo de edição
        self.edRA.setReadOnly(True)     # não permite alterar (digitar) esse controle
        self.edNome.setReadOnly(False)
        self.cbxCurso.setEnabled(True)
        self.edNome.setFocus()          # coloca cursor nesse controle
        self.statusBar.showMessage("Altere os dados acima e pressione [Salvar]")
    
    def salvarRegistro(self):
        if self.osAlunos.situacao == Situacao.incluindo:   # está no modo de inclusão
            curso = self.cbxCurso.currentText()[0:2]             #  a
            novoAluno = Aluno()                                  #  a
            novoAluno.atribuirDados(self.edRA.text(), self.edNome.text(), curso)
            self.osAlunos.incluirEm(novoAluno, self.osAlunos.posicaoAtual)   # c, d
            self.osAlunos.posicaoAtual = self.osAlunos.posicaoAtual  #  f
            self.atualizarTela()                                 #  f
        elif self.osAlunos.situacao == Situacao.editando: 
            alunoEditado = Aluno()
            alunoEditado.atribuirDados(self.edRA.text(), self.edNome.text(),
                                       self.cbxCurso.currentText()[0:2])
            self.osAlunos._dados[self.osAlunos.posicaoAtual] = alunoEditado
                
        self.osAlunos.situacao  = Situacao.navegando   # e - terminou a inclusão/edição
        self.atualizarTela()
                
    def excluirRegistro(self):
        self.osAlunos.situacao  = Situacao.excluindo
        if self.exibirMensagem("Atenção!", 
                               "Deseja realmente excluir esse registro?", 
                               QMessageBox.Warning):
            
            alunoExcluido = self.osAlunos.valorDe(self.osAlunos.posicaoAtual)
            
            for i in range(0, self.asReservas.tamanho):
                if i < self.asReservas.tamanho:
                    ReservaAtual = self.asReservas.valorDe(i)
                    if ReservaAtual.RA == alunoExcluido.ra:
                        self.asReservas.excluir(i)   
                    
            self.osAlunos.excluir(self.osAlunos.posicaoAtual)
            if self.osAlunos.posicaoAtual >= self.osAlunos.tamanho :
                self.osAlunos.irAoFim()
            self.atualizarTela()
        self.osAlunos.situacao  = Situacao.navegando   # terminou a exclusão
        
    def cancelarAcao(self):
        self.osAlunos.situacao = Situacao.navegando
        self.atualizarTela()
        # verificar se precisa limpar ou mudar o registro exibido na tela

    def testarRA(self, raProcurado):     # raProcurado é a string que foi digitada em edRA
        if  self.osAlunos.situacao == Situacao.incluindo or \
            self.osAlunos.situacao == Situacao.buscando:
            self.edRA.setText(raProcurado)
            if len(raProcurado) == 5:    # terminamos de digitar um RA
                if self.osAlunos.busca(raProcurado) :   # atribui valor a osAlunos.ondeEsta
                    # se o fluxo entra aqui, achamos o raProcurado no vetor _dados
                    if self.osAlunos.situacao == Situacao.incluindo:
                        self.exibirMensagem("ATENÇÃO!", "RA já existe!", 
                                            QMessageBox.Warning)
                        self.osAlunos.situacao = Situacao.navegando
                        self.atualizarTela()        # restaura dados anteriores
                    else:
                        # aqui, estamos na busca e achamos o raProcurado, vamos
                        # atualizar a tela com o registro encontrado
                        self.osAlunos.posicaoAtual = self.osAlunos.posicaoAtual # local onde achou
                        self.atualizarTela()            
                else:
                    # se o fluxo entra aqui, não achamos o raProcurado
                    if self.osAlunos.situacao == Situacao.incluindo:
                        #nao existe, podemos continuar incluindo
                        self.edNome.setFocus()
                        self.statusBar.showMessage(f"Digite os demais dados")
                    else:
                        # aqui, estamos em modo de busca e não achamos o raProcurado:
                        self.exibirMensagem("ATENÇÂO!","RA não encontrado.", QMessageBox.Information)
                        self.atualizarTela()

    def mudarAba(self):
        if self.abas.currentIndex() == 1:
            # buscar no objeto de manutenção de alunos os registros para exibí-los
            # no TableWidget grdAluno
            try:
                numeroDeLinhas = self.osAlunos.tamanho  # quantos registros estão armazenados
                self.grdAluno.setRowCount(numeroDeLinhas) # ajusta o número de linhas do grid

                for indice in range(0, numeroDeLinhas, 1):
                    alunoAtual = self.osAlunos.valorDe(indice)
                    item_ra    = QTableWidgetItem(alunoAtual.ra)
                    item_nome  = QTableWidgetItem(alunoAtual.nome)
                    item_curso = QTableWidgetItem(alunoAtual.curso)
                    
                    self.grdAluno.setItem(indice, 0, item_ra)       # linha índice, coluna 0
                    self.grdAluno.setItem(indice, 1, item_nome)     # linha índice, coluna 1
                    self.grdAluno.setItem(indice, 2, item_curso)    # linha índice, coluna 2
                    
                self.grdAluno.resizeColumnsToContents()  # redimensiona largura das colunas
                self.grdAluno.resizeRowsToContents()     # redimensiona altura das linhas
                self.statusBar.showMessage("Listagem")
                    
            except Exception as erro:   # em caso de erro
                if hasattr(erro, 'message'):
                    mensagem = erro.message 
                else: 
                    mensagem = erro.args[1] 
                self.statusBar.showMessage(mensagem) 
        else:   
            self.rbPorRA.setChecked(True) # Quando voltar para primeira aba volta o radio para ordenar por RA