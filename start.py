import time
import os

import pyscreenshot as ImageGrab            # screenshot

from PIL import Image, ImageTk, ImageOps, ImageEnhance

import pytesseract                      # OCR
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\x\AppData\Local\Tesseract-OCR\tesseract.exe'


import pynput                               # input
from pynput.mouse import Button as mouseButton, Controller
mouse = Controller()
from pynput.keyboard import Key, Listener, Controller
keyboard = Controller()


import _tkinter                      # GUI
from tkinter import Tk, Label, IntVar, StringVar, Radiobutton, Button, Entry, Listbox, END
import tkinter.ttk as ttk
window = Tk()

import glob

acc_name = "abcabc"
acc_name = "blue sky"


if( acc_name == 'abcabc' ):
    config_buy = "config_buy/abcabc.txt"
elif( acc_name == 'blue sky' ):
    config_buy = "config_buy/blue sky.txt"
    


config_sell = "config_sell/valuables.txt"
zarobek = 1



# TREE #
tree = ttk.Treeview( window )


    
tree_buy = tree.insert( '', 'end', text = "create offers" )
list_buy = glob.glob( "config_buy/*.txt" )
for item in list_buy:
    item_name = item.replace( 'config_buy\\', '' )
    if( item.find( '_' ) ): # show only files without underscore _
        tree.insert( tree_buy, 'end', text = item_name )

tree_sell = tree.insert( '', 'end', text = "buy items" )
list_sell = glob.glob( "config_sell/*.txt" )
for item in list_sell:
    item_name = item.replace( 'config_sell\\', '' )
    if( item.find( '_' ) ): # show only files without underscore _
        tree.insert( tree_sell, 'end', text = item_name )
        
#tree.grid( row = 200, column = 200 )

# END OF TREE #

def getTreeValue():
    return tree.item( tree.focus() ).get( 'text' )


def readFileToArray( filename ):
    file = open( filename, "r" )
    single_lines = file.read().split( ';\n' )
    final_output = []
    for val in single_lines:
        if( val.find( '#' ) != -1 ):
            continue
        val = val.replace( ';', '' ) #remove last srednik
        final_output.append( val.split( ':' ) )
    for val in final_output:
        try:
            val[1] = int( val[1] )
            val[2] = int( val[2] )
        except:
            pass

    #print( final_output )
    return final_output

def getValFromArray( array, nameOfValue ):
    for val in array:
        if( val[0] == nameOfValue ):
            return val[1]

dimensions = readFileToArray( "config_dimensions.txt" )

def saveBoxDimensions():
    file = open( "config_dimensions.txt", "r+" )

    string = ( 'x1: ' + str( market.x1 )
              + ';\ny1: ' + str( market.y1 )
              + ';\nx2: ' + str( market.x2 )
              + ';\ny2: ' + str( market.y2 ) + ';' )
    
    file.write( string )

    
# vars #
class Box: # rectangular box with name
    def __init__( self, x1, y1, x2, y2 ):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
class Xy:
    def __init__( self, x, y ):
        self.x = x
        self.y = y



market = Box( getValFromArray( dimensions, 'x1' ),
              getValFromArray( dimensions, 'y1' ),
              getValFromArray( dimensions, 'x2' ),
              getValFromArray( dimensions, 'y2' ) )

market_size_x = market.x2 - market.x1
market_size_y = market.y2 - market.y1

search_list = Box( market.x1 + market_size_x * 0.0187668,
                  market.y1 + market_size_y * 0.2933579,
                  market.x1 + market_size_x * 0.2135278,
                  market.y1 + market_size_y * 0.8210332 )

first_buy_item_price = Box( market.x1 + market_size_x * 0.502000,
                            market.y1 + market_size_y * 0.4852398,
                            market.x1 + market_size_x * 0.613000,
                            market.y1 + market_size_y * 0.5166051 )
