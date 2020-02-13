import unittest

from matscholar_web.tests.util import MatScholarWebBaseTest
from matscholar_web.search.subviews.tests.util import common_arg_combos
import matscholar_web.search.subviews.abstracts as msweb_ssa
from matscholar_web.constants import api_key, endpoint

"""
Tests for the abstracts subview of search.
"""


class TestSearchAbstractsSubview(MatScholarWebBaseTest):
    @unittest.skipIf(not api_key and not endpoint, "API access and endpoint not set.")
    def test_abstracts_results_html(self):
        """
        This generally tests everything in the subview since all functions are
        dependent on the single results html.

        Hence we don't need run_test_for_all_functions_in_submodule.
        """
        f = msweb_ssa.abstracts_results_html
        self.run_test_for_individual_arg_combos(f, common_arg_combos)


