import datetime
import os
import platform
import webbrowser
import speech_recognition as sr

# Tenta usar pyttsx3 para resposta por voz (se instalado)
try:
  import pyttsx3

  engine = pyttsx3.init()
except ImportError:
  engine = None


def falar(texto):
  """Emite resposta por voz e no console."""
  print(f'🤖 Assistente: {texto}')
  if engine:
    engine.say(texto)
    engine.runAndWait()


def ouvir_microfone():
  """Captura áudio do microfone e converte em texto via Google Speech Recognition."""
  recognizer = sr.Recognizer()

  with sr.Microphone() as source:
    # Redução de ruído ambiente
    recognizer.adjust_for_ambient_noise(source, duration=0.8)
    print('\n🎤 Ouvindo... Fale um comando:')
    audio = recognizer.listen(source)

  try:
    frase = recognizer.recognize_google(audio, language='pt-BR')
    print(f'👤 Você disse: "{frase}"')
    return frase.lower()

  except sr.UnknownValueError:
    falar('Não consegui entender o que você disse.')
    return ''
  except sr.RequestError as e:
    falar('Erro de conexão com o serviço de reconhecimento.')
    return ''


def executar_comando(comando):
  """Interpreta o comando de voz e executa a automação correspondente."""
  if not comando:
    return True

  # 1. Abrir Navegador
  if 'abrir navegador' in comando or 'abrir google' in comando:
    falar('Abrindo o navegador.')
    webbrowser.open('https://www.google.com')

  # 2. Pesquisar na Web
  elif 'pesquisar' in comando or 'buscar' in comando:
    termo = (
        comando.replace('pesquisar sobre', '')
        .replace('pesquisar', '')
        .replace('buscar', '')
        .strip()
    )
    if termo:
      falar(f'Pesquisando por {termo} no Google.')
      webbrowser.open(f'https://www.google.com/search?q={termo}')
    else:
      falar('O que você gostaria que eu pesquisasse?')

  # 3. Abrir YouTube / Tocar Música
  elif 'youtube' in comando or 'música' in comando:
    falar('Abrindo o YouTube.')
    webbrowser.open('https://www.youtube.com')

  # 4. Informar Horário
  elif 'horas' in comando or 'horário' in comando:
    agora = datetime.datetime.now().strftime('%H:%M')
    falar(f'Agora são {agora}.')

  # 5. Encerrar
  elif 'encerrar' in comando or 'sair' in comando or 'fechar' in comando:
    falar('Até logo! Encerrando assistente.')
    return False

  else:
    falar(
        'Comando não reconhecido. Você pode pedir para abrir o navegador, pesquisar algo ou ver as horas.'
    )

  return True


def main():
  falar('Olá! Sou sua assistente de automação por voz. Como posso ajudar?')
  ativo = True
  while ativo:
    comando = ouvir_microfone()
    ativo = executar_comando(comando)


if __name__ == '__main__':
  main()