first_buy_item_username = Box( market.x1 + market_size_x * 0.250334672021419,
                               market.y1 + market_size_y * 0.48523985239852396,
                               market.x1 + market_size_x * 0.41767068273092367,
                               market.y1 + market_size_y * 0.514760147601476 )


rest_buy_item_username = Box( market.x1 + market_size_x * 0.2483221476510067,
                              market.y1 + market_size_y * 0.5166666666666667,
                              market.x1 + market_size_x * 0.4214765100671141,
                              market.y1 + market_size_y * 0.6944444444444444 )
first_sell_item_price = Box( market.x1 + market_size_x * 0.5046979865771812,
                             market.y1 + market_size_y * 0.15185185185185185,
                             market.x1 + market_size_x * 0.6161073825503356,
                             market.y1 + market_size_y * 0.18333333333333332 )
###############################

cap_location = Box( 777, 281, 806, 291 )

##########################################                

my_offers_list = Box( market.x1 + market_size_x * 0.022757697456492636,
                      market.y1 + market_size_y * 0.5682656826568265,
                      market.x1 + market_size_x * 0.9625167336010709,
                      market.y1 + market_size_y * 0.5996309963099631 )
my_offers_button = Box( market.x1 + market_size_x * 0.7777777777777778,
                        market.y1 + market_size_y * 0.9428044280442804,
                        market.x1 + market_size_x * 0.8674698795180723,
                        market.y1 + market_size_y * 0.9686346863468634 )
actual_page = Box( market.x1 + market_size_x * 0.4577181208053691,
                     market.y1 + market_size_y * 0.001851851851851852,
                     market.x1 + market_size_x * 0.5463087248322148,
                     market.y1 + market_size_y * 0.0292 )

#1p1 = 1; 1p2 = 0.5
my_offers_1p1 = Box( market.x1 + market_size_x * 0.020134228187919462,
                     market.y1 + market_size_y * 0.5701107011070111,
                     market.x1 + market_size_x * 0.28456375838926173,
                     market.y1 + market_size_y * 0.8966789667896679 )
                     



input_search = Xy( market.x1 + market_size_x * 0.115384,
                   market.y1 + market_size_y * 0.876383 )
first_item = Xy( market.x1 + market_size_x * 0.110000,
                 market.y1 + market_size_y * 0.320000 )
click_set_max_sell_amount = Xy( market.x1 + market_size_x * 0.7100671140939597,
                           market.y1 + market_size_y * 0.09259259259259259 )
click_accept = Xy( market.x1 + market_size_x * 0.9557046979865772,
                   market.y1 + market_size_y * 0.09259259259259259 )

click_buy = Xy( market.x1 + market_size_x * 0.250663,
                market.y1 + market_size_y * 0.793357 )
click_amount_more = Xy( market.x1 + market_size_x * 0.688759,
                  market.y1 + market_size_y * 0.791511 )
input_price = Xy( market.x1 + market_size_x * 0.515915,
                  market.y1 + market_size_y * 0.828413 )
click_anonymous = Xy( market.x1 + market_size_x * 0.799777,
                      market.y1 + market_size_y * 0.876383 )
click_create = Xy( market.x1 + market_size_x * 0.938992,
                 market.y1 + market_size_y * 0.876383 )

click_my_offers = Xy( market.x1 + market_size_x * 0.8246318607764391,
                      market.y1 + market_size_y * 0.9538745387453874 )
click_cancel = Xy( market.x1 + market_size_x * 0.9384203480589023,
                   market.y1 + market_size_y * 0.5018450184501845 )
click_market = Xy( market.x1 + market_size_x * 0.92904953145917,
                   market.y1 + market_size_y * 0.955719557195572 )



items_to_sell = []
items_to_buy = []


def showBoxBounding( obj ):
    mouse.position = ( obj.x1, obj.y1 )
    while( mouse.position[0] < obj.x2 ): #right
        mouse.move( 1, 0 )
        time.sleep( 0.001 )
    while( mouse.position[1] < obj.y2 ): #down
        mouse.move( 0, 1 )
        time.sleep( 0.001 )
    
    while( mouse.position[0] > obj.x1 ): #left
        mouse.move( -1, 0 )
        time.sleep( 0.001 )
    while( mouse.position[1] > obj.y1 ): #up
        mouse.move( 0, -1 )
        time.sleep( 0.001 )

