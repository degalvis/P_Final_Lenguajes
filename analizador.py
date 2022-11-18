class analizador:
    def __init__(self, sujeto: str, verbo: str, predicado:str):
        self.sujeto = sujeto
        self.verbo = verbo
        self.predicado = predicado
    
    def analizarSintaxis(self) -> bool:
        sujetos = ["carlos", "anna", "maria", "diego", "julian", "el niño", "la niña"]
        verbos = ["corre", "salta", "camina", "come", "pela", "salta", "juega"]  
        predicados = ["en el parque", "en la cancha", "en el colegio", "en un trampolin", ""] 
        bool = sujetos.__contains__(self.sujeto) and verbos.__contains__(self.verbo) and predicados.__contains__(self.predicado)
        return bool
        

            
            
