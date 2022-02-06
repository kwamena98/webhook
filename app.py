from typing import Counter
from flask import Flask, redirect, url_for,render_template,request,session,flash
import time
import tweepy
import json
import psycopg2
import threading
import os
import random

import re

app=Flask(__name__)
app.config['SECRET_KEY']='myapp'

dbName="dvoaicd61vk1t"
user_="afftbbpopraylc"
password="ba1ebd591ccd47d24a687e26e41183de23d0f2ce88a83dfa62dd7164137fda56"
db_host="ec2-52-0-93-3.compute-1.amazonaws.com"


conn=psycopg2.connect(dbname=dbName,user=user_,password=password,host=db_host)
cur=conn.cursor()

#########################################################


API_KEY="eBCgqjNvty7jjagaJFXEXOZHe"
API_SECRET="O9T7kEEy8BphwSDEuwEqx2bLGzaZDF7L443ktAdmfw1VzYZK7w"
ACCESS_TOKEN = "1075083604353564672-S31X1C6sz5qsQOlxzvnhZi70m3KL4P"
ACCESS_SECRET = "9vz3BlOE1DzoRYfU98rTpsxJLSUoeUCkB72yga9yVMYIA"





# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


############################################






def credentials(liks):


    API_KEY="eBCgqjNvty7jjagaJFXEXOZHe"
    API_SECRET="O9T7kEEy8BphwSDEuwEqx2bLGzaZDF7L443ktAdmfw1VzYZK7w"
    ACCESS_TOKEN = "1075083604353564672-S31X1C6sz5qsQOlxzvnhZi70m3KL4P"
    ACCESS_SECRET = "9vz3BlOE1DzoRYfU98rTpsxJLSUoeUCkB72yga9yVMYIA"








    # Pass OAuth details to tweepy's OAuth handler
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)


    tweets=[]

    for l in liks:
        i=l[1]
        tweets.append(i)


    tags=[]

    for t in liks:
        y=t[3]
        tags.append(y)




    
    counter=0

    for tweet in tweets:
        statu="Working On"

        cur.execute("""
            UPDATE lins
            SET status=%s
            WHERE link=%s
        """, (statu,tweet))
        conn.commit()

        # print(tweet)
        
        id_=tweet.split("/")
        id_=id_[5]
        id_=int(id_)
        print(id_)


        tweet=api.get_status(id_,tweet_mode="extended")
        
        try:
            tweet=tweet.retweeted_status.full_text
        
        except AttributeError:  # Not a Retweet
            tweet=tweet.full_text
            




        mentions=re.findall(r"@(\w+)",tweet)
        print(mentions)

        data=cur.execute("SELECT * FROM comment")
        data=cur.fetchall()

        lsit=[]
        for l in data:
            comment=l[1]
            lsit.append(comment)





        data=cur.execute("SELECT * FROM fan ")

        data=cur.fetchall()

        



        # data=list(data)
        

        for something in data:
            token=something[1]
            token_secret=something[3]
            # com=random.sample(lsit)

            sample_space=(tags[counter])


            comment_s=random.sample(lsit,int(sample_space))

            outcome=', '.join(map(str, comment_s))
            s = outcome.replace(',', '')

            API_KEYS="eBCgqjNvty7jjagaJFXEXOZHe"
            API_SECRETS="O9T7kEEy8BphwSDEuwEqx2bLGzaZDF7L443ktAdmfw1VzYZK7w"
            ACCESS_TOKENS = token
            ACCESS_SECRETS =token_secret



            auth = tweepy.OAuthHandler(API_KEYS, API_SECRETS)
            auth.set_access_token(ACCESS_TOKENS, ACCESS_SECRETS)

                    


            try:

                apis = tweepy.API(auth, wait_on_rate_limit=True,
                    wait_on_rate_limit_notify=True)

                print(apis.me())

                apis.update_status(s,in_reply_to_status_id=id_, auto_populate_reply_metadata=True)
                apis.create_favorite(id_)
                apis.retweet(id_)
                print("DOne")

                try:
                    for n in mentions:
                        apis.create_friendship(n)

                except:
                    print("No mentioning")




                stats="Active"

                

                

            except Exception as e:



                # pass

                stats="Disabled"
                print (e)



            cur.execute("""
                UPDATE fan 
                SET status=%s
                WHERE access_token=%s
            """, (stats,token))
            conn.commit()
            
            print("waiting for the next move")
            time.sleep(6)

        
    cur.execute("DELETE FROM lins WHERE link='{}';".format(id_))
    conn.commit()

    counter=counter+1

    time.sleep(60*4)
        # break
        

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

    auth = tweepy.OAuthHandler("eBCgqjNvty7jjagaJFXEXOZHe","O9T7kEEy8BphwSDEuwEqx2bLGzaZDF7L443ktAdmfw1VzYZK7w")
    auth.request_token = { "oauth_token": oauth_token, "oauth_token_secret": oauth_verifier }
    auth.get_access_token(oauth_verifier)
    

    api_ke="eBCgqjNvty7jjagaJFXEXOZHe"
    api_se="O9T7kEEy8BphwSDEuwEqx2bLGzaZDF7L443ktAdmfw1VzYZK7w"
    accesstoken=auth.access_token
    accesssecret=auth.access_token_secret


    auth = tweepy.OAuthHandler(api_ke, api_se)
    auth.set_access_token(accesstoken, accesssecret)

    apis_ = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    s=apis_.me()
    username=s.screen_name
    username=str(username)

    status="New"


  


    
    # print(access_token)
    # print(access_secret)

    
    cur.execute("INSERT INTO fan (access_token,access_secret,status,username) VALUES (%s,%s,%s,%s)",[accesstoken,accesssecret,status,username])
    conn.commit()




    return redirect('/dashboard')





