Se você é um médico que trabalha em plantões de clínica médica ou emergência, provavelmente está familiarizado com a insanidade que é conseguir plantões em grupos de WhatsApp, onde há uma perpétua competição entre 
médicos, especialmente recém-formados, para responder o mais rapidamente possível às oportunidades de coberturas. Assim que me formei, achei absurdo a ideia de ter que ficar de plantão no WhatsApp para pegar plantões, 
razão pela qual decidi desenvolver este bot.
Ele foi criado para monitorar constantemente meu grupo de plantões favorito, filtrando as ofertas que me convém e as respondendo, tudo em menos de 1 segundo. 
Pode parecer difícil configurá-lo pela primeira vez, mas abaixo apresento um guia detalhado de como você pode configurar este bot em sua própria máquina. 
Sinta-se à vontade para utilizar o código como desejar, mas lembre-se de dar os devidos créditos. 
Bom grinding de plantões! :)

Pré-requisitos

Antes de usar este bot, você precisará:

    Python 3.8 ou superior instalado no seu sistema.
    Tesseract-OCR instalado no seu sistema.
    As seguintes bibliotecas Python instaladas:
        pyautogui
        pytesseract
        Pillow

Você pode instalar as bibliotecas necessárias com o seguinte comando no prompt de comandos do windows (cmd):

pip install pyautogui pytesseract Pillow

Instalando Tesseract-OCR

    Windows: Baixe e instale o Tesseract via GitHub oficial: https://github.com/UB-Mannheim/tesseract/wiki
    Linux: Use sudo apt-get install tesseract-ocr.
    macOS: Use brew install tesseract.

Configuração

    Clone ou baixe este projeto para o seu computador.

    Configure a Imagem da Seta:
    A imagem seta.png na pasta imagens é usada para identificar um botão específico no tema escuro do WhatsApp. Se você estiver usando um tema diferente, pode ser necessário capturar uma nova imagem da seta correspondente ao seu tema e substituir a imagem existente.

    Encontre as Coordenadas Necessárias:
    Use o script pos.py para encontrar as coordenadas x, y para as áreas de captura de tela e os locais de clique necessários em seu computador. Execute pos.py e mova o cursor para os locais desejados para obter as coordenadas.

    Atualize o Script bot.py:
    Com as coordenadas em mãos, atualize as variáveis em bot.py para corresponder às posições corretas na sua tela.

Uso

Com o bot configurado, execute o script principal para iniciar a automação no cmd:

python bot.py

O bot começará a monitorar as mensagens e responderá automaticamente com base nos critérios definidos no script.
Observações Finais

    Monitoramento: Supervisione o funcionamento do bot, especialmente nas primeiras execuções, para garantir que tudo esteja funcionando como esperado.
    Personalização: Adapte os critérios de resposta no script bot.py conforme necessário para atender às suas necessidades específicas.