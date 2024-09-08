from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ManufacturersDashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Title and action buttons
        title_frame = ttk.Frame(self)
        title_frame.pack(fill="x", padx=10, pady=10)

        title_label = ttk.Label(title_frame, text="Manufacturers Dashboard", font=("Helvetica", 16, "bold"))
        title_label.pack(side="left")

        add_button = ttk.Button(title_frame, text="Add Manufacturer")
        add_button.pack(side="right", padx=5)
        edit_button = ttk.Button(title_frame, text="Edit Manufacturer")
        edit_button.pack(side="right", padx=5)
        delete_button = ttk.Button(title_frame, text="Delete Manufacturer")
        delete_button.pack(side="right", padx=5)

        # Summary cards
        summary_frame = ttk.Frame(self)
        summary_frame.pack(fill="x", padx=10, pady=10)

        manufacturer_summary = ttk.LabelFrame(summary_frame, text="Manufacturer Summary")
        manufacturer_summary.pack(side="left", expand=True, fill="both", padx=5)
        ttk.Label(manufacturer_summary, text="Total Manufacturers: 50").pack(anchor="w", padx=10, pady=2)
        ttk.Label(manufacturer_summary, text="Active Manufacturers: 45").pack(anchor="w", padx=10, pady=2)

        top_manufacturers = ttk.LabelFrame(summary_frame, text="Top Manufacturers")
        top_manufacturers.pack(side="right", expand=True, fill="both", padx=5)
        self.create_top_manufacturers_chart(top_manufacturers)

        # Manufacturer information table
        table_frame = ttk.LabelFrame(self, text="Manufacturer Information")
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("Manufacturer Number", "Manufacturer Name", "Telephone", "Discount Percent", "Federal Tax ID", "Manufacturer Currency")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(expand=True, fill="both", padx=5, pady=5)

    def create_top_manufacturers_chart(self, parent):
        # Sample data
        manufacturers = ['Mfg A', 'Mfg B', 'Mfg C', 'Mfg D', 'Mfg E']
        values = [30, 25, 20, 15, 10]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(manufacturers, values)
        ax.set_ylabel('Percentage')
        ax.set_title('Top Manufacturers by Volume')

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both", padx=5, pady=5)