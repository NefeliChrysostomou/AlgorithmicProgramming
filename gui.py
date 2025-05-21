import tkinter as tk
from tkinter import messagebox, filedialog, ttk, scrolledtext
import data_structures as ds
import algorithms as algo
import utils
import time

pady = 5

def try_int_conversion(val):
    try:
        return int(val)
    except ValueError:
        return val

class Application():
    def __init__(self):
        self.tk = tk.Tk()
        self.filename = None
        self.data_structure = ds.DynamicArray()
        self.ds_options = {"Dynamic Array": ds.DynamicArray,
                           "Singly Linked List": ds.SinglyLinkedList,
                           "Doubly Linked List": ds.DoublyLinkedList,
                           "Binary Tree": ds.BinaryTree,
                           "BST": ds.BST}
        self.sorting_algorithms = {"Quicksort": algo.quicksort, "Merge sort": algo.merge_sort}
        self.search_algorithms = {"Linear Search": algo.linear_search, "Binary Search": algo.binary_search_by_key}
        self.search_algorithms_trees = {"DFS Search": algo.dfs_search, "BFS Search": algo.bfs_search, "BST Search": algo.bst_search}
        self.search_key = None
        self.search_attribute = None

        self.model_class = None
        self.operation_type = None
        self.chosen_algorithm = None

        self.raw_data = None
        self.memory = None

        self.tk.title("Algorithm & Datastructure Demo")
        self.tk.geometry("1000x600")
        self.create_widgets()

    def create_widgets(self):
        # Files
        self.import_file_label = tk.Label(self.tk, text="Please Select a File")
        self.import_file_label.grid(row=0, column=0, pady=pady, sticky="w")

        self.import_file_button = tk.Button(self.tk, text="Import File", command=self.select_file)
        self.import_file_button.grid(row=0, column=1, pady=pady, sticky="w")

        self.reimport_button = tk.Button(self.tk, text="Reimport File", command=self.reimport_file)
        self.reimport_button.grid(row=0, column=2, pady=pady, sticky="w")
        self.reimport_button.grid_remove()

        # Data Structure
        self.data_structure_label = tk.Label(self.tk, text="Please Select a Data Structure")
        self.data_structure_label.grid(row=1, column=0, pady=pady, sticky="w")

        self.data_structure_options = ttk.Combobox(self.tk, values=list(self.ds_options.keys()))
        self.data_structure_options.grid(row=2, column=0, pady=pady, sticky="w")
        self.data_structure_options.bind("<<ComboboxSelected>>", self.select_data_structure)
        self.data_structure_options.set("Dynamic Array")

        # Operation Type
        self.operation_label = tk.Label(self.tk, text="Please Select an Operation")
        self.operation_label.grid(row=3, column=0, pady=pady, sticky="w")

        self.operation_options = ttk.Combobox(self.tk, values=["Sort", "Search"])
        self.operation_options.grid(row=4, column=0, pady=pady, sticky="w")
        self.operation_options.set("Select Operation")
        self.operation_options.bind("<<ComboboxSelected>>", self.select_operation)

        # Algorithm
        self.algorithm_label = tk.Label(self.tk, text="Please Select an Algorithm")
        self.algorithm_label.grid(row=5, column=0, pady=pady, sticky="w")

        self.algorithm_options = ttk.Combobox(self.tk, values=["Choose Operation Type First"])
        self.algorithm_options.grid(row=6, column=0, pady=pady, sticky="w")
        self.algorithm_options.set("Select Algorithm")
        self.algorithm_options.grid_remove()
        self.algorithm_options.bind("<<ComboboxSelected>>", self.select_algo)
        self.search_attr = ttk.Combobox(self.tk, values=["Load Data First"])
        self.search_attr.grid(row=7, column=0, pady=pady, sticky="w")
        self.search_attr.set("Select Search Attribute")
        self.search_attr.grid_remove()
        self.search_key_label = tk.Label(self.tk, text="Please Enter Search Key")
        self.search_key_label.grid(row=7, column=1, pady=pady, sticky="w")
        self.search_key_label.grid_remove()
        self.search_key = ttk.Entry(self.tk)
        self.search_key.grid(row=7, column=2, pady=pady, sticky="w")
        self.search_key.grid_remove()

        self.run_button = tk.Button(self.tk, text="Run Algorithm", command=self.run_algorithm)
        self.run_button.grid(row=8, column=0, pady=pady, sticky="w")

        # Display Results
        self.results_box = scrolledtext.ScrolledText(self.tk, wrap=tk.WORD, width=80, height=20)
        self.results_box.grid(row=9, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
        self.results_box.insert(tk.END, "Execution Results:\n")
        self.results_box.config(state='disabled')  # Make read-only initially

        self.tk.grid_rowconfigure(9, weight=1)
        self.tk.grid_columnconfigure(4, weight=1)

        self.execution_time_label = tk.Label(self.tk, text="Execution Time: ", foreground="blue")
        self.execution_time_label.grid(row=10, column=0, pady=pady, sticky="w")
        self.execution_time_label.grid_remove()

    
    def update_file_widget(self):
        if self.filename:
            self.import_file_label.config(text=f"Selected file: {self.filename}", background="green", foreground="white")
            self.reimport_button.grid()
        else:
            self.import_file_label.config(text="Please Select a File", background="white", foreground="black")
            self.reimport_button.grid_remove()


    def update_ds_widget(self):
        if self.data_structure:
            self.data_structure_label.config(text=f"Selected Data Structure: {self.data_structure_options.get()}", background="green", foreground="white")
    
    def update_results_widget(self, status):
        """
        out = ""
        generator = self.memory
        print(generator)
        if isinstance(self.memory, ds.BinaryTree): 
            generator = self.memory.inorder_generator()
        if isinstance(self.memory, ds.SinglyLinkedList):
            generator = self.memory.get_all()
        elif not isinstance(self.memory, ds.SinglyLinkedList) or not isinstance(self.memory, ds.DynamicArray):
            generator = (self.memory,)
        for i in generator:
            if isinstance(i, ds.TreeNode):
                i = i.data
            try:
                if (iter(i) is not None):
                    for j in i:
                        out += str(j) + "\n"
            except TypeError:
                out += str(i) + "\n"
            #else:
            #    out += str(i) + "\n"
        self.results_label.config(text=f"{status} Execution Results: {out}", background="black", foreground="white")
        """
        output = ""
        gen = self.memory

        if isinstance(self.memory, ds.BinaryTree):
            gen = self.memory.inorder_generator()
        elif isinstance(self.memory, ds.SinglyLinkedList):
            gen = self.memory.get_all()
        elif not isinstance(self.memory, (ds.SinglyLinkedList, ds.DynamicArray)):
            gen = [self.memory]

        for item in gen:
            if isinstance(item, ds.TreeNode):
                item = item.data
            try:
                output += "\n".join(str(x) for x in item) + "\n"
            except TypeError:
                output += str(item) + "\n"
        
        self.results_box.config(state='normal')  # Enable editing
        self.results_box.delete("1.0", tk.END)   # Clear previous output
        self.results_box.insert(tk.END, f"{status} Execution Results:\n\n{output}")
        self.results_box.config(state='disabled')  # Make read-only again
        
    def select_file(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            self.filename = filename
            self.import_file(filename)
            messagebox.showinfo("File Imported", f"File '{filename}' imported successfully.")
        else:
            messagebox.showerror("Error", "No file selected.")

        self.update_file_widget()

    def import_file(self, filename):
        headers, data = utils.import_csv(filename)
        if headers and data:
            self.model_class = utils.match_headers(headers)
            if self.model_class:
                objects = utils.data_to_objects(data, headers)
                self.load_data(objects, self.data_structure)
                self.update_results_widget("Data Loaded: \n")
            else:
                messagebox.showerror("Error", "Unknown CSV format.")
        else:
            messagebox.showerror("Error", "Failed to import file.")
        
    def reimport_file(self):
        if self.filename:
            self.import_file(self.filename)
            messagebox.showinfo("File Reimported", f"File '{self.filename}' reimported successfully.")
        else:
            messagebox.showerror("Error", "No file selected for reimport.")

    def load_data(self, data, ds):
        self.raw_data = data
        self.memory = utils.insert_into_ds(ds, data)
        self.search_attr.config(values=self.get_possible_attributes())
        print(self.memory)

    def select_data_structure(self, event):
        selected_ds = self.data_structure_options.get()
        if selected_ds in self.ds_options:
            self.data_structure = self.ds_options[selected_ds]()
            self.load_data(self.raw_data, self.data_structure)
            self.update_ds_widget()
            self.update_results_widget("Data Loaded: ")
            search_options = []
            if self.operation_type == "Search":
                if isinstance(self.data_structure, ds.BinaryTree):
                    search_options = list(self.search_algorithms_trees.keys())
                    if not isinstance(self.data_structure, ds.BST):
                        search_options.remove("BST Search")
                else:
                    search_options = list(self.search_algorithms.keys())                
            elif self.operation_type == "Sort":
                self.search_options = list(self.sorting_algorithms.keys())
        else:
            messagebox.showerror("Error", "Invalid data structure selected.")
            return
        self.algorithm_options.config(values=search_options)

    def select_operation(self, event):
        selected_op = self.operation_options.get()
        if selected_op == "Sort":
            self.operation_type = "Sort"
            self.algorithm_options.config(values=list(self.sorting_algorithms.keys()))
            
        elif selected_op == "Search":
            self.operation_type = "Search"
            if isinstance(self.data_structure, ds.BinaryTree):
                self.algorithm_options.config(values=list(self.search_algorithms_trees.keys()))
            else:
                self.algorithm_options.config(values=list(self.search_algorithms.keys()))
            self.search_key_label.grid()
            self.search_key.grid()
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return
        
        self.operation_label.config(text=f"Selected Operation: {self.operation_options.get()}", background="green", foreground="white")
        self.algorithm_options.grid()
        self.search_attr.grid()
        self.search_attr.config(values=self.get_possible_attributes())
        self.search_attr.bind("<<ComboboxSelected>>", self.select_search_attribute)

    def select_algo(self, event):
        selected_algo = self.algorithm_options.get()
        if selected_algo in self.sorting_algorithms:
            self.chosen_algorithm = self.sorting_algorithms[selected_algo]
        elif selected_algo in self.search_algorithms:
            self.chosen_algorithm = self.search_algorithms[selected_algo]
        elif selected_algo in self.search_algorithms_trees:
            self.chosen_algorithm = self.search_algorithms_trees[selected_algo]
        else:
            messagebox.showerror("Error", "Invalid algorithm selected.")
            return
        
        self.algorithm_label.config(text=f"Selected Algorithm: {self.algorithm_options.get()}", background="green", foreground="white")

    def select_search_attribute(self, event):
        self.search_attribute = self.search_attr.get()
        if self.search_attribute and isinstance(self.data_structure, ds.BST):
            new_bst = ds.BST()
            for item in self.memory.inorder_generator():
                item.set_compare_attribute(self.search_attribute)
                new_bst.insert(item)

    def run_algorithm(self):
        if self.chosen_algorithm is algo.binary_search_by_key:
            algo.quicksort(self.memory, lambda x: self.get_attr(x))
        
        if self.chosen_algorithm in self.search_algorithms.values():
            start_time = time.time()
            self.memory = self.chosen_algorithm(self.memory, try_int_conversion(self.search_key.get()), lambda x: self.get_attr(x))
            end_time = time.time()
        elif self.chosen_algorithm in self.sorting_algorithms.values():
            start_time = time.time()
            self.memory = self.chosen_algorithm(self.memory, lambda x: self.get_attr(x))
            end_time = time.time()
        if self.chosen_algorithm in self.search_algorithms_trees.values():
            if isinstance(self.memory, ds.TreeNode):
                gen = [self.memory]
            else:
                gen = self.memory.inorder_generator()
            for item in gen:
                item.set_compare_attribute(self.search_attribute)
            start_time = time.time()
            self.memory = self.chosen_algorithm(self.memory, try_int_conversion(self.search_key.get()))
            end_time = time.time()

        self.execution_time_label.config(text=f"Execution Time: {end_time - start_time:.4f} seconds")
        self.execution_time_label.grid()

        self.update_results_widget("Algorithm Executed: \n")

    def get_attr(self, item):
        item.set_compare_attribute(self.search_attribute)
        return item.get_compare_value()
    
    def get_possible_attributes(self):
        if self.model_class:
            attributes = [attr.replace("get_", "") for attr in dir(self.model_class) if attr.startswith("get_") and attr not in ("get_compare_value", "get_compare_attribute")]
            return attributes
        else:
            messagebox.showerror("Error", "No model class found.")
            return []