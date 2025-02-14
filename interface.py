import tkinter as tk
from comparador import executar_comando
from comando_voz import escutar_voz
from playsound3 import playsound
from tkinter import PhotoImage

# Função para exibir a janela de dúvidas
def abrir_duvidas():
    duvidas_janela = tk.Toplevel(janela)
    duvidas_janela.title('Dúvidas')
    duvidas_janela.geometry('500x450')
    duvidas_janela.configure(bg='#e0f7fa')
    janela.withdraw() 

    # Função para voltar para a janela principal
    def voltar():
        duvidas_janela.destroy()
        janela.deiconify()

    # Função que toca o áudio com os apps e sites disponíveis
    def listar_apps_sites_audio():
        playsound('frases_voice_python/lista_apps_sites.mp3')

    # Função que toca o áudio com os comandos disponiveis
    def listar_comandos():
        playsound('frases_voice_python/lista_comandos.mp3')
    
    # Pular linha (texto invisivel)
    label_pular = tk.Label(duvidas_janela, text='')
    label_pular.pack(pady=15)

    # Título
    label_titulo = tk.Label(duvidas_janela, text='Qual é a sua dúvida?', font=('Arial', 16), bg='#e0f7fa')
    label_titulo.pack(pady=20, anchor="center")

    # Exibe botões de perguntas
    botao_apps_sites = tk.Button(duvidas_janela, text='Listar Apps e Sites', font=('Arial', 12), bg='#00796b', fg='white', command=listar_apps_sites_audio)
    botao_apps_sites.pack(pady=10, anchor="center")

    botao_apps_sites = tk.Button(duvidas_janela, text='Listar Comandos', font=('Arial', 12), bg='#00796b', fg='white', command=listar_comandos)
    botao_apps_sites.pack(pady=10, anchor="center")

    botao_explicacao_codigo = tk.Button(duvidas_janela, text='Não me conhece? Clique aqui', font=('Arial', 12), bg='#00796b', fg='white', command=lambda: playsound('frases_voice_python/explicacao_codigo.wav'))
    botao_explicacao_codigo.pack(pady=20, anchor="center")

    # Botão de voltar
    botao_voltar = tk.Button(duvidas_janela, text='Voltar', font=('Arial', 12), bg='#ff5722', fg='white', command=voltar)
    botao_voltar.pack(pady=20, anchor="center")

# Função que chama os modulos 
def on_button_click():
    frase = escutar_voz()
    executar_comando(frase)

 # Função que toca o áudio de bem vindo
def tocar_audio_inicio():
    playsound('frases_voice_python/bem_vindo.mp3')

# Criando a interface principal
janela = tk.Tk()
janela.title('Voice Python')
janela.geometry('500x450')
janela.configure(bg='#e0f7fa')
janela.iconbitmap('imagens/logo_voice_python.ico')

# Adicionando a logo
logo_img = PhotoImage(file='imagens/logo_voice_python.png')
logo_img = logo_img.subsample(5, 5)
label_logo = tk.Label(janela, image=logo_img, bg='#e0f7fa')
label_logo.pack(pady=0, anchor="center")

# Título
label_titulo = tk.Label(janela, text='Aperte o botão para falar', font=('Arial', 16), bg='#e0f7fa')
label_titulo.pack(pady=5, anchor="center")

# Botão para iniciar o reconhecimento de voz
botao_falar = tk.Button(janela, text='Falar', font=('Arial', 14), command=on_button_click, bg='#00796b', fg='white', width=20, height=2)
botao_falar.pack(pady=5, anchor="center")

# Texto informativo
label_info = tk.Label(janela, text='Clique para iniciar o reconhecimento de voz.', font=('Arial', 12), bg='#e0f7fa')
label_info.pack(pady=5, anchor="center")

# Pular linha (texto invisivel)
label_pular = tk.Label(janela, text='')
label_pular.pack(pady=0)

# Botão para abrir dúvidas
botao_duvidas = tk.Button(janela, text='Dúvidas? Clique aqui', font=('Arial', 12), command=abrir_duvidas, bg='#00796b', fg='white', width=20, height=1)
botao_duvidas.pack(pady=20, anchor="center")

# Frase de iniciação do codigo
janela.after(60, tocar_audio_inicio)

# Loop principal da janela
janela.mainloop()
