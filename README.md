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

Falando sobre a aplicação em si, vamos interpolar os pontos do gráfico de medo e
ganância, porém para evitar instabilidades com muitos pontos não usaremos a 
interpolação de Lagrange e sim a interpolação de slipnes cubicas, dessa forma 
evitaremos instabilidade na extremidade que será o alvo da análise preservando 
a suavidade da curva. Com o polinomio criado podemos derivar sem problemas duas 
vezes e medir a acelaração com que a derivada começa a perder seu caráter.
