from optimizar import Optimizar

def test_optimizacion_media():
    optimizacion = Optimizar()
    optimizacion.addToArray(4)
    optimizacion.addToArray(5)
    optimizacion.addToArray(6)
    print("La media es: "+str(optimizacion.calcularMedia()))
    assert optimizacion.calcularMedia() == (4+5+6)/len(optimizacion.userInputArray)
    optimizacion.userInputArray.clear()

def test_optimizacion_array():
    optimizacion = Optimizar()
    a = [1,10,3,5,6]
    optimizacion.addToArray(a)
    print("La media es: " + str(optimizacion.calcularMedia()))
    assert len(optimizacion.userInputArray) == len(a)