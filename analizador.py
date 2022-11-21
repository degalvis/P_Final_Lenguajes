class analizador:
    def __init__(self, sujeto: str, verbo: str, predicado:str):
        self.sujeto = sujeto
        self.verbo = verbo
        self.predicado = predicado
        self.sujetos = ["carlos", "anna", "maria", "diego", "julian", "el niño", "la niña", "david", "el"]
        self.plurales = ["ellos","ustedes"]
        self.verbop = ["corren", "saltan", "caminan", "comen", "pelan", "saltan", "juegan","leen","cantan","meditan"]  
        self.comidas = ["una pizza", "unas uvas", "cereal", "arepa", "pera", "bandeja paisa", "una crepa"]
        self.comer = ["come","cena","alumerza","desayuna","prepara"]
        self.comerp = ["comen","cenan","tiran","desayunan","preparan"]
        self.verbos = ["corre", "salta", "camina", "come", "pela", "salta", "juega", "lee", "canta","medita"]  
        self.predicados = ["en el parque", "en la cancha", "en el colegio", "en un trampolin", "en casa", "en el vecindario", "en la iglesia", "en el escenario"] 
        self.mascotas = ["el perro", "el gato", "el perico", "el hamster", "El loro"]
        self.mascotasA = ["come", "sonrie", "orina", "duerme", "nada"]
        self.mascotasl = ["en el lago", "en la casa", "en la finca", "duerme", "nada"]
    def analizarSintaxis(self) -> bool:
        if  self.sujetos.__contains__(self.sujeto):
                  return self.analizarsing()
        elif self.plurales.__contains__(self.sujeto):   
                  return self.analizarplural() 
        elif self.mascotas.__contains__(self.sujeto):   
                  return self.analizarMascotas()       
        else:
            return False       
        
    def analizarsing(self):
        return self.verbos.__contains__(self.verbo) and self.predicados.__contains__(self.predicado) or self.comer.__contains__(self.verbo) and self.comidas.__contains__(self.predicado)
    
    def analizarplural(self):
        return self.verbop.__contains__(self.verbo) and self.predicados.__contains__(self.predicado) or self.comerp.__contains__(self.verbo) and self.comidas.__contains__(self.predicado)
    
    def analizarMascotas(self):
        return self.mascotasA.__contains__(self.verbo) and self.mascotasl.__contains__(self.predicado) 
            

            
            
