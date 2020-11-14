from flask import Flask, redirect, url_for,render_template,request,session,flash
# from flaskext.mysql import MySQL
# import json
app=Flask(__name__)
app.config['SECRET_KEY']='myapp'

@app.route('/')


@app.route('/login',methods=['GET','POST'])
def thepage():
    if request.method =='POST':
        status=request.form['username']
        email=request.form['groupcode']
        print(status)
        print(email)

        if status=='Derrick' and email=='Kwamena' :
            flash('You were successfully logged in')
            return (redirect(url_for('home_page')))
            
        elif status=="" and email=="":
            return (redirect(url_for('thepage')))

        else:
            flash("Account doesn't exist")
            return (redirect(url_for('thepage')))
            
            
    return render_template('login.html')
    

@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
        username=request.form['username']
        groupname=request.form['groupname']
        groupcode=request.form['groupcode']

        list_of_users=['kwamena','yaw','ama']
        if  groupname and groupcode  in list_of_users:
            flash('This Group Name and Group Code already exist')
            return redirect(url_for('sign_up'))

        elif username=="" and groupcode=="" and groupcode=="":
            return redirect(url_for('sign_up'))


        else:
            flash("You've Created an Account Login to continue")
            return (redirect(url_for('thepage')))






        print(username)
        print(groupcode)
        print(groupname)




    return render_template('sign_up.html')


@app.route('/home_page',methods=['GET','POST'])
def home_page():

    return render_template('homepage.html')

    

if __name__=='__main__':
    app.run(debug=True)

