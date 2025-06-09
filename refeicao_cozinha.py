import tkinter as tk
import csv
import os

def carregar_pedidos():
    pedidos = []
    if os.path.exists('refeicoes.csv'):
        with open('refeicoes.csv', mode='r', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                if len(linha) == 6:
                    pedidos.append(linha)  # nome, quarto, data, hora, alimentos, alergias
    return pedidos

def exibir_pedidos():
    pedidos = carregar_pedidos()

    for widget in frame_interno.winfo_children():
        widget.destroy()

    if not pedidos:
        tk.Label(frame_interno, text="Nenhum pedido encontrado.", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        return

    for i, pedido in enumerate(reversed(pedidos)):
        nome, quarto, data, hora, alimentos, alergias = pedido
        card = tk.Frame(frame_interno, bg="white", bd=2, relief="groove", padx=15, pady=10)
        card.pack(fill="x", padx=20, pady=10)

        tk.Label(card, text=f"Pedido #{len(pedidos) - i}", font=("Arial", 14, "bold"), fg="#1f4e79", bg="white").pack(anchor="w")
        tk.Label(card, text=f"Nome: {nome}", font=("Arial", 12), bg="white").pack(anchor="w", pady=2)
        tk.Label(card, text=f"Quarto: {quarto}", font=("Arial", 12), bg="white").pack(anchor="w", pady=2)
        tk.Label(card, text=f"Data: {data} - Hora: {hora}", font=("Arial", 11, "italic"), bg="white", fg="gray").pack(anchor="w", pady=(2, 6))

        if alergias.strip().lower() != "nenhuma":
            alerta = tk.Label(card, text=f"⚠ Alergias: {alergias}", font=("Arial", 12, "bold"), bg="red", fg="white")
            alerta.pack(anchor="w", pady=6, fill="x")

        tk.Label(card, text="Alimentos:", font=("Arial", 12, "underline"), bg="white").pack(anchor="w")
        for alimento in alimentos.split("; "):
            tk.Label(card, text=f"• {alimento}", font=("Arial", 12), bg="white", anchor="w").pack(anchor="w", padx=10)

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def atualizar_periodicamente():
    exibir_pedidos()
    root_cozinha.after(3000, atualizar_periodicamente)

# Janela principal
root_cozinha = tk.Tk()
root_cozinha.title("Cozinha - NutriSabará")
root_cozinha.geometry("1000x800")
root_cozinha.configure(bg='#1f4e79')

tk.Label(root_cozinha, text="📋 Pedidos para a Cozinha", font=("Arial", 26, "bold"), fg="red", bg="#1f4e79").pack(pady=(20, 10))

# Área com canvas + scrollbar
container = tk.Frame(root_cozinha, bg="#1f4e79")
container.pack(fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(container, bg="#1f4e79", highlightthickness=0)
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

frame_pedidos = tk.Frame(canvas, bg="#1f4e79")
canvas.create_window((0, 0), window=frame_pedidos, anchor="nw")

frame_interno = tk.Frame(frame_pedidos, bg="#1f4e79")
frame_interno.pack(fill="both", expand=True)

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame_pedidos.bind("<Configure>", on_configure)
canvas.bind_all("<MouseWheel>", on_mousewheel)

atualizar_periodicamente()
root_cozinha.mainloop()
