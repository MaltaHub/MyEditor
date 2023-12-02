import tkinter as tk
from tkinter import messagebox

def salvar_nota():
    global nota_selecionada
    nota_atual = texto.get("1.0", "end-1c")
    if nota_atual:
        notas[nota_selecionada] = nota_atual

def nova_nota():
    global nota_selecionada
    salvar_nota()
    notas.append("")
    nota_selecionada = len(notas) - 1
    atualizar_lista_notas()

def excluir_nota():
    global nota_selecionada
    if nota_selecionada != -1:
        del notas[nota_selecionada]
        atualizar_lista_notas()
        if nota_selecionada >= len(notas):
            nota_selecionada = len(notas) - 1
        selecionar_nota()

def selecionar_nota(event=None):
    index = lista_notas.nearest(event.y)
    item_selecionado = lista_notas.get(index)
    print("Item selecionado antes da mudança:", item_selecionado)

    if texto.get("1.0", "end-1c") != notas[index]:
        print("Texto igual!")
        return

    global nota_selecionada
    index = lista_notas.curselection()

    if nota_selecionada != -1:
        nota_atual = texto.get("1.0", "end-1c")
        if nota_atual != notas[nota_selecionada]:
            resposta = messagebox.askyesno("Salvar Alterações", "Deseja salvar as alterações?")
            if resposta:
                salvar_nota()

    if index:
        nota_selecionada = int(index[0])
        texto.delete("1.0", tk.END)
        texto.insert(tk.END, notas[nota_selecionada])

def atualizar_lista_notas():
    lista_notas.delete(0, tk.END)
    for i, _ in enumerate(notas):
        lista_notas.insert(tk.END, f"Nota {i+1}")

def alteracao_nota(event=None):
    global nota_selecionada
    #if nota_selecionada != -1:
    #    nota_atual = texto.get("1.0", "end-1c")
    #    if nota_atual != notas[nota_selecionada]:
    #        resposta = messagebox.askyesno("Salvar Alterações", "Deseja salvar as alterações?")
    #        if resposta:
    #            salvar_nota()

root = tk.Tk()
root.title("Editor de Notas")
root.geometry("600x400")

notas = [""]
nota_selecionada = -1

frame = tk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.Y)

lista_notas = tk.Listbox(frame)
lista_notas.pack(fill=tk.Y)
#lista_notas.bind("<<ListboxSelect>>", selecionar_nota)
lista_notas.bind("<Button-1>", selecionar_nota)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

notebook = tk.Frame(root)
notebook.pack(fill=tk.BOTH, expand=True)

texto = tk.Text(notebook, wrap="word", yscrollcommand=scrollbar.set)
texto.pack(fill=tk.BOTH, expand=True)
texto.bind("<KeyRelease>", alteracao_nota)

scrollbar.config(command=texto.yview)

botoes_frame = tk.Frame(frame)
botoes_frame.pack(fill=tk.X)

btn_nova_nota = tk.Button(botoes_frame, text="Nova Nota", command=nova_nota)
btn_nova_nota.pack(fill=tk.X)

btn_excluir_nota = tk.Button(botoes_frame, text="Excluir Nota", command=excluir_nota)
btn_excluir_nota.pack(fill=tk.X)

btn_salvar = tk.Button(botoes_frame, text="Salvar", command=salvar_nota)
btn_salvar.pack(fill=tk.X)

root.mainloop()