from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Interaction, Note
from .forms import CustomerForm, InteractionForm, NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class LoginView(auth_views.LoginView):
    template_name="login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('customer_list')

@login_required
def customer_list(request):
    """
    Displays a list of all customers.
    """
    customers = Customer.objects.all()
    return render(request, 'crm/customer_list.html', {'customers': customers})

@login_required
def customer_detail(request, pk):
    """
    Displays details of a specific customer, including interactions and notes.
    """
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'crm/customer_detail.html', {'customer': customer})

@login_required
def add_customer(request):
    """
    Handles the creation of a new customer.
    """
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'crm/add_customer.html', {'form': form})

@login_required
def add_interaction(request, customer_id):
    """
    Handles the creation of a new interaction for a customer.
    """
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.customer = customer
            interaction.save()
            return redirect('customer_detail', pk=customer_id)
    else:
        form = InteractionForm()
    return render(request, 'crm/add_interaction.html', {'form': form, 'customer': customer})

@login_required
def add_note(request, customer_id):
    """
    Handles the creation of a new note for a customer.
    """
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.customer = customer
            note.save()
            return redirect('customer_detail', pk=customer_id)
    else:
        form = NoteForm()
    return render(request, 'crm/add_note.html', {'form': form, 'customer': customer})


@login_required
def delete(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method=="POST":
        customer.delete()
        return redirect('customer_list')

    return redirect('customer_list')
