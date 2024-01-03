from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
import logging

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo
from petstagram.accounts.forms import PetstagramUserCreateForm, LoginForm, PetstagramUserEditForm

User = get_user_model()

logger = logging.getLogger(__name__)


class UserRegisterView(views.CreateView):
    model = User
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login-user')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('homepage')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login-user')


class UserEditView(views.UpdateView):
    model = User
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class UserProfileView(LoginRequiredMixin, views.DetailView):
    model = User
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'profile'

    profile_image = static('images/person.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_likes_count = sum(p.like_set.count() for p in self.object.photo_set.all())

        context['profile_image'] = self.get_profile_image()
        context['pets'] = Pet.objects.filter(user=self.object).all()
        context['total_likes_count'] = total_likes_count
        logger.debug(f"Before processing: Current User: {self.request.user}")
        # TODO: This here is the issue, figure out on you own on how to retrieve the page's owner and be logged in as
        #  the current user.
        #  Check your logic when checking who the user is => self.request.user = self.object turns the user into the
        #  object aka. the owner. This is what has been breaking the code. Now with that knAwledge, go and fix the issue Day 4
        context['profile_owner'] = self.object
        print(f'Logged in User: {self.request.user}')
        print(f'Page owner: {self.object}')
        print(f"Session User: {self.request.session.get('_auth_user_id')}")

        logger.debug(f"After processing: Current User: {self.request.user}")
        logger.debug(f"Profile User: {self.object}")
        if self.request.user.first_name and self.request.user.last_name:
            context['both_names'] = self.request.user.first_name + ' ' + self.request.user.last_name
        context['photos'] = Photo.objects.filter(user=self.object).all().order_by('-date_of_publication')

        return context


# def register(request):
#     return render(request, 'accounts/register-page.html')


# def login(request):
#     return render(request, 'accounts/login-page.html')

#
# def profile_details(request):
#     return render(request, 'accounts/profile-details-page.html')


#
# def profile_edit(request):
#     return render(request, 'accounts/profile-edit-page.html')


def profile_delete(request):
    return render(request, 'accounts/profile-delete-page.html')
