from flask import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap
import secrets
import os

# Generate a secure random string (use this as your secret key)
secret_key = secrets.token_hex(16)
print(secret_key)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your_generated_secret_key')

hotels_data = [
    {
        "id": 1,
        "name": "Ojai Valley Inn",
        "image_url": "/static/css/ojai_Valley_Inn.jpeg",  
        "location": "Southern California",
        "price": "$526 per night",
        "description": "A luxurious hotel with stunning views and top-notch services. Some services included are spa, meditative sound bath, four pools, rock climbing, horseback riding, and kayaking.",
    },
    {
        "id": 2,
        "name": "Alaska Grizzly Lodge",
        "image_url": "/static/css/Alaska Grizzly Lodge.jpg",
        "location": "Alaska",
        "price": "$229 per night",
        "description": "A cozy hotel with a friendly staff that are always happy to give a helping hand. Enjoy a delicious breakfast, followed by relaxing next to the cozy fire, and finally, at night look up to the sky and amaze yourself with the beautiful aurora borealis",
    },
    {
        "id": 3,
        "name": "Turquosie Place",
        "image_url": "\static\css/Turquosie Place.jpg",
        "location": "Alabama",
        "price": "$250 per night",
        "description": "An elegant hotel offering a tranquil escape and excellent amenities. Enjoy relaxing under the sun on the beach or enjoy the lazy river, the food and bar next to the pool, and enjoy the music that plays on the weekends.",
    },
    {
        "id": 4,
        "name": "Boulders Resort & Spa",
        "image_url": "/static/css/Boulders Resort & Spa.jpg",  
        "location": "Arizona",
        "price": "$397 per night",
        "description": "Enjoy your stay at breathtaking scenery, 3 outdoor pools, private rooms, delicious food at 5 restaurants, and friendly staff. Enjoy the classy vibe that Boulders Resort & Spa provides.",
    },
    {
        "id": 5,
        "name": "Pratt Place Inn and Barn",
        "image_url": "/static/css/Pratt Place Inn and Barn.jpg",  
        "location": "Arkansas",
        "price": "$189 to 227 per night",
        "description": "Enjoy your stay at Pratt Place Inn and Barn where being surrounded by 140 acres of woodland, would be the perfect place to escape to the outdoors, with the gentle rooms with period furnishing features en suite bathrooms, 4-poster beds, garden viewing area, and sitting areas. Upgraded rooms get a fireplace and balconies or porches. Enjoy your stay with amenities such as a wraparound porch, landscaped garden, patio, and event space in a converted barn. Breakfast, Free Wi-Fi, free parking, accessible, Air-conditions, and kid-friendly are some of the few amenities that would be provided.",
    },
    {
        "id": 6,
        "name": "Gateway Canyons Resort",
        "image_url": "/static/css/gateway-canyons-resort.jpg",  
        "location": "Colorado",
        "price": "$249 per night",
        "description": "Enjoy your stay at Gateway Canyons Resort designed to blend in with the surroundings, along with overlooking a pond that hosts the Gateway Auto Museum. Enjoy the different atmosphere for the rooms with the rustic-chic vibe, suites, and cottages that hold southwestern textiles, TVs, bars, coffee makers, and mini-fridges. There are 3 restaurants, a heated outdoor pool, and a hot tub. Some amenities are a spa, and fitness center, and an additional surcharge applies for horseback riding, jeep tours, and air torus. Free Wi-Fi, free parking, accessible, Air-conditioned and outdoor pool are some amenities that are provided as well.",
    },
    {
        "id": 7,
        "name": "Winvian",
        "image_url": "/static/css/Winvian.jpg",  
        "location": "Connecticut",
        "price": "$799 per night",
        "description": "This rustic-chic hotel in the Litchfield Hills is housed in charming farmhouses and buildings on 113 wooded acres. The distance from Litchfield town is 4.3 miles."
        " The luxurious, well-furnished cottages, the majority of which have woodsy-chic furnishings, come with patios or screened porches, fireplaces, jacuzzi tubs, Wi-Fi, loaner bikes, and coffee makers. There's also a funny treehouse and a 1968 helicopter that has been transformed."
        " A spa and seasonal activities like culinary workshops and horseback riding are available as amenities. Produce from the hotel's gardens is served at an upscale farm-to-table restaurant. There's parking and a cooked breakfast offered.",
    },
    {
        "id": 8,
        "name": "Hotel du Pont",
        "image_url": "/static/css/Hotel du Pont.jpg",  
        "location": "Delaware",
        "price": "$230 per night",
        "description": "This elegant hotel is located in a downtown 1913 landmark across from Rodney Square. It is 1 mile from the Amtrak station and 6 miles from the Winterthur Museum."
        "Free Wi-Fi, flat-screen TVs with streaming services, and soaking tubs are amenities found in tastefully decorated, traditional rooms with modern twists. Rich suites come with separate dining and living rooms. There is room service available."
        "Rich décor adorns an elegant French restaurant/bar. There's a cozy bar and a lobby lounge with additional dining options. On-site amenities include a spa, a workout center equipped with Peloton bikes, and a historic performing arts theater. Transport into the city center can be scheduled.",
    },
    {
        "id": 9,
        "name": "Montage Kapalua Bay",
        "image_url": "/static/css/Montage Kapalua Bay.jpg",  
        "location": "Hawaii",
        "price": "$530 per night",
        "description": "Situated amidst 24-acre beachfront grounds, this modern resort offers stunning views of Namalu Bay and is just a 4-minute walk from the Bay Course of Kapalua Golf Club. The distance to the Dragon's Teeth rock formations is one mile."
        "Quiet one- to four-bedroom condos with views of the garden or the ocean and contemporary, island-inspired décor. Each has a fully equipped kitchen, living room, private lanai, and luxurious amenities and bedding."
        "In addition to an outdoor pool area featuring a sundeck, cabanas, and a poolside bar, there's a gourmet Hawaiian restaurant, a laid-back terrace bistro, and a gift shop selling locally made goods. A chic day spa and meeting/event spaces are among the additional features.",
    },
    {
        "id": 10,
        "name": "Coeur d'Alene Resort",
        "image_url": "/static/css/Coeur d'Alene Resort.jpg",  
        "location": "Idaho",
        "price": "$200 per night",
        "description": "This luxurious resort on Lake Coeur d'Alene's shores is just five minutes' walk from City Park & Beach."
        "Simple apartments in the North Wing and rooms in the hotel's 17-story tower are among the lodging options. All have sleek, modern furnishings, complimentary WiFi, and flat-screen TVs. Tower rooms include fireplaces, private balconies, and/or views of the lake in addition to bay or picture windows. There is room service available."
        "A golf course with a distinctive floating green is one of the amenities, along with a spa and salon. Additionally, there are a number of eateries, lounges, and pubs serving Italian, Asian, and locally produced food.",
    },
]

# User's selected hotels
user_hotels = []

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('User created successfully')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/hotel', methods=['GET', 'POST'])
def hotel():
    if request.method == 'POST':
        hotel_id = int(request.form.get('hotel_id'))
        hotel_name = request.form.get('hotel_name')

        if hotel_id and hotel_name:
            user_hotels.append({"id": hotel_id, "name": hotel_name})

    user_hotel_ids = [hotel["id"] for hotel in user_hotels]

    return render_template('hotel.html', hotels=hotels_data, user_hotels=user_hotels, user_hotel_ids=user_hotel_ids)


@app.route('/my_hotels', methods=['GET', 'POST'])
def my_hotels():
    if request.method == 'POST':
        hotel_id_to_remove = int(request.form.get('hotel_id_to_remove'))
        user_hotels[:] = [hotel for hotel in user_hotels if hotel["id"] != hotel_id_to_remove]

    return render_template('my_hotels.html', user_hotels=user_hotels)

@app.route('/logout')
def logout():
    # Clear the session data
    session.clear()
    # Redirect to the home page or login page
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
