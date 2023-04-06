# APS4_ALGLIN

Esse é um projeto da matéria de Algebra Linear e Teoria da Informação do Insper para o curso de Ciência da Computação

## Descrição do Projeto
O projeto consiste em fazer a implementação da projeção de um mundo 3D em uma tela 2D usando o algoritmo da pinhole camera. No qual o objetivo deste projeto é fazer uma projeção em tempo real de um cubo em *wireframe* que gira em todas as direções das três dimensões.

# Projeto: a projeção 3D de um cubo

Neste projeto, utilizamos a biblioteca `pygame`, usando a função `pygame.draw.line` para desenhar as linhas na tela. Ademais, as transformações foram implementadas manualmente.

## Descrição Matemática 

O modelo matemático utilizado para o desenvolvimento do projeto foi o experimento da câmera pinhole, que consiste em mostrar de maneira simples como as imagens são formadas. Geometricamente, nós conseguimos representar esse experimento em um plano cartesiano $x,y$, como na imagem abaixo:
<img src="pinhole.png">

Na imagem, conseguimos visualizar o objeto, na coordenada $[x_o,y_o]$, o pinhole, que no exemplo está na coordenada $[0,0]$ e a imagem projetada, que se situa na coordenada $[x_p,y_p]$. Já que queremos encontrar o ponto $[x_p,y_p]$, podemos utilizar a seguinte dedução:

- A distância entre a imagem projetada e o pinhole é $d$ (distância focal), então podemos concluir que $x_p=-d$.

Através de semelhança de triângulos, podemos encontrar a razão entre as coordenadas $X$ e $Y$ da imagem e do objeto:

$$
\frac{y_p}{x_p} = \frac{y_o}{x_o}
$$

Logo, podemos encontrar a coordenada $Y_p$ substituindo $x_p$ por $-d$:

$$
Y_p = \frac{y_o}{x_o}(-d)
$$

Como queremos fazer transformações matriciais para a projeção, nós precisamos converter as coordenadas dos pontos em coordenadas homogêneas. Para isso, basta adicionar uma variável auxiliar, no exemplo vamos utilizar a variável $$z_p = \frac{-x_o}{d} $$, e então concluimos, por substituição, que $y_p z_p = y_o$.

Nós sabemos que, para chegar em uma matriz de transformação linear:

$$
\begin{bmatrix}
x_p\\
y_p\\
z_p
\end{bmatrix} =
M_t 
\begin{bmatrix}
x_o\\
y_o\\
z_o
\end{bmatrix}
$$

Portanto, podemos escrever a matriz de transformação linear como:

$$
M_t = 
\begin{bmatrix}
0 & 0 & -d\\
0 & 1 & 0\\
-1/d & 0 & 0
\end{bmatrix}
$$


### Rotações em direções arbitrárias

Em 3D, é possível rotacionar pontos ao redor de cada um dos eixos usando as matrizes:

### Projeções 3D

Uma projeção de 3D para 2D funciona de uma maneira muito parecida com a projeção de 2D para 1D que fizemos na aula. Uma boa ideia é imaginar um mundo 3D com dimensões X, Y, Z, de tal forma que o *pinhole* fica no ponto $[0,0,0]$ e o anteparo fica no plano $z=-d$.

### Como modelar e posicionar um cubo




### Rotações em direções arbitrárias

Em 3D, é possível rotacionar pontos ao redor de cada um dos eixos usando as matrizes:

$$
R_x = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) & 0 \\
0 & \sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_y = \begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_z = \begin{bmatrix}
\cos(\theta) & - \sin(\theta) & 0 & 0 \\
\sin(\theta) & \cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$




### Funcao 

### Funcao 


## Como rodar o projeto






    
## Prévia



## Autores

- [@st4pzz](https://github.com/st4pzz)
- [@WeeeverAlex](https://github.com/WeeeverAlex)
