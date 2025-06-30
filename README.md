Análise de Desempenho de Pipeline PDI - Arquitetura de Computadores
📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da avaliação da disciplina de Arquitetura de Computadores do curso de Engenharia da Computação da Universidade Federal do Maranhão (UFMA).

O objetivo principal é demonstrar de forma prática como diferentes etapas de um pipeline de Processamento Digital de Imagens (PDI) impactam a performance de um sistema. A aplicação simula um cenário comum em sistemas embarcados e visão computacional, onde uma imagem é capturada, pré-processada (redução de ruído) e submetida a uma tarefa de reconhecimento (detecção de objetos simulada).

A ferramenta permite analisar métricas de desempenho cruciais, como latência (em milissegundos) e taxa de quadros por segundo (FPS), conectando os conceitos teóricos de arquitetura de computadores aos gargalos computacionais de uma aplicação real.

🖼️ Interface da Aplicação
A aplicação conta com uma interface gráfica intuitiva que permite ao usuário carregar uma imagem, executar o pipeline de processamento e visualizar em tempo real os resultados e as métricas de desempenho.

(Imagem da interface da aplicação)

✨ Funcionalidades
Carregar Imagem: Permite selecionar uma imagem local nos formatos JPG, PNG, etc.

Controle de Parâmetros: Um slider interativo para ajustar a intensidade do filtro de redução de ruído.

Execução de Pipeline: Um único botão para executar todo o pipeline de processamento.

Visualização Comparativa: Exibe a imagem original e o resultado final lado a lado.

Relatório de Desempenho: Mostra a latência de cada etapa do pipeline e o FPS total estimado, atualizados a cada execução.

Salvar Resultado: Permite salvar a imagem processada no disco.

🛠️ Tecnologias Utilizadas
O projeto foi construído utilizando Python 3 e as seguintes bibliotecas:

CustomTkinter: Para a criação da interface gráfica moderna.

OpenCV (cv2): Para as funções de processamento de imagem, como a redução de ruído.

Pillow (PIL): Para a manipulação e exibição de imagens na interface.

NumPy: Para a manipulação eficiente de arrays, base para o OpenCV.

🚀 Como Executar o Projeto
Siga os passos abaixo para configurar e executar a aplicação em seu ambiente local.

Pré-requisitos
Python 3.8 ou superior.

Instalação
Clone o repositório ou baixe os arquivos para o seu computador.

Crie um ambiente virtual (recomendado):

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

Instale as dependências:

pip install opencv-python numpy customtkinter Pillow

Execução
Certifique-se de que você tem uma imagem de teste (ex: sua_imagem.jpg) na pasta do projeto ou em um local de fácil acesso.

Execute o script principal:

python nome_do_script.py

📖 Como Usar a Aplicação
Com a aplicação aberta, clique no botão "Carregar Imagem" e selecione um arquivo.

A imagem original será exibida à esquerda.

(Opcional) Ajuste o slider "Intensidade do Filtro" para um valor desejado.

Clique no botão "Executar Pipeline".

A imagem processada aparecerá à direita e o Relatório de Desempenho será atualizado com as novas métricas de latência e FPS.

(Opcional) Clique em "Salvar Resultado" para salvar a imagem final.

✒️ Autor
[JOÃO FELIPE PEREIRA CAMPOS] - joaofelipe4142@gmail.com
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
