import pytest
from utilities import OpenTheBrowser
from scroll import ScrollTo
from perform import GetTheValueFrom, InsertValueInto, EraseTheValueFrom, ClickOn


@pytest.fixture(scope='function')
def pre_condition():
    OpenTheBrowser().go_to_site()


@pytest.fixture(scope='function')
def post_work():
    yield
    OpenTheBrowser().close_browser()


def test_if_sell_field_becomes_empty_after_filling_buy_field(pre_condition):
    ScrollTo().currency_conversion_calculator()
    InsertValueInto().buy_field()
    assert GetTheValueFrom().sell_field() == ''


def test_if_buy_field_becomes_empty_after_filling_sell_field(pre_condition):
    ScrollTo().currency_conversion_calculator()
    EraseTheValueFrom().sell_field()
    InsertValueInto().buy_field()
    InsertValueInto().sell_field()
    assert GetTheValueFrom().buy_field() == ''


def test_if_currency_changes_according_to_country(pre_condition):
    ScrollTo().bottom()
    ClickOn().localization_btn()
    ClickOn().countries_dropdown_btn()
    ClickOn().United_kingdom_btn()
    ScrollTo().currency_conversion_calculator()
    assert GetTheValueFrom().sell_selected_currency() == 'GBP'


def test_if_sell_price_lower_than_paysera_price_and_text_box_appears(pre_condition):
    ScrollTo().currency_conversion_calculator()
    EraseTheValueFrom().sell_field()
    InsertValueInto().sell_field('200')
    ClickOn().buy_currency_selection()
    ClickOn().usd_from_buy_selection_list()
    ClickOn().filter_btn()
    assert GetTheValueFrom().bank_provider_rate_difference_with_paysera() < 0


def test_if_clear_filter_reset_the_calculator(pre_condition):
    ScrollTo().currency_conversion_calculator()
    EraseTheValueFrom().sell_field()
    InsertValueInto().sell_field('356')
    ClickOn().sell_currency_selection()
    ClickOn().cad_from_sell_selection_list()
    ClickOn().clear_filter_btn()
    assert GetTheValueFrom().sell_field() == '100'


def test_if_alphanumeric_value_is_accpeted_in_sell_field(pre_condition):
    ScrollTo().currency_conversion_calculator()
    EraseTheValueFrom().sell_field()
    InsertValueInto().sell_field('12cat')
    ClickOn().filter_btn()
    assert GetTheValueFrom().warning() == 'Invalid parameters'


def test_if_alphanumeric_value_is_accpeted_in_buy_field(pre_condition):
    ScrollTo().currency_conversion_calculator()
    EraseTheValueFrom().sell_field()
    InsertValueInto().buy_field('ca12t')
    ClickOn().filter_btn()
    assert GetTheValueFrom().warning() == 'Invalid parameters'


def test_if_all_selected_in_buy_than_sell_goes_to_according_to_selected_country(pre_condition):
    ScrollTo().currency_conversion_calculator()
    ClickOn().buy_currency_selection()
    ClickOn().all_from_buy_selection_list()
    ClickOn().sell_currency_selection()
    ClickOn().all_from_sell_selection_list()
    assert GetTheValueFrom().buy_selected_currency() == 'EUR'


def test_if_sell_and_buy_both_selected_as_same_nothing_will_appear(pre_condition):
    ScrollTo().currency_conversion_calculator()
    ClickOn().buy_currency_selection()
    ClickOn().eur_from_buy_selection_list()
    ClickOn().filter_btn()
    assert GetTheValueFrom().currency_table() == '-'


def test_if_buy_n_sell_both_kept_empty_and_filter_clicked(pre_condition, post_work):
    ScrollTo().currency_conversion_calculator()
    EraseTheValueFrom().sell_field()
    ClickOn().filter_btn()
    assert GetTheValueFrom().sell_field() == '100'