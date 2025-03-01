# advanced_features_and_security/README.md

## Permissions and Groups Setup
This section describes the setup and usage of permissions and groups in the application.

### Custom Permissions
Custom permissions are defined in the `CustomUser` model to control actions such as viewing, creating, editing, and deleting items.

### Groups
The following groups are set up in the Django admin interface:
- **Editors:** Can view, create, and edit items.
- **Viewers:** Can view items.
- **Admins:** Can view, create, edit, and delete items.

### Enforcing Permissions
Permissions are enforced in views using the `permission_required` decorator.
Example:
```python
@permission_required('app.can_edit', raise_exception=True)
def edit_view(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    return render(request, 'edit.html', {'user': user})