def setMousePosition( obj ):
    mouse.position = ( obj.x, obj.y )
    time.sleep( 0.01 )

def testAllDimensions():
    showBoxBounding( market )
    #showBoxBounding( search_list )
    #showBoxBounding( first_buy_item_price )
    #showBoxBounding( my_offers_list )
    #showBoxBounding( cap_location )

    #setMousePosition( input_search )
    #setMousePosition( first_item )
    #setMousePosition( click_buy )
    #setMousePosition( click_amount_more )
    #setMousePosition( input_price )
    #setMousePosition( click_anonymous )
    #setMousePosition( click_create )
    
    #setMousePosition( click_my_offers )
    #setMousePosition( click_cancel )
    #setMousePosition( click_set_max_sell_amount )
#-#





img = Image.open( "market_window.JPG" ) #load image
w = int( img.width / 4 ) # make image smaller
h = int( img.height / 4 ) # make image smaller
image = ImageTk.PhotoImage( img.resize( ( w, h ) ) ) # make tkinker object
img = Label( window, image = image ) #create label
img.grid( row = 10, column = 10, rowspan = 10, columnspan = 10) #show image on canvas


btn_selected = IntVar()
btn_x1y1 = Radiobutton( window, variable = btn_selected, value = 1 )
btn_x2y2 = Radiobutton( window, variable = btn_selected, value = 2 )
btn_x1y1.grid( row = 10, column = 10 )
btn_x2y2.grid( row = 19, column = 19 )

left_text = Label( text = ( market.x1, "x", market.y1 ) )
right_text = Label( text = ( market.x2, "x", market.y2 ) )
left_text.grid( row = 9, column = 10 )
right_text.grid( row = 20, column = 19 )

btn_test = Button( window, text = "test dimensions", command = testAllDimensions )
btn_save = Button( window, text = "save dimensions", command = lambda:saveBoxDimensions() )
btn_test.grid( row = 15, column = 15 )
btn_save.grid( row = 16, column = 15 )

def loadItems():
    #items_to_buy = readFileToArray( "config_buy.txt" )
    #items_to_sell = readFileToArray( "config_sell.txt" )
    pass

btn_load = Button( window, text = "load config file", command = loadItems )
#btn_load.grid( row = 8, column = 11 )


def returnTextFromImage( obj, size_mult, psm, language ):
    time.sleep( 0.2 )
    x1 = int( obj.x1 )
    y1 = int( obj.y1 )
    x2 = int( obj.x2 )
    y2 = int( obj.y2 )
    psm = 'psm=' + str(psm)
    im = ImageGrab.grab( bbox=( x1, y1, x2, y2 ) )
    
    new_size = tuple( size_mult*x for x in im.size )
    im = im.resize( new_size, Image.ANTIALIAS )
    
    #im = ImageOps.posterize( im,2 )
    #enhancer = ImageEnhance.Contrast(im)
    #im_new = enhancer.enhance( 40000 )
    #im_new.show()
    text = pytesseract.image_to_string( im, config = psm, lang = language )
    i = 0
    while( i < 5 and text == '' ):
        i = i+1
        text = pytesseract.image_to_string( im, config = psm, lang = language )
        time.sleep( 0.05 )
    
    if( text == '' ):
        time.sleep( 0.2 )
        im = ImageOps.invert( im )
        text = pytesseract.image_to_string( im, config = psm, lang = language )
    text = text.lower()

    name = str(text) + '.jpg'
    if( text == '' ):
        #name = 'foto/' + "none.jpg"
        #im.save( name )
        return
        
    #name = 'foto/' + name
    name = 'foto/' + '1p1.jpg'
    im.save( name )

    return text
