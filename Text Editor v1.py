import tkinter as tk
from tkinter import filedialog, messagebox


class NoteGUI:
    def __init__(self, master):
        self.master = master
        
        master.geometry("450x650+100+400")
        self.create_widgets()
        
        self.color_combinations = (
            ["Monochrome Black", "#FFFFFF", "#000000", "#1E1E1E"],
            ["Classic White", "#000000", "#FFFFFF", "#DDDDDD"],
            ["Nordic Light Gray", "#2E3440", "#D8DEE9", "#E5E9F0"],
            ["Forest Mist", "#A3BE8C", "#4B5263", "#6B7082"],
            ["Autumn Twilight", "#D08770", "#4C566A", "#5E81AC"],
            ["Sapphire Sky", "#89BDDE", "#F3F3F3", "#3A3A3A"],
            ["Mint Frost", "#A3BE8C", "#E5EDF0", "#E2F0F3"],
            ["Crystal Clear", "#C0D3E3", "#F0F6F9", "#E7F3FA"],
            ["Ashen Slate", "#636363", "#D2D5D8", "#F1F1F1"],
            ["Arctic Night", "#2E3440", "#D8DEE9", "#EFF6FF"], 
            ["Golden Horizon", "#E1AD75", "#F3DFA2", "#E6D7B2"], 
            ["Mauve Mist", "#D49BD9", "#F6F2F9", "#BFAAC2"], 
            ["Ocean Breeze", "#61A0A8", "#A7CACF", "#E1E7ED"], 
            ["Coral Reef", "#F25F5C", "#FFE066", "#247BA0"],
            ["Sunset Serenade", "#FFA69E", "#FAE3D9", "#AED9E0"],
            ["Emerald Isle", "#719949", "#A5C882", "#D0E2AA"],
            ["Onyx Black", "#F2F2F2", "#333333", "#1A1A1A"],
            ["Midnight Velvet", "#2E2E2E", "#4B4B4B", "#6C6C6C"],
            ["Raven's Feather", "#3A3A3A", "#5D5D5D", "#7F7F7F"],
            ["Dark Green", "#00FF00", "#222222", "#006400"],
            ["Dark Blue", "#3E90FF", "#222222", "#000BCD"],
            ["Gothic Grace", "#191919", "#2A2A2A", "#383838"],
            ["Sable Sunset", "#8B4513", "#9E8700", "#AD7F38"]
        )

    def create_widgets(self):
        
        self.had_file = False
        
        self.fg_color = "black"
        self.current_bg_color = "white"
        self.current_btn_color = "light gray"
                
        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)
        
        text_area_frame = tk.Frame(self.master)
        text_area_frame.pack()
        
        self.text_area = tk.Text(text_area_frame, font=("Mono sans", 11), width=30, height=70)
        self.scrollbar = tk.Scrollbar(text_area_frame, command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.text_area.pack(side=tk.LEFT)
        
        self.file_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=self.file_menu, label="File")
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Close File", command=self.close_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=quit)
        
        self.edit_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=self.edit_menu, label="Edit")
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Paste",command=self.paste_text)
        self.edit_menu.add_command(label="Select All",command=self.select_all_text)
        
        self.editor_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(menu=self.editor_menu, label="Theme")
        self.editor_menu.add_command()
        self.editor_menu.add_command(label="Choose Theme", command=self.choose_theme)        
    
    def save_file(self):
        text = self.text_area.get("1.0", tk.END)
        if text.strip() == "" or text is None:
            messagebox.showerror("Saving File Error", "Can't save an empty text")
            return
            
        if not self.had_file:
            self.frame = tk.Toplevel(self.master, bg=self.current_bg_color)
            self.frame.title("Enter the file name")
            self.entry = tk.Entry(self.frame, fg=self.fg_color)
            self.entry.pack(ipady=7, padx=10, pady=(20,10))
            self.confirm_button = tk.Button(self.frame, text="Confirm", bd=5, relief=tk.RAISED, bg=self.current_btn_color, fg=self.fg_color, command=lambda t=text: self.save_text_title(t))
            self.confirm_button.pack(pady=(0,20))
            
        else:
            self.file_input = open(self.file_path, "w+")
            self.file_input.write(text)
            self.file_input.close()
            self.text_area.delete("1.0", tk.END)
            messagebox.showinfo("Done!!!", "Text successfully saved!!!")
            
    def save_text_title(self, text):
        filename = self.entry.get()
        if filename:
            file_path = f"/storage/emulated/0/documents/{filename}.txt"
            file = open(file_path, "w+")
            file.write(text)
            file.close()
            self.frame.destroy()
            messagebox.showinfo("Done!!!", "Text successfully saved!!!")
            self.text_area.delete("1.0", tk.END)
        else:
            messagebox.showerror("Empty text file name", "Please enter the file\nname of your text!!!!")
    
    def choose_theme(self):
        
        color_choose_frame = tk.Toplevel(self.master)
        color_choose_frame.resizable(False, False)
        color_choose_frame.title("Theme")
        self.theme_box = tk.Listbox(color_choose_frame)
        self.theme_box.pack(side=tk.LEFT)
        
        scrollbar = tk.Scrollbar(color_choose_frame, command=self.theme_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.theme_box.config(yscrollcommand=scrollbar.set)
        
        for bg_text_value, txt_color, bg_color, btn_color in self.color_combinations:
            self.theme_box.insert(tk.END, bg_text_value)
        self.theme_box.bind("<<ListboxSelect>>", self.change_theme)
    
    def change_theme(self, event):
        selected_indices = self.theme_box.curselection()
        if not selected_indices:  # Check if anything is selected
            messagebox.showerror("No Theme Selected", "Please select a theme.")
            return

        chosen_bg_color_index = selected_indices[0]
        chosen_bg_color = self.color_combinations[chosen_bg_color_index][0]

        for bg_text_value, txt_color, bg_color, btn_color in self.color_combinations:
            if chosen_bg_color == bg_text_value:
                self.fg_color = txt_color
                self.current_bg_color = bg_color
                self.current_btn_color = btn_color
                self.change_widgets_theme()
    
    def change_widgets_theme(self):
        self.menubar.config(bg=self.current_bg_color, fg=self.fg_color)
        self.text_area.config(bg=self.current_bg_color, fg=self.fg_color)
        self.scrollbar.config(bg=self.current_bg_color)
        self.file_menu.config(bg=self.current_bg_color, fg=self.fg_color)
        self.edit_menu.config(bg=self.current_bg_color, fg=self.fg_color)
        self.editor_menu.config(bg=self.current_bg_color, fg=self.fg_color)
        
    def open_file(self):
        file = File()
        self.file_path = file.open()
        if self.file_path:
            self.file_input = open(self.file_path, "r")
            text = self.file_input.read()
            self.text_area.insert(tk.END, text)
            self.file_input.close()
            self.had_file = True
        else:
            messagebox.showerror("Opening File Error", "Please select the file text you want to choose")
    
    def close_file(self):
        if self.had_file:
            self.had_file = False
            self.text_area.delete("1.0", tk.END)
        else:
            messagebox.showerror("Closing File Error", "No file is currently open!!!")
    
    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
    
    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")
    
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")
    
    def select_all_text(self):
        self.text_area.tag_add("sel", "1.0", tk.END)
    
        
class File:
        def open(self):
            file_path = filedialog.askopenfilename(filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
                ], 
                initialdir="/storage/emulated/0/documents",
                title="Select file to open")
            return file_path
        
        def save(self, text):
            file = filedialog.asksaveasfile()
            if file:
                file_text = open(file, "w")
                file_text.write(text)
                file_text.close()
        
def main():
    root = tk.Tk()
    NoteGUI(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()