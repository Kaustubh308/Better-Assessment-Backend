def test_create_comment(client):
    res = client.post(
        "/tasks/1/comments",
        json={"content": "Engineering done right"}
    )
    assert res.status_code == 201
    assert res.json["content"] == "Engineering done right"

def test_comment_validation(client):
    res = client.post("/tasks/1/comments", json={"content": ""})
    assert res.status_code == 400

def test_update_comment(client):
    create = client.post(
        "/tasks/1/comments",
        json={"content": "Old"}
    )
    cid = create.json["id"]

    update = client.put(
        f"/comments/{cid}",
        json={"content": "New"}
    )
    assert update.json["content"] == "New"

def test_delete_comment(client):
    create = client.post(
        "/tasks/1/comments",
        json={"content": "Temp"}
    )
    cid = create.json["id"]

    delete = client.delete(f"/comments/{cid}")
    assert delete.status_code == 200
