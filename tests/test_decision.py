from app.core.decision import decide


def test_weather_intent():
    d = decide("what's the weather and what to pack for Tokyo?")
    assert d.intent in {"weather", "packing"}
    assert d.use_weather