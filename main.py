from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window




def db():
	import pymongo
	client = pymongo.MongoClient("mongodb+srv://suz123:suz123@suzedu.igslm.mongodb.net/?retryWrites=true&w=majority")
	db = client.Election
	return db

class ElectionApp(MDApp):
	def build(self):

		global screen_manager
		self.icon = "loogoo.png"
		screen_manager = ScreenManager()
		screen_manager.add_widget(Builder.load_file("pre_slash.kv"))
		screen_manager.add_widget(Builder.load_file("login.kv"))
		screen_manager.add_widget(Builder.load_file("loggedin.kv"))
		return screen_manager

	def on_start(self):
		Clock.schedule_once(self.login, 1)

	def login(self, *args):
		screen_manager.current = "login"

	def bbtn(self):
		db1 = db()
		details = db1["detailsFromAgents"]

		ward =  str(screen_manager.get_screen('loggedin').ids.ward.text)
		poling =  str(screen_manager.get_screen('loggedin').ids.poling.text)
		presiding =  str(screen_manager.get_screen('loggedin').ids.presiding.text)
		dpresiding =  str(screen_manager.get_screen('loggedin').ids.dpresiding.text)

		mydict = { "ward": ward , "poling": poling,"presiding":presiding, "dpresiding":dpresiding}

		x = details.insert_one(mydict)
		if(x is not None):
			screen_manager.get_screen('loggedin').ids.myerror.text = 'Data Submitted'
		else:
			screen_manager.get_screen('loggedin').ids.myerror.text = 'Sorry, No Data Submitted'

	def btn(self):
		
		db2 = db()

		mycol = db2["users"]

		if(mycol is not None):
			loginUsername =  str(screen_manager.get_screen('login').ids.loginUsername.text)
			loginPassword =  str(screen_manager.get_screen('login').ids.loginPassword.text)	
			if(mycol.find_one({'username': loginUsername,'password':loginPassword})):
				screen_manager.current = 'loggedin'
			else:
				screen_manager.get_screen('login').ids.myerror.text = 'INCORRECT USERNAME OR PASSWORD'
		else:
			screen_manager.get_screen('login').ids.myerror.text = 'NOT INTERNET CONNECTION'		


if __name__ == "__main__":
	ElectionApp().run()		