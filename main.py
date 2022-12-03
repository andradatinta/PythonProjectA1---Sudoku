import random
import pygame

width = 750
background = (52, 58, 64)
number_color = (248, 249, 250)
grid_test = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
[6, 0, 0, 0, 7, 5, 0, 0, 9],
[0, 0, 0, 6, 0, 1, 0, 7, 8],
[0, 0, 7, 0, 4, 0, 2, 6, 0],
[0, 0, 1, 0, 5, 0, 9, 3, 0],
[9, 0, 4, 0, 6, 0, 0, 0, 5],
[0, 7, 0, 3, 0, 0, 0, 1, 2],
[1, 2, 0, 0, 0, 7, 4, 0, 0],
[0, 4, 9, 2, 0, 6, 0, 0, 7]]
grid_test_copy = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
[6, 0, 0, 0, 7, 5, 0, 0, 9],
[0, 0, 0, 6, 0, 1, 0, 7, 8],
[0, 0, 7, 0, 4, 0, 2, 6, 0],
[0, 0, 1, 0, 5, 0, 9, 3, 0],
[9, 0, 4, 0, 6, 0, 0, 0, 5],
[0, 7, 0, 3, 0, 0, 0, 1, 2],
[1, 2, 0, 0, 0, 7, 4, 0, 0],
[0, 4, 9, 2, 0, 6, 0, 0, 7]]

def choose_sudoku_game():
    grid = [
        [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ],
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 7, 0, 8, 0],
            [0, 0, 8, 2, 0, 9, 1, 0, 4],
            [1, 0, 0, 0, 7, 0, 2, 6, 6],
            [4, 5, 9, 0, 0, 0, 0, 0, 0],
            [6, 8, 0, 0, 0, 3, 4, 0, 0],
            [0, 0, 1, 5, 9, 2, 0, 6, 8],
            [0, 6, 0, 0, 0, 4, 9, 0, 2],
            [8, 9, 0, 7, 1, 0, 5, 0, 3]
        ]
    ]
    # grid_copy = grid.copy()
    # print(random.choice(grid))

    return random.choice(grid)

def insert_user_number(game_window, cell_coordinates, chosen_grid, chosen_grid_copy):
    grid_font = pygame.font.SysFont('Comic Sans MS', 35)
    x, y = cell_coordinates[1], cell_coordinates[0] # flipping the values
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if chosen_grid_copy[x-3][y-3] != 0: # daca e ocupata casuta
                    return
                if event.key == 48: #   check with 0 if the value is correct or not
                    chosen_grid[x-3][y-3] = 0  # sau event.key - 48
                    pygame.draw.rect(game_window, background,
                                     (cell_coordinates[0]*50 + 5, cell_coordinates[1]*50 + 5, 50 - 5, 50 - 5))
                    pygame.display.update()
                if 0 < event.key - 48 < 10: # check for valid input
                    pygame.draw.rect(game_window, background,
                                     (cell_coordinates[0] * 50 + 5, cell_coordinates[1] * 50 + 5, 50 - 5, 50 - 5))
                    value = grid_font.render(str(event.key - 48), True, number_color)
                    game_window.blit(value, (cell_coordinates[0]*50 + 15, cell_coordinates[1]*50))
                    chosen_grid[x-3][y-3] = event.key - 48
                    pygame.display.update()
                return
            return

def initialize_game_window(chosen_grid, chosen_grid_copy):
    pygame.init()
    game_window = pygame.display.set_mode((width, width))
    game_window.fill(background)
    grid_font = pygame.font.SysFont('Comic Sans MS', 35)
    pygame.display.set_caption("FIISudoku")

    for line_number in range(0, 10):
        if line_number % 3 == 0:
            # vertical
            pygame.draw.line(game_window, (247, 131, 172), (150 + 50 * line_number, 150), (150 + 50 * line_number, 600), 6)
            # horizontal
            pygame.draw.line(game_window, (247, 131, 172), (150, 150 + 50 * line_number), (600, 150 + 50 * line_number), 6)
        # vertical
        pygame.draw.line(game_window, (208, 191, 255), (150 + 50 * line_number, 150), (150 + 50*line_number, 600), 3)
        # horizontal
        pygame.draw.line(game_window, (208, 191, 255), (150, 150 + 50 * line_number), (600, 150 + 50 * line_number), 3)
    pygame.display.update()

    for i in range(0, len(chosen_grid[0])):
        for j in range(0, len(chosen_grid[0])):
            if 0 < chosen_grid[i][j] < 10:
                value = grid_font.render(str(chosen_grid[i][j]), True, number_color)
                # game_window.blit(value, ((j + 1) * 50 + 100, (i + 1) * 50 + 100))
                game_window.blit(value, ((j + 1) * 50 + 115, (i + 1) * 50 + 100))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                cell_coordinates = pygame.mouse.get_pos()
                print(cell_coordinates)
                insert_user_number(game_window, (cell_coordinates[0]//50, cell_coordinates[1]//50), chosen_grid, chosen_grid_copy) # get index //50
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    # chosen_grid = choose_sudoku_game()
    # chosen_grid_copy = chosen_grid.copy()
    # initialize_game_window(chosen_grid, chosen_grid_copy)
    initialize_game_window(grid_test, grid_test_copy)
    # choose_sudoku_game()
