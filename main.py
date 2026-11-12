import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from models import WallPaper, Tile, Laminate
from reporter import save_report_to_word

root = tk.Tk()
root.title("Вариант №10. Отделочные материалы")
root.geometry("1180x640")

def calculateSomething():
    area_str = squareMetersEntity.get()
    material_str = typeMaterialCombobox.get()
    price_str = valueForUnitEntity.get()

    resultText.delete("1.0", tk.END)

    try:
        area = float(area_str)
        price = float(price_str)

        if material_str == "Обои":
            material_obj = WallPaper(area, price)
        elif material_str == "Плитка":
            material_obj = Tile(area, price)
        else:
            material_obj = Laminate(area, price)

        quantity = material_obj.calculate_quantity()
        unit = material_obj.get_unit()
        total_cost = material_obj.get_price()

        resultText.insert(tk.END, "    РЕЗУЛЬТАТ РАСЧЕТА    \n\n")
        resultText.insert(tk.END, f"Материал: {material_str}\n")
        resultText.insert(tk.END, f"Площадь: {area} кв.м.\n")
        resultText.insert(tk.END, f"Цена за 1 ед.: {price} руб.\n")
        resultText.insert(tk.END, "-" * 85 + "\n")
        resultText.insert(tk.END, f"Нужно купить: {quantity:.2f} {unit}\n")
        resultText.insert(tk.END, f"ИТОГО К ОПЛАТЕ: {total_cost:.2f} руб.\n")

    except ValueError as e:
        messagebox.showerror("Ошибка ввода", f"Некорректные данные!\n\n{e}")

def saveReportForNow():
    text_to_save = resultText.get("1.0", tk.END)

    if not text_to_save.strip():
        messagebox.showwarning("Внимание","Сначала нажмите на кнопку рассчитать")
        return

    filepath = filedialog.asksaveasfilename(
        title="Сохранить отчет:",
        defaultextension=".docx",
        filetypes = [("Word Document", "*.docx")]
    )

    if filepath:
        try:
            save_report_to_word(filepath, text_to_save)
            messagebox.showinfo("Успех", "Отчет успешно сохранен в Word!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")







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
saveReportButton = tk.Button(root, text="СОХРАНИТЬ ОТЧЕТ", font=("Arial",14), command=saveReportForNow)
saveReportButton.place(relx=0.23,rely=0.35)

resultText = tk.Text(root, font=("Arial", 14))
resultText.place(relx=0.5, rely=0.05, relwidth=0.45, relheight=0.9)






root.mainloop()

