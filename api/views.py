from rest_framework.response import Response
from rest_framework.decorators import api_view
from books.models import Book
from .serializers import BookSerializer

# SO FAR ONLY NEW FILE IN API FOLDER

#DECORATOR @
@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    # Create instance of ItemSerializer class
    # many = True means serialize multiple items as opposed to one 
    serializer = BookSerializer(books, many=True)
    # want to return data
    return Response(serializer.data)

    # queryset = Book.objects.all().order_by('ratings_total')

@api_view(['POST'])
def addBook(request):
    # pass in data to this class and create item
    # data send from front end = data
    serializer = BookSerializer(data=request.data)
    # check if valid
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# SEND DATA AS FOLLOWING, must be double qoutes
# {"name":"Crunch"}