@app.route('/api/authorize_twitter')
def authorize_twitter():

    auth = tweepy.OAuthHandler("eBCgqjNvty7jjagaJFXEXOZHe","O9T7kEEy8BphwSDEuwEqx2bLGzaZDF7L443ktAdmfw1VzYZK7w","https://barlpro.herokuapp.com/api/callback")

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





    cur.execute("SELECT * FROM fan")
    data=cur.fetchall()
    data=list(data)
    # print(data)

    return render_template('dashboard.html',req=data)


# @app.route("/start",methods=["GET","POST"])
# def start():

#     return render_template("tweets.html")






    
@app.route("/tweet",methods=["GET","POST"])
def tweet():



    
    try:
        if request.method =="POST":

            link=request.form['link']
            n=request.form['select_from']
            statu="In queue"


            cur.execute("INSERT INTO lins(link,status,tag) VALUES (%s,%s,%s)",[link,statu,n])
            conn.commit()





    except:


        if request.method=="POST":

            n=request.form['_token']
            print(n)


            cur.execute("SELECT * FROM lins")
            lins_=cur.fetchall()

            t = threading.Thread(target=credentials(lins_))
            t.start()






    

        
    cur.execute("SELECT * FROM lins")
    dat=cur.fetchall()

    print(dat)
            



 


  

        # print(type(id_))


        # print(tweet)
    return render_template("tweets.html",data=dat)















@app.route("/comment",methods=["GET","POST"])
def comment():
    if request.method=="POST":

        comment=request.form['comment']
        cur.execute("INSERT INTO comment(messagename) VALUES (%s)",[comment])
        conn.commit()

    
    cur.execute("SELECT * FROM comment")
    data=cur.fetchall()
    print(data)
    return render_template('comment.html',data=data)









@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):

    cur.execute("DELETE FROM fan WHERE user_id=%s", [id_data])
    conn.commit()
    return redirect(url_for('dashboard'))


@app.route('/delete_/<string:id_data>', methods = ['GET'])
def delete_(id_data):

    cur.execute("DELETE FROM comment WHERE message_id=%s", [id_data])
    conn.commit()
    return redirect(url_for('comment'))












if __name__=='__main__':
        
        # starting thread 1



    app.run(debug=True,threaded=True)
