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
# LibraryProject/README.md

## Security Measures Implemented

### Secure Settings
- `DEBUG` set to `False` in production.
- `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF` configured for additional protections.
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` set to `True` to enforce HTTPS.

### CSRF Protection
- All forms include CSRF tokens to protect against CSRF attacks.

### Secure Data Access
- Views updated to use Django’s ORM and ensure safe handling of user input.

### Content Security Policy (CSP)
- `django-csp` middleware added and configured to reduce the risk of XSS attacks.
