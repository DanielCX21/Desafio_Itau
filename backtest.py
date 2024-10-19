import numpy as np
import matplotlib.pyplot as plt
import dados

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
    for i in range(len(medo) - translacao):
        if not situacao_long and angulo[i] < (90 * param1) and medo[i + translacao] >= 0:
            #compra long!
            situacao_long, quantidade = compras_long(situacao_long,patrimonio,preco[i + translacao])
            #print(f"LONG:Comprei dia {datas[i + translacao]} por {preco[i + translacao]}")
        if situacao_long and angulo[i] < (90 * param2) and medo[i + translacao] < 0:
            #venda long!
            situacao_long, patrimonio = vendas_long(situacao_long,quantidade,preco[i + translacao])
            contador += 1
            #print(f"LONG:Vendi dia {datas[i + translacao]} por {preco[i + translacao]}")
    if situacao_long:
        patrimonio = quantidade * preco[-1]
        contador += 1
        #print(f"terminei comprado e vendi no ultimo dia por {datas[i + translacao]}")
    return patrimonio, contador

preco = dados.preco_close
medo = dados.medo
datas = dados.data
y_interpolar = list()
coefs_angular = list()
estou_comprado = False
estou_vendido = False
patrimonio = 1

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

            print(Z.max())
            print(np.unravel_index(np.argmax(Z),Z.shape))

            angulos.clear()
            Z = np.zeros(X.shape)
            x_interpolar.clear()

    else:
        if escolha_timeframes_unico == 2:
            
            parametro = int(input("Qual sera o timeframe limite:")) 

            if parametro < 3:
                print("não é possivel!")
                pass
            else:
                
                maximos = list()
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
                    print(Z.max())
                    print(np.unravel_index(np.argmax(Z),Z.shape))

                    maximos.append({"timeframe":time,"maximo":Z.max(),"indices":np.unravel_index(np.argmax(Z),Z.shape)})

                    angulos.clear()
                    Z = np.zeros(X.shape)
                    x_interpolar.clear()
                    coefs_angular.clear()
                    estou_comprado = False

                eixo_x = list(range(3,parametro + 1))

                print(maximos)

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
