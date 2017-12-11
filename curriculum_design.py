#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# date: 2017-12-8
# author: fszhuangb
# this is my curriculum design
# collecting coupons

'''
   There are 52 cards and we should stimulate getting 4 cards
   1. print out the 4 cards and the number of picks
   2. use turtle to draw the 4 cards
'''

import time
import random
import turtle as do

# use a dict to put all cards : heart♥(a->10, J,Q,K)
#                               spade♠(a->10, J,Q,K)
#                               club♣ (a->10, J,Q,K)
#                               diamond♦(a->10, J,Q,K)


poker_dict = {'the arc of hearts': 1,
              '2 of hearts': 2,
              '3 of hearts': 3,
              '4 of hearts': 4,
              '5 of hearts': 5,
              '6 of hearts': 6,
              '7 of hearts': 7,
              '8 of hearts': 8,
              '9 of hearts': 9,
              '10 of hearts': 10,
              'the jack of hearts': 'j',
              'the queen of hearts': 'q',
              'the king of hearts': 'k',
              'the arc of spades': 1,
              '2 of spades': 2,
              '3 of spades': 3,
              '4 of spades': 4,
              '5 of spades': 5,
              '6 of spades': 6,
              '7 of spades': 7,
              '8 of spades': 8,
              '9 of spades': 9,
              '10 of spades': 10,
              'the jack of spades': 'j',
              'the queen of spades': 'q',
              'the king of spades': 'k',
              'the arc of clubs': 1,
              '2 of clubs': 2,
              '3 of clubs': 3,
              '4 of clubs': 4,
              '5 of clubs': 5,
              '6 of clubs': 6,
              '7 of clubs': 7,
              '8 of clubs': 8,
              '9 of clubs': 9,
              '10 of clubs': 10,
              'the jack of clubs': 'j',
              'the queen of clubs': 'q',
              'the king of clubs': 'k',
              'the arc of diamonds': 1,
              '2 of diamonds': 2,
              '3 of diamonds': 3,
              '4 of diamonds': 4,
              '5 of diamonds': 5,
              '6 of diamonds': 6,
              '7 of diamonds': 7,
              '8 of diamonds': 8,
              '9 of diamonds': 9,
              '10 of diamonds': 10,
              'the jack of diamonds': 'j',
              'the queen of diamonds': 'q',
              'the king of diamonds': 'k'}


def fetch_cards(user_dict):
    '''
        this function can fetch different 4 words
        parameter:
        user_dict:a dict to fetch
    '''

    # initial the counter
    numbers_of_pick = 0
    different_cards_list = []
    colors = []
    while True:

        # this code judge whether there've got 4 cards
        cards_numbers = len(different_cards_list)
        if cards_numbers == 4:
            print("The computer have got 4 different cards!\n")
            print("They are %s, \n" % different_cards_list[0])
            print("%s,\n" % different_cards_list[1])
            print("%s,\n" % different_cards_list[2])
            print("%s,\n" % different_cards_list[3])
            print("numbers of pick: %d" % numbers_of_pick)
            break

        # use the random module random.choice() to get a card from a dict
        # in python 3.*, the method dict.keys() returns a iterator
        # so you should use list()
        cards_get = random.choice(list(user_dict.keys()))
        color_get = cards_get.split()[-1]
        numbers_of_pick += 1
        if color_get not in colors:
            colors.append(color_get)
            if cards_get not in different_cards_list:
                different_cards_list.append(cards_get)
                print('we have got %s!\n' % cards_get)
            else:
                print('we have got %s!\n' % cards_get)
                continue
        else:
            continue
    return different_cards_list


def generate_rectangle(x, y, length):
    '''
       this function generate a rectangle
       parameters:
       x: x coordinate
       y: y coordinate
       length: the length you want to draw
    '''
    do.penup()
    do.goto(x, y)
    do.pendown()
    do.setheading(0)
    for i in range(2):
        do.fd(length / 1.5)
        do.left(90)
        do.fd(length)
        do.left(90)


