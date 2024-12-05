import tkinter as tk

class ResultPlotter:
    def __init__(self, master, width=600, height=200):
        self.master = master
        self.width = width
        self.height = height
        self.plot_canvas = None

    def plot(self, history_best_function):
        if self.plot_canvas is not None:
            self.plot_canvas.destroy()

        self.plot_canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg='white')
        self.plot_canvas.pack(pady=10, fill='x', expand=True)

        if not history_best_function:
            return

        generations = [gen for gen, val in history_best_function]
        values = [val for gen, val in history_best_function]

        min_val = min(values)
        max_val = max(values)
        min_gen = min(generations)
        max_gen = max(generations)

        w = self.width
        h = self.height

        gen_range = max_gen - min_gen if max_gen != min_gen else 1
        val_range = max_val - min_val if max_val != min_val else 1

        def scale_x(gen):
            return 50 + (gen - min_gen) / gen_range * (w - 100)

        def scale_y(val):
            return h - 20 - ((val - min_val) / val_range * (h - 40))

        self.plot_canvas.create_line(40, h - 20, w - 40, h - 20, fill='black')
        self.plot_canvas.create_line(50, 20, 50, h - 20, fill='black')

        for i in range(len(values) - 1):
            x1 = scale_x(generations[i])
            y1 = scale_y(values[i])
            x2 = scale_x(generations[i + 1])
            y2 = scale_y(values[i + 1])
            self.plot_canvas.create_line(x1, y1, x2, y2, fill='blue', width=2)

        final_x = scale_x(generations[-1])
        final_y = scale_y(values[-1])
        self.plot_canvas.create_oval(final_x - 4, final_y - 4, final_x + 4, final_y + 4, fill='red', outline='red')

        self.plot_canvas.create_text(50, 10, text="Best Function Value", anchor='w', font=('Arial', 10, 'bold'))
        self.plot_canvas.create_text(w // 2, h - 5, text="Generation", anchor='center', font=('Arial', 10, 'bold'))

        self.plot_canvas.create_text(55, scale_y(min_val), text=f"{min_val:.2f}", anchor='w', font=('Arial', 8))
        self.plot_canvas.create_text(55, scale_y(max_val), text=f"{max_val:.2f}", anchor='w', font=('Arial', 8))

        if gen_range > 0:
            self.plot_canvas.create_text(scale_x(min_gen), h - 15, text=str(min_gen), anchor='center', font=('Arial', 8))
            self.plot_canvas.create_text(scale_x(max_gen), h - 15, text=str(max_gen), anchor='center', font=('Arial', 8))
