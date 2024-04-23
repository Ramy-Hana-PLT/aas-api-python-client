# coding: utf-8

"""
    DotAAS Part 2 | HTTP/REST | Entire API Collection

    All APIs of the Specification of the [Specification of the Asset Administration Shell: Part 2](http://industrialdigitaltwin.org/en/content-hub) in one collection. Please not that this API is not intended to generate productive code but only for overview purposes.   Publisher: Industrial Digital Twin Association (IDTA) 2023\"  # noqa: E501

    OpenAPI spec version: V3.0.1
    Contact: info@idtwin.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import aas_api_python_client
from aas_api_python_client.api.concept_description_repository_api_api import ConceptDescriptionRepositoryAPIApi  # noqa: E501
from aas_api_python_client.rest import ApiException


class TestConceptDescriptionRepositoryAPIApi(unittest.TestCase):
    """ConceptDescriptionRepositoryAPIApi unit test stubs"""

    def setUp(self):
        self.api = ConceptDescriptionRepositoryAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_concept_description_by_id(self):
        """Test case for delete_concept_description_by_id

        Deletes a Concept Description  # noqa: E501
        """
        pass

    def test_get_all_concept_descriptions(self):
        """Test case for get_all_concept_descriptions

        Returns all Concept Descriptions  # noqa: E501
        """
        pass

    def test_get_concept_description_by_id(self):
        """Test case for get_concept_description_by_id

        Returns a specific Concept Description  # noqa: E501
        """
        pass

    def test_post_concept_description(self):
        """Test case for post_concept_description

        Creates a new Concept Description  # noqa: E501
        """
        pass

    def test_put_concept_description_by_id(self):
        """Test case for put_concept_description_by_id

        Updates an existing Concept Description  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
