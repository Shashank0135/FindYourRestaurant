from flask import Flask, jsonify, request, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Read the CSV file
df = pd.read_csv("restaurants.csv", encoding='ISO-8859-1')

# Convert the DataFrame to a dictionary for easy access
restaurants = df.to_dict(orient='records')

PER_PAGE = 10

# Home route
@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE
    paginated_restaurants = restaurants[start:end]
    
    prev_url = None
    next_url = None
    if start > 0:
        prev_url = f"?page={page - 1}"
    if end < len(restaurants):
        next_url = f"?page={page + 1}"
    
    return render_template('home.html', restaurants=paginated_restaurants, prev_url=prev_url, next_url=next_url)

# Endpoint to retrieve restaurant details by ID and render template
@app.route('/restaurant/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    for restaurant in restaurants:
        if restaurant['Restaurant ID'] == restaurant_id:
            return render_template('restaurant.html', restaurant=restaurant)
    return jsonify({'error': 'Restaurant not found'}), 404

# Route to handle the search form submission
@app.route('/search', methods=['GET'])
def search():
    restaurant_id = request.args.get('restaurant_id')
    return redirect(url_for('get_restaurant', restaurant_id=restaurant_id))

if __name__ == '__main__':
    app.run(debug=True)