def generate_heart(x, y, size, start_angle):
    '''
       this function generate a '♥'
       parameters:
       just like last function
    '''
    drawing = do.getcanvas()
    drawing.create_text(x, y, text='♥', angle=start_angle,
                        fill='red', font=("Arial", size, "normal"))


def generate_club(x, y, size, start_angle):
    '''
       This fuction generate club♣
       parameters:
       x: x coordinate
       y: y coordinate
       r: it is the size of the function
       start_angle: the club's direction
    '''
    do.speed(10)
    do.penup()
    do.setheading(start_angle)
    do.pensize(1)
    do.goto(x, y)
    do.pendown()
    do.fillcolor("black")
    do.begin_fill()
    do.fd(1.4 * size)
    do.left(110)
    do.fd(2 * size)
    do.right(200)
    do.circle(size, 300)
    for x in range(2):
        do.right(180)
        do.circle(size, 300)
    do.right(200)
    do.fd(2 * size)
    do.end_fill()


def generate_spade(x, y, size, start_angle):
    '''
       this function generate a '♠'
       parameters:
       just like last function
    '''
    drawing = do.getcanvas()
    drawing.create_text(x, y, text='♠', angle=start_angle,
                        font=("Arial", size, "normal"))


def generate_diamond(x, y, size, start_angle):
    '''
       this function generate a '♦'
       parameters:
       just like last function
    '''
    drawing = do.getcanvas()
    drawing.create_text(x, y, text='♦', angle=start_angle,
                        fill='red',
                        font=("Arial", size, "normal"))


def generate_A(x, y, size, start_angle):
    '''
       this function generate A
       parameter:
       x: x coordinate
       y: y coordinate
       start_angle: the A's direction
       size: this is the size of A
    '''
    do.penup()
    do.goto(x, y)
    do.pensize(3)
    do.setheading(start_angle)
    do.pendown()
    do.fd(size)
    do.right(140)
    do.fd(size)
    do.bk(size * 2 / 5)
    do.right(110)
    do.fd(size * 2 / 5)


def generate_digital(number, x, y, size, start_angle, color='black'):
    '''
       this function generate a '5-10'
       parameters:
       just like last function
    '''
    drawing = do.getcanvas()
    drawing.create_text(x, y, text=number, angle=start_angle,
                        fill=color,
                        font=("Arial", size, "normal"))


def generate_big_char(char, x, y, size, start_angle, color='black'):
    '''
       this function generate a 'J, K, Q'
       parameters:
       just like last function
    '''

    drawing = do.getcanvas()
    drawing.create_text(x, y, text=char, angle=start_angle,
                        fill=color,
                        font=("Lucida Calligraphy", size, "normal"))


