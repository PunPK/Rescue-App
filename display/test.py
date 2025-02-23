# import the necessary Kivy libraries
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# import the MongoClient class
from pymongo import MongoClient, errors

# global variables for MongoDB host (default port is 27017)
DOMAIN = "localhost:"
PORT = 27017

# use a try-except indentation to catch MongoClient() errors
try:
    # try to instantiate a client instance
    client = MongoClient(
        host=[str(DOMAIN) + str(PORT)],
        serverSelectionTimeoutMS=3000,  # 3 second timeout
    )

    # print the version of MongoDB server if connection successful
    print("server version:", client.server_info()["version"])

except errors.ServerSelectionTimeoutError as err:
    # set the client and db names to 'None' and [] if exception
    client = None

    # catch pymongo.errors.ServerSelectionTimeoutError
    print("pymongo ERROR:", err)


# create a new class for the Kivy MongoDB app
class MongoApp(App):

    # define the build() function for the app
    def build(self):

        # change the app's attributes
        self.title = "Rescue MongoDB App"

        # concatenate the host's domain and port variables
        self.mongo_domain = str(DOMAIN) + str(PORT)

        # set the layout for the Kivy application
        self.layout = BoxLayout(orientation="vertical")

        # change font title labels
        db_label = Label(font_size=50)
        domain_label = Label(font_size=40)

        self.layout.add_widget(db_label)
        self.layout.add_widget(domain_label)

        if client != None:
            domain_label.text = "Connected!\n" + str(self.mongo_domain)
            db_label.text = "Select a MongoDB database"
        else:
            domain_label.text = "Your client's host parameters are invalid,"
            domain_label.text += "\nor your MongoDB server isn't running."
            db_label.text = "ERROR: Not connected to MongoDB"

        return self.layout


MongoApp().run()
