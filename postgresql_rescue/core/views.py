from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def home(request):
    """
    Home page for PostgreSQL Rescue Records.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse("<h1>PostgreSQL Rescue Records</h1>"
                        f"<p>Welcome current time is {now}.</p>")

def about(request):
    """
    About the company / course.
    """
    html = """
    <h1>About PostgreSQL Rescue Records</h1>
    <p>This is a fictional music label used for our 10-day Django training.</p>
    <p>We will build multiple apps: music library, cafe orders, shop, clinic, and real estate marketplace.</p>
    """
    return HttpResponse(html)

def album_detail(request):
    """
    Simple info page for 'The PostgreSQL Rescue' album.
    """
    html = """
    <h1>The PostgreSQL Rescue – Album</h1>
    <p>Debut concept album used as the central theme for this course.</p>
    <ul>
        <li>Artist: PostgreSQL Rescue All-Stars</li>
        <li>Genre: Tech Rock</li>
        <li>Release: 2026 (training edition)</li>
    </ul>
    <p>Later in the week, this album will appear in the music library and shop. </p>
    """
    return HttpResponse(html)


def contact(request):
    return HttpResponse("<h1>Contact</h1><p>Email: training@example.com</p>")


def roadmap(request):
    return HttpResponse(
        "<h1>Platform Roadmap</h1>"
        "<p>Coming soon: music library, cafe orders, shop, clinic, realestate.</p>"
    )
def greet(request, name):
    return HttpResponse(f"<h1>Hello, {name}!</h1><p>Welcome to PostgreSQL Rescue Records.</p>")