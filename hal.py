import numpy as np
import matplotlib.pyplot as plt
import dados
import transform_data
from funcoes import *

tolerancia = 3

preco = dados.preco_close
medo = dados.medo
datas = dados.data
coefs_angular = list()
estou_comprado = False
patrimonio = 1
nome_moeda = dados.nome_arquivo[19:22]

print(f"ATIVO:{nome_moeda}")

data_inicio = transform_data.unix_dh(dados.data_inicio)[:-9]
data_final = transform_data.unix_dh(dados.data_final)[:-9]

escolha_data_inicial = str(input(f"Digite a data de inicio até {data_inicio}: "))

if transform_data.dh_unix(escolha_data_inicial) < dados.data_inicio:
    print(f"Será usada a data limite de {data_inicio}")
    inicio = 0
else:
    inicio = datas.index(escolha_data_inicial)

escolha_data_final = str(input(f"Digite a data final até {data_final}: "))

if transform_data.dh_unix(escolha_data_final) > dados.data_final:
    print(f"Será usada a data limite de {data_final}")
    fim = len(datas) + 1
else:
    fim = datas.index(escolha_data_final) + 1

datas = datas[inicio:fim]
preco = preco[inicio:fim]
medo = medo[inicio:fim]

escolha_long_short = int(input("(Long)(1) x (Long+Short)(2):"))

if escolha_long_short == 1:

    escolha_timeframes_unico = int(input("(Um timeframe)(1) x (Varios timeframes)(2)"))

    if escolha_timeframes_unico == 1:

        parametro = int(input("Qual sera o timeframe:"))  

        if parametro < 3:
            pass
        else:
            x = np.linspace(0,1,100)
            y = np.linspace(0,1,100)
            X,Y = np.meshgrid(x,y)
            Z = np.zeros(X.shape)

            angulos = criar_angulos(medo, parametro)

            for a in range(X.shape[0]):
                for b in range(X.shape[1]):
                    Z[a, b] = backtest(parametro,angulos,X[a,b],Y[a,b],medo,1,preco)[0]
    
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(X, Y, Z, cmap='viridis')
            ax.set_xlabel('Parâmetro-1')
            ax.set_ylabel('Parâmetro-2')
            ax.set_zlabel('Patrimônio final')
            plt.show()

            submatriz = Z[tolerancia:,tolerancia:]

            indices = np.unravel_index(np.argmax(submatriz),submatriz.shape)
            primeiro = int(indices[0]) + tolerancia
            segundo = int(indices[1]) + tolerancia
            print(f"Indices: {(primeiro,segundo)}. Parametros: {float(X[primeiro,segundo]),float(Y[primeiro,segundo])}")
            print(f"Maximo: {submatriz.max()}. Confirmacao: {Z[primeiro,segundo]}. Confirmacao: {backtest(parametro,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)}")
            print(f"Numero de trades:{backtest(parametro,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[1]}")
            print(f"(Retorno x risco) do parametro: {backtest(parametro,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[2]}")

    else:

        multiplicidade = preco[-1] / preco[0]

        if escolha_timeframes_unico == 2:
            
            parametro = int(input("Qual sera o timeframe limite:")) 

            if parametro < 3:
                print("não é possivel!")
                pass
            else:
                
                maximos = list()
                maximos_second = list()
                eixo_y = list()
                teste = []

                for time in range(3,parametro + 1):

                    x = np.linspace(0,1,100)
                    y = np.linspace(0,1,100)
                    X,Y = np.meshgrid(x,y)
                    Z = np.zeros(X.shape)

                    angulos = criar_angulos(medo, time)

                    for a in range(X.shape[0]):
                        for b in range(X.shape[1]):
                            Z[a, b] = backtest(time,angulos,X[a,b],Y[a,b],medo,1,preco)[0]

                    submatriz = Z[tolerancia:,tolerancia:]

                    print(submatriz.max())
                    indices = np.unravel_index(np.argmax(submatriz),submatriz.shape)
                    primeiro = indices[0] + tolerancia
                    segundo = indices[1] + tolerancia
                    print((int(primeiro),int(segundo)))
                    maximos.append({"timeframe":time,"maximo":float(submatriz.max()),"número de trades":int(backtest(time,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[1]),"Trades certos" : int(backtest(time,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[3])})
                    maximos_second.append({"indices":(int(primeiro),int(segundo)),"Aproveitamento": float(submatriz.max()/multiplicidade), "retorno x risco":float(backtest(time,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[2]), })

                    angulos.clear()
                    submatriz = np.zeros(submatriz.shape)
                    coefs_angular.clear()

                eixo_x = list(range(3,parametro + 1))

                for m in range(len(maximos)):
                    print(maximos[m])
                    print(maximos_second[m])
                    print("")

                for maximo in maximos:
                    eixo_y.append(maximo['maximo'])

                plt.plot(eixo_x,eixo_y)
                plt.show()
                print(f"Um possível melhor timeframe é: {escolhedor(maximos) + 3}")

            maximos.clear()
            maximos_second.clear()
            eixo_y.clear()
            teste.clear()
            eixo_x.clear()

        else:
            pass
else: 
    if escolha_long_short == 2:
        print("nada")
    else:
        pass
