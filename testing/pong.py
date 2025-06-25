import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("Pong Game")
window.resizable(False, False)

# Constants
WIDTH = 800
HEIGHT = 400
BALL_SPEED = 3
PADDLE_SPEED = 20

# Create canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Create paddles and ball
left_paddle = canvas.create_rectangle(20, 150, 30, 250, fill="white")
right_paddle = canvas.create_rectangle(WIDTH - 30, 150, WIDTH - 20, 250, fill="white")
ball = canvas.create_oval(WIDTH // 2 - 10, HEIGHT // 2 - 10, WIDTH // 2 + 10, HEIGHT // 2 + 10, fill="white")

# Ball movement variables
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Paddle movement variables
left_paddle_dy = 0
right_paddle_dy = 0

# Scores
left_score = 0
right_score = 0

# Display scores
score_text = canvas.create_text(WIDTH // 2, 20, text="0 : 0", fill="white", font=("Arial", 24))

# Move paddles
def move_paddles():
    canvas.move(left_paddle, 0, left_paddle_dy)
    canvas.move(right_paddle, 0, right_paddle_dy)

    # Prevent paddles from going out of bounds
    for paddle in [left_paddle, right_paddle]:
        coords = canvas.coords(paddle)
        if coords[1] < 0:
            canvas.move(paddle, 0, -coords[1])
        elif coords[3] > HEIGHT:
            canvas.move(paddle, 0, HEIGHT - coords[3])

# Move ball
def move_ball():
    global ball_dx, ball_dy, left_score, right_score

    canvas.move(ball, ball_dx, ball_dy)
    ball_coords = canvas.coords(ball)

    # Bounce off top and bottom walls
    if ball_coords[1] <= 0 or ball_coords[3] >= HEIGHT:
        ball_dy = -ball_dy

    # Bounce off paddles
    if (ball_coords[0] <= canvas.coords(left_paddle)[2] and
        canvas.coords(left_paddle)[1] < ball_coords[3] and
        canvas.coords(left_paddle)[3] > ball_coords[1]) or \
       (ball_coords[2] >= canvas.coords(right_paddle)[0] and
        canvas.coords(right_paddle)[1] < ball_coords[3] and
        canvas.coords(right_paddle)[3] > ball_coords[1]):
        ball_dx = -ball_dx

    # Reset ball if it goes out of bounds and update score
    if ball_coords[0] <= 0:
        right_score += 1
        reset_ball()
    elif ball_coords[2] >= WIDTH:
        left_score += 1
        reset_ball()

    # Update score display
    canvas.itemconfig(score_text, text=f"{left_score} : {right_score}")

# Reset ball to the center
def reset_ball():
    global ball_dx, ball_dy
    canvas.coords(ball, WIDTH // 2 - 10, HEIGHT // 2 - 10, WIDTH // 2 + 10, HEIGHT // 2 + 10)
    ball_dx = BALL_SPEED if ball_dx > 0 else -BALL_SPEED
    ball_dy = BALL_SPEED if ball_dy > 0 else -BALL_SPEED

# Bot logic for right paddle
def move_bot():
    ball_coords = canvas.coords(ball)
    paddle_coords = canvas.coords(right_paddle)

    # Move the bot paddle towards the ball
    if paddle_coords[1] + (paddle_coords[3] - paddle_coords[1]) / 2 < ball_coords[1]:
        canvas.move(right_paddle, 0, PADDLE_SPEED)
    elif paddle_coords[1] + (paddle_coords[3] - paddle_coords[1]) / 2 > ball_coords[1]:
        canvas.move(right_paddle, 0, -PADDLE_SPEED)

    # Prevent the bot paddle from going out of bounds
    if paddle_coords[1] < 0:
        canvas.move(right_paddle, 0, -paddle_coords[1])
    elif paddle_coords[3] > HEIGHT:
        canvas.move(right_paddle, 0, HEIGHT - paddle_coords[3])

# Key press handlers
def on_key_press(event):
    global left_paddle_dy
    if event.keysym == "w":
        left_paddle_dy = -PADDLE_SPEED
    elif event.keysym == "s":
        left_paddle_dy = PADDLE_SPEED

def on_key_release(event):
    global left_paddle_dy
    if event.keysym in ("w", "s"):
        left_paddle_dy = 0

# Bind keys
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)

# Game loop
def game_loop():
    move_paddles()
    move_ball()
    move_bot()
    window.after(16, game_loop)

# Start the game loop
game_loop()

# Run the application
window.mainloop()