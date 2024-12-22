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


09/10/2024

Uma grande parte já feita da parte mais dificill, temos agora que ajustar a ordem das condições na função
de compra para contemplar de forma certa cada caso analisado. O nosso timeframe será de mais de um dia e
nossa análise no tempo diário, não importando o que ocorre dentro da vela diária.
Devemos ter cuidado para não inventar uma estratégia que funciona com condições futurísitcas como por exemplo,
o ponto de máximo ou mínimo da vela. Devemos levar em conta os parâmetros absolutos da vela: abertura e fechamento
que sempre ocorrerão no mesmo horário e montar nosso trade system a partir dele. Os dados de máximo e mínimo 
que serão utilizados devem estar somente para observação dos fatos, não para comparação.
Como já discutido anteriormente, iremos ter um ponto de saída parcial baseado em uma constante da diferença
dos preços, assim poderemos aproveitar os grandes "pumps", mas fica a questão novamente:

*Iremos aproveitar de fato(?).

A resposta para essa pergunta não é simples, a constante utilizada vai medir tal fator, mas ainda assim 
poderemos ter uma constante que mede melhor os pumps e outra que consegue ganhar mais dinheiro. Da mesma
forma, iremos avaliar para outros períodos e verificar quais são as melhores constantes. Iremos avaliar
a estratégia contra o HODL em alguns períodos e podemos até tirar algumas previsões do futuro:
*A estratégia desempenha bem no inverno?
*A estratégia ganha em um ciclo completo?
*A estratégia ganha se aplicada em qualquer ponto do ciclo?
Todas essas perguntas devem ser respondidas com um backtest bem executado.

16/10/2024

Após dias iremos testar a estratégia da regressão linear do gráfico de medo e ganância.

17/10/2024

Estamos desenvolvendo após muitos testes com estratégias variadas a ideia da interpolação dos pontos
do gráfico de medo e ganância:
Ao interpolar o gráfico de medo e ganância encontraremos os possíveis pontos de compra e venda baseado 
no ângulo da reta de regressão linear.

A partir disso, vamos fazer a arctg e [-90°,90°] pegar seu módulo.

As vendas serão feitas na ganância e as compras no medo.

Precisamos implementar o mecanismo de short para operar na ponta da compra.

Revisar o método de obtenção do patrimônio.

Testes para serem analisados:

* Comparação da estratégia com um trade aleatório. SIM, trades aleatórios e ver o quão fácil é ganhar 
dinheiro com BTC.

* Comparação da estratégia com uma boa entrada no inverno e uma boa saída na bull run.

* Comparação da estratégia com um ciclo de 4 anos.

* Pegar os parâmetros para outros intervalos de tempo.

* Verificar a linearidade do parâmetro.

* Verificar o parâmetro mais seguro.

Mas... Antes de tudo isso, precisamos deixar o backtest muito preciso e genérico.
Para que todos os testes possam ser feitos com segurança e escalabilidade.

17/10/2024 A Tarde:

Arrumar o código do backtest final com a estratégia da curva para começar a plotar 
os gráficos e fazer as simulações.

18/10/2024:

Programa criado para fazer as análises nescessárias.

Também já temos o programa com os trades aleatórios. <-> Melhorar alguns parâmetros
para poder encontrar bons resultados de sorte em trades.

O principal motivo é argumentar que nossa estratégia não é baseada em sorte.

Agora basicamente devemos expandir a base de dados e simular os trades para várias
situações de forma a encontrar o melhor param1 e param2!

19/10/2024 Manhã:

Não vamos fazer operações para o medo neutro.
Ajustar o parâmetro dos ângulos no backtest e procurar parâmetros sólidos ao longo do tempo.
Adicionar o parâmetro de quantos trades eu realizo nos testes.

20/10/2024:

Adicionado programa visual que mostra as retas com as devidas regressões.
Não esquecer de pensar como será dividido o portfólio.

Procurar as regiões em que é aceitável fazer os trades dentro do plano (param1,param2).
De forma a encontrar o melhor parâmetro dentro de todos os intervalos. 

Para os próximos dias, pensar em como aumentar a segurança, encontrar um parâmetro que
meça risco x retorno das operações e dos parâmetros.

23/10/2024:
Inicialmente, pensamos em medir o risco como a média percentual das perdas. Podemos
fazer também como a média percentual dos ganhos/ média percentual das perdas para cada 
parâmetro. Temos também um gráfico de cores que indica quais parâmetros são "Aceitáveis".
A intercessão dos parâmetros mais aceitáveis e com menos risco medidos em todos os timeframes
serão os melhores parâmetros e um deles será escolhido universalmente para cada moeda.

