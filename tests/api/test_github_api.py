import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0



@pytest.mark.api 
def test_repo_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0



@pytest.mark.api 
def test_does_emoji_exist(github_api):
    r = github_api.get_emojis()
    assert r['cup_with_straw'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f964.png?v8'

    
@pytest.mark.api 
def test_does_another_emoji_exist(github_api):
    r = github_api.get_emojis()
    assert r['octopus'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f419.png?v8'



@pytest.mark.api
def test_what_commits_exist(github_api):
    r = github_api.list_commits('zheniaaaa', 'QaAutoDolgopolova')
    print(r)


@pytest.mark.api
def test_does_last_commit_exist(github_api):
    r = github_api.list_commits('zheniaaaa', 'QaAutoDolgopolova')
    assert r[0]['url'] == 'https://api.github.com/repos/zheniaaaa/QaAutoDolgopolova/commits/9d993aa81294a7426f464de1f23055dc76aedc2f'


@pytest.mark.api 
def test_sha(github_api):
    r = github_api.list_commits('zheniaaaa', 'QaAutoDolgopolova')
    assert r[0]['sha'] == '9d993aa81294a7426f464de1f23055dc76aedc2f'