#!/usr/bin/env python3
import requests


def register_user(email: str, password: str) -> None:
    form_data = {"email": email, "password": password}
    resp = requests.post('http://0.0.0.0:5000/users', data=form_data)
    assert resp.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    form_data = {"email": email, "password": password}
    resp = requests.post('http://0.0.0.0:5000/sessions', data=form_data)
    assert resp.status_code == 401


def log_in(email: str, password: str) -> str:
    form_data = {"email": email, "password": password}
    resp = requests.post('http://0.0.0.0:5000/sessions', data=form_data)
    status_code = resp.status_code
    assert status_code == 200
    session_id = resp.cookies.get('session_id')
    return session_id


def profile_unlogged() -> None:
    resp = requests.get('http://0.0.0.0:5000/profile')
    assert resp.status_code == 403


def profile_logged(session_id: str) -> None:
    cookies = {'session_id': session_id}
    resp = requests.get('http://0.0.0.0:5000/profile', cookies=cookies)
    assert resp.status_code == 200


def log_out(session_id: str) -> None:
    cookies = {'session_id': session_id}
    resp = requests.delete('http://0.0.0.0:5000/sessions', cookies=cookies)
    assert resp.status_code == 200


def reset_password_token(email: str) -> str:
    form_data = {'email': email}
    resp = requests.post('http://0.0.0.0:5000/reset_password', data=form_data)
    assert resp.status_code == 200
    return resp.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    form_data = {'email': email, 'reset_token': reset_token,
                 'new_password': new_password}
    resp = requests.put('http://0.0.0.0:5000/reset_password', data=form_data)
    assert resp.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    # log_in(EMAIL, NEW_PASSWD)
