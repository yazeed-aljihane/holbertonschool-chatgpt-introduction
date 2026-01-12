#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines_count = mines
        # التأكد من عدم تجاوز عدد الألغام لمساحة اللوحة
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(str(i).ljust(2) for i in range(self.width)))
        for y in range(self.height):
            print(str(y).ljust(2), end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('* ', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f"{count if count > 0 else ' '} ", end=' ')
                else:
                    print('. ', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height) or self.revealed[y][x]:
            return True
        
        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)
        return True

    # الآلية الجديدة للكشف عن الفوز
    def is_win(self):
        revealed_count = sum(row.count(True) for row in self.revealed)
        safe_cells_count = (self.width * self.height) - self.mines_count
        return revealed_count == safe_cells_count

    def play(self):
        while True:
            self.print_board()
            
            # التحقق من الفوز في بداية كل دورة
            if self.is_win():
                self.print_board(reveal=True)
                print("Congratulations! You revealed all safe cells. YOU WIN!")
                break
                
            try:
                x = int(input(f"Enter x (0-{self.width-1}): "))
                y = int(input(f"Enter y (0-{self.height-1}): "))
                
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid coordinates.")

if __name__ == "__main__":
    game = Minesweeper(width=5, height=5, mines=3) # تصغير الحجم للتجربة السريعة
    game.play()
