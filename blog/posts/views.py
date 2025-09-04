from django.shortcuts import render
from django.http import HttpResponse

# Create your posts here
posts = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is my very first blog post in Django!"
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "Learning Django step by step is fun."
    },
    {
        "id": 3,
        "title": "Third Post",
        "content": "Django makes it easy to build web applications quickly."
    },
    {
        "id": 4,
        "title": "Fourth Post",
        "content": "Understanding views and URLs is the core of Django."
    },
    {
        "id": 5,
        "title": "Fifth Post",
        "content": "Templates help separate design from logic in Django apps."
    },
    {
        "id": 6,
        "title": "Sixth Post",
        "content": "The Django admin is powerful for managing your data."
    },
]

def home(request):
    html = ""
    for post in posts:
        html += f"""
        <div>
            <a href="/post/{post['id']}/'>
            <h1>{post['id']} - {post['title']}</h1>
            <p>{post['content']}</p>
        </div>
        <hr>
        """
    return HttpResponse(html)

def post(request, id):
    for post in posts:
        if post['id'] == id:
            post_dict = post
            break

    html = '''
        <h1>{post_dict['title']}</h1>
        <p>{post_dict['content']}</p>
    
    '''
    return HttpResponse(html)
