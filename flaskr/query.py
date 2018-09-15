import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db
bp = Blueprint('query', __name__, url_prefix='/query')

@bp.route('/findTweetID', methods=('GET', 'POST'))
def queryid():
    if request.method == 'POST':
        userID = request.form['userID']
        db = get_db()
        error = None

        if not userID:
            error = 'Username is required.'
        elif db.execute(
            'SELECT id FROM records WHERE userID = ?', (userID,)
        ).fetchone() is not None:
            error = db.execute('SELECT tweetID FROM records WHERE userID = ?',(userID,)),


        if error is None:
            #USE TWITTER API HERE TO FIND tweetID
            tweetID=5
            db.execute(
                'INSERT INTO records (userID, tweetID) VALUES (?, ?)',
                (userID, tweetID,)
            )
            db.commit()
            return redirect(url_for('query.data'))

        flash(error)

    return render_template('query/findTweetID.html')

@bp.route('/data', methods=('GET', 'POST'))
def data():
    return render_template('query/data.html')
