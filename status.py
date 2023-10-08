"""
    Status Class
    @author Lehrman, Aidin
"""

import math
import time
from colors import red, green, blue, yellow

class Status:
    def __init__(self, image_width: int, image_height: int) -> None:
        self.image_width: int = image_width
        self.image_height: int = image_height
        self.start_time: float = 0
        self.average_time_per_row: float = 0
        self.samples = 0
        
    def reset(self) -> None:
        self.start_time =  0
        
    def start(self) -> None:
        self.start_time: float = time.time()
    
    def get_time(self) -> float:
        return time.time() - self.start_time
    
    def set_rolling_average(self, new_sample: float) -> float:
        self.samples += 1
        self.average_time_per_row -= self.average_time_per_row / self.samples
        self.average_time_per_row += new_sample / self.samples
        return self.average_time_per_row
    
    def calculate_estimated_time_left(self, j: int) -> float:
        rows_left: int = self.image_height - j
        return self.average_time_per_row * rows_left
    
    def print_status(self, j: int) -> None:
        # Progress
            scanlines_remaining = self.image_height - j
            completed_percent: int = math.floor(j / self.image_height * 50)
            upcomming_percent: int = math.floor(50 - completed_percent)

            # Prints progress bar and percentage
            print(yellow('\r\tScanlines Remaining: '), end='')
            print(blue(f"{' ' * ( 3 - len(str(scanlines_remaining)))}{scanlines_remaining}\t"), end='')
            print(green(f"|{'■' * completed_percent}{' ' * upcomming_percent}| "), end='')
            print(red(f"{j / self.image_height * 100:.2f}%\t"), end='')
            print(blue(f'Average Time per Row: {self.average_time_per_row:.3f} seconds\tEstimated Time Left: {self.calculate_estimated_time_left(j):.3f} seconds\t\t\t\t\t'), end='')