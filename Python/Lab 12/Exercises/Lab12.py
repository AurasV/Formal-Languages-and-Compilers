import uuid
import pymysql
from flask import Flask, request, redirect, render_template
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

pymysql.install_as_MySQLdb()

# Create Flask app
app = Flask(__name__)
# Add CORS to app
CORS(app)
# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://sql7707802:C45mHm4j2m@sql7.freesqldatabase.com/sql7707802"
# Add SQLAlchemy to app
db = SQLAlchemy(app)


# Create class for a new table in the database
# Table AlbumYourName with columns id-pk, band_name, genre, and album
class AlbumYourName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(250))
    genre = db.Column(db.String(250))
    album = db.Column(db.String(250))


# Comment if you run the code more than once
with app.app_context():
    # Create table in db - call only once
    db.create_all()
    # Commit changes
    db.session.commit()


# Route to main page; function to retrieve all data from the database
@app.route('/', methods=['GET', 'POST'])
def retrieveAll():
    holder = list()
    # Query table AlbumYourName
    albums = AlbumYourName.query.all()
    for i in albums:
        # Append in list the values from each table row
        holder.append({'band_name': i.band_name, 'genre': i.genre, 'album': i.album})
    # Return landing.html page - our home page
    # Holder is also a variable defined in the HTML file where data will be displayed
    return render_template('landing.html', holder=holder)


# Endpoint to add data to db
@app.route('/postData', methods=['POST'])
def postData():
    # Get values for bandName, genre, album inputted by the user
    band_name = request.form['bandName']
    genre = request.form['genre']
    album = request.form['album']
    # Create a new record in the AlbumYourName table
    new_album = AlbumYourName(band_name=band_name, genre=genre, album=album)
    db.session.add(new_album)
    db.session.commit()
    return redirect(url_for('retrieveAll'))


# Endpoint to delete data from db - it deletes based on band_name
@app.route('/deleteData', methods=['POST'])
def deleteData():
    # Retrieve value for bandNameDelete inputted by the user
    band_name = request.form['bandNameDelete']
    # Delete record from the AlbumYourName table based on band_name
    AlbumYourName.query.filter_by(band_name=band_name).delete()
    db.session.commit()
    return redirect(url_for('retrieveAll'))


@app.route('/update', methods=['POST'])
def updateData():
    # Retrieve values for band name and updated band name inputted by the user
    band_name = request.form['bandNameUpdate']
    updated_band_name = request.form['bandNameUpdated']
    # Update band_name in records where band_name matches the input
    albums = AlbumYourName.query.filter_by(band_name=band_name).all()
    for album in albums:
        album.band_name = updated_band_name
    db.session.commit()
    return redirect(url_for('retrieveAll'))


if __name__ == '__main__':
    app.run()

