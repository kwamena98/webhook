from flask import Flask, redirect, url_for,render_template,request,session,flash
import time
import tweepy
import json
import psycopg2
import threading
import os

app=Flask(__name__)
app.config['SECRET_KEY']='myapp'


app.config['SECRET_KEY']='myapp'

dbName="dvoaicd61vk1t"
user_="afftbbpopraylc"
password="ba1ebd591ccd47d24a687e26e41183de23d0f2ce88a83dfa62dd7164137fda56"
db_host="ec2-52-0-93-3.compute-1.amazonaws.com"


conn=psycopg2.connect(dbname=dbName,user=user_,password=password,host=db_host)
cur=conn.cursor()




def credentials(tweet_id):

    data=cur.execute("SELECT * FROM newdata")

    data=cur.fetchall()


    # data=list(data)
    

    for something in data:
        token=something[1]
        token_secret=something[2]
        comment=something[3]

        API_KEY="Oi0L0L9HpJ922WQhkX6Qkcwlo"
        API_SECRET="Vd8ZVFgy4NHKHGT9z1taquyfSKfYwd3E5o5u6Dqcm3LjjoCfZe"
        ACCESS_TOKEN = token
        ACCESS_SECRET =token_secret



        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        try:
            api = tweepy.API(auth, wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True)

            api.update_status(comment,in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)

            stats="Active"

            

            

        except:



            # pass

            stats="Disabled"



        cur.execute("""
            UPDATE newdata
            SET status=%s
            WHERE access_token=%s
        """, (stats,token))
        conn.commit()
        
        print("waiting for the next move")
        time.sleep(60*3)
        

@app.route('/')

@app.route('/login', methods=["GET","POST"])
def First_page():
    # cur= mysql.connection.cursor()
    if request.method =='POST':
        username=request.form['user']
        password=request.form['user_pass']
        

        if username=="mytweet" and password=="Mastergrand56":

            return redirect('/dashboard')

        else:   
            return ("Invalid Credentials")



        # if username==str:
        #     redirect(url_for('Home'))

        



    return render_template("login.html")

@app.route('/thepage')
def thepage():

    return render_template('thepage.html')





@app.route('/api/callback')
def api_callback():
    # cur=mysql.connection.cursor()
    oauth_token = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')
    print("oauth_token: ", oauth_token)
    print("oauth_verifier: ", oauth_verifier)

    auth = tweepy.OAuthHandler("Oi0L0L9HpJ922WQhkX6Qkcwlo","Vd8ZVFgy4NHKHGT9z1taquyfSKfYwd3E5o5u6Dqcm3LjjoCfZe")
    auth.request_token = { "oauth_token": oauth_token, "oauth_token_secret": oauth_verifier }
    auth.get_access_token(oauth_verifier)
    
    # print(auth.access_token)
    # print(auth.access_token_secret)
    # user_id = session['user_id']
    # print(user_id)

    access_token=auth.access_token
    access_secret=auth.access_token_secret

    
    cur.execute("INSERT INTO newdata(access_token,access_secret) VALUES (%s,%s)",[access_token,access_secret])
    conn.commit()




    return redirect('/dashboard')





@app.route('/api/authorize_twitter')
def authorize_twitter():

    auth = tweepy.OAuthHandler("Oi0L0L9HpJ922WQhkX6Qkcwlo","Vd8ZVFgy4NHKHGT9z1taquyfSKfYwd3E5o5u6Dqcm3LjjoCfZe","https://commenttwitter.herokuapp.com/api/callback")

    try:
        redirect_url = auth.get_authorization_url()
        print("REDIRECT: ", redirect_url)
        # session.set('request_token', auth.request_token['oauth_token'])
        return redirect(redirect_url)
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
        return json.dumps({"message":"Failed to get request token"})




@app.route('/dashboard',methods=["GET","POST"])
def dashboard():
    cur=conn.cursor()

 
    global messages
    global cus



    if request.method =='POST':

        messages=request.form['rate']
        cus=request.form['cus']
        print(messages)
        print(cus)




        cur.execute("""
            UPDATE newdata
            SET comment=%s
            WHERE access_token=%s
        """, (messages,cus))
        conn.commit()
        return redirect(url_for('dashboard'))


    cur.execute("SELECT * FROM newdata")
    data=cur.fetchall()
    data=list(data)
    # print(data)

    return render_template('dashboard.html',req=data)



# @app.route("/stop",methods=["GET","POST"])
# def interupt():
#     # if exist_event.is_set():
#         t1.join()
#         print("Ended Hmmmmm")
        
    
#         return ("You stopped The bots from Running Go back refresh the page  and Start Again")



    
@app.route("/tweet",methods=["GET","POST"])
def tweet():
    if request.method=="POST":

        tweet=request.form['tweet']

        id_=tweet.split("/")
        id_=id_[5]
        id_=int(id_)
        print(id_)

        

        



        t = threading.Thread(target=credentials, args=(id_,))
        t.start()



  

        # print(type(id_))


        # print(tweet)
    return render_template("tweet.html")

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):

    cur.execute("DELETE FROM newdata WHERE id=%s", [id_data])
    conn.commit()
    return redirect(url_for('dashboard'))








if __name__=='__main__':
        
        # starting thread 1



    app.run(debug=True,threaded=True)
