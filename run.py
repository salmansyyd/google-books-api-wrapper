from google_books_api_wrapper.api import GoogleBooksAPI

client = GoogleBooksAPI()
response = client.search_book("atomic habits")

print(response.data)
