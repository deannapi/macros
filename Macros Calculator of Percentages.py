#Macros based off percentages

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Find my macros')

bw = tk.Label(root, text ='Enter bodyweight (in lbs):')
bw.grid(column = 1, columnspan=2, row=1)
bw_var = tk.IntVar()
bw_var.set('')
bw_entry = tk.Entry(root, textvariable =bw_var)
bw_entry.grid(column =3, row=1)

prt_pcnt = tk.Label(root, text='Enter the % for Protein, Carbs and Fats:', justify=tk.RIGHT)
prt_pcnt.grid(column =1, row=3, columnspan=2)
prt_var = tk.IntVar()
prt_var.set('')
prt_entry = tk.Entry(root, textvariable =prt_var)
prt_entry.grid(column =3, row=3)
carb_var = tk.IntVar()
carb_var.set('')
carb_entry = tk.Entry(root, textvariable =carb_var)
carb_entry.grid(column =4, row=3)
fat_var = tk.IntVar()
fat_var.set('')
fat_entry = tk.Entry(root, textvariable =fat_var)
fat_entry.grid(column =5, row=3)

plans = {
        'Maintain': 0,
        'Fat Loss': -500, 
        'Muscle Gain': 350
        }

levels = {
        'Low': 12,
        'Low Medium': 13,
        'Medium': 14,
        'Medium High': 15,
        'High': 16
        }

plan = tk.Label(root, text = 'Choose a plan:',justify=tk.RIGHT)
plan.grid(column = 1, columnspan = 2, row = 5)
plan_var = tk.StringVar(root)
plan_var.set('Maintain')
plan_dropdown = tk.OptionMenu(root, plan_var, *plans)
plan_dropdown.grid(column = 3, row = 5)

agg = tk.Label(root, text='Choose a calorie level: ', justify = tk.RIGHT)
agg.grid(column = 1, columnspan = 2, row = 7)
maint_var = tk.StringVar(root)
maint_var.set('Low')
maint_dropdown = tk.OptionMenu(root, maint_var, *levels)
maint_dropdown.grid(column = 3, row = 7)

results = tk.Label(root, text='Results:', justify = tk.LEFT, font=('helvetica 12 bold'), fg='purple2')
results.grid(column = 1, row = 11)
protein_label = tk.Label(root, text='Protein', justify=tk.LEFT, font=('verdana 10 bold'))
protein_label.grid(column = 2, row=12, columnspan = 1)
carbs_label = tk.Label(root, text='Carbs', justify=tk.LEFT,font=('verdana 10 bold'))
carbs_label.grid(column = 3, row=12, columnspan = 1)
fat_label = tk.Label(root, text='Fat', justify=tk.LEFT,font=('verdana 10 bold'))
fat_label.grid(column = 4, row=12, columnspan = 1)
grams_lb = tk.Label(root, text='Grams', justify=tk.RIGHT,font=('verdana 10 bold'))
grams_lb.grid(column = 1, row=14)
cal_lb = tk.Label(root, text='Calories',justify=tk.RIGHT,font=('verdana 10 bold'))
cal_lb.grid(column =1, row=15)
total_lb = tk.Label(root, text='Total',font=('verdana 10 bold'))
total_lb.grid(column = 5, row=12, columnspan = 1)

#BUTTON for submitting bodweight and percent selections
def calculate():
   calories_total = plans[plan_var.get()] + levels[maint_var.get()] * int(bw_entry.get())
   print(calories_total)
   total_cals = tk.Label(root, text=calories_total, font=('verdana 10 bold'), fg='violet red')
   total_cals.grid(column=5, row=15)
   prt_cals = calories_total * float(prt_entry.get())/float(100)
   carb_cals = calories_total * float(carb_entry.get())/float(100)
   fat_cals = calories_total * float(fat_entry.get())/float(100)
   print(prt_cals, carb_cals, fat_cals)
   prt_cals2 = tk.Label(root, text=prt_cals)
   prt_cals2.grid(column=2, row=15, columnspan = 1)
   carb_cals2 = tk.Label(root, text=carb_cals)
   carb_cals2.grid(column=3, row=15, columnspan = 1)
   fat_cals2 = tk.Label(root, text=fat_cals)
   fat_cals2.grid(column=4, row=15, columnspan = 1)
   prt_grams = round(prt_cals / 4,0)
   prt_grams2 = tk.Label(root, text=prt_grams)
   prt_grams2.grid(column=2, row=14, columnspan = 1)
   carb_grams = round(carb_cals /4,0)
   carb_grams2 = tk.Label(root, text=carb_grams)
   carb_grams2.grid(column=3, row=14, columnspan = 1)
   fat_grams = round(fat_cals / 9,0)
   fat_grams2 = tk.Label(root, text=fat_grams)
   fat_grams2.grid(column=4, row=14, columnspan = 1)
   total_percent = int(prt_entry.get()) + int(carb_entry.get()) + int(fat_entry.get())
   if total_percent >100 or total_percent < 100:
       tk.messagebox.showerror('Error','Percentages must equal 100!')
    
submit = tk.Button(root, text='Calculate', command=calculate, font=('helvetica 10 bold'),background='PaleVioletRed1', fg='gray1')
submit.grid(column=3, row=9)

root.mainloop()