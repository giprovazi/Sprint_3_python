import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

categorias = {
    "Proteínas 🍖": [
        "Frango Grelhado 🍗", "Carne Assada 🥩", "Ovo Cozido 🍳", "Costelinha 🍖", "Peixe Assado 🐟",
        "Hambúrguer 🍔", "Filé de Frango 🍗", "Almôndega 🍝", "Tofu 🍣", "Linguiça 🌭"
    ],
    "Acompanhamentos 🍚": [
        "Arroz 🍚", "Feijão 🍲", "Salada 🥗", "Macarrão 🍝", "Batata Cozida 🥔",
        "Alface 🥬", "Pepino 🥒", "Cenoura 🥕", "Milho 🌽", "Ervilha 🟢",
        "Torrada 🍞", "Pão 🍞", "Purê de Batata 🥔", "Farofa 🍽️", "Brócolis 🥦"
    ],
    "Sobremesas 🍓": [
        "Morango 🍓", "Uva 🍇", "Maçã 🍎", "Abacaxi 🍍", "Cereja 🍒",
        "Melancia 🍉", "Banana 🍌", "Limão 🍋", "Laranja 🍊", "Chocolate 🍫",
        "Sorvete 🍦", "Bolo 🎂", "Pudim 🍮", "Gelatina 🍧", "Iogurte 🍨"
    ]
}

alimentos_vars = {}
nome_usuario = ""
quarto_usuario = ""
alergia_usuario = ""

def fazer_login():
    global nome_usuario, quarto_usuario, alergia_usuario

    nome_usuario = nome_entry.get().strip()
    quarto_usuario = quarto_entry.get().strip()
    alergia_usuario = alergia_var.get()

    if not nome_usuario or not quarto_usuario:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos.")
        return

    login_window.destroy()
    iniciar_interface_principal()

def listar_alimentos_selecionados():
    return [alimento for alimento, var in alimentos_vars.items() if var.get() == 1]

def salvar_escolhas_csv(selecionados):
    agora = datetime.now()
    data = agora.strftime("%Y-%m-%d")
    hora = agora.strftime("%H:%M:%S")
    with open('refeicoes.csv', mode='a', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([nome_usuario, quarto_usuario, data, hora, ";".join(selecionados), alergia_usuario])

def confirmar_escolhas():
    selecionados = listar_alimentos_selecionados()
    if not selecionados:
        messagebox.showwarning("Nenhum alimento", "Por favor, selecione pelo menos um alimento.")
        return
    resposta = messagebox.askyesno("Editar Escolhas", "Deseja remover algum alimento antes de confirmar?")
    if resposta:
        remover_alimentos(selecionados)
        return
    salvar_escolhas_csv(selecionados)
    mensagem = "Você selecionou:\n" + "\n".join(f"- {a}" for a in selecionados)
    messagebox.showinfo("Alimentos Escolhidos", mensagem)

def remover_alimentos(selecionados):
    for alimento in selecionados:
        if messagebox.askyesno("Remover Alimento", f"Deseja remover {alimento}?"):
            alimentos_vars[alimento].set(0)

def iniciar_interface_principal():
    root = tk.Tk()
    root.title("NutriSabará")
    root.configure(bg="#1f4e79")
    root.geometry("900x800")

    frame = tk.Frame(root, bg="#1f4e79")
    frame.pack(pady=10)

    tk.Label(frame, text="NutriSabará", font=("Arial", 28, "bold"), fg="red", bg="#1f4e79").grid(row=0, column=0, columnspan=3, pady=20)

    alergia_alimentos_bloqueados = {
        "Lactose": ["Iogurte 🍨", "Bolo 🎂", "Pudim 🍮", "Sorvete 🍦", "Chocolate 🍫"],
        "Glúten": ["Pão 🍞", "Torrada 🍞", "Bolo 🎂", "Macarrão 🍝", "Farofa 🍽️"],
        "Amendoim": ["Chocolate 🍫"],
        "Frutos do Mar": ["Peixe Assado 🐟"],
    }

    bloqueados = alergia_alimentos_bloqueados.get(alergia_usuario, [])

    coluna = 0
    for categoria, itens in categorias.items():
        tk.Label(frame, text=categoria, font=("Arial", 18, "bold"), fg="white", bg="#1f4e79").grid(row=1, column=coluna, sticky="w", padx=20, pady=(10, 5))
        for idx, alimento in enumerate(itens, start=2):
            var = tk.IntVar()
            alimentos_vars[alimento] = var
            chk = tk.Checkbutton(
                frame, text=alimento, variable=var, font=("Arial", 14),
                bg="#1f4e79", fg="white", activebackground="#1f4e79",
                activeforeground="white", selectcolor="#1f4e79"
            )
            if alimento in bloqueados:
                chk.config(state="disabled", disabledforeground="gray")
            chk.grid(row=idx, column=coluna, sticky="w", padx=40)
        coluna += 1

    botao = tk.Button(frame, text="Confirmar Escolhas", font=("Arial", 16, "bold"),
                      bg="red", fg="white", command=confirmar_escolhas)
    botao.grid(row=30, column=0, columnspan=3, pady=40)

    root.mainloop()


login_window = tk.Tk()
login_window.title("Login - NutriSabará")
login_window.geometry("500x400")
login_window.configure(bg="#1f4e79")

tk.Label(login_window, text="NutriSabará", font=("Arial", 26, "bold"), fg="red", bg="#1f4e79").pack(pady=20)

tk.Label(login_window, text="Nome do Paciente:", font=("Arial", 14), fg="white", bg="#1f4e79").pack(pady=(10, 5))
nome_entry = tk.Entry(login_window, font=("Arial", 14))
nome_entry.pack()

tk.Label(login_window, text="Número do Quarto:", font=("Arial", 14), fg="white", bg="#1f4e79").pack(pady=(10, 5))
quarto_entry = tk.Entry(login_window, font=("Arial", 14))
quarto_entry.pack()

tk.Label(login_window, text="Alergia:", font=("Arial", 14), fg="white", bg="#1f4e79").pack(pady=(10, 5))
alergias = ["Nenhuma", "Lactose", "Glúten", "Amendoim", "Frutos do Mar"]
alergia_var = tk.StringVar(value=alergias[0])
alergia_menu = tk.OptionMenu(login_window, alergia_var, *alergias)
alergia_menu.config(font=("Arial", 14), bg="white")
alergia_menu.pack()

tk.Button(login_window, text="Entrar", font=("Arial", 16, "bold"), bg="red", fg="white", command=fazer_login).pack(pady=30)

login_window.mainloop()
