"""
Main entrance of app and UI logic

*********************************************************
CREATED AND MAINTAINED BY ANDRES QUIROZ
*********************************************************

"""

import tkinter as tk

from pyparsing import col
from app_logic import generate_truth_table, difference, union, intersection, symetric_difference

current_option_menu = None


def clear_main_area():
    global main_area
    for widgets in main_area.winfo_children():
        widgets.destroy()

def sets_widgets():
    """
    Function that renders the widgets of the sets operations part
    """

    global main_area, current_option_menu, main_area

    if current_option_menu == "sets_operation": # we are already in the option
        return
    
    clear_main_area()
    current_option_menu = "sets_operation"
    res_grid = tk.Frame(main_area, width=500, height=500)
    
    def execute_set_action(action):
        # global set_a_entry_text, set_b_entry_text, set_c_entry_text
        """
        Executes the set action based on the parameter

        HERE WE REFERENCE 'app_logic.py' TO CALL LOGIC
        """
        set_a = set(set_a_entry_text.get().split(','))
        set_b = set(set_b_entry_text.get().split(','))
        set_c = set(set_c_entry_text.get().split(','))

        if len(set_a) == 1 and '' in set_a:
            set_a = {}
        if len(set_b) == 1 and '' in set_b:
            set_b = {}
        if len(set_c) == 1 and '' in set_c:
            set_c = {}
        
        print(set_a)
        print(set_b)
        print(len(set_c))
        
        res = {}

        if action == "u":
            res = union(set_a, set_b, set_c)
        elif action == "i":
            res = intersection(set_a, set_b, set_c)
        elif action == "d":
            res = difference(set_a, set_b, set_c)
        else:
            res = symetric_difference(set_a, set_b, set_c)
        
        # print result

        res_grid.pack()

        for i in range(len(res.keys())):
            key = list(res.keys())[i]

            key_entry = tk.Entry(res_grid)
            key_entry.insert(0, key)
            key_entry.grid(row=i,column=0)

            value_entry = tk.Entry(res_grid)
            value_entry.insert(0, res[key])
            value_entry.grid(row=i,column=1)


            

    
    # instructions label

    ins_label = tk.Label(main_area, text="""
        Introduce los elementos en los conjuntos de tu preferencia (puedes dejar un conjunto vacio,
            no se tomará en cuenta), IMPORTANTE, usa comas para separar los elementos del conjunto y no uses
            otros caracteres fuera de los alfanuméricos
        """)
    
    ins_label.pack()


    operations_grid = tk.Frame(main_area, width=500, height=500)

    title_set_a = tk.Label(operations_grid, text="A = {")
    title_set_a.grid(row=0, column=0)

    set_a_entry_text = tk.StringVar()
    set_a = tk.Entry(operations_grid, textvariable=set_a_entry_text)
    set_a.grid(row=0, column=1)

    end_title_set_a = tk.Label(operations_grid, text="}")
    end_title_set_a.grid(row=0, column=2)

    title_set_b = tk.Label(operations_grid, text="B = {")
    title_set_b.grid(row=1, column=0)

    set_b_entry_text = tk.StringVar()
    set_b = tk.Entry(operations_grid, textvariable=set_b_entry_text)
    set_b.grid(row=1, column=1)

    end_title_set_b = tk.Label(operations_grid, text="}")
    end_title_set_b.grid(row=1, column=2)

    title_set_c = tk.Label(operations_grid, text="C = {")
    title_set_c.grid(row=2, column=0)

    set_c_entry_text = tk.StringVar()
    set_c = tk.Entry(operations_grid, textvariable=set_c_entry_text)
    set_c.grid(row=2, column=1)

    end_title_set_c = tk.Label(operations_grid, text="}")
    end_title_set_c.grid(row=2, column=2)

    operations_grid.pack()


    # buttons

    button_container = tk.Frame(main_area, width=500, height=500)
    button_container.pack(pady=10)

    tk.Button(button_container, text="∪", width=5, height=2, command=lambda:execute_set_action("u")).grid(row=0, column=0, pady=5, padx=5)
    tk.Button(button_container, text="∩", width=5, height=2, command=lambda:execute_set_action("i")).grid(row=0, column=1, pady=5, padx=5)
    tk.Button(button_container, text="≠", width=5, height=2, command=lambda:execute_set_action("d")).grid(row=1, column=0, pady=5, padx=5)
    tk.Button(button_container, text="Δ", width=5, height=2, command=lambda:execute_set_action("ds")).grid(row=1, column=1, pady=5, padx=5)



