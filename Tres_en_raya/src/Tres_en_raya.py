import tkinter as tk
from tkinter import messagebox

player, game_over = 'X', False

def comprobacion_victoria():
    """Verifica si hay un ganador."""
    for row in range(3):
        # Verificar filas y columnas
        if (buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '') or \
           (buttons[0][row]['text'] == buttons[1][row]['text'] == buttons[2][row]['text'] != ''):
            return True
    # Verificar diagonales
    if (buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '') or \
       (buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != ''):
        return True
    return False

def clicar_boton(row, col):
    """Maneja la acción de un clic en el botón."""
    global player, game_over
    if buttons[row][col]['text'] == '' and not game_over:
        buttons[row][col]['text'] = player
        buttons[row][col]['bg'] = '#37474F' if player == 'X' else '#455A64'

        if comprobacion_victoria():
            messagebox.showinfo(title='Tres en Raya', message=f'¡El jugador {player} gana!')
            game_over = True
        elif all(buttons[r][c]['text'] != '' for r in range(3) for c in range(3)):
            messagebox.showinfo(title='Empate', message='¡Es un empate!')
            game_over = True
        else:
            player = 'O' if player == 'X' else 'X'

def resetear_partida():
    """Reinicia el tablero para una nueva partida."""
    global player, game_over
    player = 'X'
    game_over = False
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''
            buttons[row][col]['bg'] = '#263238'

# Configuración de la ventana principal
root = tk.Tk()
root.title('Tres en Raya')
root.geometry('400x450')
root.configure(bg='#263238')

# Crear tablero de botones
frame = tk.Frame(root, bg='#263238')
frame.place(relx=0.5, rely=0.4, anchor='center')

buttons = [[tk.Button(frame, text='', font='normal 20 bold', width=5, height=2, bg='#263238', fg='white',
                      command=lambda row=row, col=col: clicar_boton(row, col)) for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col, padx=10, pady=10)

# Botón de reinicio
reset_button = tk.Button(root, text='Reiniciar', font='normal 15 bold', command=resetear_partida,
                         bg='#546E7A', fg='white')
reset_button.place(relx=0.5, rely=0.9, anchor='center')

# Ejecutar el bucle principal de la aplicación
root.mainloop()