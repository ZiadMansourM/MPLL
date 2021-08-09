from django.shortcuts import render


# {{ post.date_posted|date:"F d, Y - P" }}
posts = [
    {
        "img": "path",
        "title": "Thanawya AMMA",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque
        pariatur praesentium temporibus dolorum cum corporis?Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque
        pariatur praesentium temporibus dolorum cum corporis? Optio, dignissimos error. 
        Sit ex magni eaque nesciunt exercitationem aliquid minus amet explicabo rerum. At?Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque
        pariatur praesentium temporibus dolorum cum corporis? Optio, dignissimos error. 
        Sit ex magni eaque nesciunt exercitationem aliquid minus amet explicabo rerum. At?Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque
        pariatur praesentium temporibus dolorum cum corporis? Optio, dignissimos error. 
        Sit ex magni eaque nesciunt exercitationem aliquid minus amet explicabo rerum. At? Optio, dignissimos error. 
        Sit ex magni eaque nesciunt exercitationem aliquid minus amet explicabo rerum. At?""",
        "author": "Ziad Mansour Mohamed",
        "date_posted": "August 10, 2021 - 12:30 a.m.",
        "last_modified": "August 11, 2021 - 1:30 p.m.",
    },
    {
        "img": "path",
        "title": "Test Driven Development",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque pariatur praesentium temporibus dolorum cum corporis? Optio, dignissimos error. Sit ex magni eaque nesciunt exercitationem aliquid minus amet explicabo rerum. At?",
        "author": "Mando Wael",
        "date_posted": "August 15, 2021 - 12:30 a.m.",
        "last_modified": "",
    }
]


# Create your views here.
def home(requests):
    context = {
        "posts": posts
    }
    return render(requests, 'blog/home.html', context)