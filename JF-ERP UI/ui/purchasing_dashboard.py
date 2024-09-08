from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PurchasingDashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Title and action buttons
        title_frame = ttk.Frame(self)
        title_frame.pack(fill="x", padx=10, pady=10)

        title_label = ttk.Label(title_frame, text="Purchasing Dashboard", font=("Helvetica", 16, "bold"))
        title_label.pack(side="left")

        create_po_button = ttk.Button(title_frame, text="Create Purchase Order")
        create_po_button.pack(side="right", padx=5)
        view_pos_button = ttk.Button(title_frame, text="View Purchase Orders")
        view_pos_button.pack(side="right", padx=5)
        delete_po_button = ttk.Button(title_frame, text="Delete Purchase Order")
        delete_po_button.pack(side="right", padx=5)
        print_po_button = ttk.Button(title_frame, text="Print Purchase Order")
        print_po_button.pack(side="right", padx=5)
        confirm_status_button = ttk.Button(title_frame, text="Confirm Status")
        confirm_status_button.pack(side="right", padx=5)

        # Summary cards
        summary_frame = ttk.Frame(self)
        summary_frame.pack(fill="x", padx=10, pady=10)

        po_summary = ttk.LabelFrame(summary_frame, text="Purchase Order Summary")
        po_summary.pack(side="left", expand=True, fill="both", padx=5)
        ttk.Label(po_summary, text="Total POs: 100").pack(anchor="w", padx=10, pady=2)
        ttk.Label(po_summary, text="Open POs: 25").pack(anchor="w", padx=10, pady=2)
        ttk.Label(po_summary, text="Overdue POs: 5").pack(anchor="w", padx=10, pady=2)

        purchasing_performance = ttk.LabelFrame(summary_frame, text="Purchasing Performance")
        purchasing_performance.pack(side="right", expand=True, fill="both", padx=5)
        self.create_purchasing_performance_chart(purchasing_performance)

        # Recent purchase orders table
        table_frame = ttk.LabelFrame(self, text="Recent Purchase Orders")
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("PO Number", "Vendor", "Order Date", "Need Date", "Promise Date", "Amount", "Status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        column_widths = {
            "PO Number": 120,
            "Vendor": 150,
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

    def create_purchasing_performance_chart(self, parent):
        # Sample data
        categories = ['On Time', 'Late', 'Early']
        values = [70, 20, 10]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Purchase Order Performance')

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both", padx=5, pady=5)