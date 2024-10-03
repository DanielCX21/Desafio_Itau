# Desafio_Itau

Desenvolver uma estratégia de investimentos quantitativa.

11/09/2024
A estratégia será baseada no índice de medo e ganância e 
utilizará de uma abordagem psicológica do mercado.

A maioria dos investidores do mercado são sardinhas, como o mercado de
criptomoedas é mais "liberal", no sentido de que existem menos
instrumentos capazes de regulamentar as ações tomadas pelos investidores, 
ocorre que alguns fenômenos são frequentes como o FOMO e o FUD, 
que podem ser bem descritos utilizando os índices de medo e ganância.

FOMO: Ocorre na extrema ganância quando as sardinhas são bombardeadas
pelo aumento de preço e a promessa de dinheiro fácil e rápido, geralmente
é o momento em que se ouve que tal moeda é uma grande solução de camada 1,
a outra tem tecnologia disruptiva inovadora e dessa forma todos querem
estar posicionados, por mais que, quando se ouve esse tipo de informação, 
já está na hora de sair fora pelo menos com uma parte do patrimônio, pois
é a hora que os grandes players vão começar o despejo já que já estavam
posicionados no momento de medo(FUD).

FUD: Ocorre no medo extremo quando as sardinhas são bombardeadas por notícias
de crash, crises internas... Dessa forma, aqueles que estavam posicionados
na extrema ganância ávidos por dinheiro fácil e rápido serão devidamente 
engolidos pelo institucional que fará de tudo para que vendam nessa situação
catastrófica. E estarão vendendo para quem? Para as baleias que sabem que de 
fato tal ativo possui tecnologia disruptiva inovadora e pode ser de fato uma 
grande solução para algum problema.

Assim sendo, nossa estratégia consistirá em deixar o mercado ir para o extremo 
medo ou ganância e só agir quando ouver uma "desaceleração" do movimento.
Havendo desaceleração na ganância é indicativo de venda.
Havendo desaceleração no medo é indicativo de compra.

Tal fenômeno pode ser explicado, pois em pontos de grande aceleração para qualquer
um dos lados geralmente as sardinhas estão muito emotivas e o movimento de 
compra ou venda vai permanecer enquanto houver espaço para FOMO ou FUD.
Ao encerrar esse movimento, geralmente o mercado criptográfico "corrige" 
brutalmente essas anomalias.

12/09/2024
Falando sobre a aplicação em si, vamos interpolar os pontos do gráfico de medo e
ganância, porém para evitar instabilidades com muitos pontos não usaremos a 
interpolação de Lagrange e sim a interpolação de slipnes cubicas, dessa forma 
evitaremos instabilidade na extremidade que será o alvo da análise preservando 
a suavidade da curva. Com o polinomio criado podemos derivar sem problemas duas 
vezes e medir a acelaração com que a derivada começa a perder seu caráter.

13/09/2024
Ainda sobre a aplicação vamos fazer alguma analogia com algum fenômeno físico
provavelmente utilizando resistência do ar ou potencial elétrico. Ainda assim,
vamos utilizar a mesma estratégia citada em (12/09/2024). Porém o fenômeno físico
será uma forma de vizualização e analogia com o fenômeno psicológico utilizado
para fazer as compras e vendas.

21/09/2024
Após alguns dias apenas olhando e pensando sem sair do lugar, voltamos a realizar
progresso. Traçamos o gráfico do medo interpolando os pontos 3 a 3 em polinomios
cúbicos para que seja feita a segunda derivada e por consequência os pontos de 
inflexão. Além disso vamos deixar disponíveis alguns dados para que possam ser
levados em conta:
Por Agora:
1) Mudança na concavidade (*)
2) Período sem variação brusca no índice (Regressão linear do índice) (Reg Lin *)
3) Verificar quantos dias passamos longe do neutro (*)
4) Juntar os dois primeiros
5) Média móvel de 50 dias no volume (*)

25/09/2024
Vamos estabelecer entre os critérios acima mencionados pesos, assim teremos pontos
muito suscetíveis a fazer a compra e pontos em que não faz sentido, pois as condições
não são favoráveis. Testaremos aonde as condições se adaptam melhor para escolher
os melhores pesos possíveis.

30/09/2024
Como agrupar todas as informações de forma a se conectar com o problema original?
Uma possibilidade é calcular todas as vezes e encontrar os melhores valores na mão.
Outra abordagem é ir reduzindo a pequenos problemas que serão mais facilmente
resolvidos. De forma que tenhamos no final algo humanamente ruim, porém computacionalmente 
viável e numéricamente acessível.

02/10/2024
VolumeFROM -> Número total de unidades da moeda(fsym) transacionada no candle.
VolumeTO -> Número total de moeda base(tsym) transacionado no candle.
Divida to/from e veja um valor entre high e low no candle, pois dará um 
preço "médio" de uma média obtida atráves de todo o "preço do candle"
dividido por quantas moedas(fsym) passaram por ele. Assim, o volumeTO é 
o melhor para verificar pontos de alta liquidação. 
Geramos o RSI para fazer sinais de compra e venda e o de volume para sinal 
de operação (tanto faz compra e venda)!
Agora vamos analisar usando uma fórmula de previsão de preço achada através 
da resolução da eq dif da resistência do ar:

