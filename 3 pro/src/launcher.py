"""  
    - Launcher used to build .exe of the whole application
    - can have a short welcome screen
    - here we use delays and other stuff to make user experience pleasant,
      we didnt want to use it in application class. because we dont want to have
      6 seconds wait every time when testing code
"""
from app import Application
from time import sleep

if __name__ == '__main__':
    # create instance
    app = Application()

    # wait for user to see splash screen
    app.splash_screen()
    sleep(3)

    # start
    app.start()
    
    # application loop here
    app.run()

    # close the application
    app.end()
    
    # wait for user to see farawell screen
    sleep(3)

 