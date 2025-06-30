from lib.post import Post

def test_instance_created():
    post = Post(1, 'chris post', 'I am the best', 1, 2)
    assert post.id == 1
    assert post.title == 'chris post'
    assert post.content == 'I am the best'
    assert post.views == 1
    assert post.user_id == 2

def test_if_returned_is_what_was_expected():
    post = Post(1, 'chris post', 'I am the best', 1, 2)
    post2 = Post(1, 'chris post', 'I am the best', 1, 2)
    assert post == post2

def test_if_return_value_is_formatted_correctly():
    post = Post(1, 'chris post', 'I am the best', 1, 2)
    assert str(post) == 'Post(1, chris post, I am the best, 1, 2)'

