import tkinter as tk
import logging
from ui import ERPApplication

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Starting ERP Application")
        root = tk.Tk()
        app = ERPApplication(root)
        root.mainloop()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    finally:
        logging.info("ERP Application closed")

if __name__ == "__main__":
    main()