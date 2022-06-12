from logging import exception
from turtle import title
from django.shortcuts import render
from home.models import *
from django import forms


# Create your views here.

CHOICES = [('M', 'Male'), ('F', 'Female')]


def index(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        gender = request.POST.get("dropdown")

        schools = request.POST.get("school")
        books = request.POST.get("books")
        student = Student(firstname=firstname, lastname=lastname,
                          email=email, gender=gender, schools=schools, books=books)
        student.save()
    return render(request, "index.html")


def search(request):
    return render(request, "search.html")


def searchByName(name):
    query = name

    sinfo = Student.objects.filter(firstname__icontains=query)
    temp = ""
    for p in sinfo:
        temp = p.schools
        temp1 = p.books

    schoolinfo = School.objects.filter(school__icontains = temp)
    bookInfo = Book.objects.filter(title__icontains = temp1)
    params = {"sinfo": sinfo, "schoolinfo" : schoolinfo, "query": query, "bookInfo": bookInfo}       
    return params
            

def searchByID(id):
    query = id
    sinfo = Student.objects.filter(id__icontains=query)
    temp = ""
    for p in sinfo:
        temp = p.schools
        temp1 = p.books
    

    schoolinfo = School.objects.filter(school__icontains = temp)
    bookInfo = Book.objects.filter(title__icontains = temp1)

    params = {"sinfo": sinfo, "schoolinfo" : schoolinfo, "query": query, "bookInfo": bookInfo} 
    return params 

def searchResults(request):
    if request.GET['ID'] == "":
        return render(request, "searchResults.html", searchByName(request.GET['Name']))
    else:           
        return render(request, "searchResults.html", searchByID(request.GET['ID']))


    
def searchUrlByName(request, query):
    query = str(query)
    if query.isdigit():
        return render(request, "searchResults.html", searchByID(query))
    else:
        return render(request, "searchResults.html", searchByName(query))
         
    

#Not used in the UI
def uploadcsv(request):
    if "GET" == request.method:
        return render(request, "savecsv.html")
    try:
        csv_file = request.FILES["csv_file"]
        try:
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            flag = 0
            for line in lines:
                fields = line.split(",")
                if flag==1:
                    try:
                        firstname = fields[1]
                        lastname = fields[2]
                        email = fields[3]                    
                        gender = fields[4]
                        schools = fields[5]
                        books = fields[6]
                        
                        # title = fields[0]
                        # author_name= fields[1]
                        # date_of_Publication = fields[2]
                        # number_of_Pages = fields[3]
                        
                        # school = fields[0]
                        # email = fields[1]
                        # principal = fields[2]
                        # phone = fields[3]
                        # address2 = fields[4]
                        
                        # print(title,author_name,date_of_Publication,number_of_Pages)
                        
                        student = Student(firstname=firstname, lastname=lastname,
                                        email=email, gender=gender, schools=schools, books=books)
                        # book = Book(title = title, author_name = author_name, date_of_Publication=date_of_Publication,
                        #              number_of_Pages = number_of_Pages)
                        # sname = School(school = school, email = email, principal = principal, phone =phone, address2 =address2)
                        student.save()
                    except exception as e:
                        pass
                else:
                    flag=1

        except Exception as e:
            pass
        
        return render(request, "savecsv.html")

    
    except Exception as e:
        pass
       

      
    
