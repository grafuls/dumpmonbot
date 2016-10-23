import config

def test_config():
    assert config.EMAILER_SUFFIX
    assert config.EMAILER_SERVER
    assert config.EMAILER_PORT

    assert config.C_KEY
    assert config.C_SECRET
    assert config.A_TOKEN
    assert config.A_SECRET
    assert config.T_USER
    assert config.QUERY
