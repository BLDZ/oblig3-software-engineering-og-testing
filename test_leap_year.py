from leap_year import LeapYear


class TestLeapYear:
    def test_result_is_boolean(self):
        leapYear = LeapYear()
        result = leapYear.isLeapYear(1000)

        assert (result == True) or (result == False)

    def test_is_year_dividable_with_4_and_not_100(self):
        leap_year = LeapYear()
        result = leap_year.isLeapYear(4)
        assert result == True

    def test_is_year_dividable_with_400(self):
        leap_year = LeapYear()
        result = leap_year.isLeapYear(400)
        assert result == True

    def test_is_year_not_dividable_with_4(self):
        leap_year = LeapYear()
        result = leap_year.isLeapYear(409)
        assert result == False

    def test_is_year_dividable_with_100_and_not_400(self):
        leap_year = LeapYear()
        result = leap_year.isLeapYear(300)
        assert result == False

    def test_2000_is_leap_year(self):
        leap_year = LeapYear()
        result = leap_year.isLeapYear(2000)
        assert result == True

    def test_1700_is_leap_year(self):
        leap_year = LeapYear()
        result = leap_year.isLeapYear(1700)
        assert result == False
