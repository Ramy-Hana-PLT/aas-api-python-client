# coding: utf-8

"""
    DotAAS Part 2 | HTTP/REST | Entire API Collection

    All APIs of the Specification of the [Specification of the Asset Administration Shell: Part 2](http://industrialdigitaltwin.org/en/content-hub) in one collection. Please not that this API is not intended to generate productive code but only for overview purposes.   Publisher: Industrial Digital Twin Association (IDTA) 2023\"  # noqa: E501

    OpenAPI spec version: V3.0.1
    Contact: info@idtwin.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Resource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'path': 'AllOfResourcePath',
        'content_type': 'AllOfResourceContentType'
    }

    attribute_map = {
        'path': 'path',
        'content_type': 'contentType'
    }

    def __init__(self, path=None, content_type=None):  # noqa: E501
        """Resource - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._content_type = None
        self.discriminator = None
        self.path = path
        if content_type is not None:
            self.content_type = content_type

    @property
    def path(self):
        """Gets the path of this Resource.  # noqa: E501


        :return: The path of this Resource.  # noqa: E501
        :rtype: AllOfResourcePath
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Resource.


        :param path: The path of this Resource.  # noqa: E501
        :type: AllOfResourcePath
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def content_type(self):
        """Gets the content_type of this Resource.  # noqa: E501


        :return: The content_type of this Resource.  # noqa: E501
        :rtype: AllOfResourceContentType
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Resource.


        :param content_type: The content_type of this Resource.  # noqa: E501
        :type: AllOfResourceContentType
        """

        self._content_type = content_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Resource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other