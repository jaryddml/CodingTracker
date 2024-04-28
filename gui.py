import tkinter as tk
from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def fetch_detailed_data():
    conn = sqlite3.connect('tracker.db')
    cur = conn.cursor()
    cur.execute("SELECT name, extension, directory, duration FROM tasks")
    rows = cur.fetchall()
    conn.close()
    return rows

def fetch_extension_data():
    conn = sqlite3.connect('tracker.db')
    cur = conn.cursor()
    cur.execute("SELECT extension, SUM(duration) FROM tasks GROUP BY extension ORDER BY SUM(duration) DESC")
    data = cur.fetchall()
    conn.close()
    return data
def setup_gui():
    root = tk.Tk()
    root.title("Data Viewer with Pie Chart")

    # Create a top frame for the Treeview
    top_frame = ttk.Frame(root)
    top_frame.pack(fill=tk.BOTH, expand=True)

    # Create a bottom frame for the pie chart
    bottom_frame = ttk.Frame(root)
    bottom_frame.pack(fill=tk.BOTH, expand=True)

    # Setup the Treeview in the top frame
    tree = ttk.Treeview(top_frame, columns=("Name", "Extension", "Directory", "Duration"), show="headings")
    tree.heading("Name", text="File Name")
    tree.heading("Extension", text="File Extension")
    tree.heading("Directory", text="Directory")
    tree.heading("Duration", text="Duration")
    tree.pack(expand=True, fill=tk.BOTH)

    # Fetching detailed data and inserting into the Treeview
    detailed_data = fetch_detailed_data()
    for row in detailed_data:
        tree.insert('', 'end', values=row)

    # Setup pie chart in the bottom frame
    data = fetch_extension_data()
    extensions = [x[0] for x in data]
    durations = [x[1] for x in data]

    fig = Figure(figsize=(6, 6), dpi=100)
    plot = fig.add_subplot(1, 1, 1)
    plot.pie(durations, labels=extensions, autopct='%1.1f%%', startangle=140)
    plot.set_title('Time Spent on Different File Extensions')

    canvas = FigureCanvasTkAgg(fig, master=bottom_frame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()

