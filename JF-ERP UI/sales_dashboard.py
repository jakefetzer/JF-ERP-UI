from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SalesDashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Title and action buttons
        title_frame = ttk.Frame(self)
        title_frame.pack(fill="x", padx=10, pady=10)

        title_label = ttk.Label(title_frame, text="Sales Dashboard", font=("Helvetica", 16, "bold"))
        title_label.pack(side="left")

        create_invoice_button = ttk.Button(title_frame, text="Create Invoice")
        create_invoice_button.pack(side="right", padx=5)
        view_invoices_button = ttk.Button(title_frame, text="View Invoices")
        view_invoices_button.pack(side="right", padx=5)
        delete_sale_button = ttk.Button(title_frame, text="Delete Sale")
        delete_sale_button.pack(side="right", padx=5)
        print_sale_button = ttk.Button(title_frame, text="Print Sale")
        print_sale_button.pack(side="right", padx=5)
        confirm_status_button = ttk.Button(title_frame, text="Confirm Status")
        confirm_status_button.pack(side="right", padx=5)

        # Summary cards
        summary_frame = ttk.Frame(self)
        summary_frame.pack(fill="x", padx=10, pady=10)

        sales_summary = ttk.LabelFrame(summary_frame, text="Sales Summary")
        sales_summary.pack(side="left", expand=True, fill="both", padx=5)
        ttk.Label(sales_summary, text="Total Sales: $1,234,567").pack(anchor="w", padx=10, pady=2)
        ttk.Label(sales_summary, text="Open Invoices: 25").pack(anchor="w", padx=10, pady=2)
        ttk.Label(sales_summary, text="Overdue Invoices: 5").pack(anchor="w", padx=10, pady=2)

        sales_performance = ttk.LabelFrame(summary_frame, text="Sales Performance")
        sales_performance.pack(side="right", expand=True, fill="both", padx=5)
        self.create_sales_performance_chart(sales_performance)

        # Recent sales table
        table_frame = ttk.LabelFrame(self, text="Recent Sales")
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("Invoice Number", "Customer", "Order Date", "Need Date", "Promise Date", "Amount", "Status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        column_widths = {
            "Invoice Number": 120,
            "Customer": 150,
            "Order Date": 100,
            "Need Date": 100,
            "Promise Date": 100,
            "Amount": 100,
            "Status": 100
        }

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths[col])

        self.tree.pack(expand=True, fill="both", padx=5, pady=5)

    def create_sales_performance_chart(self, parent):
        # Sample data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        sales = [100000, 120000, 95000, 110000, 130000]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(months, sales, marker='o')
        ax.set_ylabel('Sales ($)')
        ax.set_title('Monthly Sales Performance')

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both", padx=5, pady=5)