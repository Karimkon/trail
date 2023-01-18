from django.forms import ModelForm, DateInput

from blog.models import Gamepark, Visitor, Payment, Warden, Wildlife_animal

class GameparkForm(ModelForm):
    class Meta:
        model = Gamepark
        fields = '__all__'

class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ("payment_date","visitor_id","amount_paid","recieved_by")

        widgets = {
            "payment_date":DateInput(attrs={"type":"date"})
        }



class WardenForm(ModelForm):
    class Meta:
        model = Warden
        fields = '__all__'

class Wildlife_animalForm(ModelForm):
    class Meta:
        model = Wildlife_animal
        fields = '__all__'