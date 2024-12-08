from flask import Flask, render_template, request,flash,session,redirect,url_for,g
#from werkzeug import secure_filename
#from KnnImplementation import perpetator_sex_predict
import sqlite3 as sql
from EncodingValues import  Encodings
import knn2
import  LinearRegressionImplementation
from Graphs import Analyse1
from Graphs import Analyse2
from Graphs import Analyse7
from Graphs import Analyse8
from Graphs import Analyse9
from Graphs import Analyse6
from Graphs import Analyse10
from Graphs import Analyse5
from Relationship import Relation


app = Flask(__name__)
app.config['SECRET_KEY'] = 'defaultkey'

@app.route('/')
def home():
    return render_template('mainpage.html')


@app.route('/login_form', methods=['GET', 'POST'])
def login_form():
    return render_template('login.html')


@app.route('/protected')
def protected():
    if g.user:
        return render_template('next1.html', user=session['user'])

    return redirect(url_for('home'))


@app.before_request
def before_request():
    g.user=None

    if 'user' in session:
        g.user= session['user']


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    session.pop('relation', None)
    return redirect(url_for('home'))

@app.route('/relationship', methods=['GET', 'POST'])
def relationship():

        #relation=Relation()
       # session.pop('perperator_sex');
        #print(relation)

           # print("relatin :" + session['relation'])
            if session['relation']==True:

                print("relatin :"+session['relation'])
                if session['perperator_sex']=='Male':
                    relation1= 'Acquaintance'
                    flash("Perperator Sex Prediction is : " + relation1)
                    return render_template('Relationship.html')

                elif session['perperator_sex']=='Female' :
                    relation1 = 'Wife'
                    flash("Perperator Sex Prediction is : " + relation1)
                    return render_template('Relationship.html')
                else:
                    relation1 = 'Unknown'
                    flash("Perperator Sex Prediction is : " + relation1)
                    return render_template('Relationship.html')
            else:
                flash("No relationship exists")
                return render_template('Relationship.html')



@app.route('/backofrelation', methods=['GET', 'POST'])
def backofrelation():

    return render_template('CrimePredictionSex.html')

@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))


@app.route('/next', methods=['GET', 'POST'])
def next():

    select = request.form['selector1']
    if select == 'Sex':
        return render_template('crimePredictionSex.html')
    else:
        return render_template('crimePredictionAge.html')


@app.route('/next1', methods=['GET', 'POST'])
def next1():

    select = request.form['selector1']
    if select == 'graph':
        return render_template('Analyse.html')
    else:
        return render_template('next.html')


@app.route('/analysis', methods=['GET', 'POST'])
def analysis():

    select = request.form['analyse']
    if select == 'Number of Homicides in USA':
        Analyse1.test()
        return render_template('Analyse.html')

    if select == 'Month-Wise Analysis':
        Analyse2.test()
        return render_template('Analyse.html')

    if select == 'Crimes Solved':
        Analyse5.test()
        return render_template('Analyse.html')

    if select == 'Crime Rate Solved':
        Analyse6.test()
        return render_template('Analyse.html')

    if select == 'Age Analysis':
        Analyse7.test()
        return render_template('Analyse.html')

    if select == 'Rate of Victims':
        Analyse8.test()
        return render_template('Analyse.html')

    if select == 'Perpetrator Race':
        Analyse9.test()
        return render_template('Analyse.html')

    if select == 'Crime Type':
        Analyse10.test()
        return render_template('Analyse.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            user = request.form['username']
            passw = request.form['pass']

            with sql.connect("CrimeDatabase.db") as con:
                cur = con.cursor()
                query="select *from Login where username= ? and password=?"
                data=cur.execute(query,(user,passw))
                session['user']= user;
                if (len(cur.fetchall()) > 0):
                    return render_template('next1.html')
                else:
                    flash("please check details")
                    return render_template('login.html')
        except:

            flash("please check details")


@app.route('/predictsex', methods=['POST', 'GET'])
def predictsex():

    if request.method == 'POST':
        State = request.form['state']
        crimeType=request.form['crime_type']
        victimSex = request.form['victim_sex']
        victimAge = request.form['victim_age']
        victimRace = request.form['victim_race']
        victimCount = request.form['victim_count']
        weapon = request.form['weapon']

        state_value = Encodings.state_values(State)
        crime_type = Encodings.crime_type(crimeType)
        victim_sex = Encodings.victim_sex(victimSex)
        victim_race = Encodings.victim_race(victimRace)
        weapons = Encodings.weapons(weapon)


        result=knn2.knnPrediction(state_value, crime_type, victim_sex, victimAge, victim_race,victimCount, weapons)
        if result ==0:
            perperator_sex= 'Female'
            relation='Wife'

        elif result ==1:
            perperator_sex='Male'
            relation = 'Acquaintance'

        else:
            perperator_sex = 'Unknown'
            relation = 'Unknown'

        flash("Perperator Sex Prediction is : " + perperator_sex)
        flash("Perperator Relation is : " + relation)
        return render_template('crimePredictionSex.html')


@app.route('/predictage', methods=['POST', 'GET'])
def predictage():
    if request.method == 'POST':
        State = request.form['state']
        crimeType = request.form['crime_type']
        victimSex = request.form['victim_sex']
        victimAge = request.form['victim_age']
        victimRace = request.form['victim_race']
        victimCount = request.form['victim_count']
        weapon = request.form['weapon']

        state_value = Encodings.state_values(State)
        crime_type = Encodings.crime_type(crimeType)
        victim_sex = Encodings.victim_sex(victimSex)
        victim_race = Encodings.victim_race(victimRace)
        weapons = Encodings.weapons(weapon)

       # perperator_age1,perperator_age2,perperator_age3  = LinearRegressionImplementation.predictAge(state_value, crime_type, victim_sex, victimAge, victim_race, victimCount,
        #                                weapons)
        LinearRegressionImplementation.predictAge(state_value, crime_type, victim_sex, victimAge,victim_race ,victimCount,
                                                                                                      weapons)

        #flash("Perperator Age Prediction is : " + perperator_age1)
        return render_template('crimePredictionAge.html')

if __name__ == '__main__':
    app.debug = True
    app.run()