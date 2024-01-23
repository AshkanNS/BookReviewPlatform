import requests
from flask import request, jsonify, abort
from app import app, db
from app.models import Book, Review
from sqlalchemy.sql import func

# Fetch all books
@app.route('/books', methods=['GET'])
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    genre = request.args.get('genre')

    query = Book.query
    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if genre:
        query = query.filter(Book.genre.contains(genre))

    books = query.all()
    return jsonify({'books': [book.to_dict() for book in books]})

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = Book(title=data['title'], author=data['author'], summary=data['summary'], genre=data['genre'])
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

# Fetch a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

# Update a specific book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()

    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.summary = data.get('summary', book.summary)
    book.genre = data.get('genre', book.genre)

    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

# Delete a specific book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

# Add a new review
@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    # Check so the given rating is between 1-5
    rating = data.get('rating')
    if not (1 <= rating <= 5):
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400
    # Creating a new review
    new_review = Review(
        book_id=data['book_id'],
        user=data['user'],
        rating=rating,
        review_text=data['review_text']
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully'}), 201

# Fetch all reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify({'reviews': [review.to_dict() for review in reviews]})

# Fetch all reviews for a single book
@app.route('/reviews/<int:book_id>', methods=['GET'])
def get_reviews_for_book(book_id):
    reviews = Review.query.filter_by(book_id=book_id).all()
    return jsonify({'reviews': [review.to_dict() for review in reviews]})

# Fetch the top 5 books with the highest average rating
@app.route('/books/top', methods=['GET'])
def get_top_books():
    top_books = db.session.query(
        Book.title,
        func.avg(Review.rating).label('average_rating')
    ).join(Review, Review.book_id == Book.book_id) \
     .group_by(Book.book_id) \
     .order_by(func.avg(Review.rating).desc()) \
     .limit(5) \
     .all()

    top_books_list = [{'title': book.title, 'average_rating': round(book.average_rating, 2)} for book in top_books]
    return jsonify({'top_books': top_books_list})

# Fetch summary of an author and their books using a external API
@app.route('/author/<string:author_name>', methods=['GET'])
def get_author(author_name):
    # replaces spaces with underscore so the name works in URL
    author_name_formatted = author_name.replace(" ", "_")
    # the API we are using
    api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{author_name_formatted}"

    # sends error if author not found
    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        abort(404, description=f"Author information for '{author_name}' not found.")

    # exctract data to JSON
    author_data = response.json()

    # extracting what type of information we are looking for
    formatted_response = {
        'name': author_data.get('title', 'No name available'),
        'summary': author_data.get('extract', 'No summary available'),
    }

    return jsonify(formatted_response)