#-#


def lClick():
    mouse.click( mouseButton.left, 1 )
def getPrice( obj, zoom, psm, language ):
    try:
        text = returnTextFromImage( obj, zoom, psm, language )
        text = text.replace( ',', '' )
        return int( text )
    except:
        return

def searchAndBuyOffers():
    items_to_buy = readFileToArray( config_sell )
    
    txt = returnTextFromImage( actual_page, 4, 0, 'eng' )
    if( txt == "my offers" ):
        setMousePosition( click_market )
        lClick()

    for val in items_to_buy:
        setMousePosition( input_search )
        lClick()
        keyboard.press( Key.ctrl_l )
        keyboard.press( 'a' )
        keyboard.release( 'a' )
        keyboard.release( Key.ctrl_l )
        keyboard.press( Key.backspace )
        keyboard.release( Key.backspace )
        keyboard.type( val[0] )
        setMousePosition( first_item )
        lClick()
        time.sleep( 0.2 )
        text = getPrice( first_sell_item_price, 4, "-c tessedit_char_whitelist=0123456789 -oem 0", 'tib')
        if( text == '' ):
            continue
        
        try:
            price = getPrice( first_sell_item_price, 4, "-c tessedit_char_whitelist=0123456789 -oem 0", 'tib' )
            
            max_price = val[1] - zarobek
            if( price > max_price ):
                string = price, '>', val[1]
                print( string )
                continue
            while( price <= max_price ):
                string = price, '<', val[1]
                print( string )
                
                price = getPrice( first_sell_item_price, 4, "-c tessedit_char_whitelist=0123456789 -oem 0", 'tib' )
                if( price <= max_price ):
                    setMousePosition( click_set_max_sell_amount )
                    lClick()
                    setMousePosition( click_accept )
                    lClick()
                    time.sleep( 0.5 )
        except:
            pass




def checkRestOffersAndCreateAgain( obj ):
    item_name = obj
    text = returnTextFromImage( my_offers_1p1, 30, 1, 'tib-text' )
    print( 'x' )
    print( text )
    
    
def checkRestOffersAndCreateAgains( obj ):
    text = returnTextFromImage( rest_buy_item_username, 4, 6, 'tib-text' )
    #if( text.find( 'acc_name' ) == -1 ): # not found
    if( 1 == -1 ):
        return 0
    else:                                # found
        item_name = obj[0]
        #setMousePosition( click_my_offers )
        lClick()
        text = returnTextFromImage( my_offers_1p1, 4, 0, 'tib-text' )
        print( text )
        if( text.find( item_name ) == -1 ):  # not found
            i = 0
            #while( i < 10 ):
                #i = i+1
                #keyboard.press( Key.down )
                #keyboard.release( Key.down )
        else:                               # found
            print( 'found' )

        time.sleep( 1 )
        #exit()
        return 1
    return






    
def createBuyOffers():
    checkRestOffersAndCreateAgain( "gold insgot" )

    
