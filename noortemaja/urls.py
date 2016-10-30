"""noortemaja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from eventmanager import views
from django.conf.urls import include, url
from eventmanager.views import(
   LoanDeleteAPIView,
   LoanDetailAPIView,
   LoanListView,
   LoanUpdateAPIView,
   LenderLoanDeleteAPIView,
   LenderLoanDetailAPIView,
   GivenLoanListView,
   TakenLoanListView,
   LenderLoanUpdateAPIView,
   LenderLogDeleteAPIView,
   LenderLogDetailAPIView,
   LenderLogListView,
   LenderLogUpdateAPIView
)


admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^loans/', views.LoanListView.as_view()),
    url(r'^loan/(?P<id>[\w\-]+)', views.LoanDetailAPIView.as_view()),
    url(r'^loan/update/(?P<id>[\w\-]+)', views.LoanUpdateAPIView.as_view()),
    url(r'^loan/delete/(?P<id>[\w\-]+)', views.LoanDeleteAPIView.as_view()),

    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/givenloans/', views.GivenLoanListView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/givenloans/', views.TakenLoanListView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loan/(?P<id>[0-9]+)', views.LenderLoanDetailAPIView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loan/update/(?P<id>[0-9]+)', views.LenderLoanUpdateAPIView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loan/delete/(?P<id>[0-9]+)', views.LenderLoanDeleteAPIView.as_view()),

    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/logs/', views.LenderLogListView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/log/(?P<id>[0-9]+)', views.LenderLogDetailAPIView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/log/update/(?P<id>[0-9]+)', views.LenderLogUpdateAPIView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/log/delete/(?P<id>[0-9]+)', views.LenderLogDeleteAPIView.as_view()),

    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancredits/loan/(?P<loan_fk>[0-9]+)', views.LoanCreditListView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loandiscredits/loan/(?P<loan_fk>[0-9]+)', views.LoanDiscreditListView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancredits/loan/(?P<loan_fk>[0-9]+)/credit/(?P<id>[0-9]+)', views.LoanCreditDetailAPIView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancredits/update/loan/(?P<loan_fk>[0-9]+)/credit/(?P<id>[0-9]+)', views.LoanCreditUpdateAPIView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancredits/delete/loan/(?P<loan_fk>[0-9]+)/credit/(?P<id>[0-9]+)', views.LoanCreditDeleteAPIView.as_view()),

    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomments/loan/(?P<loan_fk>[0-9]+)', views.CommentListView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDetailAPIView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/update/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentUpdateAPIView.as_view()),
    url(r'^lender/(?P<lender>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/loancomment/delete/loan/(?P<loan_fk>[0-9]+)/comment/(?P<id>[0-9]+)', views.CommentDeleteAPIView.as_view()),
]
