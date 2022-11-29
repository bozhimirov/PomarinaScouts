from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as views

from Scouts.core.utils import get_photo_url
from Scouts.items.models import Item, UsedItem

# from Scouts.web.forms import SearchPhotosForm, PhotoCommentForm

UserModel = get_user_model()


class IndexView(views.TemplateView):
    model = UserModel
    template_name = 'index.html'


class SuccessView(views.TemplateView):
    model = UserModel
    template_name = 'core/success.html'


class ContactsView(views.TemplateView):
    model = UserModel
    template_name = 'core/contacts.html'


class ForParentsView(views.TemplateView):
    model = UserModel
    template_name = 'info_for_parents.html'


#
# def index(request):
#     search_form = SearchPhotosForm(request.GET)
#     search_pattern = None
#     if search_form.is_valid():
#         search_pattern = search_form.cleaned_data['pet_name']
#
#     photos = Item.objects.all()
#
#     if search_pattern:
#         photos = photos.filter(tagged_pets__name__icontains=search_pattern)
#
#     # photos = [apply_likes_count(photo) for photo in photos]
#     # photos = [apply_user_liked_photo(photo) for photo in photos]
#     # print(photos)
#     context = {
#         'photos': photos,
#         'comment_form': PhotoCommentForm(),
#         'search_form': search_form,
#     }
#
#     return render(
#         request,
#         'common/home-page.html',
#         context,
#     )

#
# def like_photo(request, photo_id):
#     user_liked_photos = get_user_liked_photos(photo_id)
#     if user_liked_photos:
#         user_liked_photos.delete()
#     else:
#         # Variant 2
#         PhotoLike.objects.create(
#             photo_id=photo_id,
#         )
#
#     return redirect(get_photo_url(request, photo_id))
#
#     # # Variant 1
#     # photo_like = PhotoLike(
#     #     photo_id=photo_id,
#     # )
#     # photo_like.save()
#
#     # # Variant 3 (wrong - additional call to db)
#     # # Correct, only if validation is needed
#     # photo = Photo.objects.get(pk=photo_id)
#     # PhotoLike.objects.create(
#     #     photo=photo,
#     # )


# def share_photo(request, photo_id):
#     photo_details_url = reverse('details photo', kwargs={
#         'pk': photo_id
#     })
#     pyperclip.copy(photo_details_url)
#     return redirect(get_photo_url(request, photo_id))
#


@login_required
def comment_photo(request, item_id):
    if request.method == 'POST':
        item = Item.objects.filter(pk=item_id).get()
        form = PhotoCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)  # Does not persist to DB
            comment.to_photo = item
            comment.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{item_id}')


def scout_store(request):
    all_items = Item.objects.all()
    all_used_items = UsedItem.objects.all()
    count_of_items = all_items.count()
    count_of_used_items = all_used_items.count()

    context = {
        'all_items': all_items,
        'all_used_items': all_used_items,
        'count_of_items': count_of_items,
        'count_of_used_items': count_of_used_items,
    }

    return render(request, template_name='core/marketplace.html', context=context)


def scout_store_new(request):
    all_items = Item.objects.all()

    context = {
        'all_items': all_items
    }

    return render(request, template_name='core/marketplace-new.html', context=context)


@login_required()
def scout_store_used(request):
    all_used_items = UsedItem.objects.all()

    context = {
        'all_used_items': all_used_items
    }

    return render(request, template_name='core/marketplace-used.html', context=context)
