Bot Automatizado para Captação de Plantões Médicos

Se você é um médico que trabalha em plantões de clínica médica ou emergência, provavelmente está familiarizado com a insanidade que é conseguir plantões em grupos de WhatsApp, onde há uma perpétua competição entre 
médicos, especialmente recém-formados, para responder o mais rapidamente possível às oportunidades de coberturas. Assim que me formei, achei absurda a ideia de ter que ficar de plantão no WhatsApp para pegar plantões, 
razão pela qual decidi desenvolver este bot.
Ele foi criado para monitorar constantemente meu grupo de plantões favorito, filtrando as ofertas que me convém e as respondendo, tudo em menos de 1 segundo. 
Pode parecer difícil configurá-lo pela primeira vez, mas abaixo apresento um guia detalhado de como você pode configurar este bot em sua própria máquina. 
Sinta-se à vontade para utilizar o código como desejar, mas lembre-se de dar os devidos créditos. 
Bom grinding de plantões! :)

Pré-requisitos

Antes de usar este bot, você precisará:
1) Python 3.8 ou superior instalado no seu sistema: https://www.python.org/downloads/
2) Tesseract-OCR instalado no seu sistema.
3) As seguintes bibliotecas Python:
        pyautogui
        pytesseract
        Pillow

Você pode instalar as bibliotecas necessárias com o seguinte comando no prompt de comandos do windows (cmd):

    pip install pyautogui pytesseract Pillow

Instalando Tesseract-OCR
   Windows: Baixe e instale o Tesseract via GitHub oficial: https://github.com/UB-Mannheim/tesseract/wiki
 
Configuração  

    Clone ou baixe este projeto para o seu computador.

    Configure a Imagem da Seta:
    A imagem seta.png na pasta imagens é usada para identificar o botão de rolagem para baixo no tema 
    escuro do WhatsApp. Se você estiver usando o tema escuro, você não precisa mudar a imagem, caso 
    contrário, será necessário capturar uma nova imagem da seta correspondente ao seu tema e substituir 
    a imagem existente.

Encontre as Coordenadas Necessárias:
Use o script pos.py para encontrar as coordenadas x, y para as áreas de captura de tela e os locais de 
clique necessários em seu computador. 
Execute pos.py com o comando abaixo no cmd e mova o cursor para os locais desejados para descobrir as 
suas coordenadas:

    python pos.py
    
Atualize o Script bot.py:
    Com as coordenadas em mãos, atualize as variáveis em bot.py para corresponder às posições corretas 
    na sua tela:
    No arquivo bot.py, atualize as variáveis de coordenadas (x, y, largura, altura) na função 
    capturar_e_transcrever_texto com os valores obtidos:

    def capturar_e_transcrever_texto():
    x, y, largura, altura = 618, 844, 800, 68  # Atualize esses valores com as coordenadas de sua tela 
    onde as mensagens de whatsapp aparecem.
     
Atualize também as coordenadas de clique (campo_texto_x, campo_texto_y) na função responder_mensagem:

    def responder_mensagem():
    campo_texto_x, campo_texto_y = 1043, 967  # Atualize esses valores onde se encontra o campo de 
    mensagem, para que o bot certifique que está realmente digitando a mensagem antes de enviá-la.
   
Configurando Palavras-chave:    
Para personalizar quais mensagens o bot deve responder, ajuste as palavras-chave positivas e negativas na função deve_responder. 
Palavras-chave positivas são aquelas que devem estar presentes para que uma resposta seja enviada, enquanto palavras-chave negativas 
previnem a resposta caso estejam presentes na mensagem. Vamos ajustar o trecho do código para incluir as palavras-chave "irmãos penteados", 
"clínica", "médica", "ficha verde" como critérios para as mensagens às quais o bot deve responder, e "emergência", "ficha vermelha" como 
critérios para as mensagens que o bot deve ignorar:

    if re.search(r'irmãos penteados|clínica|médica|ficha verde', texto, re.IGNORECASE) and not re.search(r'emergência|ficha vermelha', texto, re.IGNORECASE):

Explicação:

Neste trecho de código, a função re.search() é usada duas vezes para aplicar a lógica de filtragem:

 A primeira chamada de re.search() procura por qualquer ocorrência das palavras-chave positivas no texto. Isso é feito utilizando o operador | (pipe) para significar "OU" entre as palavras-chave, portanto, se qualquer uma das palavras-chave "irmãos penteados", "clínica", "médica", ou "ficha verde" for encontrada no texto, essa parte da condição será avaliada como verdadeira.

 A segunda chamada de re.search() procura por qualquer ocorrência das palavras-chave negativas no texto, também usando o operador | para separá-las. Se qualquer uma das palavras "emergência" ou "ficha vermelha" for encontrada no texto, essa parte da condição será avaliada como verdadeira.

 O and not entre as duas chamadas de re.search() serve para garantir que o código só prosseguirá (isto é, considerará o texto como adequado para resposta) se a primeira condição for verdadeira (ou seja, contém pelo menos uma das palavras-chave positivas) e a segunda condição for falsa (ou seja, não contém nenhuma das palavras-chave negativas).

Como Isso Funciona na Prática:

O bot lê uma mensagem. Se a mensagem incluir palavras como "irmãos penteados", "clínica", "médica" ou "ficha verde", sem incluir "emergência" ou "ficha vermelha", o bot considera a mensagem como relevante e procede com a resposta "pego" para aceitar o plantão pelo usuário. Caso contrário, a mensagem é ignorada. Isso permite um filtro eficiente, focando apenas nas mensagens de interesse e excluindo as que contêm indicadores de serem não relevantes ou fora do escopo desejado pelo usuário.


Uso e créditos

Com o bot configurado, execute o script principal para iniciar a automação no cmd:

    python bot.py

O bot começará a monitorar as mensagens e responderá automaticamente com base nos critérios definidos no script.
Observações Finais
  Monitoramento: Supervisione o funcionamento do bot, especialmente nas primeiras execuções, para garantir que tudo esteja funcionando como esperado.
  Personalização: Adapte os critérios de resposta no script bot.py conforme necessário para atender às suas necessidades específicas.
