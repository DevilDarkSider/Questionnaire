from django.db import models

class Student(models.Model):
    m_sEmail = models.OneToOneField('auth.User', unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    m_sPassword = models.CharField(max_length=20)
    m_sFullName = models.CharField(max_length=50)
    m_sGroup = models.CharField(max_length=30)

    def __str__(self):
        return self.m_sFullName
    
class Teacher(models.Model):
    m_sEmail = models.OneToOneField('auth.User', unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    m_sPassword = models.CharField(max_length=20)
    m_sFullName = models.CharField(max_length=50)
    m_sFaculty = models.CharField(max_length=30)
    m_sDiscipline = models.ForeignKey('Discipline', on_delete=models.CASCADE)
    m_nRating = models.IntegerField(default=0)

    def __str__(self):
        return self.m_sFullName

class Discipline(models.Model):
    m_sDiscipline = models.CharField(max_length=30, primary_key=True)
    m_bGroup_F_11 = models.BooleanField(default=False)
    m_bGroup_M_12 = models.BooleanField(default=False)
    m_bGroup_I_13 = models.BooleanField(default=False)


    def __str__(self):
        return self.m_sDiscipline

class Answer(models.Model):
    m_sStEmail = models.CharField(max_length=50)
    m_sTeachEmail = models.CharField(max_length=50)
    m_nScores1 = models.IntegerField(default=0)
    m_nScores2 = models.IntegerField(default=0)
    m_nScores3 = models.IntegerField(default=0)
    m_nScores4 = models.IntegerField(default=0)
    m_nScores5 = models.IntegerField(default=0)
    
    