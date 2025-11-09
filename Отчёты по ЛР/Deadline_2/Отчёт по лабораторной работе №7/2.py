def build_user_profile(user_id: int, **kwargs):
    profile = {'user_id': user_id}
    profile.update(kwargs)
    return profile
profile = build_user_profile(101, name="Анна", email="anna@example.com", status="online")
print(profile)