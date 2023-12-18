from app_constants import TEST_URL


def test_ui_register(app):
    'Проверяю позитивный сценарий регистрации пользователя через UI.'

    app.open_home_page()
    app.check_register_page()
    app.fill_register_form()
    app.submit()
    assert app.check_current_url() == TEST_URL + ':8080/#/profile'
