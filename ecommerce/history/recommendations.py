from collections import Counter
from .models import HistoryModel, BooksModel
from bson import ObjectId

def get_user_interactions(user):
    """
    Get all books a user interacted with (like, purchase, cart).
    """
    return HistoryModel.objects.filter(user=user._id).values('book', 'interaction')


def recommend_books_based_on_user(user, top_n=5):
    """
    Recommend books to a user based on other users who interacted with similar books.
    """
    # Get books the user interacted with
    user_interactions = get_user_interactions(user)
    print('user_interactions------------------')
    print(user_interactions)
    interacted_books = [interaction['book'] for interaction in user_interactions]
    print('interacted_books------------------')
    print(interacted_books)
    # Find other users who interacted with these books
    similar_users = HistoryModel.objects.filter(book_id__in=interacted_books).exclude(user=user)
    print('similar_users------------------')
    print(similar_users)
    # Get books interacted with by these similar users (exclude already interacted books)
    similar_books = HistoryModel.objects.filter(user_id__in=similar_users.values('_id')).filter(book_id__in=interacted_books)
    similar_books = HistoryModel.objects.exclude(book_id__in = [x for x in similar_books])
    # .exclude(book_id__in=interacted_books)
    print('similar_books------------------')
    print(similar_books)
    # Count the frequency of each book
    book_counter = Counter(similar_books.values_list('book_id', flat=True))
    print('book_counter------------------')
    print(book_counter)
    # Get the top N books most frequently interacted with by similar users
    recommended_books_ids = [book_id for book_id, _ in book_counter.most_common(top_n)]
    print("OOOOOOKKKKKKK")

    # Fetch the recommended books from the database
    recommended_books = BooksModel.objects.filter(_id__in=recommended_books_ids)
    print("OOOOOOKKKKKKK")

    return recommended_books

def recommend_books_by_category(user, top_n=5):
    """
    Recommend books to a user from the same category as books they liked or purchased.
    """
    # Get books the user has interacted with (liked or purchased)
    user_interactions = get_user_interactions(user)
    liked_books = [interaction['book'] for interaction in user_interactions if interaction['interaction'] in ['like', 'purchase']]
    print("OOOOOOOOKKKKKKK")
    print(liked_books)
    # Get the categories of the books they interacted with
    categories = BooksModel.objects.filter(_id__in=liked_books).values_list('category', flat=True).distinct()
    print("KOKOKOKOK")
    print(categories)
    # Find books in the same categories, excluding already interacted books
    recommended_books = BooksModel.objects.filter(category__in=[x for x in categories]).exclude(_id__in=liked_books)
    print("FINSL")
    print(recommended_books)
    # .exclude(_id__in=liked_books)

    return recommended_books

def get_book_recommendations(user, top_n=5):
    """
    Combine both interaction-based and category-based recommendations.
    """
    interaction_based_books = recommend_books_based_on_user(user, top_n)
    category_based_books = recommend_books_by_category(user, top_n)

    # Combine the two sets of books and remove duplicates
    recommended_books = interaction_based_books | category_based_books

    # Limit to top N recommendations
    return recommended_books[:top_n]
