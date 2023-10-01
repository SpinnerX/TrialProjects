import pygame

# Stack overflow ref because need button: https://stackoverflow.com/questions/10168447/how-to-make-buttons-in-python-pygame

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.ogcol = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.buttonClickedState = False

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('Consolas', 24)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    #  Checking if the button has been clicked
    # Since the button has two states, clicked and not clicked
    def isClicked(self):
        return self.buttonClickedState

    def processEvents(self, event, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.color = (128,128,128)
            else:
                self.color = self.ogcol
        else:
            self.color = self.ogcol

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