def truth_table_generator_widgets():
    """
    Function that packs all the widgets of the truth table generator
    section of the app
    """
    global main_area, current_option_menu, main_area

    if current_option_menu == "truth_table": # we are already in the option
        return

    clear_main_area()
    table_container = tk.Frame(main_area, width=500, height=500)
   
    def generate_table_tkinter():
        """"
        Creates all entries
        """
        table = generate_truth_table(entry_text.get()) # matrix
        table_container.pack()

        # first pack the headers
        for i in range(0, len(table[0])):
            header = tk.Entry(table_container)
            header.insert(0, table[0][i])
            header.grid(row=0, column=i)
        
        # pack the content
        for j in range(1, len(table)):
            for i in range(0, len(table[j])):
                cell_content = tk.Entry(table_container)
                cell_content.insert(0, table[j][i])
                cell_content.grid(row=j, column=i)

    def clear_contents():
        """
        Limpia los contenidos del programa
        """
        table_container.pack_forget()
        main_entry.delete(0, tk.END)
        

    def change_text(text):
        main_entry.insert(tk.END, text)


    current_option_menu = "truth_table"
    entry_text = tk.StringVar()
    main_entry = tk.Entry(main_area, textvariable=entry_text)
    main_entry.pack(pady=20)
    
    tk.Button(main_area, text="Generar", command=lambda:generate_table_tkinter()).pack(pady=5)
    tk.Button(main_area, text="Limpiar", command=lambda:clear_contents()).pack(pady=5)

    # operator buttons
    button_container = tk.Frame(main_area, width=500, height=500)
    button_container.pack()

    tk.Button(button_container, text="p", width=5, height=2, command=lambda:change_text("p")).grid(row=1, column=0)
    tk.Button(button_container, text="q", width=5, height=2, command=lambda:change_text("q")).grid(row=1, column=1)
    tk.Button(button_container, text="r", width=5, height=2, command=lambda:change_text("r")).grid(row=1, column=2)
    tk.Button(button_container, text="s", width=5, height=2, command=lambda:change_text("s")).grid(row=1, column=3)
    tk.Button(button_container, text="t", width=5, height=2, command=lambda:change_text("t")).grid(row=1, column=4)
    tk.Button(button_container, text="(", width=5, height=2, command=lambda:change_text("(")).grid(row=1, column=5)

    tk.Button(button_container, text="u", width=5, height=2, command=lambda:change_text("u")).grid(row=2, column=0)
    tk.Button(button_container, text="w", width=5, height=2, command=lambda:change_text("w")).grid(row=2, column=1)
    tk.Button(button_container, text="x", width=5, height=2, command=lambda:change_text("x")).grid(row=2, column=2)
    tk.Button(button_container, text="y", width=5, height=2, command=lambda:change_text("y")).grid(row=2, column=3)
    tk.Button(button_container, text="z", width=5, height=2, command=lambda:change_text("z")).grid(row=2, column=4)
    tk.Button(button_container, text=")", width=5, height=2, command=lambda:change_text(")")).grid(row=2, column=5)

    tk.Button(button_container, text="^", width=5, height=2, command=lambda:change_text("^")).grid(row=3, column=0)
    tk.Button(button_container, text="v", width=5, height=2, command=lambda:change_text("v")).grid(row=3, column=1)
    tk.Button(button_container, text="~", width=5, height=2, command=lambda:change_text("~")).grid(row=3, column=2)
    tk.Button(button_container, text="->", width=5, height=2, command=lambda:change_text("->")).grid(row=3, column=3)
    tk.Button(button_container, text="<->", width=5, height=2, command=lambda:change_text("<->")).grid(row=3, column=4)



def main():
    truth_table_generator_widgets()

root = tk.Tk()
# defining layouts ----

# header
headbar = tk.Frame(root, bg='#CCC', height=40, borderwidth=2)
headbar.pack(expand=False, fill='both', side='top', anchor='nw')

# sidebar
sidebar = tk.Frame(root, width=200, bg='green', height=500, relief='sunken', borderwidth=2)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

# main content area
main_area = tk.Frame(root, width=500, height=500)
main_area.pack(expand=True, fill='both', side='right', padx=10, pady=10)

# defining widgets -----

# main title
tk.Label(headbar, text="Tablify", bg="#CCC", font=('Arial', 15)).grid(row=0,column=0)

# sidebar buttons
tk.Button(sidebar, command=truth_table_generator_widgets, text="Generador tablas de verdad", bg="green", relief="flat").grid(row=0, column=0)
tk.Button(sidebar, command=sets_widgets, text="Operaciones con conjuntos", bg="green", relief="flat").grid(row=1, column=0)

main()

root.mainloop()




