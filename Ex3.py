def calcular_distancia(consumo_km: int) -> int:
    litros = int(input('Quantos litros de gasolina há no seu tanque: '))
    return consumo_km * litros

print(f'Então seu carro irá pecorrer: {calcular_distancia(15)}Km')