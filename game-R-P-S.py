# เกมเป่ายิ้งฉุบด้วย tkinter
import tkinter as tk
import random

def play(user_choice):
    choices = ['ค้อน', 'กระดาษ', 'กรรไกร']
    computer_choice = random.choice(choices)
    result = ''
    if user_choice == computer_choice:
        result = 'เสมอ!'
    elif (
        (user_choice == 'ค้อน' and computer_choice == 'กรรไกร') or
        (user_choice == 'กระดาษ' and computer_choice == 'ค้อน') or
        (user_choice == 'กรรไกร' and computer_choice == 'กระดาษ')
    ):
        result = 'คุณชนะ!'
    else:
        result = 'คุณแพ้!'
    label_result.config(text=f'คุณเลือก: {user_choice}\nคอมพิวเตอร์เลือก: {computer_choice}\nผลลัพธ์: {result}')

root = tk.Tk()
root.title('เกมเป่ายิ้งฉุบ')
root.geometry('300x250')

label_title = tk.Label(root, text='เลือก ค้อน กระดาษ หรือ กรรไกร', font=('Arial', 12))
label_title.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_rock = tk.Button(frame_buttons, text='ค้อน', width=10, command=lambda: play('ค้อน'))
btn_rock.grid(row=0, column=0, padx=5)

btn_paper = tk.Button(frame_buttons, text='กระดาษ', width=10, command=lambda: play('กระดาษ'))
btn_paper.grid(row=0, column=1, padx=5)

btn_scissors = tk.Button(frame_buttons, text='กรรไกร', width=10, command=lambda: play('กรรไกร'))
btn_scissors.grid(row=0, column=2, padx=5)

label_result = tk.Label(root, text='', font=('Arial', 11))
label_result.pack(pady=20)

root.mainloop()
