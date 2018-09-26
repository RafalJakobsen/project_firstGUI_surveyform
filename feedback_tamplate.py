from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Feedback:

    def __init__(self, master):
        # 21. Program title
        master.title("Explore California Feedback")
        # 22. Resize
        master.resizable(False, False)
        # 23. Background
        master.configure(background="#e1d8b9")

        # 24. defult background for widget
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#e1d8b9")
        self.style.configure("TButton", background="#e1d8b9")
        self.style.configure("TLabel", background="#e1d8b9", font=("Arial", 11))
        self.style.configure("Header.TLabel", font=("Arial", 18, "bold"))

        # 1. Frame: header
        self.frame_header = ttk.Frame(master)
        # 9. place into window with pack
        self.frame_header.pack()

        # 2. Label: logo(image)
        self.logo = PhotoImage(file="tour_logo.gif")

        # 3. Label: header #11. add grid directly to code #15. added padding # 25. added style
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2, padx=5)
        ttk.Label(self.frame_header, text='Thanks for Exploring!', style="Header.TLabel").grid(row=0, column=1, padx=5)
        ttk.Label(self.frame_header, wraplength=300,
                  text="We`re glad you chose Explore California for your recent adventure.   "
                       "Please tell us what you thought about the `Desert to Sea` tour").grid(row=1, column=1, padx=5)

        # 4. Frame: contents
        self.frame_content = ttk.Frame(master)
        # 10. place into window
        self.frame_content.pack()

        # 5. Label: Name, Email, Comments #12. add grid directly to code #14. adding padding #17. adding sticky "sw"
        ttk.Label(self.frame_content, text="Name: ").grid(row=0, column=0, padx=5, sticky="sw")
        ttk.Label(self.frame_content, text="Email: ").grid(row=0, column=1, padx=5, sticky="sw")
        ttk.Label(self.frame_content, text="Comments: ").grid(row=2, column=0, padx=5, sticky="sw")

        # 6. Entry: name, email
        self.entry_name = ttk.Entry(self.frame_content, width=24, font=("Arial", 10))
        self.entry_email = ttk.Entry(self.frame_content, width=24, font=("Arial", 10))

        # 7. Text: comments
        self.text_comments = Text(self.frame_content, width=50, height=10, font=("Arial", 10))

        # 13. call grid on entry variables
        self.entry_name.grid(row=1, column=0)
        self.entry_email.grid(row=1, column=1)
        self.text_comments.grid(row=3, column=0, columnspan=2)

        # 8. Button: submit, clear #14. add grid directly to code since no variable #16. added padding #18. adding sticky
        ttk.Button(self.frame_content, text="Submit", command=self.submit).grid(row=4, column=0, padx=5, sticky="e")
        ttk.Button(self.frame_content, text="Clear", command=self.clear).grid(row=4, column=1, padx=5, sticky="w")

    # 19. submit action, then connect above with command code
    def submit(self):
        print("Name: {}".format(self.entry_name.get()))
        print("Email: {}".format(self.entry_email.get()))
        print("Comments: {}".format(self.text_comments.get(1.0, "end")))
        self.clear()
        messagebox.showinfo(title="Explore California Feedback", message="Comments Submitted")

    # 20. clear action
    def clear(self):
        self.entry_name.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.text_comments.delete(1.0, "end")


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__": main()
