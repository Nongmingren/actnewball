#Import library sys and pygame
import sys, pygame

#Initialize imported pygame modules
pygame.init()

#Determine size variable
size = width, height = 900, 700

#Determine speed variable
speed = [1, 1]

#Determine background colour
background = 255, 255, 255

#Set Screen size
screen = pygame.display.set_mode(size)

#Set app title
pygame.display.set_caption("Bouncing ball")

#Set defaul image size
DEFAULT_IMAGE_SIZE = (200,200)

#Define ball as the image downloaded
ball = pygame.image.load("venv/Sports-Ball-Transparent.png")

#Make ball size
ball = pygame.transform.scale(ball, DEFAULT_IMAGE_SIZE)

#Get ball rect
ballrect = ball.get_rect()

#set ball center
ballrect.center = (50, 400)

#Define ball as the image downloaded
hoop = pygame.image.load("venv/Scripts/hoopmahog.jpg")

#Make hoop size
hoop = pygame.transform.scale(hoop, DEFAULT_IMAGE_SIZE)

#get hoop perimeter
hooprect = hoop.get_rect()

class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(button1.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
                    nextscreen = "yes"
                    screen.fill("white")
        return nextscreen


sys.argv[0]

# Starting mainloop for in game event
def mainloop():
    while True:
        for event in pygame.event.get():
            pygame.quit()
            button1.click(event)
        button1.show()
        pygame.display.update()


button1 = Button(
    "Click here",
    (380, 100),
    font=30,
    bg="navy",
    feedback="You clicked me")



#First screen check event if left mouse button is press then it goes to the next loop
black=(0,0,0)
end_it=False
while (end_it==False):
    screen.fill(black)
    myfont=pygame.font.SysFont("Britannic Bold", 40)
    nlabel=myfont.render("To start press anywhere on the screen", 2, (255, 0, 0))
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            end_it=True
    screen.blit(nlabel,(200,200))
    pygame.display.flip()



aim = True

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()


    screen.fill(background)
    screen.blit(ball, (50, 400))
    screen.blit(hoop, (700, 100))

    goforb = 0

    while aim == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    goforb + 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.display.flip()
                    aim = False
            pygame.display.flip()

    ballrect = ballrect.move(speed)

    for i in range(goforb):
        speed[1] = -speed[1]
        pygame.display.flip()

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background)

    screen.blit(hoop, (700,100))

    screen.blit(ball, ballrect)

    pygame.display.flip()