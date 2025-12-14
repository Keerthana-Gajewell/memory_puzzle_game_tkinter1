import tkinter as tk
import random
import time
from tkinter import messagebox

EMOJIS = ["🍎","🍇","🍒","🍓","🍉","🍐","🍌"]
PAIRS =  EMOJIS*2
TIME_LIMIT = 60

class MemoryGame:
    def __init__(self, root):
        self.root = root
        root.title("Memory Puzzle Game")
        root.geometry("420x520")
        root.resizable(False,False)

        self.button = []
        self.filpped = []
        self.matched = set()
        self.time_left = TIME_LIMIT
        self.first_click_match = None

        self.create_widget()
        self.reset_game()
    
        def create_widget(self):
            title = tk.Label(self.root, text="Memory Puzzle Game", font=("Arial", 22, "bold"))
            title.pack(pady=10)
    
            self.timer_label = tk.Label(self.root, text=f"time_left:{self.time_left}", font=("Arial", 16))
            self.timer_label.pack(pady=5)
    
            self.frame = tk.Frame(self.root)
            self.frame.pack()
    
            # create 16 buttons (4x4 grid):
            for i in range(16):
                btn = tk.Button(self.frame, text="❓", font=("Arial", 16), command=lambda i=i: self.flip_card(i))
                btn.grid(row=i // 4, column=i % 4, padx=10, pady=10)
                self.button.append(btn)
    
            restart_btn = tk.Button(self.root, text="Restart Game", font=("Arial", 14), bg="Orange", fg="White", command=self.reset_game)
            restart_btn.pack(pady=10)
    
        def reset_game(self):
            random.shuffle(PAIRS)
            self.cards = PAIRS.copy()
            self.time_left = TIME_LIMIT
            self.flipped = []
            self.matched = set()
            self.update_timer()
    
            for btn in self.button:
                btn.config(text="❓", state="normal", bg="SystemButtonFace")
    
        def update_timer(self):
            self.timer_label.config(text=f"time_left:{self.time_left}")
    
            if self.time_left <= 0:
                messagebox.showinfo("⌛ Time's Up!", "You ran out of time")
                self.disable_all()
                return
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
    
        def flip_card(self, index):
            if index in self.matched:
                return
            if index in self.flipped:
                return
            
            btn = self.button[index]
            btn.config(text=self.cards[index])
            
            self.flipped.append(index)
    
            if len(self.flipped) == 2:
                self.root.after(600, self.check_match)
    
        def check_match(self):
            i, j = self.flipped
    
            if self.cards[i] == self.cards[j]:
                self.matched.add(i)
                self.matched.add(j)
    
                self.button[i].config(bg="LightGreen", state="disabled")
                self.button[j].config(bg="LightGreen", state="disabled")
    
                if len(self.matched) == 16:
                    messagebox.showinfo("Congratulations!", "🎉 You matched all the cards!")
            else:
                self.button[i].config(text="❓")
                self.button[j].config(text="❓")
    
            self.flipped = []
    
        def disable_all(self):
            for btn in self.button:
                btn.config(state="disabled")
    
    
        # ---Run Game---
    if __name__ == "__main__":
        root = tk.Tk()
        app = MemoryGame(root)
        root.mainloop()

            

                       

