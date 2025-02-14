import os
import webbrowser
from playsound3 import playsound

def executar_comando(frase):
    if not frase:
        return
    
    if 'navegador' in frase or 'chrome' in frase:
        os.system('Start chrome.exe')  # Google Chrome
        playsound('frases_voice_python/chrome.mp3')
    elif 'calculadora' in frase:
        os.system('Start calc.exe')  # Calculadora
        playsound('frases_voice_python/calculadora.mp3')
    elif 'bloco de notas' in frase:
        os.system('Start notepad.exe')  # Bloco de Notas
        playsound('frases_voice_python/bloco_de_notas.mp3')
    elif 'explorador de arquivos' in frase:
        os.system('Start explorer.exe')  # Explorador de Arquivos
        playsound('frases_voice_python/explorador_de_arquivos.mp3')
    elif 'paint' in frase:
        os.system('Start mspaint.exe')  # Paint
        playsound('frases_voice_python/paint.mp3')
    elif 'gerenciador de tarefas' in frase:
        os.system('Start taskmgr.exe')  # Gerenciador de Tarefas
        playsound('frases_voice_python/gerenciador_de_tarefas.mp3')
    elif 'prompt de comando' in frase or 'cmd' in frase:
        os.system('Start cmd.exe')  # Prompt de Comando
        playsound('frases_voice_python/cmd.mp3')
    elif 'wordpad' in frase or 'word pad' in frase:
        os.system('Start wordpad.exe')  # WordPad
        playsound('frases_voice_python/wordpad.mp3')
    elif 'powershell' in frase:
        os.system('Start powershell.exe')  # PowerShell
        playsound('frases_voice_python/powershell.mp3')
    elif 'configurações' in frase or 'painel de controle' in frase:
        os.system('Start control.exe')  # Painel de Controle
        playsound('frases_voice_python/configuracoes.mp3')
    elif 'vscode' in frase or 'visual studio code' in frase:
        os.system('Start code.exe')  # Visual Studio Code
        playsound('frases_voice_python/vscode.mp3')

    # Programas do Pacote Office
    elif 'word' in frase:
        os.system('Start winword.exe')  # Microsoft Word
        playsound('frases_voice_python/word.mp3')
    elif 'excel' in frase:
        os.system('Start excel.exe')  # Microsoft Excel
        playsound('frases_voice_python/excel.mp3')
    elif 'powerpoint' in frase:
        os.system('Start powerpnt.exe')  # Microsoft PowerPoint
        playsound('frases_voice_python/powerpoint.mp3')
    elif 'outlook' in frase:
        os.system('Start outlook.exe')  # Microsoft Outlook
        playsound('frases_voice_python/outlook.mp3')
    elif 'onenote' in frase:
        os.system('Start onenote.exe')  # Microsoft OneNote
        playsound('frases_voice_python/onenote.mp3')

    # Programas do Pacote Adobe
    elif 'photoshop' in frase:
        os.system('Start photoshop.exe')  # Adobe Photoshop
        playsound('frases_voice_python/photoshop.mp3')
    elif 'illustrator' in frase:
        os.system('Start illustrator.exe')  # Adobe Illustrator
        playsound('frases_voice_python/illustrator.mp3')
    elif 'premiere' in frase:
        os.system('Start premiere.exe')  # Adobe Premiere Pro
        playsound('frases_voice_python/premiere.mp3')
    elif 'after effects' in frase:
        os.system('Start afterfx.exe')  # Adobe After Effects
        playsound('frases_voice_python/after_effects.mp3')

    # Sites
    elif 'google' in frase:
        webbrowser.open('https://www.google.com')  # Google
        playsound('frases_voice_python/google.mp3')
    elif 'youtube' in frase:
        webbrowser.open('https://www.youtube.com')  # YouTube
        playsound('frases_voice_python/youtube.mp3')
    elif 'facebook' in frase:
        webbrowser.open('https://www.facebook.com')  # Facebook
        playsound('frases_voice_python/facebook.mp3')
    elif 'instagram' in frase:
        webbrowser.open('https://www.instagram.com')  # Instagram
        playsound('frases_voice_python/instagram.mp3')
    elif 'twitter' in frase or 'x' in frase:
        webbrowser.open('https://www.twitter.com')  # Twitter
        playsound('frases_voice_python/twitter.mp3')
    elif 'linkedin' in frase:
        webbrowser.open('https://www.linkedin.com')  # LinkedIn
        playsound('frases_voice_python/linkedin.mp3')
    elif 'reddit' in frase:
        webbrowser.open('https://www.reddit.com')  # Reddit
        playsound('frases_voice_python/reddit.mp3')
    elif 'github' in frase:
        webbrowser.open('https://www.github.com')  # GitHub
        playsound('frases_voice_python/github.mp3')
    elif 'wikipedia' in frase:
        webbrowser.open('https://www.wikipedia.org')  # Wikipedia
        playsound('frases_voice_python/wikipedia.mp3')
    elif 'netflix' in frase:
        webbrowser.open('https://www.netflix.com')  # Netflix
        playsound('frases_voice_python/netflix.mp3')
    elif 'whatsapp' in frase:
        webbrowser.open('https://web.whatsapp.com')  # WhatsApp Web
        playsound('frases_voice_python/whatsapp.mp3')
    elif 'amazon' in frase:
        webbrowser.open('https://www.amazon.com')  # Amazon
        playsound('frases_voice_python/amazon.mp3')
    elif 'mercado livre' in frase:
        webbrowser.open('https://www.mercadolivre.com.br')  # Mercado Livre
        playsound('frases_voice_python/mercado_livre.mp3')
    elif 'ebay' in frase:
        webbrowser.open('https://www.ebay.com')  # eBay
        playsound('frases_voice_python/ebay.mp3')
    elif 'submarino' in frase:
        webbrowser.open('https://www.submarino.com.br')  # Submarino
        playsound('frases_voice_python/submarino.mp3')
    elif 'americanas' in frase:
        webbrowser.open('https://www.americanas.com.br')  # Americanas
        playsound('frases_voice_python/americanas.mp3')
    elif 'magazine luiza' in frase:
        webbrowser.open('https://www.magazineluiza.com.br')  # Magazine Luiza
        playsound('frases_voice_python/magazine_luiza.mp3')

    else:
        playsound('frases_voice_python/nao_encontrado.mp3')
