from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import pygame


# Initialize Pygame display first
pygame.init()
pygame.font.init()

# Game Fonts
font = "Retro.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

# Game Resolution
screen_width = 1200
screen_height = 700

# Initialize Pygame display
screen = pygame.display.set_mode((screen_width, screen_height))

# Load sound effect for menu selection
menu_sound = pygame.mixer.Sound("sound\\byebye.mp3")

# Play when you enter the main menu
menu_sound.play()

# Main Menu
def main_menu():

    menu = True
    selected = "start"


    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        print("Start")
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill((255, 165, 0))
        title = text_format("Response Time", font, 90, (255, 255, 0))
        text_start = text_format("START", font, 75, (255, 255, 255) if selected == "start" else (0, 0, 0))
        text_quit = text_format("QUIT", font, 75, (255, 255, 255) if selected == "quit" else (0, 0, 0))

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()


        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 360))

        pygame.display.update()
        clock.tick(FPS)
        splash.withdraw()

    menu.protocol("WM_DELETE_WINDOW")


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)


# Splash screen
splash = Tk()
height = 600
width = 800
x = (splash.winfo_screenwidth() // 2) - (width // 2)
y = (splash.winfo_screenheight() // 2) - (height // 2)
splash.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Load GIF
gif_image_path = "img\\firefighters.gif"
gif_image = Image.open(gif_image_path)
frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(gif_image)]

# Initialize Pygame for sound effects
pygame.mixer.init()

# Load sound effect
sound_effect_path = "sound\\siren1.mp3"
pygame.mixer.music.load(sound_effect_path)


# Function to play sound effect
def play_sound_effect():
    pygame.mixer.music.play()


# Calculate center coordinates for the GIF label
gif_width = 800
gif_height = 600
x_centered = (width - gif_width) // 2
y_centered = (height - gif_height) // 2

# Display GIF centered
gif_label = Label(splash, image=frames[0])
gif_label.place(x=x_centered, y=y_centered, width=gif_width, height=gif_height)

# For deleting the tk() view
splash.overrideredirect(True)

# Function to update GIF frames
def update_gif_frame(count):
    gif_label.configure(image=frames[count])

    # Check if it's the first frame (count == 0)
    if count == 0:
        # Add a delay before playing the sound effect
        splash.after(2000, play_sound_effect)

    count += 1
    if count == len(frames):
        count = 0
    splash.after(50, lambda: update_gif_frame(count))

# Splash Screen timer
splash.after(9850, main_menu)

# Start updating GIF frames
update_gif_frame(0)

splash.mainloop()