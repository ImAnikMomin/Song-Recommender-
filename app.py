from flask import Flask, redirect, request, session, url_for, render_template
from recommender import Recommender
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY
recommender = Recommender()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authorize')
def authorize():
    auth_url = recommender.spotify_client.get_auth_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = recommender.spotify_client.get_token(code)
    session['token_info'] = token_info
    return redirect(url_for('playlists'))

@app.route('/playlists')
def playlists():
    if 'token_info' not in session:
        return redirect(url_for('index'))
    playlists = recommender.spotify_client.get_user_playlists()
    return render_template('playlists.html', playlists=playlists)

@app.route('/recommendations', methods=['POST'])
def recommendations():
    playlist_id = request.form['playlist_id']
    tracks = recommender.spotify_client.get_playlist_tracks(playlist_id)
    recommendations = recommender.openai_client.generate_recommendations(tracks)
    return render_template('recommendations.html', recommendations=recommendations)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
