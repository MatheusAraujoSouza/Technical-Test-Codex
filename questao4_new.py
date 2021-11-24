from tkinter import *
from tkinter import messagebox
from tkinter.font import Font




'''
Funcao para adicionar uma task no list box
  Descricao: Um teste será realizado para verificar se a entrada não é vazia e logo depois 
  a variavel vai ser inserida no list box.
'''
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)#A variavel lb atribuída à caixa de listagem.
        my_entry.delete(0, END)#END significa que um novo item será adicionado no final. Se END for substituído por 0 , novos dados serão adicionados no topo.
    else:
        messagebox.showwarning("warning", "Please enter some task.")

'''
Funcao para deletar uma task.
  Descricao: O usuario ira clicar no item e logo depois em um botão com o nome 'Delete Task',
  assim a task vai ser deletada. 
'''
def deleteTask():
    lb.delete(ANCHOR)#ANCHOR se refere ao item selecionado na caixa de listagem.

'''
Funcao para deletar todos os itens do list box
  Descricao: o usuario vai clicar no botão 'Delete all' e todos os itens do list box
  vão ser deletados.
'''    
def deleteall():
   messagebox.showwarning('Delete All','Are you sure? Because this action will delete everything.')
   lb.delete(0,END)#lb atribuída à caixa de listagem.

#Criando a interface de interação.    
ws = Tk()
ws.geometry('550x550+400+100')#largura x altura + posição x + posição y. 
ws.title('Todo list')
ws.config(bg='#272324')#cor de fundo da janela. 
ws.resizable(width=False, height=False)

frame = Frame(ws)#Frame será usado para colocar widgets como Listbox e Scrollbars dentro dele. 
frame.pack(pady=5)#acolchoamento extra ao redor da moldura externa. 

lb = Listbox(
    frame,
    width=30,
    height=10,
    font=('Old English Text MT', 20),
    
    bg="#666666",
    bd=0,
    fg="#bf9000",
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

#lista fictícia 
stuff = ["Write documentation","Learn something","Write software","Go to the gym","Walk with the dog", "Buy groceries", "Take a nap", "Learn Tkinter", "Rule the world"]
#Adicionar lista fictícia à caixa de lista.
for item in stuff:
	lb.insert(END, item)

'''
Barras de rolagem
  Descrição: Barras de rolagem são usadas para que os usuários possam rolar as 
  informações que são colocadas em um tamanho limitado na janela.
'''
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
sb.config(bg="#7f6000")

lb.config(yscrollcommand=sb.set)#vinculando a caixa de listagem com a barra de rolagem.
sb.config(command=lb.yview)##yview significa que a barra de rolagem irá na direção vertical.


my_entry = Entry(#Caixa de entrada para obter informações do Usuario.
    ws,
    font=('Old English Text MT', 15),
     bg="#666666",
     fg="#bf9000"
    )

my_entry.pack(pady=17)

#Usamos moldura separada para botões.
button_frame = Frame(ws)
button_frame.pack(pady=17)

'''
Criando os tkinter.Button.
  Descrição: Quando o botão é clicado, a função mencionada no comando é chamada. 
  Neste caso, se o usuário clica no botão addTask_btn, em seguida a função newtask 
  é chamada e quando o usuário clica no botão delTask_btn então a função delTask é chamada, 
  o mesmo ocorre para a função delall.

  lb: é o nome da variável para armazenar a caixa de listagem.
  width: o espaço horizontal fornecido.
  height: numero de linhas na posição vertical são fornecidas.
  font: a fonte.
  bd = 0 refere-se à borda é zero.
  fg:  é a cor do primeiro plano ou cor do texto.
  highlightthickness=0 toda vez que o foco é movido para qualquer item, então ele não deve mostrar nenhum movimento com valor 0 fornecido. por padrão, tem algum valor.
  selectbackground: ele decide a cor do item em foco na caixa de listagem.
  activestyle=”none” remove o sublinhado que aparece quando o item é selecionado ou focalizado.
  geometry manager: usado é pack ().
  side=LEFT: isso manterá a caixa de listagem do lado esquerdo do quadro. Fizemos isso de propósito para que possamos atribuir a posição certa às barras de rolagem.
  fill=BOTH  isso irá preencher o espaço em branco em ambas as direções que são x e y.
'''


addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Old English Text MT',15),
    bg="#38761d",
    fg="#bf9000",
    padx=30,
    pady=20,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Old English Text MT',15),
    bg='#990000',
    fg="#bf9000",
    padx=30,
    pady=20,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delall_btn = Button(
    button_frame,
    text='Delete all',
    font=('Old English Text MT',15),
    bg='#660000',
    fg="#bf9000",
    padx=30,
    pady=20,
    command=deleteall
)
delall_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()#Loop vai segurar a tela para possibilitar visualizar a janela.