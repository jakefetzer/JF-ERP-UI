from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

class FinanceDashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Create a notebook for sub-tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        # Create sub-tabs
        self.overview_tab = ttk.Frame(self.notebook)
        self.revenue_tab = ttk.Frame(self.notebook)
        self.expenses_tab = ttk.Frame(self.notebook)
        self.time_tracking_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.overview_tab, text="Overview")
        self.notebook.add(self.revenue_tab, text="Revenue")
        self.notebook.add(self.expenses_tab, text="Expenses")
        self.notebook.add(self.time_tracking_tab, text="Time Tracking")

        # Overview tab
        self.create_overview_tab()

        # Revenue tab
        self.create_revenue_tab()

        # Expenses tab
        self.create_expenses_tab()

        # Time Tracking tab
        self.create_time_tracking_tab()

    def create_overview_tab(self):
        # Title
        title_label = ttk.Label(self.overview_tab, text="Financial Overview", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Summary cards
        summary_frame = ttk.Frame(self.overview_tab)
        summary_frame.pack(fill="x", padx=10, pady=10)

        card_data = [
            ("Total Revenue", "$285,000"),
            ("Total Expenses", "$200,000"),
            ("Net Profit", "$85,000"),
            ("Profit Margin", "29.8%")
        ]

        for title, value in card_data:
            card = ttk.LabelFrame(summary_frame, text=title)
            card.pack(side="left", expand=True, fill="both", padx=5)
            ttk.Label(card, text=value, font=("Helvetica", 14, "bold")).pack(pady=10)

        # Charts
        charts_frame = ttk.Frame(self.overview_tab)
        charts_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.create_revenue_expenses_chart(charts_frame)
        self.create_expense_breakdown_chart(charts_frame)

    def create_revenue_expenses_chart(self, parent):
        chart_frame = ttk.LabelFrame(parent, text="Revenue vs Expenses")
        chart_frame.pack(side="left", expand=True, fill="both", padx=5)

        # Sample data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        revenue = [50000, 55000, 60000, 58000, 62000]
        expenses = [40000, 42000, 45000, 44000, 46000]

        fig, ax = plt.subplots(figsize=(6, 4))
        x = range(len(months))
        width = 0.35

        ax.bar([i - width/2 for i in x], revenue, width, label='Revenue')
        ax.bar([i + width/2 for i in x], expenses, width, label='Expenses')

        ax.set_ylabel('Amount ($)')
        ax.set_title('Revenue vs Expenses')
        ax.set_xticks(x)
        ax.set_xticklabels(months)
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")

    def create_expense_breakdown_chart(self, parent):
        chart_frame = ttk.LabelFrame(parent, text="Expense Breakdown")
        chart_frame.pack(side="right", expand=True, fill="both", padx=5)

        # Sample data
        categories = ['Inventory', 'Labor', 'Overhead', 'Marketing']
        values = [40, 30, 20, 10]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Expense Breakdown')

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")

    def create_revenue_tab(self):
        # Title
        title_label = ttk.Label(self.revenue_tab, text="Revenue by Product", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Revenue table
        table_frame = ttk.Frame(self.revenue_tab)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("Product", "Revenue", "% of Total")
        self.revenue_tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.revenue_tree.heading(col, text=col)
            self.revenue_tree.column(col, width=100)

        self.revenue_tree.pack(expand=True, fill="both")

        # Sample data
        revenue_data = [
            ("HP Color LaserJet 5 Printers", "$100,000", "35%"),
            ("IBM Infoprint 1312", "$80,000", "28%"),
            ("HP Color LazerJet 4400", "$60,000", "21%"),
            ("IBM Infoprint 1226", "$45,000", "16%"),
        ]

        for item in revenue_data:
            self.revenue_tree.insert("", "end", values=item)

    def create_expenses_tab(self):
        # Title
        title_label = ttk.Label(self.expenses_tab, text="Expense Categories", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Expenses table
        table_frame = ttk.Frame(self.expenses_tab)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("Category", "Amount", "% of Total")
        self.expenses_tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.expenses_tree.heading(col, text=col)
            self.expenses_tree.column(col, width=100)

        self.expenses_tree.pack(expand=True, fill="both")

        # Sample data
        expense_data = [
            ("Inventory", "$80,000", "40%"),
            ("Labor", "$60,000", "30%"),
            ("Overhead", "$40,000", "20%"),
            ("Marketing", "$20,000", "10%"),
        ]

        for item in expense_data:
            self.expenses_tree.insert("", "end", values=item)

    def create_time_tracking_tab(self):
        # Title
        title_label = ttk.Label(self.time_tracking_tab, text="Time Tracking", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Current time display
        self.time_label = ttk.Label(self.time_tracking_tab, text="", font=("Helvetica", 14))
        self.time_label.pack(pady=5)
        self.update_time()

        # Clock in/out button
        self.clock_button = ttk.Button(self.time_tracking_tab, text="Clock In", command=self.toggle_clock)
        self.clock_button.pack(pady=10)

        # Recent time entries
        table_frame = ttk.Frame(self.time_tracking_tab)
        table_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("Date", "Clock In", "Clock Out", "Hours Worked")
        self.time_tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.time_tree.heading(col, text=col)
            self.time_tree.column(col, width=100)

        self.time_tree.pack(expand=True, fill="both")

        # Sample data
        time_data = [
            ("2024-09-06", "09:00 AM", "05:00 PM", "8"),
            ("2024-09-05", "08:30 AM", "04:30 PM", "8"),
            ("2024-09-04", "09:15 AM", "05:15 PM", "8"),
        ]

        for item in time_data:
            self.time_tree.insert("", "end", values=item)

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=f"Current Time: {current_time}")
        self.after(1000, self.update_time)

    def toggle_clock(self):
        if self.clock_button.cget("text") == "Clock In":
            self.clock_button.config(text="Clock Out")
            # Here you would typically record the clock-in time
        else:
            self.clock_button.config(text="Clock In")
            # Here you would typically record the clock-out time and calculate hours worked