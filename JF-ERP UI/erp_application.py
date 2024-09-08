import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb
from config import APP_NAME, WINDOW_SIZE, THEME

from .inventory_dashboard import InventoryDashboard
from .customers_dashboard import CustomersDashboard
from .sales_dashboard import SalesDashboard
from .purchasing_dashboard import PurchasingDashboard
from .manufacturers_dashboard import ManufacturersDashboard
from .supply_chain_dashboard import SupplyChainDashboard
from .finance_dashboard import FinanceDashboard

class ERPApplication(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title(APP_NAME)
        self.master.geometry(WINDOW_SIZE)
        
        self.style = ttkb.Style(theme=THEME)
        self.style.configure("TNotebook", background="#4B9CD3")
        self.style.configure("TNotebook.Tab", background="#4B9CD3", foreground="white")
        self.style.map("TNotebook.Tab", background=[("selected", "#3A7CA5")])

        self.create_widgets()
        self.pack(fill=tk.BOTH, expand=True)

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.inventory_tab = InventoryDashboard(self.notebook)
        self.customers_tab = CustomersDashboard(self.notebook)
        self.sales_tab = SalesDashboard(self.notebook)
        self.purchasing_tab = PurchasingDashboard(self.notebook)
        self.manufacturers_tab = ManufacturersDashboard(self.notebook)
        self.supply_chain_tab = SupplyChainDashboard(self.notebook)
        self.finance_tab = FinanceDashboard(self.notebook)

        self.notebook.add(self.inventory_tab, text="Inventory")
        self.notebook.add(self.customers_tab, text="Customers")
        self.notebook.add(self.sales_tab, text="Sales")
        self.notebook.add(self.purchasing_tab, text="Purchasing")
        self.notebook.add(self.manufacturers_tab, text="Manufacturers")
        self.notebook.add(self.supply_chain_tab, text="Supply Chain")
        self.notebook.add(self.finance_tab, text="Finance")