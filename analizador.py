class analizador:
    def __init__(self, sujeto: str, verbo: str, predicado:str):
        self.sujeto = sujeto
        self.verbo = verbo
        self.predicado = predicado
    
    def analizarSintaxis(self) -> bool:
        sujetos = ["carlos", "anna", "maria", "diego", "julian", "el niño", "la niña"]
        verbos = ["corre", "salta", "camina", "come", "pela", "salta", "juega"]  
        predicados = ["en el parque", "en la cancha", "en el colegio", "en un trampolin", ""] 
        bool = False
        boolSujeto = False
        boolverbo = False
        boolpredicado = False 
        
       
        for i in range(0, len(sujetos)-1):
            if self.sujeto == sujetos[i]:
                boolSujeto = True
                break
            
        for i in range(0, len(verbos)-1):
            if self.verbo == verbos[i]:
                boolverbo = True
                break
        
        for i in range(0, len(predicados)-1):
            if self.predicado == predicados[i]:
                boolpredicado = True
                break
            
        if boolSujeto == True and boolpredicado == True and boolverbo == True:
            bool = True
        
        return bool
        

            
            
