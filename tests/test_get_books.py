import pytest
from app import app, db
from app.models import Book, Review

# Flask app for testing
@pytest.fixture
def app_context():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()

# test client
@pytest.fixture
def client(app_context):
    return app.test_client()

# Test for GET /books endpoint
def test_get_books(client):
    # Set up a sample book
    sample_book = Book(title='Test Book', author='Test Author', summary='Test Summary', genre='Test Genre')
    db.session.add(sample_book)
    db.session.commit()

    # Perform the test
    response = client.get('/books')
    assert response.status_code == 200
    assert b'Test Book' in response.data

# Test for POST /reviews endpoint
def test_post_review(client):
    review_data = {
        'book_id': 4,
        'user': 'Ashkan',
        'rating': 5,
        'review_text': 'Bra Bok'
    }

    # POST request to add a new review
    response = client.post('/reviews', json=review_data)
    assert response.status_code == 201
    assert b'Review added successfully' in response.data