def draw_card(keys, value):
    '''This function draw cards
       parameters:
       keys: this is the kinds of card
       value: this is the number of card
    '''
    if 'club' in keys:  # judge whether the card is club
        do.speed(10)
        generate_rectangle(50, 20, 210)
        generate_club(70, 180, 4, 0)
        generate_club(175, 70, 4, -180)
        if value == 1:
            generate_A(65, 200, 20, 70)
            generate_A(180, 50, 20, -110)
            generate_club(105, 80, 15, 0)
        elif value == 2:
            generate_club(126, 70, 7, -180)
            generate_club(120, 170, 7, 0)
            generate_digital(2, 73, -212, 20, 0)
            generate_digital(2, 175, -35, 20, -180)
            # do.mainloop()
        elif value == 3:
            generate_club(113, 170, 7, 0)
            generate_club(113, 105, 7, 0)
            generate_club(125, 70, 7, -180)
            generate_digital(3, 73, -212, 20, 0)
            generate_digital(3, 175, -35, 20, -180)
            # do.mainloop()
        elif value == 4:
            generate_club(150, 170, 7, 0)
            generate_club(90, 170, 7, 0)
            generate_club(155, 70, 7, -180)
            generate_club(100, 70, 7, -180)
            generate_digital(4, 73, -212, 20, 0)
            generate_digital(4, 175, -35, 20, -180)
            # do.mainloop()
        elif value == 5:
            generate_club(150, 170, 7, 0)
            generate_club(90, 170, 7, 0)
            generate_club(155, 70, 7, -180)
            generate_club(100, 70, 7, -180)
            generate_club(120, 110, 7, 0)  # the club in the middle
            generate_digital(5, 73, -212, 20, 0)
            generate_digital(5, 175, -35, 20, -180)
            # do.mainloop()
        elif value == 6:
            generate_club(150, 170, 7, 0)
            generate_club(90, 170, 7, 0)
            generate_club(155, 70, 7, -180)
            generate_club(100, 70, 7, -180)
            generate_club(150, 110, 7, 0)
            generate_club(90, 110, 7, 0)
            generate_digital(6, 73, -212, 20, 0)
            generate_digital(6, 175, -35, 20, -180)
            # do.mainloop()
        elif value == 7:
            generate_club(150, 170, 7, 0)
            generate_club(90, 170, 7, 0)
            generate_club(155, 70, 7, -180)
            generate_club(100, 70, 7, -180)
            generate_club(150, 110, 7, 0)
            generate_club(90, 110, 7, 0)
            generate_club(120, 125, 7, 0)  # the club in the middle
            generate_digital(7, 73, -212, 20, 0)
            generate_digital(7, 175, -35, 20, -180)
            # do.mainloop()
        elif value == 8:
            generate_club(150, 180, 6, 0)
            generate_club(90, 180, 6, 0)
            generate_club(155, 65, 6, -180)
            generate_club(100, 65, 6, -180)
            generate_club(150, 130, 6, 0)
            generate_club(90, 130, 6, 0)
            generate_club(160, 110, 6, -180)
            generate_club(100, 110, 6, -180)
            generate_digital(8, 73, -212, 20, 0)
            generate_digital(8, 175, -35, 20, -180)
            # do.mainloop()
        elif value == 9:
            generate_club(150, 180, 6, 0)
            generate_club(90, 180, 6, 0)
            generate_club(155, 65, 6, -180)
            generate_club(100, 65, 6, -180)
            generate_club(150, 130, 6, 0)
            generate_club(90, 130, 6, 0)
            generate_club(160, 110, 6, -180)
            generate_club(100, 110, 6, -180)
            generate_club(120, 150, 6, 0)  # the club in the middle
            generate_digital(9, 73, -212, 20, 0)
            generate_digital(9, 175, -35, 20, -180)
            # do.mainloop()
        elif value == 10:
            generate_club(150, 180, 6, 0)
            generate_club(90, 180, 6, 0)
            generate_club(155, 65, 6, -180)
            generate_club(100, 65, 6, -180)
            generate_club(150, 130, 6, 0)
            generate_club(90, 130, 6, 0)
            generate_club(160, 110, 6, -180)
            generate_club(100, 110, 6, -180)
            generate_club(120, 150, 6, 0)  # the club in the middle
            generate_club(130, 100, 6, -180)
            generate_digital(10, 73, -212, 19, 0)
            generate_digital(10, 175, -35, 19, -180)
            # do.mainloop()
        elif value == 'j':
            generate_big_char('J', 115, -130, 55, 0)
            generate_big_char('J', 73, -212, 19, 0)
            generate_big_char('J', 175, -35, 19, -180)
            # do.mainloop()
        elif value == 'q':
            generate_big_char('Q', 115, -130, 55, 0)
            generate_big_char('Q', 73, -212, 19, 0)
            generate_big_char('Q', 175, -35, 19, -180)
            # do.mainloop()
        elif value == 'k':
            generate_big_char('K', 115, -130, 55, 0)
            generate_big_char('K', 73, -212, 19, 0)
            generate_big_char('K', 175, -35, 19, -180)
            # do.mainloop()

    elif 'spade' in keys:
        do.speed(10)
        generate_rectangle(-190, 20, 210)
        generate_spade(-180, -190, 30, 0)
        generate_spade(-60, -55, 30, -180)
        if value == 1:
            generate_A(-187, 200, 20, 70)
            generate_A(-53, 50, 20, -110)
            generate_spade(-120, -128, 60, 0)
            # do.mainloop()
        elif value == 2:
            generate_spade(-126, -53, 60, -180)
            generate_spade(-126, -187, 60, 0)
            generate_digital(2, -176, -212, 20, 0)
            generate_digital(2, -62, -35, 20, -180)
            # do.mainloop()
        elif value == 3:
            generate_spade(-124, -190, 40, 0)
            generate_spade(-124, -130, 40, 0)
            generate_spade(-124, -70, 40, -180)
            generate_digital(3, -178, -212, 20, 0)
            generate_digital(3, -60, -35, 20, -180)
            # do.mainloop()
        elif value == 4:
            generate_spade(-147, -180, 40, 0)
            generate_spade(-98, -180, 40, 0)
            generate_spade(-147, -60, 40, -180)
            generate_spade(-98, -60, 40, -180)
            generate_digital(4, -178, -212, 20, 0)
            generate_digital(4, -60, -35, 20, -180)
            # do.mainloop()
        elif value == 5:
            generate_spade(-150, -170, 40, 0)
            generate_spade(-90, -170, 40, 0)
            generate_spade(-150, -70, 40, -180)
            generate_spade(-90, -70, 40, -180)
            generate_spade(-120, -130, 40, 0)  # the spade in the middle
            generate_digital(5, -178, -212, 20, 0)
            generate_digital(5, -60, -35, 20, -180)
            # do.mainloop()
        elif value == 6:
            generate_spade(-150, -205, 40, 0)
            generate_spade(-90, -205, 40, 0)
            generate_spade(-150, -50, 40, -180)
            generate_spade(-90, -50, 40, -180)
            generate_spade(-150, -130, 40, 0)
            generate_spade(-90, -130, 40, 0)
            generate_digital(6, -178, -212, 20, 0)
            generate_digital(6, -60, -35, 20, -180)
            # do.mainloop()
        elif value == 7:
            generate_spade(-150, -205, 40, 0)
            generate_spade(-90, -205, 40, 0)
            generate_spade(-150, -50, 40, -180)
            generate_spade(-90, -50, 40, -180)
            generate_spade(-150, -130, 40, 0)
            generate_spade(-90, -130, 40, 0)
            generate_spade(-120, -145, 40, 0)  # the spade in the middle
            generate_digital(7, -178, -212, 20, 0)
            generate_digital(7, -60, -35, 20, -180)
            # do.mainloop()
        elif value == 8:
            generate_spade(-150, -205, 40, 0)
            generate_spade(-90, -205, 40, 0)
            generate_spade(-150, -50, 40, -180)
            generate_spade(-90, -50, 40, -180)
            generate_spade(-150, -150, 40, 0)
            generate_spade(-90, -150, 40, 0)
            generate_spade(-150, -105, 40, -180)
            generate_spade(-90, -105, 40, -180)
            generate_digital(8, -178, -212, 20, 0)
            generate_digital(8, -60, -35, 20, -180)
            # do.mainloop()
        elif value == 9:
            generate_spade(-150, -205, 40, 0)
            generate_spade(-90, -205, 40, 0)
            generate_spade(-150, -50, 40, -180)
            generate_spade(-90, -50, 40, -180)
            generate_spade(-150, -150, 40, 0)
            generate_spade(-90, -150, 40, 0)
            generate_spade(-150, -105, 40, -180)
            generate_spade(-90, -105, 40, -180)
            generate_spade(-120, -165, 40, 0)  # the spade in the middle
            generate_digital(9, -178, -212, 20, 0)
            generate_digital(9, -60, -35, 20, -180)
            # do.mainloop()
        elif value == 10:
            generate_spade(-150, -195, 40, 0)
            generate_spade(-90, -195, 40, 0)
            generate_spade(-150, -50, 40, -180)
            generate_spade(-90, -50, 40, -180)
            generate_spade(-150, -150, 40, 0)
            generate_spade(-90, -150, 40, 0)
            generate_spade(-150, -105, 40, -180)
            generate_spade(-90, -105, 40, -180)
            generate_spade(-120, -165, 40, 0)  # the spade in the middle
            generate_spade(-120, -100, 40, -180)
            generate_digital(10, -178, -212, 20, 0)
            generate_digital(10, -60, -35, 20, -180)
            # do.mainloop()
        elif value == 'j':
            generate_big_char('J', -130, -130, 55, 0)
            generate_big_char('J', -178, -212, 19, 0)
            generate_big_char('J', -60, -35, 19, -180)
            # do.mainloop()
        elif value == 'q':
            generate_big_char('Q', -130, -130, 55, 0)
            generate_big_char('Q', -178, -212, 19, 0)
            generate_big_char('Q', -60, -35, 19, -180)
            # do.mainloop()
        elif value == 'k':
            generate_big_char('K', -130, -130, 55, 0)
            generate_big_char('K', -178, -212, 19, 0)
            generate_big_char('K', -60, -35, 19, -180)
            # do.mainloop()
    elif 'heart' in keys:
        do.speed(10)
        generate_rectangle(-190, -230, 210)
        generate_heart(-173, 55, 25, 0)
        generate_heart(-73, 190, 25, -180)
        if value == 1:
            generate_A(-167, -40, 20, 70)
            generate_A(-79, -200, 20, -110)
            generate_heart(-120, 128, 60, 0)
            # do.mainloop()
        elif value == 2:
            generate_heart(-126, 170, 60, -180,)
            generate_heart(-126, 70, 60, 0)
            generate_digital(2, -175, 35, 20, 0, color='red')
            generate_digital(2, -73, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 3:
            generate_heart(-125, 190, 40, 0)
            generate_heart(-125, 130, 40, 0)
            generate_heart(-125, 70, 40, -180)
            generate_digital(3, -175, 35, 20, 0, color='red')
            generate_digital(3, -73, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 4:
            generate_heart(-150, 180, 40, 0)
            generate_heart(-100, 180, 40, 0)
            generate_heart(-150, 60, 40, -180)
            generate_heart(-100, 60, 40, -180)
            generate_digital(4, -175, 35, 20, 0, color='red')
            generate_digital(4, -73, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 5:
            generate_heart(-150, 170, 40, 0)
            generate_heart(-90, 170, 40, 0)
            generate_heart(-150, 70, 40, -180)
            generate_heart(-90, 70, 40, -180)
            generate_heart(-120, 130, 40, 0)  # the spade in the middle
            generate_digital(5, -175, 35, 20, 0, color='red')
            generate_digital(5, -73, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 6:
            generate_heart(-150, 205, 40, 0)
            generate_heart(-90, 205, 40, 0)
            generate_heart(-150, 50, 40, -180)
            generate_heart(-90, 50, 40, -180)
            generate_heart(-150, 130, 40, 0)
            generate_heart(-90, 130, 40, 0)
            generate_digital(6, -175, 35, 20, 0, color='red')
            generate_digital(6, -73, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 7:
            generate_heart(-150, 205, 40, 0)
            generate_heart(-90, 205, 40, 0)
            generate_heart(-150, 50, 40, -180)
            generate_heart(-90, 50, 40, -180)
            generate_heart(-150, 130, 40, 0)
            generate_heart(-90, 130, 40, 0)
            generate_heart(-120, 145, 40, 0)  # the spade in the middle
            generate_digital(7, -175, 35, 20, 0, color='red')
            generate_digital(7, -73, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 8:
            generate_heart(-150, 205, 40, 0)
            generate_heart(-90, 205, 40, 0)
            generate_heart(-150, 50, 40, -180)
            generate_heart(-90, 50, 40, -180)
            generate_heart(-150, 150, 40, 0)
            generate_heart(-90, 150, 40, 0)
            generate_heart(-150, 105, 40, -180)
            generate_heart(-90, 105, 40, -180)
            generate_digital(8, -175, 35, 20, 0, color='red')
            generate_digital(8, -73, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 9:
            generate_heart(-150, 205, 40, 0)
            generate_heart(-90, 205, 40, 0)
            generate_heart(-150, 50, 40, -180)
            generate_heart(-90, 50, 40, -180)
            generate_heart(-150, 150, 40, 0)
            generate_heart(-90, 150, 40, 0)
            generate_heart(-150, 105, 40, -180)
            generate_heart(-90, 105, 40, -180)
            generate_heart(-120, 165, 40, 0)  # the spade in the middle
            generate_digital(9, -175, 35, 20, 0, color='red')
            generate_digital(9, -73, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 10:
            generate_heart(-150, 195, 36, 0)
            generate_heart(-90, 195, 36, 0)
            generate_heart(-150, 50, 36, -180)
            generate_heart(-90, 50, 36, -180)
            generate_heart(-150, 150, 36, 0)
            generate_heart(-90, 150, 36, 0)
            generate_heart(-150, 105, 36, -180)
            generate_heart(-90, 105, 36, -180)
            generate_heart(-120, 165, 36, 0)  # the spade in the middle
            generate_heart(-120, 100, 36, -180)
            generate_digital(10, -175, 35, 18, 0, color='red')
            generate_digital(10, -73, 212, 18, -180, color='red')
            # do.mainloop()
        elif value == 'j':
            generate_big_char('J', -125, 130, 55, 0, color='red')
            generate_big_char('J', -175, 35, 19, 0, color='red')
            generate_big_char('J', -73, 212, 19, -180, color='red')
            # do.mainloop()
        elif value == 'q':
            generate_big_char('Q', -125, 130, 55, 0, color='red')
            generate_big_char('Q', -175, 35, 19, 0, color='red')
            generate_big_char('Q', -73, 212, 19, -180, color='red')
            # do.mainloop()
        elif value == 'k':
            generate_big_char('K', -120, 130, 55, 0, color='red')
            generate_big_char('K', -175, 35, 19, 0, color='red')
            generate_big_char('K', -73, 212, 19, -180, color='red')
            # do.mainloop()
    elif 'diamond' in keys:
        do.speed(10)
        generate_rectangle(50, -230, 210)
        generate_diamond(73, 55, 30, 0)
        generate_diamond(173, 190, 30, -180)
        if value == 1:
            generate_A(65, -42, 20, 70)
            generate_A(180, -200, 20, -110)
            generate_diamond(120, 128, 60, 0)
            # do.mainloop()
        elif value == 2:
            generate_diamond(126, 170, 60, -180,)
            generate_diamond(120, 70, 60, 0)
            generate_digital(2, 73, 35, 20, 0, color='red')
            generate_digital(2, 175, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 3:
            generate_diamond(125, 70, 40, 0)
            generate_diamond(125, 130, 40, 0)
            generate_diamond(125, 190, 40, -180)
            generate_digital(3, 73, 35, 20, 0, color='red')
            generate_digital(3, 175, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 4:
            generate_diamond(150, 180, 40, 0)
            generate_diamond(100, 180, 40, 0)
            generate_diamond(150, 60, 40, -180)
            generate_diamond(100, 60, 40, -180)
            generate_digital(4, 73, 35, 20, 0, color='red')
            generate_digital(4, 175, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 5:
            generate_diamond(150, 170, 40, 0)
            generate_diamond(90, 170, 40, 0)
            generate_diamond(150, 70, 40, -180)
            generate_diamond(90, 70, 40, -180)
            generate_diamond(120, 130, 40, 0)  # the spade in the middle
            generate_digital(5, 73, 35, 20, 0, color='red')
            generate_digital(5, 175, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 6:
            generate_diamond(150, 205, 40, 0)
            generate_diamond(90, 205, 40, 0)
            generate_diamond(150, 50, 40, -180)
            generate_diamond(90, 50, 40, -180)
            generate_diamond(150, 130, 40, 0)
            generate_diamond(90, 130, 40, 0)
            generate_digital(6, 73, 35, 20, 0, color='red')
            generate_digital(6, 175, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 7:
            generate_diamond(150, 205, 40, 0)
            generate_diamond(90, 205, 40, 0)
            generate_diamond(150, 50, 40, -180)
            generate_diamond(90, 50, 40, -180)
            generate_diamond(150, 130, 40, 0)
            generate_diamond(90, 130, 40, 0)
            generate_diamond(120, 145, 40, 0)  # the spade in the middle
            generate_digital(7, 73, 35, 20, 0, color='red')
            generate_digital(7, 175, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 8:
            generate_diamond(150, 205, 40, 0)
            generate_diamond(90, 205, 40, 0)
            generate_diamond(150, 50, 40, -180)
            generate_diamond(90, 50, 40, -180)
            generate_diamond(150, 150, 40, 0)
            generate_diamond(90, 150, 40, 0)
            generate_diamond(150, 105, 40, -180)
            generate_diamond(90, 105, 40, -180)
            generate_digital(8, 73, 35, 20, 0, color='red')
            generate_digital(8, 175, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 9:
            generate_diamond(150, 205, 40, 0)
            generate_diamond(90, 205, 40, 0)
            generate_diamond(150, 50, 40, -180)
            generate_diamond(90, 50, 40, -180)
            generate_diamond(150, 150, 40, 0)
            generate_diamond(90, 150, 40, 0)
            generate_diamond(150, 105, 40, -180)
            generate_diamond(90, 105, 40, -180)
            generate_diamond(120, 85, 40, 0)  # the diamond in the middle
            generate_digital(9, 73, 35, 20, 0, color='red')
            generate_digital(9, 175, 212, 20, -180, color='red')
            # do.mainloop()
        elif value == 10:
            generate_diamond(150, 195, 40, 0)
            generate_diamond(90, 195, 40, 0)
            generate_diamond(150, 50, 40, -180)
            generate_diamond(90, 50, 40, -180)
            generate_diamond(150, 150, 40, 0)
            generate_diamond(90, 150, 40, 0)
            generate_diamond(150, 105, 40, -180)
            generate_diamond(90, 105, 40, -180)
            generate_diamond(120, 165, 40, 0)  # the spade in the middle
            generate_diamond(120, 100, 40, -180)
            generate_digital(10, 73, 35, 18, 0, color='red')
            generate_digital(10, 175, 212, 18, -180, color='red')
            # do.mainloop()
        elif value == 'j':
            generate_big_char('J', 115, 130, 55, 0, color='red')
            generate_big_char('J', 73, 35, 19, 0, color='red')
            generate_big_char('J', 175, 212, 19, -180, color='red')
            # do.mainloop()
        elif value == 'q':
            generate_big_char('Q', 115, 130, 55, 0, color='red')
            generate_big_char('Q', 73, 35, 19, 0, color='red')
            generate_big_char('Q', 175, 212, 19, -180, color='red')
            # do.mainloop()
        elif value == 'k':
            generate_big_char('K', 115, 130, 55, 0, color='red')
            generate_big_char('K', 73, 35, 19, 0, color='red')
            generate_big_char('K', 175, 212, 19, -180, color='red')
            # do.mainloop()


new_list = fetch_cards(poker_dict)

for x in range(4):
    draw_card(new_list[x], poker_dict[new_list[x]])
do.mainloop()


# fetch_cards(poker_dict)
