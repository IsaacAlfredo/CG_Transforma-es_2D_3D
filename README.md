# CG_Transformações_2D_3D

Alunos: Isaac Alfredo de Freitas Silva (18111335),

Antes de rodar o código, gostaria de avisar que a distribuição oficial do PyOpenGL não está funcionando, então tive que buscar uma distribuição não oficial. Caso tenha esse problema, o arquivo necessário está no diretório, o "PyOpenGL-3.1.6-cp310-cp310-win_amd64.whl", basta rodar: pip install "caminhoDoArquivo".

Não foi possível utilizar a matriz gerada pela primeira parte do código para modificar as figuras, visto que: 1- Não é possível passar parâmetros nos métodos "showscreen", uma vez que eles são usados no método da opengl "glutDisplayFunc" (no menuForma2d.py) e esse método não aceita callback como parâmetro; 2- Também não conseguimos fazer isso dentro do próprio escopo da função, isso faz a janela travar, provavelmente porque ela fica em loop e acaba bugando por conta dos inputs.

Pra contornar isso, criamos 3 exemplos de matrizes para testar. Eles estão em showscreen.py, as funções transfExemplo, transfExemplo2 e transfExemplo3. O primeiro usa apenas translação, rotação e escala; O segundo, usa essas transformações e suas respectivas transformações inversas, de modo que o objeto retorna para a forma inicial; O terceiro usa todas essas transformações, sem que se cancelem. O código por padrão está usando a primeira função como parâmetro dos métodos showScreen, você pode trocar para as outras duas neles (ou até mesmo editá-las).
