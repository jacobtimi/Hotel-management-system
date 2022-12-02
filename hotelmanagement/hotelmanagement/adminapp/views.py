from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from .forms import SignUpform, staff_form, User_form, Room_form
from django.views import generic
from.models import Profile, Room_table
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
# Create your views here.


class SignUpView(generic.CreateView):
    form_class = SignUpform
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def index_page(request):
    return render(request, 'index.html')


def manage_staff(request):
    staff_details = Profile.objects.all().filter(staff=True)
    return render(request, 'adminapp/manage_staff.html',{'staff':staff_details, 'status':'staff'})     

def manage_customer(request):
    customer_details = Profile.objects.all().filter(staff=False)
    return render(request, 'adminapp/manage_staff.html',{'staff':customer_details, 'status':'customer'})     


def staff_profile(request, user_id):
    staff_details= Profile.objects.all().filter(user_id = user_id)
    return render(request, 'adminapp/staff_profile.html',{'staff':staff_details})


def staff_deactivate(request, user_id):
    staff = User.objects.get(id=user_id)
    if staff.is_activate:
        staff.is_active = False
    else:
        staff.is_active = True
    staff.save()
    return staff_profile(request, user_id)

@transaction.atomic
def edit_profile(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(request.POST, instance=user)
        profile_form= staff_form(request.POST or None, request. FILES or None, instance= user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if profile_form.cleaned_data['staff']:
                user.is_staff = True
                user.save()
            else:
                user.is_staff =False
                user.save()
            messages.success(request, ('Your profile was successfully updated!'))
            staff_profile(request, user_id)
            return HttpResponsePermanentRedirect(reverse('edit_profile', args={user_id}))
        else:
            messages.error(request, ('please correct the error below!'))
            return HttpResponsePermanentRedirect(reverse('edit_profile', args={user_id}))
    else:
        user = get_object_or_404(User, id = user_id)
        user_form = User_form(instance=user)
        profile_form= staff_form(instance= user.profile)
        return render(request, 'adminapp/staff_update_form.html', {'user_form': user_form, 'profile_form': profile_form})


def upload_room(request):
    if request.method == 'POST':
        form = Room_form(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.date_upload = timezone.now()
            post.status="unbooked"
            post.save()
            return HttpResponsePermanentRedirect(reverse('upload_room'))
    else:
        form = Room_form()
        return render(request=request, template_name= 'adminapp/room_upload_form.html', context={'form':form})

def manage_room(request):
    room_details = Room_table.objects.all()
    return render(request, 'adminapp/manage_room.html', {'room':room_details })  

def edit_room(request, room_id):
    edit = get_object_or_404(Room_table, room_id)
    form = Room_form (request.POST or None, request.FILES or None)
    return 0

def delete_room(request, room_id):
    pass

def approve_Room(request, room_id):
    Room= Room_table.objects.get(room_id =  room_id)
    if Room.status == "unbooked":
        Room.status = "booked"
    else:
        Room.status = "unbooked"
    Room.save()
    return manage_room(request)