P(t) = P0 ( 1 + a * (G - F) * e ^ (b * t))

Que seria a posição ao resolver a equação dif da resistência do ar!

Para encontrar os valores de a e b vamos testar os melhores em um grande range 
de valores e a estratégia será a seguinte:

1°) Encontrar um bom ponto de entrada a partir de volume, RSI, e medo e ganância
2°) Prever o preço tanto para short quanto para long
3°) Colocar a ordem de venda a partir da previsão de um período de tempo
4°) Verificar se após o período de tempo especificado a ordem foi batida analisando 
todos os máximos(em caso de long) e todos os mínimos(em caso de short)
5°) Colocar um marcador para saber se já estou comprado ou vendido naquele ativo, assim
não podemos fazer operações com ele.

Problemas, sugestões e reflexões:

* Vamos trabalhar com diversos ativos, como fazer a ponderação?
-Podemos usar o market cap, mas para isso será nescessário outra requisição
em API para gerar os dados.
-Podemos usar algum índice de volatilidade, mas para isso será nescessário pesquisar
sobre os índices de volatilidade.
-Podemos usar valores arbitrários pensados atráves do bom senso(melhor opção, o bom senso
nunca nos trái).
-Podemos testar vários tipos de valores e ver o que melhor se encaixa para o futuro, porém 
tal estratégia não exclui a possibilidade de que resultado passado não é garantia de resultado futuro
e essa métrica não possui nenhuma analogia direta com o fenômeno em si.

* Como achar o melhor período de tempo?
-Podemos testar alguns períodos de tempo e ver o que melhor se encaixa.
Nesse caso não é igual ao último item da pergunta anterior, pois encontrariamos algo intrínseco 
ao ativo. Que é o melhor "timeframe" para se operar tal estratégia que ai sim possui um fundamento
por trás para ser estudada.
-Podemos arbitrar algum período de tempo?
-Sim, mas corremos o risco de perder a oportunidade de encontrar um "timeframe" muito bom 
para a estratégia.

* Os tempos serão somentes inteiros pela própria construção da fórmula, buscaremos uma previsão do 
preço após tantos dias, porém esse preço pode ser alcançado antes e não importa quando será 
alcançado desde que seja antes do tempo previsto, já que venderemos no preço de interesse.

* Sobre a afirmação anterior, caso o ativo atinja o alvo antes e atinjo outro alvo de operação
compraríamos novamente ou ficaríamos nesse ciclo de "x" dias.
-Nesse caso, fica claro que não é interessante estar em um ciclo de "x" dias já que estaríamos
perdendo muito potencial.

11/05/2024
Outra medida que pode ser feita é com base na "velocidade" de reações químicas que seguem o mesmo
principio. 

    dP/dT = P.K.(feg_index) => P = P0 * e ^ (K*I*t) resolvendo a eq dif...

Dessa vez podemos ter uma forma de encontrar um K particular para cada situação, ou podemos supor
o caso ideal de equilíbrio químico que K é fixo mantendo condições parecidas.

Outro método parecido seria fazer com que:

    dP/dT = PKI - RP = P * (KI - R) e encontrar a situação que dP/dT que estava crescendo começa a

diminuir, ou seja, se torna 0 => K = R / I.

Contabilizando essas duas estratégias podemos dialéticamente chegar em uma síntese que seria o
primeiro modelo nos dar a base e o segundo nos dar uma certa margem de erro.
A partir disto pensaremos em qual modelo será utilizado o I.
Nesse caso o mais lógico parece ser usar I e [-50,50].
Desse modo, uma ganância extrema levaria a uma brusca variação de preço, assim como uma pequena
ganância levaria a uma pequena variação do preço, o que é o contrário do que ocorre na realidade.
Assim, vamos chegar a determinada fórmula ajustada:

    P = P0 * e ^ (k/I) sendo esse k = k * t e t é o time frame da estratégia que é fixo.

Assim, testaremos esse método com a margem de erro sendo e ^ ( - R * t), assim a intenção é buscar
uma margem que varia com base no preço inicial, já que a margem de erro deve mudar ao longo do tempo conforme
mudança na ordem de grandeza do preço.

Nesse caso não importa o que de fato seria a exponencial: e ^ ( - R * t), somente que ela é proporcional
ao preço inicial do ativo e obviamente será menor que a variação P - P0.

Tal margem de erro serviria como um "checkpoint", ou seja, caso o preço não atinja a ordem, mas chegue 
próximo, deixaremos o ativo se movimentando e caso retorne próximo ao preço inicial, venderemos no limite
da margem, obviamente conforme long ou short.

margem = (P - P0) * k e esse k e [0,1] sempre não importando se short ou long.

Esse k da forma que foi modelada deve ser um valor universal do ativo, uma propriedade intrínseca
ao material, sua cultura, a forma como se estabeleceu na sociedade ao longo do tempo e como o universo
de traders intuitivamente preve e mede seus riscos ao realizar os trades.

Como descobrir esse k?

Se prevemos um long e o ativo dentro do timeframe pensado só caiu, não teremos um bom espaço de 
análise, o mesmo para o short.
Assim, a melhor forma é verificar nos intervalos dados quando prevemos um long que não foi atingido
até onde o ativo foi. Esse "checkpoint" será medido e faremos algum tipo de média que se encaixe 
melhor nos nossos objetivos.
