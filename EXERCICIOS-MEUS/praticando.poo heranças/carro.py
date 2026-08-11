class veiculo:
    def __init__(self, marca,modelo):
        self._marca=marca
        self._modelo=modelo
        self._protegido=False
    
    def __str__(self):
        status= 'ligado' if self._protegido else 'desligado'
        return f'marca: {self._marca}, modelo: {self._modelo} , estado: {status}'

class carros(veiculo):
    def __init__(self,marca,modelo,portas):
        super().__init__ (marca,modelo)
        self._portas= portas
    def __str__(self):
        return f'{super().__str__()} - portas: {self._portas}'

class moto(veiculo):
    def __init__(self,marca,modelo,construtor):
        super().__init__(marca,modelo)
        self._contrutor= construtor
    def __str__(self):
        return f'{super().__str__()} - tipo de moto: {self._contrutor}'
    
