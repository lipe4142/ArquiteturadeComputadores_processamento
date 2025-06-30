# Para instalar as bibliotecas necessárias, abra seu terminal ou prompt de comando e execute:
# pip install opencv-python
# pip install numpy
# pip install customtkinter
# pip install Pillow
# Projeto de Arquitetura de Computadores

import tkinter
import customtkinter
from tkinter import filedialog
import cv2
from PIL import Image
import numpy as np
import time

# Define a aparência padrão da interface
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuração da Janela Principal ---
        self.title("Benchmark de Pipeline PDI")
        self.geometry("1200x700")

        # --- Configuração do Layout em Grid ---
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Variáveis de Estado ---
        self.imagem_original_cv = None
        self.imagem_final_cv = None

        # --- FRAME DE CONTROLES (Esquerda) ---
        self.frame_controles = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        self.frame_controles.grid(row=0, column=0, rowspan=2, sticky="nsw")
        self.frame_controles.grid_rowconfigure(6, weight=1)

        self.label_titulo_controles = customtkinter.CTkLabel(self.frame_controles, text="Controles do Pipeline", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_titulo_controles.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.botao_carregar = customtkinter.CTkButton(self.frame_controles, text="Carregar Imagem", command=self.carregar_imagem)
        self.botao_carregar.grid(row=1, column=0, padx=20, pady=10)

        self.label_slider = customtkinter.CTkLabel(self.frame_controles, text="Intensidade do Filtro:")
        self.label_slider.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="w")
        self.slider_intensidade = customtkinter.CTkSlider(self.frame_controles, from_=1, to=30, number_of_steps=29)
        self.slider_intensidade.set(10)
        self.slider_intensidade.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew")

        self.botao_executar = customtkinter.CTkButton(self.frame_controles, text="Executar Pipeline", command=self.executar_pipeline)
        self.botao_executar.grid(row=4, column=0, padx=20, pady=10)
        
        self.botao_salvar = customtkinter.CTkButton(self.frame_controles, text="Salvar Resultado", command=self.salvar_resultado, state="disabled")
        self.botao_salvar.grid(row=5, column=0, padx=20, pady=10)

        # --- FRAME DO RELATÓRIO DE DESEMPENHO ---
        self.frame_relatorio = customtkinter.CTkFrame(self.frame_controles)
        self.frame_relatorio.grid(row=7, column=0, padx=20, pady=20, sticky="sew")
        
        self.label_titulo_relatorio = customtkinter.CTkLabel(self.frame_relatorio, text="Relatório de Desempenho", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.label_titulo_relatorio.pack(pady=(10, 5))
        
        self.label_latencia_prep = customtkinter.CTkLabel(self.frame_relatorio, text="Latência Pré-proc.: -- ms")
        self.label_latencia_prep.pack()
        self.label_latencia_det = customtkinter.CTkLabel(self.frame_relatorio, text="Latência Detecção: -- ms")
        self.label_latencia_det.pack()
        self.label_latencia_total = customtkinter.CTkLabel(self.frame_relatorio, text="Latência Total: -- ms", font=customtkinter.CTkFont(weight="bold"))
        self.label_latencia_total.pack(pady=(5,0))
        self.label_fps = customtkinter.CTkLabel(self.frame_relatorio, text="FPS Estimado: --", font=customtkinter.CTkFont(weight="bold"))
        self.label_fps.pack(pady=(0,10))

        # --- FRAME DA IMAGEM ORIGINAL (Centro) ---
        self.label_titulo_original = customtkinter.CTkLabel(self, text="Imagem Original", font=customtkinter.CTkFont(size=16))
        self.label_titulo_original.grid(row=0, column=1, padx=10, pady=(10,0), sticky="n")
        self.frame_original = customtkinter.CTkFrame(self)
        self.frame_original.grid(row=0, column=1, padx=10, pady=(40,10), sticky="nsew")
        self.label_original = customtkinter.CTkLabel(self.frame_original, text="Carregue uma imagem")
        self.label_original.pack(padx=10, pady=10, expand=True)

        # --- FRAME DA IMAGEM PROCESSADA (Direita) ---
        self.label_titulo_processada = customtkinter.CTkLabel(self, text="Resultado do Pipeline", font=customtkinter.CTkFont(size=16))
        self.label_titulo_processada.grid(row=0, column=2, padx=10, pady=(10,0), sticky="n")
        self.frame_processada = customtkinter.CTkFrame(self)
        self.frame_processada.grid(row=0, column=2, padx=10, pady=(40,10), sticky="nsew")
        self.label_processada = customtkinter.CTkLabel(self.frame_processada, text="O resultado aparecerá aqui")
        self.label_processada.pack(padx=10, pady=10, expand=True)

    def carregar_imagem(self):
        caminho_imagem = filedialog.askopenfilename(filetypes=[("Arquivos de Imagem", "*.jpg *.jpeg *.png *.bmp")])
        if not caminho_imagem:
            return

        self.imagem_original_cv = cv2.imread(caminho_imagem)
        self.exibir_imagem(self.imagem_original_cv, self.label_original)
        self.label_processada.configure(image=None, text="Pronto para processar")
        self.botao_salvar.configure(state="disabled")

    def executar_pipeline(self):
        if self.imagem_original_cv is None:
            tkinter.messagebox.showwarning("Aviso", "Por favor, carregue uma imagem primeiro.")
            return

        intensidade = self.slider_intensidade.get()

        # Etapa 2: Pré-processamento
        inicio_prep = time.perf_counter()
        img_sem_ruido = cv2.fastNlMeansDenoisingColored(self.imagem_original_cv, None, h=intensidade, hColor=intensidade, templateWindowSize=7, searchWindowSize=21)
        fim_prep = time.perf_counter()
        latencia_prep = (fim_prep - inicio_prep) * 1000

        # Etapa 3: Detecção Simulada
        inicio_det = time.perf_counter()
        self.imagem_final_cv = img_sem_ruido.copy()
        cv2.rectangle(self.imagem_final_cv, (350, 100), (600, 450), (0, 255, 0), 3)
        cv2.putText(self.imagem_final_cv, 'Objeto A', (355, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(self.imagem_final_cv, (700, 250), (850, 400), (255, 0, 0), 3)
        cv2.putText(self.imagem_final_cv, 'Objeto B', (705, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        time.sleep(0.04) # Simula atraso da rede neural
        fim_det = time.perf_counter()
        latencia_det = (fim_det - inicio_det) * 1000

        # Exibir resultado
        self.exibir_imagem(self.imagem_final_cv, self.label_processada)
        self.botao_salvar.configure(state="normal")

        # Atualizar relatório
        latencia_total = latencia_prep + latencia_det
        fps = 1000 / latencia_total if latencia_total > 0 else float('inf')
        self.label_latencia_prep.configure(text=f"Latência Pré-proc.: {latencia_prep:.2f} ms")
        self.label_latencia_det.configure(text=f"Latência Detecção: {latencia_det:.2f} ms")
        self.label_latencia_total.configure(text=f"Latência Total: {latencia_total:.2f} ms")
        self.label_fps.configure(text=f"FPS Estimado: {fps:.2f}")

    def salvar_resultado(self):
        if self.imagem_final_cv is None:
            return
        
        caminho_saida = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if caminho_saida:
            cv2.imwrite(caminho_saida, self.imagem_final_cv)
            tkinter.messagebox.showinfo("Sucesso", f"Imagem salva em:\n{caminho_saida}")

    def exibir_imagem(self, img_cv, label):
        largura_max = 550
        altura_max = 550
        
        h, w, _ = img_cv.shape
        escala = min(largura_max/w, altura_max/h)
        nova_largura = int(w * escala)
        nova_altura = int(h * escala)

        img_cv_redimensionada = cv2.resize(img_cv, (nova_largura, nova_altura))
        
        img_rgb = cv2.cvtColor(img_cv_redimensionada, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_ctk = customtkinter.CTkImage(light_image=img_pil, size=(nova_largura, nova_altura))
        
        label.configure(image=img_ctk, text="")
        label.image = img_ctk # Mantém referência

if __name__ == "__main__":
    app = App()
    app.mainloop()
