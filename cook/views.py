from django.shortcuts import render
from django.http import HttpResponse


def food_upload(request):
    return render(request, 'cook/index.html')

    # def form_valid(self, form):
    #     candidate = form.save(commit=False)
    #     candidate.user = UserProfile.objects.get(user=self.request.user)  # use your own profile here
    #     candidate.save()
    #     return HttpResponseRedirect(self.get_success_url())
