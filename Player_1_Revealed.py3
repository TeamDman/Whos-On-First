# 20191127

# Robin W Dawes

# Python 3

# Requires pygame

# Images used may be subject to copyright

# Click in image to refresh

import pygame
import random

num_faces = 62
use_font = 'georgia'

choices = [
            "is the oldest",
            "is the second-oldest",
            "is the youngest",
            "is the second-youngest",
            "is the tallest",
            "is the second-tallest",
            "is the shortest",
            "is the second-shortest",
            "is carrying the most keys",
            "is carrying the fewest keys",
            "is wearing the newest item of clothing",
            "has the alphabetically first first name",
            "has the alphabetically last first name",
            "has the alphabetically first last name",
            "has the alphabetically last last name", 
            "lives on the alphabetically first street",
            "lives on the alphabetically last street",            
            "was born in the alphabetically first province or state",
            "was born in the alphabetically last province or state",            
            "has the longest first name",
            "has the shortest first name",
            "has the longest last name",
            "has the shortest last name",
            "has the most siblings",
            "has the fewest siblings",
            "has visited the most nations outside Canada",
            "has visited the fewest nations outside Canada",   
            "has travelled the furthest north",
            "has travelled the furthest south",
            "lives at the lowest street number",
            "lives at the highest street number",    
            "has the lowest last digit in their Social Insurance Number",
            "has the highest last digit in their Social Insurance Number",
            "has the second-highest last digit in their Social Insurance Number",
            "has the highest (age % 7)",
            "has the lowest (age % 7)",         
            "had the most recent birthday",
            "will have the next birthday",        
            "most recently ate a donut",
            "most recently ate an apple",
            "most recently ate fish",
            "most recently ate kale",
            "most recently ate an orange",
            "most recently ate a banana",
            "most recently ate a carrot",
            "most recently ate pie",
            "most recently ate ice cream",
            "most recently ate fries",
            "most recently ate yoghurt",
            "most recently ate toast",
            "most recently ate cheese",
            "most recently ate pancakes",
            "most recently ate strawberries",
            "most recently ate avocado",
            "most recently ate chocolate",
            "most recently ate tofu",
            "most recently drank water",
            "most recently drank milk",
            "most recently rode a bus",
            "most recently rode a bicycle",            
            "most recently rode in an elevator",
            "most recently paddled a canoe or kayak",
            "most recently slept in a tent",
            "most recently walked or ran more than 1 km",
            "most recently climbed a ladder",
            "most recently climbed a tree",
            "most recently went up or down a flight of stairs",
            "most recently crossed a bridge",
            "most recently visited Toronto",
            "most recently visited Ottawa",
            "most recently visited Montreal",
            "most recently visited the USA",
            "most recently visited a farm",
            "most recently visited a zoo",
            "most recently was on a beach",
            "most recently bought flowers",
            "most recently bought music",
            "most recently bought shoes",
            "most recently bought eggs",
            "most recently bought a hot drink",
            "most recently visited a dentist",
            "least recently visited a dentist",            
            "most recently travelled by train",
            "least recently travelled by train",
            "most recently travelled by plane",
            "least recently travelled by plane",
            "most recently rode a horse or camel",
            "least recently rode a horse or camel",
            "most recently swam in a lake or river",
            "least recently swam in a lake or river",            
            "most recently watered a plant",
            "least recently watered a plant",            
            "most recently took a photograph",
            "least recently took a photograph",
            "most recently made tea",
            "least recently made tea",   
            "most recently made coffee",
            "least recently made coffee",
            "most recently watched anything on Netflix",
            "least recently watched anything on Netflix",            
            "most recently used FACEBOOK",
            "least recently used FACEBOOK",            
            "most recently sneezed",
            "most recently watched a movie in a theatre",
            "most recently replaced their phone",
            "has had their current phone the longest",           
            "most recently baked something"
          ]  


