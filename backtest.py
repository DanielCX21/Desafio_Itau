import numpy as np
import matplotlib.pyplot as plt
import dados
import transform_data
from matplotlib.colors import BoundaryNorm
from matplotlib import cm

medo_inicial = 0
tolerancia = 3

def media(vetor):
    if len(vetor) == 0:
        return 0
    else:
        med = 0
        for valor in vetor:
            med += valor
        return (med / (len(vetor)))
def compras_long(situacao,patrimonio, preco):
    quantidade = patrimonio / preco
    situacao = True
    tupla = (situacao,quantidade)
    return tupla
def vendas_long(situacao,quantidade, preco):
    patrimonio_final = quantidade * preco
    situacao = False
    tupla = (situacao,patrimonio_final)
    return tupla
def venda_short(situacao, patrimonio,preco):
    quantidade = patrimonio / preco
    situacao = True
    tupla = (situacao, quantidade)
    return tupla
def compra_short(situacao,quantidade,preco, patrimonio):
    patrimonio_final = (2 * patrimonio) - quantidade * preco
    situacao = False
    tupla = (situacao,patrimonio_final)
    return tupla
def backtest_sl(timeframe,situacao_long, situacao_short, angulo, datas, param1, param2, medo, patrimonio,preco):
    translacao = timeframe - 1
    for i in range(len(medo)):
        if not situacao_long and not situacao_short and angulo[i] < (90 * param1) and medo[i + translacao] <= 0:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            #print(f"LONG:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
        if situacao_long and not situacao_short and angulo[i] < (90 * param2) and medo[i + translacao] > 0:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            #print(f"LONG:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
        if not situacao_long and not situacao_short and angulo[i] < (90 * param2) and medo[i + translacao] > 0:
            #venda short!
            situacao_short, quantidade = venda_short(situacao_short,patrimonio,preco[i + translacao]) 
            #print(f"SHORT:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
        if not situacao_long and situacao_short and angulo[i] < (90 * param1) and medo[i + translacao] < 0:
            #compra short!
            situacao_short, patrimonio = compra_short(situacao_short,quantidade,preco[i + translacao],patrimonio)
            #print(f"SHORT:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
    if situacao_long:
        patrimonio = quantidade * preco[-1]
        #print(f"terminei comprado e vendi no ultimo dia por {datas[i + translacao]}")
    if situacao_short:
        patrimonio = (2 * patrimonio) - quantidade * preco[-1]
        #print(f"terminei vendido e vendi no último dia por {datas[i + translacao]}")
    return patrimonio
def backtest(timeframe,situacao_long,angulo, param1, param2, medo, patrimonio,preco):
    contador = 0
    translacao = timeframe - 1
    patrimonios = [1,1]
    perdas = list()
    ganhos = list()
    for i in range(len(medo) - translacao):
        if not situacao_long and angulo[i] < (90 * param1) and medo[i + translacao] > medo_inicial:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            #print(f"LONG:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
        if situacao_long and angulo[i] < (90 * param2) and medo[i + translacao] <  -medo_inicial:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            contador += 1
            #print(f"LONG:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
            patrimonios[0] = patrimonios[1]
            patrimonios[1] = patrimonio
            if patrimonios[1] < patrimonios[0]:
                perda_percentual = (patrimonios[0] - patrimonios[1]) / patrimonios[0]
                perdas.append(perda_percentual)
            if patrimonios[1] > patrimonios[0]:
                ganho_percentual = (patrimonios[1] - patrimonios[0]) / patrimonios[0]
                ganhos.append(ganho_percentual)
    if situacao_long:
        patrimonio = quantidade * preco[-1]
        contador += 1
        #print(f"terminei comprado e vendi no ultimo dia por {datas[i + translacao]}")
    if media(ganhos) == 0 or media(perdas) == 0:
        risco = False
    else:
        risco = media(ganhos) / media(perdas)
    perdas.clear() 
    return patrimonio, contador, risco

preco = dados.preco_close
medo = dados.medo
datas = dados.data
y_interpolar = list()
coefs_angular = list()
estou_comprado = False
estou_vendido = False
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
            primeiro = indices[0] + tolerancia
            segundo = indices[1] + tolerancia
            print(f"Indices: {(primeiro,segundo)}. Parametros: {X[primeiro,segundo],Y[primeiro,segundo]}")
            print(f"Maximo: {submatriz.max()}. Confirmacao: {Z[primeiro,segundo]}. Confirmacao: {backtest(parametro,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)}")
            print(f"Numero de trades:{backtest(parametro,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[1]}")
            print(f"(Retorno x risco) do parametro: {backtest(parametro,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[2]}")

            aceitavel = submatriz.max() * (3 / 5)
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
                    x = np.linspace(0,1,200)
                    y = np.linspace(0,1,200)
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

                    aceitavel = submatriz.max() * (3 / 4)
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
                    maximos.append({"timeframe":time,"maximo":float(submatriz.max()),"indices":(int(primeiro),int(segundo)),"número de trades":int(backtest(time,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[1]), "retorno x risco":float(backtest(time,estou_comprado,angulos,X[primeiro,segundo],Y[primeiro,segundo],medo,1,preco)[2])})
                    maximos_second.append({"Pares possíveis":int(numero), "Aproveitamento": float(submatriz.max()/multiplicidade)})

                    angulos.clear()
                    Z = np.zeros(X.shape)
                    submatriz = np.zeros(submatriz.shape)
                    x_interpolar.clear()
                    coefs_angular.clear()

                eixo_x = list(range(3,parametro + 1))

                for i in range(len(maximos)):
                    print(maximos[i])
                    print(maximos_second[i])
                    print("")

                for maximo in maximos:
                    eixo_y.append(maximo['maximo'])

                plt.plot(eixo_x,eixo_y)
                plt.show()

                eixo_x.clear()

        else:
            pass
else:
    if escolha_long_short == 2:
        print("nada")
    else:
        pass
