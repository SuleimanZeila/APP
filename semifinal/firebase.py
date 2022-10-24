# from firebase import firebase

# config = {
# 	"apiKey": "AIzaSyDHSZ0a5InIgBrKPadwZm81YWYwrB658xo",
# 	"authDomain": "electionapp-ab201.firebaseapp.com",
# 	"projectId": "electionapp-ab201",
#     "storageBucket": "electionapp-ab201.appspot.com",
# 	"messagingSenderId": "15977905127",
# 	"appId": "1:15977905127:web:c6dfce37dde0336c211b42",
# 	"measurementId": "G-330053BT4Q",
# 	"databaseURL":"https://electionapp-ab201-default-rtdb.asia-southeast1.firebasedatabase.app"
# }


# data = {"Username":"jabz","Password":123}


# fb = firebase(config)
# db = fb.database()

# rs = db.child('usrs').push(data)

# print(rs)


# from firebase import firebase
# firebase = firebase.FirebaseApplication('https://electionapp-ab201-default-rtdb.asia-southeast1.firebasedatabase.app', None)








import requests
fb = "https://electionapp-ab201-default-rtdb.asia-southeast1.firebasedatabase.app/Users.json"
data = {"username":"Kassimmjhgjhjh","password":12320}

res = requests.get(fb,json=data)
print(res)






