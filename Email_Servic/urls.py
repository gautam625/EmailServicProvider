from django.urls import path

from App1.views import loginForm, userLogin, emailInbox, sendEmailForm, sendEmail, signUpForm, deleteEmail,createAccount, displayEmail, searchEmail

urlpatterns = [
    path('', loginForm, name='home'),
    path('log/', userLogin, name='log'),
    path('emailInbox/', emailInbox, name='emailInbox'),
    path('sendForm/', sendEmailForm),
    path('send/', sendEmail),
    path('userForm/', signUpForm),
    path('userSave/', createAccount),
    path('delete/', deleteEmail),
    path('display/', displayEmail),
    path('search/', searchEmail),
]
