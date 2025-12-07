from django.shortcuts import render,redirect
from voter.models import VoterModel
from voter.forms import VoterForm

# Create your views here.
def post_voter(request):
    if request.method=='POST':
        form=VoterForm(request.POST,request.FILES)
        if form.is_valid():
            voter=form.save()
            return redirect('get_voter',id=voter.id)
        else:
            print(form.errors)
    else:
        form=VoterForm()
    return render(request,'form.html',{'form':form})

def get_voter(request,id):
    data=VoterModel.objects.get(id=id)
    return render(request,'votercard.html',{'data':data})
