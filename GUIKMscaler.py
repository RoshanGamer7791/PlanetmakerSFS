import tkinter as tk

root = tk.Tk()
root.title("KM to Meters Scaler")
km = tk.DoubleVar(value=315)
m = 0
mdv = 315000

    
frame = tk.Frame(root, bg="black").pack(fill="both", expand=True)
entry = tk.Entry(frame, textvariable=km, bg="black", fg="white", font=("Segoe UI", 30, "bold")).pack(fill="x", expand=True)
label = tk.Label(frame, text=f"Meters: {m}", bg="black", fg="white", font=("Segoe UI", 30, "bold"))
label.pack(fill="x", expand=True)

def scale():
    global m, mdv
    m = km.get() * 1000
    mdv = tk.DoubleVar(value=m)
    print(m)
    label.config(text=f"Meters: {m}")
    
button = tk.Button(frame, bg="black", fg="white", font=("Segoe UI", 30, "bold"), text="Submit", command=scale).pack(fill="x", expand=True)

root.mainloop()