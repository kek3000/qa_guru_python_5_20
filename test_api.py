from pprint import pprint
import requests
from jsonschema import validate

from helper import load_json_schema, reqres_session


def test_get_list_user():
    response = reqres_session.get('/api/users?page=1')

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['total'] == 12


def test_get_list_user_validate_schema():
    response = reqres_session.get('/api/users?page=1')
    schema = load_json_schema('get_list_user.json')

    pprint(response.text)
    validate(instance=response.json(), schema=schema)


def test_get_single_user():
    response = reqres_session.get('/api/users/7')

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['data']['id'] == 7
    assert response.json()['data']['email'] == 'michael.lawson@reqres.in'


def test_get_single_user_validate_schema():
    response = reqres_session.get('/api/users/7')
    schema = load_json_schema('get_single_user.json')

    pprint(response.text)
    validate(instance=response.json(), schema=schema)


def test_get_single_user_not_found():
    response = reqres_session.get('/api/users/771231317')

    pprint(response.text)
    assert response.status_code == 404


def test_get_single_user_not_found_validate_schema():
    response = reqres_session.get('/api/users/771231317')
    schema = load_json_schema('get_single_user_not_found.json')

    pprint(response.text)
    validate(instance=response.json(), schema=schema)


def test_post_create_user():
    response = reqres_session.post(
        url='/api/users/',
        json={
            "name": "Nikita",
            "job": "AQA"}
    )

    pprint(response.text)
    assert response.status_code == 201
    assert response.json()['name'] == 'Nikita'
    assert response.json()['job'] == 'AQA'


def test_post_create_user_validate_schema():
    response = reqres_session.post(
        url='/api/users/',
        json={
            "name": "Nikita",
            "job": "AQA"}
    )
    schema = load_json_schema('post_create_user.json')

    pprint(response.text)
    validate(instance=response.json(), schema=schema)


def test_put_update_user():
    response = reqres_session.put(
        url='/api/users/123',
        json={
            "name": "Nikita",
            "job": "Team Lead QA"}
    )

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['name'] == 'Nikita'
    assert response.json()['job'] == 'Team Lead QA'


def test_put_update_user_validate_schema():
    response = reqres_session.put(
        url='/api/users/123',
        json={
            "name": "Nikita",
            "job": "Team Lead QA"}
    )
    schema = load_json_schema('put_update_user.json')

    pprint(response.text)
    validate(instance=response.json(), schema=schema)


def test_patch_update_user():
    response = reqres_session.patch(
        url='/api/users/123',
        json={
            "name": "Nikita", "job": "Team Lead QA"}
    )

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['name'] == 'Nikita'
    assert response.json()['job'] == 'Team Lead QA'


def test_patch_update_user_validate_schema():
    response = reqres_session.patch(
        url='/api/users/123',
        json={
            "name": "Nikita", "job": "Team Lead QA"}
    )
    schema = load_json_schema('patch_update_user.json')

    pprint(response.text)
    validate(instance=response.json(), schema=schema)


def test_delete_update_user():
    response = reqres_session.delete('/api/users/123131231')

    pprint(response.text)
    assert response.status_code == 204


def test_post_register_user_successfull():
    response = reqres_session.post(
        url='/api/register/',
        json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"}
    )

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['id'] != ''
    assert response.json()['token'] != ''


def test_post_register_user_successfull_validate_schema():
    response = reqres_session.post(
        url='/api/register/',
        json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"}
    )
    schema = load_json_schema('post_register_user_successfull.json')

    pprint(response.text)
    validate(instance=response.json(), schema=schema)


def test_post_register_user_unsuccessfull():
    response = reqres_session.post(
        url='/api/register/',
        json={
            "email": "n.alekseev@comagic.dev"}
    )

    pprint(response.text)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_post_register_user_unsuccessfull_validate_schema():
    response = reqres_session.post(
        url='/api/register/',
        json={
            "email": "n.alekseev@comagic.dev"}
    )
    schema = load_json_schema('post_register_user_unsuccessfull.json')

    pprint(response.text)
    validate(instance=response.json(), schema=schema)


def test_post_login_user_successfull():
    response = reqres_session.post(
        url='/api/login/',
        json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['token'] != ''


def test_post_login_user_successfull_validate_schema():
    response = reqres_session.post(
        url='/api/login/',
        json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )
    schema = load_json_schema('post_login_user_successfull.json')

    pprint(response.text)
    validate(instance=response.json(), schema=schema)


def test_post_login_user_unsuccessfull():
    response = reqres_session.post(
        url='/api/login/',
        json={
            "email": "n.alekseev@comagic.dev"}
    )

    pprint(response.text)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_post_login_user_unsuccessfull_validate_schema():
    response = reqres_session.post(
        url='/api/login/',
        json={
            "email": "n.alekseev@comagic.dev"}
    )
    schema = load_json_schema('post_login_user_unsuccessfull.json')

    pprint(response.text)
    validate(instance=response.json(), schema=schema)
