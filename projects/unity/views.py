from django.shortcuts import render, HttpResponse

# Create your views here.

def index(reqeust):
    return HttpResponse('''
    <small>UNITY</small>
    <hr>
    <h1>June 2022</h1>
    <div>
        <div><samll>Email list</small><span>10,000</span></div>
        <div><samll>New this month</small><span>501</span></div>
        <div><samll>Unsubscribed</small><span>30</span></div>
    <div>
    
    <table>
        <tr><th>Email ID</th><th>Timestamp</th><th>Status</th><tr>
        <tr><td>developers@konigle.com</td><td>10 minutes ago</td><td>Subscribed</td><tr>
        <tr><td>info@konigle.com</td><td>1 hour ago</td><td>Subscribed</td><tr>
    </table>
  ''')