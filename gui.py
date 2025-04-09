import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import time  # For measuring execution time
from utils import import_csv, match_headers, data_to_objects
from data_structures import (
    SinglyLinkedList, DoublyLinkedList, BinaryTree, BST, DynamicArray
)

class FileImportComponent(tk.LabelFrame):
    def __init__(self, parent, callback=None):
        super().__init__(parent, text="Import CSV File")
        self.callback = callback
        self.file_path = None
        self.data = []

        self._create_widgets()

    def _create_widgets(self):
        self.import_button = tk.Button(self, text="Import CSV File", command=self._import_file)
        self.reimport_button = tk.Button(self, text="Re-import Last File", command=self._reimport_file)
        self.status_label = tk.Label(self, text="No file imported", fg="gray")

        self.import_button.grid(row=0, column=0, padx=10, pady=5)
        self.reimport_button.grid(row=0, column=1, padx=10, pady=5)
        self.status_label.grid(row=0, column=2, padx=10, pady=5)

    def _import_file(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            self.file_path = path
            self._read_and_notify()

    def _reimport_file(self):
        if self.file_path:
            self._read_and_notify()
        else:
            messagebox.showwarning("No File", "No file has been imported yet.")

    def _read_and_notify(self):
        try:
            headers, raw_data = import_csv(self.file_path)
            if not headers or not raw_data:
                raise ValueError("File could not be read.")

            model_class = match_headers(headers)
            if not model_class:
                raise ValueError("Unrecognized CSV structure.")

            data_objects = data_to_objects(raw_data, headers)
            self.data = data_objects
            self.status_label.config(text=f"Imported {len(data_objects)} {model_class.__name__}(s)", fg="green")

            if self.callback:
                self.callback("file_import_confirmed", model_class.__name__, data_objects, self.file_path)

        except Exception as e:
            self.status_label.config(text="Import failed", fg="red")
            if self.callback:
                self.callback("file_import_failed", str(e), [], self.file_path)


class DataStructureSelector(tk.LabelFrame):
    def __init__(self, master, on_select_structure):
        super().__init__(master, text="Data Structure Selector")
        self.on_select_structure = on_select_structure
        self.structure_var = tk.StringVar()

        self._create_widgets()

    def _create_widgets(self):
        self.dropdown = ttk.Combobox(self, textvariable=self.structure_var,
                                      values=["SinglyLinkedList", "DoublyLinkedList", "BinaryTree", "BST", "DynamicArray"],
                                      state="readonly")
        self.apply_btn = ttk.Button(self, text="Apply", command=self.apply_structure)
        self.current_label = tk.Label(self, text="Current: None", fg="blue")

        self.dropdown.grid(row=0, column=0, padx=5, pady=5)
        self.apply_btn.grid(row=0, column=1, padx=5, pady=5)
        self.current_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    def apply_structure(self):
        selected = self.structure_var.get()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a data structure first.")
            return

        structure_map = {
            "SinglyLinkedList": SinglyLinkedList,
            "DoublyLinkedList": DoublyLinkedList,
            "BinaryTree": BinaryTree,
            "BST": BST,
            "DynamicArray": DynamicArray
        }

        new_structure = structure_map.get(selected)()
        self.current_label.config(text=f"Current: {selected}")
        self.on_select_structure(new_structure, selected)


class OperationSelectionComponent(tk.LabelFrame):
    def __init__(self, master, get_model_class, on_operation_selected):
        super().__init__(master, text="Operation Selector")
        self.get_model_class = get_model_class
        self.on_operation_selected = on_operation_selected

        self._create_widgets()

    def _create_widgets(self):
        self.operation_var = tk.StringVar(value="sort")
        self.attribute_var = tk.StringVar()

        tk.Label(self, text="Select Operation:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        for idx, op in enumerate(["Sort", "Search"]):
            tk.Radiobutton(self, text=op, variable=self.operation_var, value=op.lower(), command=self.update_algorithm_options).grid(row=0, column=idx + 1, sticky="w")

        tk.Label(self, text="Compare by:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.attribute_dropdown = ttk.Combobox(self, textvariable=self.attribute_var, state="readonly")
        self.attribute_dropdown.grid(row=1, column=1, columnspan=2, sticky="we", padx=5)

        self.apply_button = ttk.Button(self, text="Apply", command=self.apply_selection)
        self.apply_button.grid(row=2, column=0, columnspan=3, pady=5)

    def apply_selection(self):
        selected_op = self.operation_var.get()
        if not selected_op:
            messagebox.showwarning("No Selection", "Please select an operation.")
            return

        model_class = self.get_model_class()
        if not model_class:
            messagebox.showwarning("No Model", "No data model available.")
            return

        sample_obj = model_class()  # Take an example object from the class
        self.update_attributes(sample_obj)

    def update_attributes(self, sample_obj):
        if sample_obj is None:
            self.attribute_dropdown['values'] = []
            self.attribute_var.set("")
            return

        attr_list = [attr for attr in dir(sample_obj)
                     if not callable(getattr(sample_obj, attr)) and not attr.startswith("_")]
        self.attribute_dropdown['values'] = attr_list
        if attr_list:
            self.attribute_var.set(attr_list[0])  # Set the first attribute as default

    def update_algorithm_options(self):
        operation_type = self.operation_var.get()
        if operation_type == "sort":
            self.attribute_dropdown.config(state="normal")
        else:
            self.attribute_dropdown.config(state="normal")


class ResultDisplayComponent(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Results")
        self._create_widgets()

    def _create_widgets(self):
        self.result_text = tk.Text(self, wrap="word", height=10, state="disabled")
        self.result_scrollbar = tk.Scrollbar(self, command=self.result_text.yview)
        self.result_text.config(yscrollcommand=self.result_scrollbar.set)

        self.result_text.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.result_scrollbar.grid(row=0, column=1, sticky="ns", padx=5, pady=5)

    def display_result(self, result):
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state="disabled")


class MainGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Structures & Algorithms GUI")
        self.geometry("900x700")

        self.model_type = None
        self.data_objects = []

        self.file_import = FileImportComponent(self, self.handle_file_import)
        self.file_import.pack(fill="x", padx=10, pady=10)

        self.structure_selector = DataStructureSelector(self, self.set_data_structure)
        self.structure_selector.pack(padx=10, pady=5, fill="x")
        self.on_operation_selected = None

        # Initialize OperationSelectionComponent with a fallback to handle empty data_objects
        self.operation_selector = OperationSelectionComponent(self, 
            lambda: self.data_objects[0].__class__ if self.data_objects else None, 
            self.on_operation_selected
        )
        self.operation_selector.pack(fill="x", padx=10, pady=10)

        self.result_display = ResultDisplayComponent(self)
        self.result_display.pack(fill="x", padx=10, pady=10)

        self.run_button = tk.Button(self, text="Run Operation", command=self.run_operation)
        self.run_button.pack(fill="x", padx=10, pady=10)

        self.current_structure = None
        self.selected_algorithm = None

    def on_algorithm_selected(self, selected_algorithm, target_value=None):
        self.selected_algorithm, self.target_value = selected_algorithm, target_value
        self.result_display.display_result(f"Selected Algorithm: {selected_algorithm}")

    def handle_file_import(self, event_type, model_type, data, file_path):
        if event_type == "file_import_confirmed":
            self.model_type, self.data_objects = model_type, data
            messagebox.showinfo("File Imported", f"Successfully imported {len(data)} records")
            # Reinitialize the operation_selector after data import
            self.operation_selector.update_attributes(self.data_objects[0] if self.data_objects else None)
        elif event_type == "file_import_failed":
            messagebox.showerror("File Import Failed", f"Error: {data}")

    def set_data_structure(self, structure, structure_name):
        self.current_structure = structure
        self.result_display.display_result(f"Selected Data Structure: {structure_name}")

    def run_operation(self):
        if not self.selected_algorithm or not self.current_structure:
            messagebox.showwarning("Invalid Selection", "Please select both algorithm and data structure.")
            return

        # Measure execution time
        start_time = time.time()
        if self.selected_algorithm == "sort":
            self.sort_data()
        elif self.selected_algorithm == "search":
            self.search_data()
        end_time = time.time()

        execution_time = end_time - start_time
        self.result_display.display_result(f"Execution time: {execution_time:.4f} seconds")

    def sort_data(self):
        if self.current_structure:
            self.current_structure.sort(lambda x: getattr(x, self.operation_selector.attribute_var.get()))
            self.result_display.display_result("Data sorted successfully.")

    def search_data(self):
        if self.current_structure and self.target_value:
            search_result = self.current_structure.search(self.target_value)
            self.result_display.display_result(f"Search result: {search_result}")

if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()
