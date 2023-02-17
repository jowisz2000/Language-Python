import zad2
import GameOfLife


board = GameOfLife.GameOfLife(30, 10, 5)
for i in range(3):
    board.evolve()

print(board)
