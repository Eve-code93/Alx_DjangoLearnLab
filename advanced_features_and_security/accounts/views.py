from django.shortcuts import render

# C# advanced_features_and_security/app/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import CustomUser

@permission_required('app.can_edit', raise_exception=True)
def edit_view(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    # Your view logic here
    return render(request, 'edit.html', {'user': user})

