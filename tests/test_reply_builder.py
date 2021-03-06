import pytest
from freezegun import freeze_time

from twitter.reply_builder import parse_tweet


@freeze_time("2021-02-22")
@pytest.mark.parametrize(["input_tweet", "expected_output"],[
    ("mx jueves 10 pm", '22:00 π²π½π¨π·πΈπ», 23:00 π¨π΄πͺπ¨π΅πͺπ΅π¦, 01:00+1 π¨π±π¦π·π΅πΎπΊπΎ, 00:00+1 π»πͺ, 05:00+1 π¬πΆ'),
    ("domingo 10 pm", '22:00 π²π½π¨π·πΈπ», 23:00 π¨π΄πͺπ¨π΅πͺπ΅π¦, 01:00+1 π¨π±π¦π·π΅πΎπΊπΎ, 00:00+1 π»πͺ, 05:00+1 π¬πΆ'),
    ("mx SΓ‘bado 10:30 pm", '22:30 π²π½π¨π·πΈπ», 23:30 π¨π΄πͺπ¨π΅πͺπ΅π¦, 01:30+1 π¨π±π¦π·π΅πΎπΊπΎ, 00:30+1 π»πͺ, 05:30+1 π¬πΆ'),
    ("cr jueves 10 pm", '22:00 π²π½π¨π·πΈπ», 23:00 π¨π΄πͺπ¨π΅πͺπ΅π¦, 01:00+1 π¨π±π¦π·π΅πΎπΊπΎ, 00:00+1 π»πͺ, 05:00+1 π¬πΆ'),
    ("ar jueves 10 pm", '19:00 π²π½π¨π·πΈπ», 20:00 π¨π΄πͺπ¨π΅πͺπ΅π¦, 22:00 π¨π±π¦π·π΅πΎπΊπΎ, 21:00 π»πͺ, 02:00+1 π¬πΆ'),
    ("gq  jueves   10   am", '03:00 π²π½π¨π·πΈπ», 04:00 π¨π΄πͺπ¨π΅πͺπ΅π¦, 06:00 π¨π±π¦π·π΅πΎπΊπΎ, 05:00 π»πͺ, 10:00 π¬πΆ'),
])
def test_parse_tweet(input_tweet, expected_output):
    reply = parse_tweet("@tzconvert " + input_tweet)

    assert reply == expected_output
