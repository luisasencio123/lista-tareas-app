import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.servicio = TareaServicio()

        # Entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento ENTER
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Lista
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack()

        # Evento doble click (extra)
        self.lista.bind("<Double-1>", self.completar_tarea_evento)

        # Botones
        tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea).pack(pady=5)
        tk.Button(root, text="Marcar Completada", command=self.completar_tarea).pack(pady=5)
        tk.Button(root, text="Eliminar", command=self.eliminar_tarea).pack(pady=5)

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            texto = tarea.descripcion
            if tarea.completado:
                texto += " [Hecho]"
            self.lista.insert(tk.END, f"{tarea.id}. {texto}")

    def agregar_tarea(self):
        texto = self.entry.get()
        if texto:
            self.servicio.agregar_tarea(texto)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Error", "Ingrese una tarea")

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def completar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.servicio.obtener_tareas()[index]
            self.servicio.completar_tarea(tarea.id)
            self.actualizar_lista()

    def completar_tarea_evento(self, event):
        self.completar_tarea()

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.servicio.obtener_tareas()[index]
            self.servicio.eliminar_tarea(tarea.id)
            self.actualizar_lista()