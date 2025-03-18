# Django Blog Authentication System

## Features
- User Registration
- Login and Logout
- Profile Management

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Eve-code93/Alx_DjangoLearnLab.git

## Comment System
### Features:
- Users can add comments to blog posts.
- Only authenticated users can comment.
- Authors can edit or delete their own comments.
- Comments are displayed under each post.
## Comment System
### Features:
- Users can add comments to blog posts.
- Only authenticated users can comment.
- Authors can edit or delete their own comments.
- Comments are displayed under each post.

### URLs:
| URL Pattern | View | Description |
|-------------|------|-------------|
| `/post/<int:pk>/comment/new/` | `CommentCreateView` | Add a new comment |
| `/comment/<int:pk>/edit/` | `CommentUpdateView` | Edit a comment |
| `/comment/<int:pk>/delete/` | `CommentDeleteView` | Delete a comment |

