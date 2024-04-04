from Pizzaria import *
import datetime

pizza1 = Pizza("Mussarela", "Tomate", "Queijo", "Pizza de Mussarela", 45.60, datetime.datetime(2023, 4, 6), 1.5)
pizza2 = Pizza("Peperoni", "Tomate", "Crocante", "Pizza de Peperoni", 40.0, datetime.datetime(2023, 4, 6), 1.6)

lanche1 = Lanche("Brioche", "Tudo", "Ketchup", "X-tudo com tomate", 23.50, datetime.datetime(2023, 4, 6),0.6)
lanche2 = Lanche("Brioche", "Bacon", "Barbecue", "X-bacon", 26.50, datetime.datetime(2023, 4, 6),0.5)

pedido1 = Pedido("Lucas", pizza1, 15.3)
pedido1.addItem(lanche2)
pedido1.addItem(lanche1)

print(f"Valor do pedido: R${pedido1.calcularValor():.2f}")
print(f"O troco deve ser: R${pedido1.calcularTroco(150.0):.2f}")