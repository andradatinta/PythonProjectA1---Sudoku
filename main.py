import random
import pygame
import copy

width = 750
background = (52, 58, 64)
number_color = (248, 249, 250)
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
    choice = random.choice(grid)
    choice_copy = copy.deepcopy(choice)

    return [choice, choice_copy]

def is_cell_empty(num):
    if num == 0:
        return True
    return False

def is_number_valid(position, num, grid):
    # check on row
    for i in range(0, len(grid[0])):
        if grid[position[0]][i] == num:
            return False
    # check on column
    for i in range(0, len(grid[0])):
        if grid [i][position[1]] == num:
            return False
    # check on box
    x = position[0] // 3*3
    y = position[1] // 3*3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x + i][y + j] == num:
                return False
    return True

solved = 0
def sudoku_solver(grid):
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if is_cell_empty(grid[i][j]):
                for k in range(1, 10):
                    if is_number_valid((i, j), k, grid):
                        grid[i][j] = k
                        sudoku_solver(grid)
                        global solved
                        if solved == 1:
                            solution = copy.deepcopy(grid)
                            return solution
                        grid[i][j] = 0
                return 0
    solved = 1
def insert_user_number(game_window, cell_coordinates, chosen_grid, chosen_grid_copy):
    grid_font = pygame.font.SysFont('comicsansms', 35)
    x, y = cell_coordinates[1], cell_coordinates[0] # flipping the values
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if chosen_grid_copy[x-3][y-3] != 0: # if the cell is occupied
                    return
                if event.key == 48: #   check with 0 if the value is correct or not
                    chosen_grid[x-3][y-3] = 0
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
                return chosen_grid
            return

def display_message(image_path, screen):
    error_image = pygame.image.load(image_path)
    rect = error_image.get_rect(center=screen.get_rect().center)
    screen.blit(error_image, rect)
    pygame.display.update()
def initialize_game_window(chosen_grid, chosen_grid_copy, test_copy):

    global to_check
    pygame.init()
    game_window = pygame.display.set_mode((width, width))
    game_window.fill(background)
    grid_font = pygame.font.SysFont('comicsansms', 35)
    pygame.display.set_caption("FIISudoku")
    clock = pygame.time.Clock()
    start = 210

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
                game_window.blit(value, ((j + 1) * 50 + 115, (i + 1) * 50 + 100))
    pygame.display.update()

    # finished = False
    while True:

        total_mins = start//60
        total_secs = start - (60 * total_mins)
        start -= 1

        if start < 0:
            # finished = True
            display_message('images/gameover.png', game_window)
        else:
            text = grid_font.render(("Time left: " + str(total_mins) + ":" + str(total_secs)), True, number_color)
            pygame.draw.rect(game_window, background, (250, 35, 300, 40))
            game_window.blit(text, (250, 30))
            pygame.display.update()
            clock.tick(1)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                cell_coordinates = pygame.mouse.get_pos()
                print(cell_coordinates)
                to_check = insert_user_number(game_window, (cell_coordinates[0]//50, cell_coordinates[1]//50),
                                              chosen_grid, chosen_grid_copy) # get index //50
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    if to_check: # if at least one number was inserted
                        if to_check == test_copy:
                            display_message('images/youwon.png', game_window)
                        else:
                            display_message('images/gameover.png', game_window)
                if event.key == pygame.K_q:
                    pygame.quit()
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    chosen_grid = choose_sudoku_game()
    check_if_solved_copy = copy.deepcopy(chosen_grid[0])
    solved_grid = sudoku_solver(check_if_solved_copy)
    print(f"rezolvat: {solved_grid}")
    print(f"nerezolvat: {chosen_grid[0]}")
    initialize_game_window(chosen_grid[0], chosen_grid[1], solved_grid)
