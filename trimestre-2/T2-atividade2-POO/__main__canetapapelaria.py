from canetapapelaria2 import Caneta
from canetapapelaria2 import Papelaria

exemplo1 = Caneta("Bic", "Vermelha", True, "5.0")
exemplo2 = Caneta("Faber castell", "Azul", False, "2.0")

exemplo2.escrever("É um dia feliz! Apareceu a vacina! =)")
exemplo2.escrever("Vora passsear! Chega de confinamento! =)")
exemplo1.escrever("Mas esse dia ainda não é hoje... =(")

objetoPapelaria = Papelaria("Calunga", "333.444.555/0001-04", "Rua Teste, 6")
objetoPapelaria.addCaneta(exemplo2)
print(objetoPapelaria.listaCanetas[0].cor)
objetoPapelaria.addCaneta(exemplo1)
print(objetoPapelaria.listaCanetas[0].cor)
print(objetoPapelaria.listaCanetas[1].marca)