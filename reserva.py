#-------------------------------------------------------#
#         Arthur Gama Jorge - RA: 23578 - 1 Info        #
#      Ion Mateus Nunes Oprea - RA: 23135 - 1 Info      #
#-------------------------------------------------------#

class Reserva:
    global iniCodMicro, iniRA, iniHorario, tamCodMicro, tamRA, tamHorario
    # mapeamento dos campos do registro
    iniCodMicro = 0
    iniRA = 10
    iniHorario = 15
    tamCodMicro = 10
    tamRA = 5
    tamHorario = 2

    def __init__(self): #variaveis da classe
        self._CodMicro = "0" * tamCodMicro  # String
        self._RA = " " * tamRA              # String
        self._Horario = 0                   # Int
        
    @property
    def RA(self):
        return self._RA
    
    @RA.setter
    def RA(self, novoRA):
        self._RA = novoRA.ljust(tamRA,' ')[0:tamRA]

    @property
    def Horario(self):
        return self._Horario
    
    @Horario.setter
    def Horario(self, novoHorario):
        if novoHorario > 0 and novoHorario <= 18:
            self._Horario = novoHorario
        else:
            raise ValueError("Horário deve estar entre 1 e 18")
            
    def leuRegistro(self, arquivo) -> bool:
        if arquivo != None:                # se objeto de arquivo foi criado 
            linhaLida = arquivo.readline()     # lê uma linha do arquivo
            if linhaLida != "":                # se consegiu ler uma linha
                self.CodMicro = linhaLida[iniCodMicro : iniRA].strip() 
                self.RA = linhaLida[iniRA : iniHorario].strip() 
                self.Horario = int(linhaLida[iniHorario:].strip())
                return True 
            else: 
                return False 
        else: 
            return False
        
    # dados de cada campo digitados individualmente pelo usuário, no módulo principal
    def atribuirDados(self, CodMicro, RA, Horario): 
        self.CodMicro = CodMicro
        self.RA = RA
        self.Horario = Horario

    def escreverRegistro(self, saida):
        if saida != None:
            saida.write(self.paCodMicroArquivo())
        else:
            raise IOError("Arquivo de gCodMicrovação não foi aberto.")

    def paCodMicroArquivo(self) -> str :
        return f"{self.CodMicro.ljust(tamCodMicro, ' ')[0:tamCodMicro]}{self.RA} {self.Horario}\n"
    
    def __str__(self):
        return f"{self.CodMicro}  {self.RA}  {self.Horario}"
