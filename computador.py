#-------------------------------------------------------#
#         Arthur Gama Jorge - RA: 23578 - 1 Info        #
#      Ion Mateus Nunes Oprea - RA: 23135 - 1 Info      #
#-------------------------------------------------------#

class Computador:
    global iniCodMicro, iniDescricao, iniPodeUsar, tamCodMicro, tamDescricao, tamPodeUsar
    # mapeamento dos campos do registro
    iniCodMicro = 0
    iniDescricao = 10
    iniPodeUsar = 60
    tamCodMicro = 10
    tamDescricao = 50
    tamPodeUsar = 5

    def __init__(self): #variaves da classe
        self._CodMicro = "0" * tamCodMicro        # String
        self._Descricao = " " * tamDescricao      # String
        self._PodeUsar = bool                     # bool (True or False)
        
    @property
    def Descricao(self):
        return self._Descricao
    
    @Descricao.setter
    def Descricao(self, novoDescricao):
        self._Descricao = novoDescricao.ljust(tamDescricao,' ')[0:tamDescricao]

    @property
    def PodeUsar(self):
        return self._PodeUsar
    
    @PodeUsar.setter
    def PodeUsar(self, novoPodeUsar):
        self._PodeUsar = novoPodeUsar
            
    def leuRegistro(self, arquivo) -> bool:
        if arquivo != None:                # se foi passado um arquivo
            linhaLida = arquivo.readline()     # lê uma linha do arquivo
            if linhaLida != "":                # se consegiu ler uma linha
                self.CodMicro = linhaLida[iniCodMicro : iniDescricao].strip() 
                self.Descricao = linhaLida[iniDescricao : iniPodeUsar].strip() 
                if linhaLida[iniPodeUsar: ].strip() == "True":
                    self.PodeUsar = True
                else:
                    self.PodeUsar = False
                return True 
            else: 
                return False 
        else: 
            return False
        
    # dados de cada campo digitados individualmente pelo usuário, no módulo principal
    def atribuirDados(self, CodMicro, Descricao, PodeUsar): 
        self.CodMicro = CodMicro
        self.Descricao = Descricao
        self.PodeUsar = PodeUsar
        
    def escreverRegistro(self, saida): #escreve no arquivo .txt
        if saida != None:
            saida.write(self.paCodMicroArquivo())
        else:
            raise IOError("Arquivo de gCodMicrovação não foi aberto.")

    def paCodMicroArquivo(self) -> str :
        return f"{self.CodMicro.ljust(tamCodMicro, ' ')[0:tamCodMicro]}{self.Descricao}{self.PodeUsar}\n"
    
    def __str__(self):
        return f"{self.CodMicro}  {self.Descricao}  {self.PodeUsar}"
