#!/usr/bin/env python3

from database.get_trials import all_trials
from database.get_trials import all_runs
from database.get_trials import percent_of_win
from database.get_trials import percent_of_2nd
from database.get_trials import percent_of_3rd
from database.random import all_days_db

class Statistics():
    """Different statistics from database."""
    def __init__(self, app_path):
        self.app_path = app_path

    def all_tt_races(self) -> int:
        """Return the total count of every TT race from database."""
        all = all_trials(self.app_path)
        return all

    def all_single_runs(self) -> int:
        """Return the total count of every single Uma's run from database."""
        runs = all_runs(self.app_path)
        return runs

    def all_race_days(self) -> int:
        """Return the total count of unique days with TT races registered in the database."""
        days = all_days_db(self.app_path)
        return int(days)

    def win_percent(self) -> float:
        """
        Return the win percentage of all individual races in the database.
        Return a placeholder string if no races are found.
        """
        percent = percent_of_win(self.app_path)
        if percent:
            return percent
        else:
            return "--"

    def second_percent(self) -> float:
        """
        Return the percentage of second-place finishes for all individual races in the database.
        Return a placeholder string if no races are found.
        """
        percent = percent_of_2nd(self.app_path)
        if percent:
            return percent
        else:
            return "--"

    def third_percent(self) -> float:
        """
        Return the percentage of third-place finishes for all individual races in the database.
        Return a placeholder string if no races are found.
        """
        percent = percent_of_3rd(self.app_path)
        if percent:
            return percent
        else:
            return "--"