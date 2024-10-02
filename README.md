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
