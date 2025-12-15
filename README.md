# voz
Neste projeto foi desenvolvido um sistema de assistência virtual, utilizando PLN (Processamento de Linguagem Natural).
# 🤖 Assistente Virtual em Python (Jarvis Simples)

Um sistema de assistência virtual desenvolvido em Python, utilizando Processamento de Linguagem Natural (PLN) simples para transformar comandos de voz em ações automatizadas no sistema operacional.

Este projeto foi criado como parte de um desafio prático de desenvolvimento de sistemas inteligentes e automação.

---

## ✨ Funcionalidades

O assistente é capaz de interagir por voz e executar as seguintes tarefas:

* **🎙️ Reconhecimento de Fala (Speech-to-Text):** Converte a voz do usuário em texto.
* **🗣️ Síntese de Voz (Text-to-Speech):** Responde ao usuário por meio de voz.
* **🌐 Automação Web:** Abre sites e realiza buscas com base no comando de voz.

### Comandos de Voz Suportados

| Comando | Intenção | Ação Executada |
| :--- | :--- | :--- |
| "Abrir YouTube" / "Ver um vídeo" | Abrir Plataforma | Abre o navegador no YouTube. |
| "Pesquisar sobre [termo]" | Busca de Conhecimento | Abre uma página da Wikipedia com a pesquisa. |
| "Onde tem farmácia" / "Drogaria" | Localização | Abre o Google Maps buscando farmácias próximas. |
| "Parar" / "Desligar" / "Sair" | Encerramento | Finaliza o assistente virtual. |

---

## 🛠️ Tecnologias e Dependências

O projeto utiliza bibliotecas padrão do Python focadas em áudio e automação.

* **`SpeechRecognition`:** Para o Módulo de Fala (STT).
* **`pyttsx3`:** Para o Módulo de Resposta de Voz (TTS).
* **`PyAudio`:** Necessário para acessar o microfone.
* **`pypiwin32`:** Dependência para funcionamento do `pyttsx3` no Windows.
* **`webbrowser` & `urllib`:** Para automação de abertura e formatação de links web.

---

## ⚙️ Configuração e Execução

Para rodar este assistente em seu ambiente local, siga os passos abaixo:

### 1. Pré-requisitos

Certifique-se de ter o **Python 3.x** e o `pip` instalados. Se estiver usando ambientes como **Miniconda** ou **Anaconda**, ative o ambiente antes de instalar e rodar.

### 2. Instalação das Bibliotecas

Abra seu Terminal, Powershell ou CMD e execute o seguinte comando para instalar todas as dependências necessárias:

```bash
pip install SpeechRecognition pyttsx3 PyAudio pypiwin32
