from app.extensions import db
from app.models.comment import Comment

def create_comment(task_id, content):
    comment = Comment(task_id=task_id, content=content)
    db.session.add(comment)
    db.session.commit()   # 🔥 THIS LINE WAS MISSING
    return comment

def update_comment(comment: Comment, content: str) -> Comment:
    comment.content = content
    db.session.commit()
    return comment

def delete_comment(comment: Comment) -> None:
    db.session.delete(comment)
    db.session.commit()

def get_comments(task_id):
    return Comment.query.filter_by(task_id=task_id).all()

