
from bank.model.BankAccount import BankAccount
from random import choice, randrange

from pyspark.sql import SparkSession


def createBankAccounts(l_cantidad , tipo_cuenta):

    l_ba = [(BankAccount("Nombre"+ str(x), choice(tipo_cuenta))) for  x in range(l_cantidad) ]

    return l_ba

def createTransactions(lista_cuenta, numeroTransacciones):

    #first we deposite between 500k to 900k to all the accounts

    for i in lista_cuenta:
        i.depositar(randrange(500000,900000,50000))

    for j in range(numeroTransacciones):
        a = choice(lista_cuenta)
        action = choice(("D","R"))
        amount = randrange(100000, 150000)
        if action == "D":
            a.depositar(amount)
        elif action == "R" and (a.mostrar_saldo()>amount or (a.mostrar_saldo()<amount and a.tipo_cuenta == "corriente") ):
            a.retirar(amount)


if __name__ == "__main__":
    lista_tipo = ["ahorro","corriente"]

    ba = createBankAccounts(50,lista_tipo )

    createTransactions(ba,500)


    sp = SparkSession.builder.appName("Agg Demo").master("local[2]").getOrCreate()

    ba_df = sp.sparkContext.parallelize([(x.titular,x.tipo_cuenta ,x.mostrar_saldo()) for x in ba]).toDF(["titular","tipo_cuenta" ,"saldo"])

    ba_df.show(20)

    ba_negative = ba_df.where("saldo < 0 ")

    ba_negative.show()