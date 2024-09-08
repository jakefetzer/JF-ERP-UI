from tkinter import ttk

class CustomersDashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Title and action buttons
        title_frame = ttk.Frame(self)
        title_frame.pack(fill="x", padx=10, pady=10)

        title_label = ttk.Label(title_frame, text="Customers Dashboard", font=("Helvetica", 16, "bold"))
        title_label.pack(side="left")

        add_button = ttk.Button(title_frame, text="Add Customer")
        add_button.pack(side="right", padx=5)
        edit_button = ttk.Button(title_frame, text="Edit Customer")
        edit_button.pack(side="right", padx=5)
        delete_button = ttk.Button(title_frame, text="Delete Customer")
        delete_button.pack(side="right", padx=5)

        # Summary cards
        summary_frame = ttk.Frame(self)
        summary_frame.pack(fill="x", padx=10, pady=10)

        customer_summary = ttk.LabelFrame(summary_frame, text="Customer Summary")
        customer_summary.pack(side="left", expand=True, fill="both", padx=5)
        ttk.Label(customer_summary, text="Total Customers: 500").pack(anchor="w", padx=10, pady=2)
        ttk.Label(customer_summary, text="New Customers: 25").pack(anchor="w", padx=10, pady=2)

        performance = ttk.LabelFrame(summary_frame, text="Performance")
        performance.pack(side="right", expand=True, fill="both", padx=5)
        ttk.Label(performance, text="Top Customer: ABC Corp").pack(anchor="w", padx=10, pady=2)
        ttk.Label(performance, text="Recently Added: XYZ Inc").pack(anchor="w", padx=10, pady=2)

        # Customer information table
        table_frame = ttk.LabelFrame(self, text="Customer Information")
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("Customer Code", "Customer Name", "Telephone", "Email", "Account Balance", "Address")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(expand=True, fill="both", padx=5, pady=5)