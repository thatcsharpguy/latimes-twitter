import pytest
from freezegun import freeze_time

from twitter.reply_builder import parse_tweet


@freeze_time("2021-02-22")
@pytest.mark.parametrize(["input_tweet", "expected_output"],[
    ("mx jueves 10 pm", '22:00 🇲🇽🇨🇷🇸🇻, 23:00 🇨🇴🇪🇨🇵🇪🇵🇦, 01:00+1 🇨🇱🇦🇷🇵🇾🇺🇾, 00:00+1 🇻🇪, 05:00+1 🇬🇶'),
    ("domingo 10 pm", '22:00 🇲🇽🇨🇷🇸🇻, 23:00 🇨🇴🇪🇨🇵🇪🇵🇦, 01:00+1 🇨🇱🇦🇷🇵🇾🇺🇾, 00:00+1 🇻🇪, 05:00+1 🇬🇶'),
    ("mx Sábado 10:30 pm", '22:30 🇲🇽🇨🇷🇸🇻, 23:30 🇨🇴🇪🇨🇵🇪🇵🇦, 01:30+1 🇨🇱🇦🇷🇵🇾🇺🇾, 00:30+1 🇻🇪, 05:30+1 🇬🇶'),
    ("cr jueves 10 pm", '22:00 🇲🇽🇨🇷🇸🇻, 23:00 🇨🇴🇪🇨🇵🇪🇵🇦, 01:00+1 🇨🇱🇦🇷🇵🇾🇺🇾, 00:00+1 🇻🇪, 05:00+1 🇬🇶'),
    ("ar jueves 10 pm", '19:00 🇲🇽🇨🇷🇸🇻, 20:00 🇨🇴🇪🇨🇵🇪🇵🇦, 22:00 🇨🇱🇦🇷🇵🇾🇺🇾, 21:00 🇻🇪, 02:00+1 🇬🇶'),
    ("gq  jueves   10   am", '03:00 🇲🇽🇨🇷🇸🇻, 04:00 🇨🇴🇪🇨🇵🇪🇵🇦, 06:00 🇨🇱🇦🇷🇵🇾🇺🇾, 05:00 🇻🇪, 10:00 🇬🇶'),
])
def test_parse_tweet(input_tweet, expected_output):
    reply = parse_tweet("@tzconvert " + input_tweet)

    assert reply == expected_output
