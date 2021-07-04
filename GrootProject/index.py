from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
	f_login = open ('./dataStore/loginList.json', "r")
	login_data = json.loads(f_login.read())
	for i in login_data['login_users']:
		print(i['user_name'])
	return render_template('Login.html')

@app.route('/login', methods = ['POST'])
def login_user() :
	if request.method == 'POST':
		form_data = request.form
		uName = form_data['uname']
		uPwd = form_data['upswd']
		f_login = open ('./dataStore/loginList.json', "r")
		login_data = json.loads(f_login.read())
		
		isValid = False
		isAdmin = False
		
		for i in login_data['login_users']:
			if uName==i['user_name'] and uPwd==i['password'] :
				isValid = True
				if i['is_admin'] == 'yes' :
					isAdmin = True
				break;
		if isValid and isAdmin :
			f_userList = open ('./dataStore/userList.json', "r")
			user_data = json.loads(f_userList.read())
			return render_template("UserList.html", user_name = uName, user_list = user_data['user_list'])
		elif isValid :
			return render_template("UserList.html", user_name = uName,user_list = login_data['login_users'][uName])
		else :
			return render_template('Login.html', message = 'User name or Password is Invalid')
	return 'Validate user'

@app.route('/users')
def display_users():
    return 'Hello!! List of users'
  
# main driver function
if __name__ == '__main__':
	app.run(debug = True)