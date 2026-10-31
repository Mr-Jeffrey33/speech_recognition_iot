# 🎙️ VoiceAssistant: Automação Residencial e de Software por Reconhecimento de Voz

> **Desafio de Projeto — Formação IoT Specialist (DIO)**  
> Desenvolvimento de uma assistente virtual inteligente capaz de capturar comandos de voz via microfone, processar linguagem natural e executar automações de software e navegação web com respostas bidirecionais (fala e texto).

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-Google%20API-orange)
![pyttsx3](https://img.shields.io/badge/pyttsx3-Text--to--Speech-green)
![Status](https://img.shields.io/badge/Status-Concluído-success)

---

## 📌 Visão Geral do Projeto

Interfaces baseadas em voz (**VUI - Voice User Interfaces**) são um dos pilares da **Internet das Coisas (IoT)** e da **Automação Residencial / Escritório Inteligente**, permitindo que usuários interajam com dispositivos de forma natural e sem o uso das mãos (*hands-free*).

Este projeto implementa uma assistente virtual em Python que:
1. Capta o fluxo de áudio pelo microfone em tempo real e aplica redução de ruído ambiente.
2. Realiza o reconhecimento de padrões de fala utilizando redes neurais via API do **Google Speech Recognition** para português do Brasil (`pt-BR`).
3. Analisa a intenção da fala do usuário (*Intent Parsing*).
4. Executa a ação solicitada (abertura de navegadores, pesquisas na web, consultas de horários ou multimídia).
5. Fornece retorno auditivo com sintetização de voz local (**Text-to-Speech** com `pyttsx3`).

---

## 🏗️ Arquitetura do Sistema

O fluxo de processamento de comandos segue a arquitetura clássica de assistentes inteligentes:

```
┌──────────────────┐      ┌─────────────────────────┐      ┌──────────────────────────┐      ┌────────────────────────┐
│  Entrada de Voz  │ ───> │ Reconhecimento de Fala  │ ───> │  Processamento & Lógica  │ ───> │ Atuação / Automação    │
│   (Microfone)    │      │  (SpeechRecognition)    │      │    (Intent Parsing)      │      │ (Web / Sistema / Fala) │
└──────────────────┘      └─────────────────────────┘      └──────────────────────────┘      └────────────────────────┘
```

1. **Captura & Filtro:** Ajuste dinâmico de sensibilidade ao ruído ambiente (`adjust_for_ambient_noise`).
2. **Reconhecimento (ASR):** Conversão de ondas sonoras em texto textual.
3. **Mapeamento de Ações:** Análise contextual dos gatilhos do comando.
4. **Execução & Feedback:** Abertura de serviços/páginas e confirmação sonora para o usuário.

---

## 🗣️ Comandos Suportados

| Comando Falado | Ação Executada | Retorno por Voz |
| :--- | :--- | :--- |
| *"Abrir navegador"* / *"Abrir Google"* | Abre a página inicial do Google | *"Abrindo o navegador."* |
| *"Pesquisar sobre [termo]"* | Abre o navegador diretamente na busca pelo termo | *"Pesquisando por [termo] no Google."* |
| *"Tocar música"* / *"Abrir YouTube"* | Abre a plataforma do YouTube | *"Abrindo o YouTube."* |
| *"Que horas são?"* / *"Horário"* | Consulta o relógio do sistema | *"Agora são HH:MM."* |
| *"Encerrar"* / *"Sair"* | Finaliza a execução do script | *"Até logo! Encerrando assistente."* |

---

## 💻 Tecnologias e Bibliotecas Utilizadas

* **Linguagem:** Python 3
* **Reconhecimento de Voz:** [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* **Sintetizador de Fala (TTS):** [pyttsx3](https://pypi.org/project/pyttsx3/)
* **Captura de Áudio:** [PyAudio](https://pypi.org/project/PyAudio/)
* **Automação Web/OS:** Módulos nativos `webbrowser`, `os` e `datetime`

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/SEU-USUARIO/voice-assistant-automation.git
cd voice-assistant-automation
```

### 2. Instalar as Dependências
```bash
pip install -r requirements.txt
```

> 💡 **Nota para macOS / Linux:** Caso encontre alguma restrição na instalação do PyAudio via pip:
> - No macOS com Homebrew: `brew install portaudio` e depois `pip install pyaudio`
> - No Linux Ubuntu/Debian: `sudo apt-get install python3-pyaudio`

### 3. Executar a Assistente
```bash
python assistente_voz.py
```
Fale no microfone quando aparecer a indicação `🎤 Ouvindo...`.

---

## 🔮 Expansões Futuras para IoT

* [ ] Integração com placa **ESP32 / Arduino** via protocolo serial ou MQTT para acionamento de relés e lâmpadas físicas.
* [ ] Integração com modelo local de linguagem (LLM) para respostas mais conversacionais.
* [ ] Implementação de palavra de ativação (*wake word* local, como *"Hey Assistente"*).

---

## 👨‍💻 Autor

Projeto desenvolvido por **[Jefferson Santos]** como parte da Formação **IoT Specialist** da [DIO (Digital Innovation One)](https://dio.me).
