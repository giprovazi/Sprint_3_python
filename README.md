# 🥗 NutriSabará – Sistema de Escolha de Refeições Interativo

## 📌 Descrição

**NutriSabará** é um sistema interativo criado para que **crianças hospitalizadas** escolham suas refeições de maneira divertida, acessível e visual. Desenvolvido em Python com `tkinter`, ele permite que a criança marque suas preferências alimentares por categoria (proteínas, acompanhamentos, sobremesas) e salve suas escolhas para consulta da cozinha hospitalar ou nutricionistas.

---

## 🎯 Objetivos

- Tornar o momento da refeição mais lúdico e humanizado.
- Permitir que a criança participe da seleção alimentar.
- Registrar automaticamente as preferências no formato `.csv`.
- Otimizar o trabalho da equipe de nutrição.

---

## 🧰 Tecnologias Utilizadas

| Ferramenta | Uso |
|------------|-----|
| Python     | Lógica principal do sistema |
| Tkinter    | Criação da interface gráfica |
| CSV        | Armazenamento local dos dados |
| Datetime   | Registro da data/hora das seleções |

---

## 🖼️ Interface do Sistema

A interface apresenta três colunas com categorias de alimentos. Cada alimento possui um emoji correspondente e pode ser selecionado via checkbox. Ao final, o botão **"Confirmar Escolhas"** salva os dados em um arquivo `.csv` e exibe uma mensagem de confirmação.

---

## ✅ Funcionalidades

- Interface gráfica com categorias:
  - **Proteínas 🍖**
  - **Acompanhamentos 🍚**
  - **Sobremesas 🍓**
- Checkboxes com emojis para facilitar a escolha.
- Confirmação visual dos alimentos escolhidos.
- Opção de remover itens antes de salvar.
- Salvamento automático no arquivo `refeicoes.csv`.

---

## 💾 Exemplo de Linha no CSV

```csv
Paciente,001,2025-04-30,15:42:10,Frango Grelhado 🍗; Arroz 🍚; Pudim 🍮

