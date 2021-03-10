import flag
from latimes.config import (
    DEFAULT_VALUES,
    LatimesConfiguration,
    LatimesOutputFormatting,
)
from latimes.latimes import convert_times

DEFAULT_TIMEZONE = "America/Mexico_City"
TIMEZONE_ABBREVIATIONS = {
    "mx": "America/Mexico_City",
    "co": "America/Bogota",
    "cl": "America/Santiago",
    "ec": "America/Guayaquil",
    "pe": "America/Lima",
    "ar": "America/Argentina/Buenos_Aires",
    "cr": "America/Costa_Rica",
    "ve": "America/Caracas",
    "gq": "Africa/Malabo",
    "sv": "America/El_Salvador",
    "py": "America/Asuncion",
    "uy": "America/Montevideo",
    "pa": "America/Panama",
}
CONVERT_TO = [
    f"{flag.flag(':'+key+':')}:{tz}" for key, tz in TIMEZONE_ABBREVIATIONS.items()
]
OUTPUT_FORMATTING = LatimesOutputFormatting(
    time_format_string="%H:%M",
    different_time_joiner=", ",
    aggregate=True,
    aggregate_joiner="",
)


def parse_tweet(tweet_text: str) -> str:
    text = tweet_text[len("@tzconvert") :].strip().lower()

    # Find specific country abbreviation
    abbr = text[:3].strip()
    if abbr in TIMEZONE_ABBREVIATIONS:
        starting_timezone = TIMEZONE_ABBREVIATIONS[abbr]
        text = text[3:]
    else:
        starting_timezone = DEFAULT_TIMEZONE

    text = " ".join(part for part in text.split(" ") if part)

    configuration = LatimesConfiguration(
        starting_timezone=starting_timezone,
        convert_to=CONVERT_TO,
        output_formatting=OUTPUT_FORMATTING,
    )
    return convert_times(text, configuration)
