def test_package_can_be_imported() -> None:
    import second_brain

    assert second_brain.__name__ == "second_brain"
