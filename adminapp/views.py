from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm
from adminapp.forms import ProductEditForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator


class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Users'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'users/create'
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('myadmin:users'))
    else:
        user_form = ShopUserRegisterForm()
    content = {'title': title, 'update_form': user_form}
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'users/edit'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES,
                                          instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('myadmin:user_update',
                                                args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {
        'title': title,
        'update_form': edit_form
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'users/delete'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        # user.is_active = False
        # user.save()
        user.delete()
        return HttpResponseRedirect(reverse('myadmin:users'))
    content = {
        'title': title,
        'user_to_delete': user
    }
    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'My admin/categories'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('myadmin:categories')
    fields = '__all__'


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('myadmin:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category/edit'

        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('myadmin:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category/delete'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # self.object.is_active = False
        # self.object.save()
        self.object.delete()

        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'My admin/product'
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'title': title,
        'category': category,
        'objects': products_list
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'Product/create'
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('myadmin:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})
    content = {
        'title': title,
        'update_form': product_form,
        'category': category
    }
    return render(request, 'adminapp/product_update.html', content)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product/details'

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = 'Product/details'
#     product = get_object_or_404(Product, pk=pk)
#     content = {
#         'title': title,
#         'object': product,
#     }
#     return render(request, 'adminapp/product_read.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'Product/create'
    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES,
                                    instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(
                reverse('myadmin:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)
    content = {
        'title': title,
        'update_form': edit_form,
        'category': edit_product.category
    }
    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'Product/delete'
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # category.is_active = False
        # category.save()
        product.delete()
        return HttpResponseRedirect(reverse('myadmin:products',
                                            args=[product.category.pk]))
    content = {'title': title,
               'product_to_delete': product
               }
    return render(request, 'adminapp/product_delete.html', content)
