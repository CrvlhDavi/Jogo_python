# Jogo de Shooter 2D em Python

Este projeto foi desenvolvido como atividade prática da disciplina de Linguagem de Programação Aplicada, no 3º semestre do curso de Engenharia de Software da UNINTER. A proposta foi criar um jogo 2D em Python, aplicando conceitos de programação orientada a objetos (POO), lógica de controle, manipulação de grafos e interface com Pygame.

O jogo funciona como um shooter em perspectiva lateral, em que o jogador controla uma nave e enfrenta inimigos que aparecem ao longo do cenário. O objetivo é sobreviver ao tempo de partida, derrotar os inimigos e acumular pontos. O sistema também inclui a possibilidade de jogar em modo de 2 jogadores, tanto cooperativo quanto competitivo, permitindo partidas com mais de um usuário.

A linguagem principal utilizada foi Python, com uso de bibliotecas como Pygame para renderização gráfica e eventos do jogo, além de SQLite3 para armazenar e gerenciar os scores dos jogadores. Os dados são salvos em banco local, permitindo registrar nome do jogador, pontuação e data da partida, além de consultar os melhores resultados.

Durante o desenvolvimento, foram aplicadas boas práticas de programação, como organização por classes e módulos, reutilização de código, separação de constantes em um arquivo `Const.py`, criação de entidades genéricas e estruturação do projeto em arquivos específicos para cada funcionalidade. O arquivo `Const.py` concentra valores e definições gerais das entidades, como velocidade, vida, dano, delay de tiro e posições do cenário, facilitando manutenção e escalabilidade do código.

Também foi utilizado o versionamento com Git, incluindo a criação de commits, atualização do repositório, uso de branches e a organização do fluxo de desenvolvimento entre branch principal (`master`) e branches de funcionalidade (`feature`). O processo de pull, push e commits foi parte essencial do trabalho para registrar evoluções do projeto, testar alterações e manter o controle das versões desenvolvidas.

Além disso, o projeto utiliza `.gitignore` para evitar o envio de arquivos desnecessários ou temporários para o repositório, como arquivos de cache, arquivos de ambiente virtual e outros artefatos que não fazem parte do código principal. Isso ajuda a manter o repositório mais limpo e organizado.

O projeto foi uma oportunidade prática de aprendizagem sobre POO, modularização, controle de fluxo, manipulação de imagens, uso de banco de dados local, organização de código e desenvolvimento colaborativo com Git. Também reforçou a importância de boas práticas de versionamento, ramificação de código e trabalho em equipe durante o processo de criação de software.

