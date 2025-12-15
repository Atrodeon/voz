import speech_recognition as sr
import pyttsx3
import webbrowser
import urllib.parse # Para formatar a pesquisa

# --- MÓDULO 1: Text-to-Speech ---
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# --- MÓDULO 2: Speech-to-Text ---
def ouvir_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🤖 Assistente está ouvindo...")
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)
    
    try:
        comando = r.recognize_google(audio, language="pt-BR")
        print(f"🎤 Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

# --- MÓDULO 3: Processamento e Ações ---
def executar_comando(texto_comando):
    # 1. Abrir YouTube
    if "youtube" in texto_comando or "vídeo" in texto_comando:
        falar("Abrindo o YouTube.")
        webbrowser.open("https://www.youtube.com")
        
    # 2. Pesquisar na Wikipedia
    elif "pesquisar" in texto_comando or "procurar" in texto_comando:
        falar("O que você deseja pesquisar?")
        termo_pesquisa = ouvir_comando() # Pede o termo em um novo ciclo de audição
        
        if termo_pesquisa:
            falar(f"Pesquisando sobre {termo_pesquisa} na Wikipédia.")
            # Codifica o termo para que o link funcione
            termo_url = urllib.parse.quote(termo_pesquisa)
            webbrowser.open(f"https://pt.wikipedia.org/wiki/{termo_url}")
            
    # 3. Localizar Farmácia
    elif "farmácia" in texto_comando or "drogaria" in texto_comando:
        falar("Buscando farmácias próximas no Google Maps.")
        webbrowser.open("https://www.google.com/maps/search/farmácia+próxima")
        
    # Resposta padrão
    else:
        falar("Desculpe, não reconheci este comando de automação.")

# --- LOOP PRINCIPAL DO ASSISTENTE ---
def assistente_virtual_main():
    falar("Olá, assistente virtual ativado. Diga um comando.")
    
    while True:
        comando = ouvir_comando()
        
        if comando:
            # Comando de SAIR para encerrar
            if "parar" in comando or "sair" in comando or "desligar" in comando:
                falar("Até logo! Desligando o assistente.")
                break 
            
            # Executa as ações definidas
            executar_comando(comando)

# Inicia o Assistente:
if __name__ == "__main__":
    assistente_virtual_main()