import tkinter as tk
import random
import time

# Sample sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language.",
    "Speed typing tests are a fun way to improve skills.",
    "Practice makes perfect when it comes to typing.",
    "The rain in Spain stays mainly in the plain."
]


class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")

        self.sentence = random.choice(sentences)
        self.start_time = None

        self.label = tk.Label(root, text="Type the following sentence:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.display_sentence = tk.Label(root, text=self.sentence, font=("Arial", 14))
        self.display_sentence.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_typing, state=tk.DISABLED)
        self.submit_button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()
            self.submit_button.config(state=tk.NORMAL)

    def check_typing(self):
        user_input = self.entry.get()
        end_time = time.time()
        time_taken = end_time - self.start_time

        words_typed = len(user_input.split())
        minutes_taken = time_taken / 60
        wpm = words_typed / minutes_taken if minutes_taken > 0 else 0

        correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(self.sentence) and c == self.sentence[i])
        accuracy = (correct_chars / len(self.sentence)) * 100 if len(self.sentence) > 0 else 0

        result_text = (
            f"Time taken: {time_taken:.2f} seconds\n"
            f"Typing Speed: {wpm:.2f} words per minute\n"
            f"Accuracy: {accuracy:.2f}%"
        )
        self.result_label.config(text=result_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()

