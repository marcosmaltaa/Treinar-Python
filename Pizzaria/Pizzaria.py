class Item:
    def __init__(self, nome, preco, data, peso) -> None:
        self.__nome = nome
        self.__preco_unitario = preco
        self.__data_validade = data
        self.__peso = peso

    
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getPrecoUnitario(self):
        return self.__preco_unitario
    
    def setPrecoUnitario(self, preco):
        self.__preco_unitario = preco

    def getDataValidade(self):
        return self.__data_validade
    
    def setDataValidade(self, data):
        self.__data_validade = data

    def getPeso(self):
        return self.__peso
    
    def setPeso(self, peso):
        self.__peso = peso

class Pizza(Item):
    
    def __init__(self, recheio, molho, borda, nome, preco, data, peso) -> None:
        super().__init__(nome, preco, data, peso)
        self.__recheio = recheio
        self.__molho = molho
        self.__borda = borda

    def getRecheio(self):
        return self.__recheio
    
    def setRecheio(self, recheio):
        self.__recheio = recheio

    def getMolho(self):
        return self.__molho
    
    def setMolho(self, molho):
        self.__molho = molho

    def getBorda(self):
        return self.__borda
    
    def setBorda(self, borda):
        self.__borda = borda

class Lanche(Item):

    def __init__(self,pao, recheio, molho, nome, preco, data, peso) -> None:
        super().__init__(nome, preco, data, peso)
        self.__pao = pao
        self.__recheio = recheio
        self.__molho = molho

    def getPao(self):
        return self.__pao
    
    def setPao(self, pao):
        self.__pao = pao

    def getRecheio(self):
        return self.__recheio
    
    def setRecheio(self, recheio):
        self.recheio = recheio

    def getMolho(self):
        return self.__molho
    
    def setMolho(self, molho):
        self.__molho = molho


class Pedido:
    def __init__(self, nome, item, taxa) -> None:
        self.__nome = nome
        self.__item = [item]
        self.__taxa = taxa


    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getItem(self):
        return self.__item
    
    def addItem(self, item):
        self.__item.append(item)

    def getTaxa(self):
        return self.__taxa
    
    def setTaxa(self, taxa):
        self.__taxa = taxa

    def calcularValor(self):
        total = sum(item.getPrecoUnitario() for item in self.__item)
        return total + self.__taxa
    
    def calcularTroco(self,valorRecebido):
        total = self.calcularValor()
        return valorRecebido - total


if __name__ == '__main__':
    pizza1 = Pizza("Calabresa", "Tomate", "Catupiry", "Pizza de calabresa", 24.5, 12/10/2024, 5.2)
    lanche1 = Lanche("Brioche", "X-bacon", "Cheedar", "X-bacon", 24.5, 10/10/2024, 0.7)

    pedido1 = Pedido("Alex", pizza1, 5.0)
    pedido1.addItem(lanche1)

    print(pedido1.calcularValor())
