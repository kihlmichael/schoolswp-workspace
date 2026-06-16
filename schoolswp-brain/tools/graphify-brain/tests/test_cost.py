import cost


def test_estimate_counts_chars_tokens_and_usd(tmp_path):
    a = tmp_path / "a.md"
    a.write_text("x" * 4000, encoding="utf-8")  # ~1000 tokens
    b = tmp_path / "b.md"
    b.write_text("y" * 4000, encoding="utf-8")
    est = cost.estimate([a, b], model="gemini-2.5-flash")
    assert est.files == 2
    assert est.total_chars == 8000
    assert est.est_tokens == 2000  # chars // 4
    assert est.est_usd > 0


def test_estimate_empty_is_zero():
    est = cost.estimate([], model="gemini-2.5-flash")
    assert est.files == 0 and est.est_tokens == 0 and est.est_usd == 0.0