def XDDDcreateBuyOffers():
    #getTreeValue()
    #exit()
    
    items_to_buy = readFileToArray( config_buy )
    
    txt = returnTextFromImage( actual_page, 2, 0, 'eng' )
    if( txt == "my offers" ):
        setMousePosition( click_market )
        lClick()

    try:
        for val in items_to_buy:
            window.update()
            setMousePosition( input_search )
            lClick()
            keyboard.press( Key.ctrl_l )
            keyboard.press( 'a' )
            keyboard.release( 'a' )
            keyboard.release( Key.ctrl_l )
            keyboard.press( Key.backspace )
            keyboard.release( Key.backspace )
            keyboard.type( val[0] )
            setMousePosition( first_item )
            lClick()
            txt = returnTextFromImage( first_buy_item_username, 2, 6, 'tib-text' )
            #print( txt )
            if( txt == acc_name ):
                continue
            # TRY ONCE AGAIN
            txt = returnTextFromImage( first_buy_item_username, 4, 6, 'tib-text' )
            if( txt == acc_name ):
                continue


            
            #if( checkRestOffersAndCreateAgain( val ) == 1 ):
                #continue


                
            
            #txt = returnTextFromImage( rest_buy_item_username, 2, 6, 'eng' )
            
            text = returnTextFromImage( first_buy_item_price, 4, "-c tessedit_char_whitelist=0123456789 -oem 0", 'tib'  )
            if( text == '' ):
                continue
            
            try:
                text = text.replace( ',', '' )
                price = int( text )
                #print( price )
                max_price = val[2] * 0.98
            
                setMousePosition( click_buy )
                lClick()
                if( price < max_price ):
                    #print( "max price: " + str(max_price) )
                    setMousePosition( input_price )
                    lClick()
                    keyboard.type( str( price+1 ) )
                    i = 0
                    if( val[1] % 100 == 0 ):
                        while( i < val[1]/100 ):
                            i = i+1
                            setMousePosition( click_amount_more )
                            keyboard.press( Key.ctrl_l )
                            lClick()
                            keyboard.release( Key.ctrl_l )
                    elif( val[1] % 10 == 0 ):
                        while( i < val[1]/10 ):
                            i = i+1
                            setMousePosition( click_amount_more )
                            keyboard.press( Key.shift_l )
                            lClick()
                            keyboard.release( Key.shift_l )
                    else:
                        while( i < val[1] ):
                            i = i+1
                            setMousePosition( click_amount_more )
                            lClick()

                    #setMousePosition( click_anonymous )
                    #lClick()
                    setMousePosition( click_create )
                    lClick()
                #-#
            except:
                new_price = int( val[2]/4 )
                print( "None found, creating auction 25% of price: " + str( val[2] ) + '/4=' + str( new_price ) )
                setMousePosition( click_buy )
                lClick()
                setMousePosition( input_price )
                lClick()
                keyboard.type( str( new_price ) )
                i = 0
                if( val[1] % 100 == 0 ):
                    while( i < val[1]/100 ):
                        i = i+1
                        setMousePosition( click_amount_more )
                        keyboard.press( Key.ctrl_l )
                        lClick()
                        keyboard.release( Key.ctrl_l )
                elif( val[1] % 10 == 0 ):
                    while( i < val[1]/10 ):
                        i = i+1
                        setMousePosition( click_amount_more )
                        keyboard.press( Key.shift_l )
                        lClick()
                        keyboard.release( Key.shift_l )
                else:
                    while( i < val[1] ):
                        i = i+1
                        setMousePosition( click_amount_more )
                        lClick()

                #setMousePosition( click_anonymous )
                #lClick()
                setMousePosition( click_create )
                lClick()
                
            #-#
            time.sleep( 1 )
            
            
    except KeyboardInterrupt: #CTRL C in console will force-break the loop
        pass
#-#

def removeAuctions():
    txt = returnTextFromImage( actual_page, 4, 0, 'eng' )
    if( txt == "market" ):
        setMousePosition( click_my_offers )
        lClick()
    txt = returnTextFromImage( actual_page, 4, 0, 'eng' )
    if( txt == "my offers" ):
        while( returnTextFromImage( my_offers_list, 1, 6, 'eng' ) ):
            setMousePosition( click_cancel )
            lClick()
        

btn_start = Button( window, text = "remove auctions", command = removeAuctions )
btn_start.grid( row = 24, column = 15 )




move_from = Xy( 1218, 624 )
move_to = []

def isset(variable):
    return variable in locals() or variable in globals()

#global i_counter

def setText( obj, text ):
    obj[ 'text' ] = text

