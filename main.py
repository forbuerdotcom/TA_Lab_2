import tkinter as tk
from tkinter import ttk, messagebox
from models import WallPaper, Tile, Laminate

root = tk.Tk()
root.title("Вариант №10. Отделочные материалы")
root.geometry("1180x640")

def calculateSomething():
    area = squareMetersEntity.get()
    material = typeMaterialCombobox.get()
    price = valueForUnitEntity.get()

    resultText.delete(1.0, tk.END)

    resultText.insert(tk.END, "     ДАННЫЕ УСПЕШНО! ПОСЧИТАНЫ     \n")
    resultText.insert(tk.END, f"Площадь: {area}\n")
    resultText.insert(tk.END, f"Материал: {material}\n")
    resultText.insert(tk.END, f"Цена: {price}\n")

squareMetersLabel = tk.Label(root, text="Площадь помещения (кв.м):", font=("Arial", 14))
squareMetersLabel.place(relx=0.04,rely=0.04)
squareMetersEntity = tk.Entry(root, font=("Arial", 14))
squareMetersEntity.place(relx=0.25,rely=0.04)

typeMaterialLabel = tk.Label(root, text="Тип материала:", font=("Arial", 14))
typeMaterialLabel.place(relx=0.04,rely=0.14)
typeMaterialCombobox = ttk.Combobox(root, values=("Обои", "Плитка","Ламинат"), state="readonly", font=("Arial", 14))
typeMaterialCombobox.place(relx=0.25,rely=0.14)

valueForUnitLabel = tk.Label(root,text="Цена за единицу(руб):", font=("Arial", 14))
valueForUnitLabel.place(relx=0.04,rely=0.24)
valueForUnitEntity = tk.Entry(root,  font=("Arial", 14))
valueForUnitEntity.place(relx=0.25,rely=0.24)

сalculateSomethingButton = tk.Button(root, text="РАССЧИТАТЬ", font=("Arial",14), command=calculateSomething)
сalculateSomethingButton.place(relx=0.07,rely=0.35)
saveReportButton = tk.Button(root, text="СОХРАНИТЬ ОТЧЕТ", font=("Arial",14))
saveReportButton.place(relx=0.23,rely=0.35)

resultText = tk.Text(root, font=("Arial", 14))
resultText.place(relx=0.5, rely=0.05, relwidth=0.45, relheight=0.9)






root.mainloop()

