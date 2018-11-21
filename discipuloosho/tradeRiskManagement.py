#!/usr/bin/env python3

def userInput():
    while True:
        try:
            totalCapital = float(input("Capital total: "))
            percentageToRisk = float(input("Riesgo en %: "))
            entryPrice = float(input("Precio de entrada: "))
            stopLossPrice = float(input("Stop Loss: "))
            break
        except ValueError:
            print("Introduce números nada más\n")
            pass
    tradeParams = [totalCapital, percentageToRisk, entryPrice, stopLossPrice]
    return tradeParams

def assetsCalc(tradeParams):
    bitfinexTakerFee = 0.2 / 100.0
    capitalToRisk = (tradeParams[0] * (tradeParams[1]/100))
    lostByAssetUntilStopLoss = abs(tradeParams[2] - tradeParams[3])
    assetsToDeal = capitalToRisk / lostByAssetUntilStopLoss
    capitalToRisk -= ((assetsToDeal * tradeParams[2] * bitfinexTakerFee) + (assetsToDeal * tradeParams[3] * bitfinexTakerFee))
    assetsToDeal = capitalToRisk / lostByAssetUntilStopLoss
    return assetsToDeal

if __name__ == '__main__':
    tradeParams = userInput()
    print(f'Activos que operar: {int(assetsCalc(tradeParams))}')