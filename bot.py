import os
import logging

# Essa parte faz o Render "pensar" que estamos usando uma porta
PORT = os.environ.get('PORT', 8000)
logging.info(f"Simulando uma porta de rede: {PORT}")


import logging
from telegram import Bot
from telegram.constants import ParseMode  # Mudança aqui!
from apscheduler.schedulers.background import BackgroundScheduler
import os

# Pegando as variáveis de ambiente
TOKEN = os.getenv('TOKEN')
CANAL_ID = os.getenv('CANAL_ID')

bot = Bot(token=TOKEN)

# Código do bloco de anúncio da Monetag
BLOCO_ANUNCIO_MONETAG = """
<div style='min-width: 300px; min-height: 250px; text-align: center;'>
    <script src='//niphaumeenses.net/vignette.min.js' data-zone='8662990' data-sdk='show_8662990'></script>
</div>

<script>
    show_8662990().then(() => {
        alert('Você visualizou o anúncio e apoiou nosso canal! Obrigado.');
    });
</script>
"""

# Configuração de logs
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# Função para enviar o anúncio Monetag no canal
def enviar_anuncio():
    try:
        mensagem_anuncio = f"""
<b>📢 Anúncio Importante</b>

Visualize este anúncio para apoiar o nosso canal e continuar recebendo conteúdo gratuito!

{BLOCO_ANUNCIO_MONETAG}
"""
        bot.send_message(
            chat_id=CANAL_ID, 
            text=mensagem_anuncio, 
            parse_mode=ParseMode.HTML, 
            disable_web_page_preview=False
        )
        logging.info(f'Anúncio Monetag enviado para o canal {CANAL_ID}')
    except Exception as e:
        logging.error(f'Erro ao enviar o anúncio: {e}')

# Função principal para iniciar o bot
def main():
    logging.info('Iniciando o bot de anúncios com Monetag...')
    scheduler = BackgroundScheduler()
    scheduler.add_job(enviar_anuncio, 'interval', hours=5)
    scheduler.start()
    
    logging.info('Bot está rodando...')
    try:
        while True:
            pass  # Mantém o bot rodando
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logging.info('Bot finalizado.')

if __name__ == '__main__':
    main()