comments = [
            "A sword-day, a red day!",
            "Ach du lieber!",
            "Are you insane?",
            "Awwwww HELL No!",
            "Ay De Mi!",
            "Bah!  Humbug!",
            "Begorrah!",
            "Bejabbers!",
            "Bless my spillikeens!",
            "Blistering blue barnacles!",
            "Blood and thunder!",
            "By the Hammer of Thor!",
            "Che fregatura!!",
            "Chiminelas Caranchita!",
            "Cry 'Havoc!'",
            "Dadgum it!",
            "DAMMIT!!",
            "Facinore horribilis!",
            "Gadsbudlikins!",
            "Gadzooks!",
            "Get OUT of here!",
            "Give me a break!",
            "Great Caesar's Ghost!",
            "Great googly moogly!",
            "Great horn spoon!",
            "Holy pretzel!",
            "How quaint.",
            "I demand justice!",
            "I want a do-over.",
            "I ... Can't ... Even.",
            "Is this a joke?",
            "Is this fake news?",            
            "It's a conspiracy!",
            "It's an outrage!",
            "It's never me!",
            "Lame as a very lame thing",
            "Mamma Mia!",
            "Mere anarchy.",
            "My kingdom for a horse!",
            "Never saw THAT coming.",
            "Nooooooooooooooooooo!",
            "No no no no no no no",
            "Not this again.",
            "Not me.  As usual.",
            "Odin's Raven!",
            "Oh come ON!",
            "Oh fishhooks!",
            "Oh my wig and whiskers!",
            "Oh sweet cheese and crackers!",
            "OMG! Are you kidding me?",
            "Please, not that!",
            "Potzblitz!",
            "Release the Kraken!",
            "Seriously?",
            "Shih Tzu and Dalmation!",
            "Shut! Up!",
            "Spank me with a wet fish!",
            "Spock!  Explain!",
            "So ein Misthaufen!",
            "That's evil.",
            "That's just silly.",
            "The system is rigged!",
            "Think you're smart, eh?",
            "This is cruel and unusual.",
            "This is just revolting!",
            "This totally sucks!",
            "Thundering typhoons!",
            "Typical.  Juuuuuust typical.",
            "Unfair!!",
            "Well call me a biscuit!",
            "Well I'll be jitterbugged",
            "Well lick my knees!",
            "Well pickle my trotters!",
            "What is WRONG with you?",
            "What the actual heck?",
            "What?",  
            "Who came up with this?",
            "Whose dumb idea was that?",
            "You monsters!",      
            "You won't get away with this!",
            "Your honour, I object.",
            "You'll pay for this!",
            "You'll regret this.",
            "Yumping Yiminy!",            
            "Zoinks!"
           ]





pygame.init()

white = (255, 255, 255)
black = (0,0,0)


display_width = 1800
display_height = 1200



display_surface = pygame.display.set_mode((display_width,display_height))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text,font='andalus',font_size = 30,centre_x= 520, centre_y = 100, line_length=26):
    text_lines = break_into_lines(text, line_length)
   
    largeText = pygame.font.SysFont(font,font_size)
    for i in range(len(text_lines)):
      TextSurf, TextRect = text_objects(text_lines[i], largeText)
      TextRect.center = (centre_x,(centre_y + i*TextRect.height))
      display_surface.blit(TextSurf, TextRect)

def break_into_lines(text,max_line_length=26):
   word_list = text.split(" ")
   lines = []
   cur_line = ""
   
   for w in word_list:
      if len(cur_line) + 1 + len(w) <= max_line_length:
         cur_line = cur_line + " " + w
      else:
         lines.append(cur_line)
         cur_line = w
   lines.append(cur_line)
   return lines


def aspect_scale(img,dim):
    """ 
    aspect_scale.py - Scaling surfaces keeping their aspect ratio
    Raiser, Frank - Sep 6, 2k++
    crashchaos at gmx.net
    Scales 'img' to fit into box bx/by.
    This method will retain the original image's aspect ratio """
    bx = dim[0]
    by = dim[1]
    ix,iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx/float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by/float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by/float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx/float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by

    return pygame.transform.scale(img, (int(sx),int(sy)))



# shuffle the random elements - avoids repetition when iterating

choice_perm = choices[:]
random.shuffle(choice_perm)

face_perm = list(range(1,num_faces+1))
random.shuffle(face_perm)

comments_perm = comments[:]
random.shuffle(comments_perm)

which_choice = 0
which_face = 0
which_comment = 0



image = pygame.image.load("Player 1 Paper 3.jpg")

display_surface.blit(image, (250,0))


image2 = pygame.image.load("face-"+str(face_perm[which_face])+".jpg")
image2 = aspect_scale(image2, (370,250))

i2_rect = image2.get_rect()

i2_rect.center = (1008,540)



display_surface.blit(image2,i2_rect)

message_display(choice_perm[which_choice].upper()+" !!!",font=use_font, centre_x = 520, centre_y = display_height//2 - 50)

message_display('"'+comments_perm[which_comment]+'"',font=use_font,font_size = 24,centre_x = 1008, centre_y = 680, line_length=32)

pygame.display.update()

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         
         quit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
         display_surface.blit(image, (250,0))
         
         which_choice = (which_choice+1) % len(choices)         
         which_face = (which_face+1) % num_faces
         which_comment = (which_comment+1) % len(comments)
         
         message_display(choice_perm[which_choice].upper()+" !!!",font=use_font, centre_x = 520, centre_y = display_height//2 - 50)

         image2 = pygame.image.load("face-"+str(face_perm[which_face])+".jpg")
         image2 = aspect_scale(image2, (370,250))         
         i2_rect = image2.get_rect()
         i2_rect.center = (1008,540)         
         display_surface.blit(image2, i2_rect)
         
         message_display('"'+comments_perm[which_comment]+'"',font=use_font,font_size = 24,centre_x = 1008, centre_y = 680, line_length=32)

         pygame.display.update()