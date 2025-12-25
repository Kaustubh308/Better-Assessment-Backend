from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.comment import Comment

comments_bp = Blueprint("comments", __name__)

# GET comments for a task
@comments_bp.route("/api/tasks/<int:task_id>/comments", methods=["GET"])
def get_comments(task_id):
    comments = Comment.query.filter_by(task_id=task_id).all()
    return jsonify([
        {
            "id": c.id,
            "content": c.content
        } for c in comments
    ])


# POST a new comment
@comments_bp.route("/api/tasks/<int:task_id>/comments", methods=["POST"])
def add_comment(task_id):
    data = request.get_json()
    comment = Comment(
        task_id=task_id,
        content=data["content"]
    )
    db.session.add(comment)
    db.session.commit()

    return jsonify({
        "id": comment.id,
        "content": comment.content
    }), 201


# DELETE a comment
@comments_bp.route("/api/tasks/<int:task_id>/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(task_id, comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return
