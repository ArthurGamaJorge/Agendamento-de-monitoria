#-------------------------------------------------------#
#         Arthur Gama Jorge - RA: 23578 - 1 Info        #
#      Ion Mateus Nunes Oprea - RA: 23135 - 1 Info      #
#-------------------------------------------------------#

class Aluno:
    global iniRA, iniNome, iniCurso, tamRA, tamNome, tamCurso
    # mapeamento dos campos do registro
    iniRA = 0
    iniNome = 5
    iniCurso = 35
    tamRA = 5
    tamNome = 30
    tamCurso = 2

    def __init__(self): #variaveis da classe
        self._ra = "0"*tamRA        # String
        self._nome = " "*tamNome    # String
        self._curso = "0"*tamCurso  # String
        
    @property # Retorna o RA
    def ra(self):
        return self._ra
    
    @ra.setter # Ajusta o tamanho do RA
    def ra(self, novoRA):
        self._ra = novoRA.rjust(tamRA, '0')[0:tamRA]
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novoNome):
        self._nome = novoNome.ljust(tamNome,' ')[0:tamNome]

    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, novoCurso):
        self._curso = novoCurso.rjust(tamCurso,'0')[0:tamCurso]
            
    def leuRegistro(self, arquivo) -> bool:
        if arquivo != None:                # se foi passado um arquivo como parametro
            linhaLida = arquivo.readline()     # lê uma linha do arquivo
            if linhaLida != "":                # se consegiu ler uma linha
                self.ra = linhaLida[iniRA : iniNome].strip()  #armazena os valores
                self.nome = linhaLida[iniNome : iniCurso].strip() 
                self.curso = linhaLida[iniCurso: ].strip()
                return True 
            else: 
                return False 
        else: 
            return False
        
    # dados de cada campo digitados individualmente pelo usuário, no módulo principal
    def atribuirDados(self, ra, nome, curso): 
        self.ra = ra 
        self.nome = nome
        self.curso = curso
        
    def escreverRegistro(self, saida): #escreve no arquivo
        if saida != None:
            saida.write(self.paraArquivo())
        else:
            raise IOError("Arquivo de gravação não foi aberto.")

    def paraArquivo(self) -> str :   
        return f"{self.ra}{self.nome}{self.curso}\n"
    
    def __str__(self):
        return f"{self.ra}  {self.nome}  {self.curso}"

    