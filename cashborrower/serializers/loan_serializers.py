from rest_framework import serializers
from ..models import Lender, Borrower, Loan

class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = ('email',) 
        #fiels = 'email' #to make single element tuple add comma.
        #it needs tuple to be serializable
class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('email',) 
        #field = 'email' #to make single element tuple add comma.
        #it needs tuple to be serializable

class LoanSerializer(serializers.ModelSerializer):
    lender = LenderSerializer(many=False)
    borrower = BorrowerSerializer(many=False)
    class Meta:
        model = Loan
        fields =('lender', 'borrower', 'amount','notes','deadline',
                 'isLoanReturned')
        #fields = '__all__'