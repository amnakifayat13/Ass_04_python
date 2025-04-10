import random
import streamlit as st

def create_board(size, mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mine_positions = set()
    
    while len(mine_positions) < mines:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        mine_positions.add((x, y))
    
    for x, y in mine_positions:
        board[x][y] = '*'
    
    return board, mine_positions

def count_adjacent_mines(board, x, y, size):
    if board[x][y] == '*':
        return '*'
    
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == '*':
            count += 1
    
    return str(count) if count > 0 else ' '

def reveal_board(board, size):
    revealed = [[' ' for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            revealed[x][y] = count_adjacent_mines(board, x, y, size)
    return revealed

def play_minesweeper():
    st.title("Minesweeper Game")
    size = st.sidebar.slider("Grid Size", 5, 10, 5)
    mines = st.sidebar.slider("Number of Mines", 1, size * size // 2, 5)
    
    if "board" not in st.session_state:
        st.session_state.board, st.session_state.mine_positions = create_board(size, mines)
        st.session_state.revealed_board = [['_' for _ in range(size)] for _ in range(size)]
        st.session_state.game_over = False
    
    board = st.session_state.board
    revealed_board = st.session_state.revealed_board
    
    def reveal_cell(x, y):
        if st.session_state.game_over:
            return
        if (x, y) in st.session_state.mine_positions:
            st.session_state.game_over = True
            st.error("Game Over! You hit a mine.")
        else:
            revealed_board[x][y] = count_adjacent_mines(board, x, y, size)
    
    for i in range(size):
        cols = st.columns(size)
        for j in range(size):
            label = revealed_board[i][j]
            if label == '_':
                if cols[j].button(" ", key=f"{i}-{j}"):
                    reveal_cell(i, j)
            else:
                cols[j].write(label)
    
    if st.session_state.game_over:
        st.write("Final Board:")
        for row in board:
            st.text(' '.join(row))
        if st.button("Restart Game"):
            del st.session_state.board
            del st.session_state.revealed_board
            del st.session_state.mine_positions
            del st.session_state.game_over
            st.rerun()

if __name__ == "__main__":
    play_minesweeper()
