__BASE_URLS: dict = {
    'qa': 'https://qa.letsdochinese.com'
}

def get_base_url(env: str):
    env = env.lower().strip()
    url = __BASE_URLS.get(env)
    if url is None:
        raise Exception(f"No base url configured for {env} environment.")
    return url