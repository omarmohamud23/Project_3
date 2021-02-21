from menu import Menu
import ui
from database import Artist, Artwork
import sys
import logging


def main():

    new_menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(new_menu)
        action = new_menu.get_action(choice)
        action()
        if choice == 'Q':
            break

#Creates Menu option 
def create_menu():

    menu_class = Menu()
    menu_class.add_option('1', 'Add Artist', add_artist)
    menu_class.add_option('2', 'Search for All Artworks by an Artist', search_artist_all)
    menu_class.add_option('3', 'Search for Available Artworks by Artist', search_artist_available)
    menu_class.add_option('4', 'Add Artwork', add_artwork)
    menu_class.add_option('5', 'Delete Artwork', delete_artwork)
    menu_class.add_option('6', 'Change Artwork Availability', availability_artwork)
    menu_class.add_option('T', 'Generate Test Tables', generate_test_tables)
    menu_class.add_option('D', 'Drop Test Tables', drop_test_tables)
    menu_class.add_option('Q', 'Quit', quit_program)

    return menu_class

##Adds a new artist to the database 
def add_artist():
    try:
        new_artist = ui.add_artist_info()
        save = new_artist.save()
        print(save)
        ui.message(f'{new_artist.artist_name} added.')
    except Exception as e:
        ui.message(e)

##Searching all artists
def search_artist_all():
    try:
        artist_msg = 'Enter artist name:\n'
        art_results = ui.artist_query(artist_msg)
        if art_results:
            ui.message(ui.print_artwork(art_results))
        else:
            ui.message('No artworks found by this artist.')
    except Exception as e:
        ui.message(e)

##checks for artist availability 
def search_artist_available():
    try:
        artist_msg = 'Enter artist name:\n'
        art_results = ui.artist_query(artist_msg, False)
        if art_results:
            ui.message(ui.print_artwork(art_results))
        else:
            ui.message('No artwork matches your query.')
    except Exception as e:
        ui.message(e)

##Adds a new artwork but checks for artist before adding
def add_artwork():
    try:
        new_artwork = ui.add_artwork_info()
        new_artwork.save()
        ui.message(f'{new_artwork.artwork_name} added.')
    except Exception as e:
        ui.message(e)

#deletes artwork
def delete_artwork():
    try:
        delete_art = ui.common_artwork_info()
        confirm = input(f'Delete "{delete_art.artwork_name}"? (y/n):\n').lower().strip()
        if confirm == 'y':
            if Artwork.delete_by_id(delete_art.id) > 0:
                ui.message(f'{delete_art.artwork_name} deleted!')
    except Exception as e:
        ui.message(e)

#This methods checks for artwork availability 
def availability_artwork():
    try:
        cng_avail = ui.common_artwork_info()
        confirm = input(f'Change "{cng_avail.artwork_name}" availability? (y/n):\n').lower().strip()
        if confirm == 'y':
            status = cng_avail.available is False
            toggle = (Artwork.update({Artwork.available: status}).where(Artwork.id == cng_avail.id))
            toggle.execute()
            ui.message(f'{cng_avail.artwork_name} status updated.')
    except Exception as e:
        ui.message(e)

#Generates test tables 
def generate_test_tables():
    try:
        new_artist_1 = Artist(artist_name='Beyonce Giselle', email='Queenbeyonce@gmail.com')
        new_artist_1.save()
        new_artist_2 = Artist(artist_name='Jay z ', email='Kingjay@gmail.com')
        new_artist_2.save()
        new_artist_3 = Artist(artist_name='Omar Mohamud', email='omarmohamud23@gmail.com')
        new_artist_3.save()
        new_artist_3 = Artist(artist_name='Aubrey Graham', email='Drizzydrake@gmail.com')
        new_artist_3.save()
        new_artwork_1 = Artwork(artwork_name='Drake', price=22.45, artist=1)
        new_artwork_1.save()
        new_artwork_2 = Artwork(artwork_name='best code ever', price=2.30, artist=2)
        new_artwork_2.save()
        new_artwork_3 = Artwork(artwork_name='Sold Artwork', price=800.9, available=False, artist=2)
        new_artwork_3.save()
        new_artwork_4 = Artwork(artwork_name='Please delete', price=900.9, available=False, artist=1)
        new_artwork_4.save()
    except Exception as e:
        ui.message(e)


def drop_test_tables():
    db.drop_tables([Artist, Artwork])
    logging.info('tables have been deleted')
    sys.exit("Tables Deleted")

#Closes the program 
def quit_program():
    ui.message('Thanks and bye!')


if __name__ == "__main__":
    main()