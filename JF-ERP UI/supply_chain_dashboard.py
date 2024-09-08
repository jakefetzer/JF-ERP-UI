from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SupplyChainDashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Create a notebook for sub-tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        # Create sub-tabs
        self.overview_tab = ttk.Frame(self.notebook)
        self.inventory_tab = ttk.Frame(self.notebook)
        self.purchasing_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.overview_tab, text="Overview")
        self.notebook.add(self.inventory_tab, text="Inventory")
        self.notebook.add(self.purchasing_tab, text="Purchasing")

        # Overview tab
        self.create_overview_tab()

        # Inventory tab
        self.create_inventory_tab()

        # Purchasing tab
        self.create_purchasing_tab()

    def create_overview_tab(self):
        # Title
        title_label = ttk.Label(self.overview_tab, text="Supply Chain Overview", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Summary cards
        summary_frame = ttk.Frame(self.overview_tab)
        summary_frame.pack(fill="x", padx=10, pady=10)

        card_data = [
            ("Open POs", "4"),
            ("On-Time Deliveries", "75%"),
            ("Low Stock Items", "2"),
            ("Total Inventory Value", "$1,234,567")
        ]

        for title, value in card_data:
            card = ttk.LabelFrame(summary_frame, text=title)
            card.pack(side="left", expand=True, fill="both", padx=5)
            ttk.Label(card, text=value, font=("Helvetica", 14, "bold")).pack(pady=10)

        # Charts
        charts_frame = ttk.Frame(self.overview_tab)
        charts_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.create_po_status_chart(charts_frame)
        self.create_inventory_levels_chart(charts_frame)

    def create_po_status_chart(self, parent):
        chart_frame = ttk.LabelFrame(parent, text="Purchase Order Status")
        chart_frame.pack(side="left", expand=True, fill="both", padx=5)

        # Sample data
        dates = ['8/15', '8/9', '8/7', '8/5', '7/30']
        open_pos = [4, 3, 2, 1, 1]
        on_time = [3, 2, 2, 1, 1]
        late = [1, 1, 0, 0, 0]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(dates, open_pos, label='Open')
        ax.bar(dates, on_time, bottom=open_pos, label='On Time')
        ax.bar(dates, late, bottom=[i+j for i,j in zip(open_pos, on_time)], label='Late')

        ax.set_ylabel('Number of POs')
        ax.set_title('Purchase Order Status')
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")

    def create_inventory_levels_chart(self, parent):
        chart_frame = ttk.LabelFrame(parent, text="Inventory Levels")
        chart_frame.pack(side="right", expand=True, fill="both", padx=5)

        # Sample data
        items = ['A00001', 'A00002', 'A00003', 'A00004', 'A00005']
        levels = [1612, 1352, 1638, 689, 630]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(items, levels, marker='o')

        ax.set_ylabel('Stock Level')
        ax.set_title('Inventory Levels')

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")

    def create_inventory_tab(self):
        # Title
        title_label = ttk.Label(self.inventory_tab, text="Inventory Status", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Inventory status table
        table_frame = ttk.Frame(self.inventory_tab)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("Item Number", "Description", "In Stock", "Status")
        self.inventory_tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.inventory_tree.heading(col, text=col)
            self.inventory_tree.column(col, width=100)

        self.inventory_tree.pack(expand=True, fill="both")

        # Sample data
        inventory_data = [
            ("A00001", "IBM Infoprint 1312", 1612, "Adequate"),
            ("A00002", "IBM Infoprint 1222", 1352, "Adequate"),
            ("A00003", "IBM Infoprint 1226", 1638, "Adequate"),
            ("A00004", "HP Color LaserJet 5 Printers", 689, "Low Stock"),
            ("A00005", "HP Color LazerJet 4400", 630, "Low Stock"),
        ]

        for item in inventory_data:
            self.inventory_tree.insert("", "end", values=item)

    def create_purchasing_tab(self):
        # Title
        title_label = ttk.Label(self.purchasing_tab, text="Recent Purchase Orders", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Recent purchase orders table
        table_frame = ttk.Frame(self.purchasing_tab)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("PO Number", "Vendor", "Order Date", "Status")
        self.po_tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.po_tree.heading(col, text=col)
            self.po_tree.column(col, width=100)

        self.po_tree.pack(expand=True, fill="both")

        # Sample data
        po_data = [
            ("PO-001", "NVIDIA", "8/15/2024", "Open"),
            ("PO-002", "NVIDIA", "8/9/2024", "Open"),
            ("PO-003", "NVIDIA", "8/7/2024", "Closed"),
        ]

        for po in po_data:
            self.po_tree.insert("", "end", values=po)