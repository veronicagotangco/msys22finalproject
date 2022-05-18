from pickle import TRUE
from django.db import models
from django.utils import timezone

#Position
class Position(models.Model):
    name = models.CharField(max_length = 200, unique = True, blank = False)
    objects = models.Manager() 

    def getName(self):
        return self.name 

    def __str__(self):
        return str(self.pk) + ' Positon Name: ' + self.name

#Candidate 
class Candidate(models.Model):
    first_name = models.CharField(max_length = 200, blank = False)
    last_name = models.CharField(max_length = 200, blank = False)
    nickname = models.CharField(max_length = 200, blank= False)
    slogan = models.CharField(max_length = 200) 
    position_id = models.ForeignKey(Position, on_delete = models.CASCADE)
    objects = models.Manager() 

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getNickname(self):
        return self.nickname 

    def getSlogan(self):
        return self.slogan

    def __str__(self):
        return str(self.pk) + ': ' + str(self.position_id) + ', ' + self.first_name + ' ' + self.last_name + ', ' + self.nickname + ', ' + self.slogan

#User
class Users(models.Model):
    username = models.CharField(max_length = 200, blank = False, unique = True)
    password = models.CharField(max_length = 200, blank = False)
    first_name = models.CharField(max_length = 200, blank = False)
    last_name = models.CharField(max_length = 200, blank = False)
    birthday = models.DateField(null = True) 
    sex = models.CharField(max_length = 200)
    objects = models.Manager() 

    def getUsername(self):
        return self.username
    
    def getPasswod(self):
        return self.password 

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name
    
    def getBirthday(self):
        return self.birthday

    def getSex(self):
        return self.sex

    def __str__(self):
        return str(self.pk) + ': ' + self.username + ', ' + self.first_name + ' ' + self.last_name + ', ' + str(self.birthday) + ', ' + str(self.sex)

#Vote 
class Vote(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.CASCADE)
    candidate_id = models.OneToOneField(Candidate, on_delete = models.CASCADE,  primary_key = True)
    comment = models.CharField(max_length = 2000) 
    objects = models.Manager()

    def getComment(self):
        return self.comment

    def __str__(self):
        return str(self.pk) + ' Candidate: ' + str(self.candidate_id) + '. ' + self.comment