Podemos também se sobrar tempo escolher os melhores parâmetros para as metas desejadas.
Porém, em investimentos não devemos levar em conta o tempo para que nosso ativo se valorize,
mas sim o risco e o retorno envolvidos na operação. Obviamente, se as probabilidades estão a 
nosso favor a tendência é mais trades => mais lucros e por aí vai...

Um dos fatores interessantes também será o número de trades que o parâmetro executa, pois
se um parâmetro tem bom riscoxretorno e realiza muitos trades, como explicado acima, a 
tendência é aumentar o patrimônio.

Agora falando sobre a apresentação temos o seguinte:

*máx 10 páginas(contando com capa e bibliografia).
*máx 2500 palavras.
*máx 12 gráficos(saber escolher bem).
*máx 12 tabelas.

As duas primeiras são obrigatórias e o resto vale o bom senso, mas basta saber escolher bem.

O objetivo do desafio: 

*Criar e apresentar uma estratégia quantitativa de investimentos e convencer o gestor
de fundo a colocá-la no portfólio, ou considerar a possibilidade de saber mais sobre a 
proposta.

*Comunicação mais prática e direta.

*Explicar a tese de investimento.

*Explicar a regra de investimento.

*Explicar a origem.

*Explicar de onde saiu.

*Explicar as fontes de dados.

*Mostrar resultados(melhor parte).

*Consistência 
*risco
*robustez

*Comentar BACKTEST

*Conclusão

***AVALIAÇÃO***:

1 - Apresentação do robô(5%)

2 - Conceito da estratégia(30%)

3 - Modelagem(15%)

4 - Backtest(20%)

5 - Resultados(20%)

6 - Conclusão(10%)

Temos bons dados para ir adiante.

25/10/2024:

Por agora, falta criar um programa que pegue a intercessão dos melhores parâmetros para que
seja feita a melhor escolha.

Além disso, ponderaremos os parâmetros com os fatores: Quantidade de trades, risco e aproveitamento.
Não sabemos ainda exatamente qual serão os critérios de desempate.

Implementar o algoritmo no scratch dentro de backtest_time

26/10/2024:

Verificando a margem aceitável para algumas datas que não nescessariamente são as que serão usadas
chegamos em 0,645 como o mais aceitável por enquanto. Testar no teste_unitário os parâmetros retornados
e ver qual que se adapta melhor nos testes de risco...

Basta definir os períodos com base nos dados, testar a aceitação e escolher os melhores.

Começar com a ideia(Problema a ser resolvido) -> Solução
Explicação Fundamentalista

Robô

Modelagem

Backtest

Conclusão

03/11/2024

Fase de conclusão - Para essa semana encontrar os melhores ângulos para as 5 moedas.

Períodos:

1) Todo período possível.

2) 4 Anos a partir do ano de halving até o ano pré halving seguinte - fim de 2019 até fim de 2023

3) 1 Ano de cada vez - Terá menor peso na decisão.

4) Caso não de os 4 anos testar somente todo o período possível.

Ou seja, 5 ou 6 medidas.
5 para SOL e 6 para o resto.

Dados todos corrigidos e agora estão sincronizados desde 01/02/2018 -> 11/09/2024

Nem todas as moedas tinham o fear_greed_value até o período inicial, então em dados é feita essa checagem 
e aonde não tem é inserido o do BTC que está completo até 01/02/2018.

31/10/2024:

Arrumar os dados de ADA, ETH, BNB

03/11/2024

Não vai mais ter BNB!

Fase de conclusão - Para essa semana encontrar os melhores ângulos para as 5 moedas.

Períodos:

1) Todo período possível.

2) 4 Anos a partir do ano de halving até o ano pré halving seguinte - fim de 2019 até fim de 2023

3) 1 Ano de cada vez - Terá menor peso na decisão.

4) Caso não de os 4 anos testar somente todo o período possível.

Ou seja, 5 ou 6 medidas.
5 para SOL e 6 para o resto.

Dados todos corrigidos e agora estão sincronizados desde 01/02/2018 -> 11/09/2024

Nem todas as moedas tinham o fear_greed_value até o período inicial, então em dados é feita essa checagem 
e aonde não tem é inserido o do BTC que está completo até 01/02/2018.

08/11/2024

Agora basta escolher o parâmetro certo para esses TIMEFRAMES
utilizar o teste_unitario para pegar os resultados.
Todos os programas já estão perfeitos, basta os resultados.
