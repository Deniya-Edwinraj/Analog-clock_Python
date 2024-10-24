import tkinter as tk
import math
import time

class EnhancedStylishAnalogClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Enhanced Stylish Analog Clock")
        self.geometry("400x400")
        self.canvas = tk.Canvas(self, width=400, height=400, bg='lightblue')
        self.canvas.pack()

        self.update_clock()

    def update_clock(self):
        # Clear the canvas
        self.canvas.delete("all")
        
        # Draw the gradient background
        self.draw_gradient_background()

        # Draw the clock face
        self.draw_clock_face()

        # Get the current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12  # Convert to 12-hour format
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Draw clock hands with smooth movement
        self.draw_hand(hours + minutes / 60, 12, 60, "black", 6)    # Hour hand
        self.draw_hand(minutes + seconds / 60, 60, 80, "black", 4)  # Minute hand
        self.draw_hand(seconds, 60, 100, "red", 2)                   # Second hand

        # Draw center dot
        self.draw_center_dot()

        # Schedule the next update
        self.after(1000, self.update_clock)

    def draw_gradient_background(self):
        # Create a gradient background
        for i in range(400):
            color = f'#{int(255 - (i * 0.5)):02x}cfe8'
            self.canvas.create_line(0, i, 400, i, fill=color)

    def draw_clock_face(self):
        # Draw the clock face circle
        self.canvas.create_oval(50, 50, 350, 350, fill="white", outline="black", width=4)

        # Draw hour markers with styling
        for i in range(12):
            angle = math.radians(i * 30)  # 360 degrees / 12 hours = 30 degrees
            x1 = 200 + 120 * math.cos(angle - math.pi / 2)
            y1 = 200 + 120 * math.sin(angle - math.pi / 2)
            x2 = 200 + 140 * math.cos(angle - math.pi / 2)
            y2 = 200 + 140 * math.sin(angle - math.pi / 2)
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=3)

            # Adding number labels
            num_label = str(i + 1)
            self.canvas.create_text(x1 + 5, y1 + 5, text=num_label, font=("Helvetica", 12, "bold"), fill="black")

    def draw_hand(self, value, max_value, length, color, width):
        angle = math.radians(value * (360 / max_value) - 90)  # Adjust angle
        x = 200 + length * math.cos(angle)
        y = 200 + length * math.sin(angle)
        # Draw hand with shadow effect
        self.canvas.create_line(200, 200, x + 2, y + 2, fill="gray", width=width)  # Shadow
        self.canvas.create_line(200, 200, x, y, fill=color, width=width)  # Hand

    def draw_center_dot(self):
        # Draw the center dot with depth
        self.canvas.create_oval(195, 195, 205, 205, fill="black")

if __name__ == "__main__":
    clock = EnhancedStylishAnalogClock()
    clock.mainloop()