i_counter = 0
next_btn = False
containers_amount = 4
def keyPressed( event ):
    if( event.keycode == 13 ):
        # set x1y1x2y2
        if( btn_selected.get() == 1 ):
            market.x1 = mouse.position[0]
            market.y1 = mouse.position[1]
            left_text[ 'text' ] = market.x1, 'x', market.y1
        if( btn_selected.get() == 2 ):
            market.x2 = mouse.position[0]
            market.y2 = mouse.position[1]
            right_text[ 'text' ] = market.x2, 'x', market.y2
            
        #set moving items, from - to
        if( btn_selected.get() == 10 ):
            global i_counter
            global next_btn
            global containers_amount
            containers_amount = int( entry.get() )
            if( next_btn == False ):
                move_from.x = mouse.position[0]
                move_from.y = mouse.position[1]
                next_btn = True
            label_from[ 'text' ] = "ALL SET!"

            if( next_btn == True and i_counter <= containers_amount ):
                if( i_counter < containers_amount ):
                    setText( label_from, 'set to ' + str( i_counter+1 ) )
                move_to.append( Xy( mouse.position[0], mouse.position[1] ) )

                i_counter = i_counter+1

                
        

        #WORK
        # get multiplier
        if( btn_selected.get() == 20 ):
            file = open( ".work_data.txt", "w+" )
            x = ( mouse.position[0] - market.x1 ) / market_size_x
            y = ( mouse.position[1] - market.y1 ) / market_size_y
            string = 'market.x1 + market_size_x * ' + str(x) + ',\nmarket.y1 + market_size_y * ' + str(y)
            file.write( string )
            
    if( event.keycode == 27 ):
        exit()
    # enter - keycode = 13 
    # ESC - keycode = 27
    

window.bind( "<Key>", keyPressed )


get_mult = Label( window, text = "get mult" )
radio_get_mult = Radiobutton( window, variable = btn_selected, value = 20 )
get_mult.grid( row = 100, column = 10, sticky = "W" )
radio_get_mult.grid( row = 100, column = 11, sticky = "E" )

    
btn_start = Button( window, text = "Create offers", command = createBuyOffers )
btn_start.grid( row = 25, column = 15 )

btn_start = Button( window, text = "Search and buy offers", command = searchAndBuyOffers )
btn_start.grid( row = 26, column = 15 )



throw_amount = 30

def moveItems():
    j = 0
    print( ' ' )
    #cap = returnTextFromImage( cap_location, 4, 6, 'eng' )
    #print( cap )
    
    while( j < containers_amount ):
        j = j+1
        #if( cap < 100 ):
            #continue
        
        try:
            keyboard.press( Key.ctrl_l )
            i = 0
            while i <= throw_amount :
                i = i+1
                setMousePosition( move_from )
                mouse.press( mouseButton.left )
                setMousePosition( move_to[j] )
                mouse.release( mouseButton.left )
            keyboard.release( Key.ctrl_l )
        except:
            pass
        
    keyboard.release( Key.ctrl_l )


label_from = Label( window, text = "set from" )
radio_from = Radiobutton( window, variable = btn_selected, value = 10 )
label_from.grid( row = 48, column = 19 )
radio_from.grid( row = 48, column = 19, sticky = "E" )

label_to = Label( window, text = "set to" )
radio_to = Radiobutton( window, variable = btn_selected, value = 11 )
#label_to.grid( row = 49, column = 19 )
#radio_to.grid( row = 49, column = 19, sticky = "E" )



containers_amount = 4
v = StringVar()
entry = Entry( window, width = 2, textvariable = v )
entry.insert( 0, containers_amount )
entry.grid( row = 47, column = 19, sticky = "E" )
entry_label = Label( window, text = 'backpacks' )
entry_label.grid( row = 47, column = 19, sticky = "W" )




def setContainersCounter( index ):
    label_to = Label( window, text = "set to " + str(index) )
    radio_to = Radiobutton( window, variable = btn_selected, value = 10+index )
    label_to.grid( row = 49, column = 19 )
    radio_to.grid( row = 49, column = 19, sticky = "E" )
        
    

btn_move_items = Button( window, text = "move items to EQ", command = moveItems )
btn_move_items.grid( row = 58, column = 19 )



    

window.mainloop()









#showBoxBounding( market )

