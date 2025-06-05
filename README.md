# icqi-qml-project

## 📚 O que é o projeto?

Este projeto propõe e compara duas abordagens distintas para a **detecção de imagens geradas por inteligência artificial (IA)** a partir de um **classificador quântico variacional**, com ênfase em imagens sintéticas criadas por modelos generativos como GANs (Redes Adversárias Generativas) e Diffusion Models. Essa iniciativa, parte em consequência da crescente dificuldade em distinguir imagens artificiais de reais, fator que levanta sérias preocupações em áreas como jornalismo, verificação de autenticidade, segurança digital e arte. Assim, este trabalho busca explorar soluções tecnológicas capazes de mitigar esse desafio emergente.

O projeto se estrutura em duas arquiteturas principais:

## 📘 Modelo V1 – Utiliza da *Principal Component Analysis* (PCA) e Circuito Quântico variacional

Nesta abordagem, as imagens são pré-processadas e reduzidas em dimensão com o algoritmo PCA (Principal Component Analysis), gerando vetores com um número menor de características representativas. Esses vetores são, então, utilizados como entrada em um circuito quântico variacional. O foco está na aplicação de embeddings angulares para a codificação dos dados em qubits, utilizando templates de entrelaçamento disponíveis no PennyLane. O objetivo é testar o potencial da computação quântica como uma alternativa leve e escalável para tarefas de classificação binária, especialmente em cenários em que o poder computacional clássico seria um gargalo.

 ## 📗 Modelo V2 – Abordagem Clássica com Extração Manual de Características

Nesta segunda abordagem, são extraídas manualmente características visuais das imagens, como entropia, cor, textura e componentes de Fourier. Essas características alimentam arquiteturas clássicas como CNNs (Convolutional Neural Networks) e Transformers. Posteriormente, os vetores extraídos também podem ser utilizados como entrada em um circuito quântico variacional, permitindo a experimentação com diferentes estratégias de codificação (como embeddings em amplitude ou nos eixos RX, RY e RZ) e com várias combinações de camadas quânticas, para fins comparativos.

Ambas as abordagens utilizam validação cruzada, ajustes de funções de perda e diferentes otimizadores para construir classificadores binários robustos, capazes de distinguir com eficiência imagens reais de imagens artificiais.

O projeto busca não apenas identificar qual técnica apresenta melhor desempenho, mas também explorar a viabilidade prática e a escalabilidade de modelos híbridos quântico-clássicos em tarefas reais de classificação de imagens. Ao unir computação clássica com computação quântica, esta proposta pretende avançar o estado da arte na detecção de imagens geradas por IA, avaliando o potencial dessas novas tecnologias em aplicações críticas do mundo real.

