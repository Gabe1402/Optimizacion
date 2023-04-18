class Optimizar:
    userInputArray = []

    def addToArray(self, n1):
        if isinstance(n1, list):
            for i in n1:
                self.userInputArray.append(i)
            return print("numero "+str(i)+" introducido")
        else:
            self.userInputArray.append(n1)
            return print("numero "+str(n1)+" introducido")

    def calcularMedia(self):
        suma=0
        for n in self.userInputArray:
            suma= suma+n
        return suma/len(self.userInputArray)