Bot  para Captação de Plantões Médicos por vm.cabello

Se você é um médico que trabalha em plantões de clínica médica ou emergência, provavelmente está familiarizado com a insanidade que é conseguir plantões em grupos de WhatsApp, onde há uma perpétua competição entre 
médicos (especialmente recém-formados) para responder o mais rapidamente possível às oportunidades de coberturas. Sempre achei absurda a ideia de ter que ficar de plantão no WhatsApp para pegar plantões, 
razão pela qual desenvolvi este bot.
O bot monitora constantemente o seu grupo de Whatsapp de plantões favorito, filtrando as ofertas de interesse e as respondendo, tudo em menos de meio (1/2) segundo. 
Pode parecer difícil configurá-lo pela primeira vez, mas abaixo apresento um guia detalhado de como você pode configurar este bot em sua própria máquina. 
Sinta-se à vontade para utilizar o código como desejar, só não se esqueça de dar os devidos créditos. 
Bom grinding de plantões! :)

Pré-requisitos

Antes de usar este bot, você precisará:
1) Python 3.8 ou superior instalado no seu sistema (use o link a seguir): https://www.python.org/downloads/
2) Tesseract-OCR instalado no seu sistema.
3) As seguintes bibliotecas Python:
        pyautogui
        pytesseract
        Pillow

Você pode instalar as bibliotecas necessárias com o seguinte comando no prompt de comandos do windows (cmd):

    pip install pyautogui pytesseract Pillow

Instalando Tesseract-OCR
   Windows: Baixe e instale o Tesseract via GitHub oficial: https://github.com/UB-Mannheim/tesseract/wiki
 
Configuração (só é necessária na primeira vez)
1) Clone ou baixe este projeto para o seu computador.

2) Configure a Imagem da Seta (opcional):
    A imagem seta.png na pasta imagens é usada para identificar o botão de rolagem para baixo no tema 
    escuro do WhatsApp. Se você estiver usando o tema escuro, você não precisa fazer nada, caso 
    contrário, será necessário atualizar a imagem da seta correspondente ao seu tema.

3) Descubra as Coordenadas Necessárias:
Use o script pos.py para encontrar as coordenadas x, y para as áreas onde aparecem as mensagens (de preferência,
no canto inferior do campo de mensagens), a seta de rolagem e a caixa de enviar texto em seu computador. 
Execute pos.py com o comando abaixo no cmd e mova o cursor sobre as áreas de interesse para descobrir as 
suas coordenadas:

        python pos.py
    
5) Atualize o Script bot.py:
    Agora que você sabe as coordenadas, atualize as variáveis em bot.py para corresponder às posições corretas 
    na sua tela:
    No arquivo bot.py, atualize as variáveis de coordenadas (x, y, largura, altura) na função 
    capturar_e_transcrever_texto com os valores obtidos para a área de mensagens:

        def capturar_e_transcrever_texto():
        x, y, largura, altura = 618, 844, 800, 68  # Atualize esses valores com as coordenadas de sua tela 
        onde as mensagens de whatsapp aparecem.
     
Atualize também as coordenadas do campo de mensagem (campo_texto_x, campo_texto_y) na função responder_mensagem:

    def responder_mensagem():
    campo_texto_x, campo_texto_y = 1043, 967  # Atualize esses valores onde se encontra o campo de 
    mensagem, para que o bot certifique que está realmente digitando a mensagem antes de enviá-la.

Para atualizar as coordenadas da seta que faz a rolagem para baixo, edite o seguinte trecho:   

        localizacao_seta = pyautogui.locateCenterOnScreen(caminho_icone_seta, region=(1818, 848, 73, 66), confidence=0.8)
        
Configurando Palavras-chave:    
Para personalizar quais mensagens o bot deve responder, ajuste as palavras-chave positivas e negativas na função deve_responder. 
Palavras-chave positivas são aquelas que devem estar presentes para que uma resposta seja enviada, enquanto palavras-chave negativas 
previnem a resposta caso estejam presentes na mensagem. Vamos ajustar o trecho do código para incluir as palavras-chave "irmãos penteados", 
"clínica", "médica", "ficha verde" como critérios para as mensagens às quais o bot deve responder, e "emergência", "ficha vermelha" como 
critérios para as mensagens que o bot deve ignorar:

    if re.search(r'irmãos penteados|clínica|médica|ficha verde', texto, re.IGNORECASE) and not re.search(r'emergência|ficha vermelha', texto, re.IGNORECASE):


Como Isso Funciona na Prática:

O bot lê uma mensagem. Se a mensagem incluir palavras como "irmãos penteados", "clínica", "médica" ou "ficha verde", sem incluir "emergência" ou "ficha vermelha", o bot considera a mensagem como relevante e procede com a resposta "pego" para aceitar o plantão pelo usuário. Caso contrário, a mensagem é ignorada. Isso permite um filtro eficiente, focando apenas nas mensagens de interesse e excluindo as que contêm indicadores de serem não relevantes ou fora do escopo desejado.

Com o bot configurado, execute o script principal para iniciar a automação no cmd:

    python bot.py

O bot começará a monitorar as mensagens e responderá automaticamente com base nos critérios definidos no script.

Observações Finais

  Monitoramento: Supervisione o funcionamento do bot, especialmente nas primeiras execuções, para garantir que tudo esteja funcionando como esperado.

  Personalização: Adapte os critérios de resposta no script bot.py conforme necessário para atender às suas necessidades específicas.

  FAQ:
1- Por que usar o PyAutoGUI para criar um bot?
R: Essa foi a solução que encontrei para permitir que o bot responda de maneira mais rápida possível, sem infringir os termos de uso do WhatsApp.

2- Por que não recorrer a APIs externas ou clientes do WhatsApp?
R: O uso desses recursos pode levar ao banimento da conta no WhatsApp.

3- É necessário manter a janela do WhatsApp sempre aberta?
R: Sim, infelizmente, essa é a única forma de impedir que o WhatsApp consiga distinguir um bot de um usuário humano.
