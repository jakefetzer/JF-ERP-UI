from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class InventoryDashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Title and action buttons
        title_frame = ttk.Frame(self)
        title_frame.pack(fill="x", padx=10, pady=10)

        title_label = ttk.Label(title_frame, text="Inventory Dashboard", font=("Helvetica", 16, "bold"))
        title_label.pack(side="left")

        add_button = ttk.Button(title_frame, text="Add Item")
        add_button.pack(side="right", padx=5)
        edit_button = ttk.Button(title_frame, text="Edit Item")
        edit_button.pack(side="right", padx=5)
        delete_button = ttk.Button(title_frame, text="Delete Item")
        delete_button.pack(side="right", padx=5)

        # Summary cards
        summary_frame = ttk.Frame(self)
        summary_frame.pack(fill="x", padx=10, pady=10)

        inventory_levels = ttk.LabelFrame(summary_frame, text="Inventory Levels")
        inventory_levels.pack(side="left", expand=True, fill="both", padx=5)
        self.create_inventory_levels_chart(inventory_levels)

        inventory_summary = ttk.LabelFrame(summary_frame, text="Inventory Summary")
        inventory_summary.pack(side="right", expand=True, fill="both", padx=5)
        ttk.Label(inventory_summary, text="Total Items: 1,245").pack(anchor="w", padx=10, pady=2)
        ttk.Label(inventory_summary, text="Low Stock Items: 37").pack(anchor="w", padx=10, pady=2)
        ttk.Label(inventory_summary, text="Out of Stock: 5").pack(anchor="w", padx=10, pady=2)
        ttk.Label(inventory_summary, text="Total Value: $1,234,567").pack(anchor="w", padx=10, pady=2)

        # Inventory status table
        table_frame = ttk.LabelFrame(self, text="Inventory Status")
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("Item Number", "Item Description", "In Stock", "Qty Ordered by Customers", "Qty Ordered from Vendors", "Last Purchase Price")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(expand=True, fill="both", padx=5, pady=5)

    def create_inventory_levels_chart(self, parent):
        # Sample data
        items = ['A00001', 'A00002', 'A00003', 'A00004', 'A00005']
        levels = [1612, 1352, 1638, 689, 630]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(items, levels)
        ax.set_ylabel('Stock Level')
        ax.set_title('Inventory Levels')

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both", padx=5, pady=5)