#!/usr/bin/env python3

# Main file for basic_authentication

# """ Main 1
# """
# from api.v1.auth.auth import Auth

# a = Auth()
# # print(a.require_auth("/api/v1/status/", ["/api/v1/stats/", "/api/v1/status/", "/api/v1/users/"]))
# # print(a.require_auth("/api/v1/status", ["/api/v1/stats/", "/api/v1/status/", "/api/v1/users/"]))
# print(a.require_auth(None, None))
# print(a.require_auth(None, []))
# print(a.require_auth("/api/v1/status/", []))
# print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
# print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
# print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
# print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))

# print(a.require_auth("/api/v1/users", ["/api/v1/stat*"]))
# print(a.require_auth("/api/v1/status", ["/api/v1/stat*"]))
# print(a.require_auth("/api/v1/stats", ["/api/v1/stat*"]))


# Main file for session_authentication task 2

#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

print("{}: {}".format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))

user_id = None
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = 89
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "fghij"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))

user_id = "abcde"
session = sa.create_session(user_id)
print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))