import numpy as np
import matplotlib.pyplot as plt
import dados
import transform_data
from matplotlib.colors import BoundaryNorm
from matplotlib import cm
from funcoes import backtest, escolhedor

tolerancia = 3

preco = dados.preco_close
medo = dados.medo
datas = dados.data
y_interpolar = list()
coefs_angular = list()
estou_comprado = False
estou_vendido = False
patrimonio = 1
nome_moeda = dados.nome_arquivo[19:22]

if nome_moeda == 'BTC':
    multiplicador = 0.6
if nome_moeda == 'BNB':
    multiplicador = (3 / 4)
if nome_moeda == 'ETH':
    multiplicador = 0.5
if nome_moeda == 'ADA':
    multiplicador = (3 / 4)
if nome_moeda == 'SOL':
    multiplicador = 0.7

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
#os 3 começam em fase quando declarados => continuam em fase agora.
#os angulos serão definidos a partir desses dados.

escolha_long_short = int(input("(Long)(1) x (Long+Short)(2):"))

if escolha_long_short == 1:

    escolha_timeframes_unico = int(input("(Um timeframe)(1) x (Varios timeframes)(2)"))

    if escolha_timeframes_unico == 1:

        parametro = int(input("Qual sera o timeframe:"))  

        if parametro < 3:
            pass
        else:
            x_interpolar = list(range(1,(parametro + 1)))
            x = np.linspace(0,1,100)
            y = np.linspace(0,1,100)
            X,Y = np.meshgrid(x,y)
            Z = np.zeros(X.shape)

            for i in range(len(medo) - parametro + 1):
                for j in range(parametro):
                    y_interpolar.append(medo[i+j])
                angular = float(np.polyfit(x_interpolar,y_interpolar,1)[0])
                coefs_angular.append(angular)
                y_interpolar.clear()

            angulos = list()

            for coef in coefs_angular:
                informacao = float(np.fabs(np.degrees(np.arctan(coef))))
                angulos.append(informacao)

            #print(len(angulos))
            #print(len(datas))

            for a in range(X.shape[0]):
                for b in range(X.shape[1]):
                    Z[a, b] = backtest(parametro,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[0]
    
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(X, Y, Z, cmap='viridis')
            ax.set_xlabel('param1')
            ax.set_ylabel('param2')
            ax.set_zlabel('Patrimônio final')
            plt.show()

            submatriz = Z[tolerancia:,tolerancia:]

            indices = np.unravel_index(np.argmax(submatriz),submatriz.shape)
            primeiro = int(indices[0]) + tolerancia
            segundo = int(indices[1]) + tolerancia
            print(f"Indices: {(primeiro,segundo)}. Parametros: {float(X[primeiro,segundo]),float(Y[primeiro,segundo])}")
            print(f"Maximo: {submatriz.max()}. Confirmacao: {Z[primeiro,segundo]}. Confirmacao: {backtest(parametro,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)}")
            print(f"Numero de trades:{backtest(parametro,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[1]}")
            print(f"(Retorno x risco) do parametro: {backtest(parametro,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[2]}")

            aceitavel = submatriz.max() * (multiplicador)
            numero = 0

            for a in range(X.shape[0] - tolerancia):
                for b in range(X.shape[1] - tolerancia):
                    if submatriz[a,b] >= aceitavel:
                        first = a + tolerancia
                        second = b + tolerancia
                        #print((X[first,second],Y[first,second]))
                        numero += 1

            print(f"Pares de parâmetros possíveis: {numero}")
            Z = Z[:-1,:-1]
            intervalos = [0,(submatriz.max() / 4) ,aceitavel,Z.max()]
            colors = ['red','yellow','red']
            cmap = cm.get_cmap('RdYlBu', len(colors))
            norm = BoundaryNorm(intervalos, cmap.N)
            plt.pcolormesh(X, Y, Z, cmap=cmap, norm=norm, shading='flat')
            plt.colorbar(boundaries=intervalos, ticks=[0,(submatriz.max() / 4) ,aceitavel,Z.max()])
            plt.show()

            angulos.clear()
            Z = np.zeros(X.shape)
            x_interpolar.clear()

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

                for time in range(3,parametro + 1):

                    x_interpolar = list(range(1,(time + 1)))
                    x = np.linspace(0,1,100)
                    y = np.linspace(0,1,100)
                    X,Y = np.meshgrid(x,y)
                    Z = np.zeros(X.shape)

                    for i in range(len(medo) - time + 1):
                        for j in range(time):
                            y_interpolar.append(medo[i+j])
                        angular = float(np.polyfit(x_interpolar,y_interpolar,1)[0])
                        coefs_angular.append(angular)
                        y_interpolar.clear()

                    angulos = list()

                    for coef in coefs_angular:
                        informacao = float(np.fabs(np.degrees(np.arctan(coef))))
                        angulos.append(informacao)

                    for a in range(X.shape[0]):
                        for b in range(X.shape[1]):
                            Z[a, b] = backtest(time,estou_comprado,angulos,X[a,b],Y[a,b],medo,1,preco)[0]
                    submatriz = Z[tolerancia:,tolerancia:]

                    aceitavel = submatriz.max() * (multiplicador)
                    numero = 0

                    for a in range(X.shape[0] - tolerancia):
                        for b in range(X.shape[1] - tolerancia):
                            if submatriz[a,b] >= aceitavel:
                                #first = a + tolerancia
                                #second = b + tolerancia
                                #print((X[first,second],Y[first,second]))
                                numero += 1

                    print(submatriz.max())
                    indices = np.unravel_index(np.argmax(submatriz),submatriz.shape)
                    primeiro = indices[0] + tolerancia
                    segundo = indices[1] + tolerancia
                    print((int(primeiro),int(segundo)))
                    maximos.append({"timeframe":time,"maximo":float(submatriz.max()),"Pares possíveis":int(numero),"número de trades":int(backtest(time,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[1]), "retorno x risco":float(backtest(time,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[2])})
                    maximos_second.append({"indices":(int(primeiro),int(segundo)),"Aproveitamento": float(submatriz.max()/multiplicidade), "Trades certos" : int(backtest(time,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[3])})

                    angulos.clear()
                    Z = np.zeros(X.shape)
                    submatriz = np.zeros(submatriz.shape)
                    x_interpolar.clear()
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
                eixo_y.clear()
                eixo_x.clear()

                print(f"Um possível melhor timeframe é: {escolhedor(maximos) + 3}")

        else:
            pass
else:
    if escolha_long_short == 2:
        print("nada")
    else:
        pass
