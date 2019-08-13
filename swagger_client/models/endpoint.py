# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: crservice@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.model import Model  # noqa: F401,E501


class Endpoint(object):
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
        'concurrent_recognitions': 'int',
        'id': 'str',
        'endpoint_kind': 'str',
        'endpoint_urls': 'dict(str, str)',
        'created_date_time': 'datetime',
        'last_action_date_time': 'datetime',
        'status': 'str',
        'models': 'list[Model]',
        'content_logging_enabled': 'bool',
        'name': 'str',
        'description': 'str',
        'properties': 'dict(str, str)',
        'locale': 'str'
    }

    attribute_map = {
        'concurrent_recognitions': 'concurrentRecognitions',
        'id': 'id',
        'endpoint_kind': 'endpointKind',
        'endpoint_urls': 'endpointUrls',
        'created_date_time': 'createdDateTime',
        'last_action_date_time': 'lastActionDateTime',
        'status': 'status',
        'models': 'models',
        'content_logging_enabled': 'contentLoggingEnabled',
        'name': 'name',
        'description': 'description',
        'properties': 'properties',
        'locale': 'locale'
    }

    def __init__(self, concurrent_recognitions=None, id=None, endpoint_kind=None, endpoint_urls=None, created_date_time=None, last_action_date_time=None, status=None, models=None, content_logging_enabled=None, name=None, description=None, properties=None, locale=None):  # noqa: E501
        """Endpoint - a model defined in Swagger"""  # noqa: E501

        self._concurrent_recognitions = None
        self._id = None
        self._endpoint_kind = None
        self._endpoint_urls = None
        self._created_date_time = None
        self._last_action_date_time = None
        self._status = None
        self._models = None
        self._content_logging_enabled = None
        self._name = None
        self._description = None
        self._properties = None
        self._locale = None
        self.discriminator = None

        if concurrent_recognitions is not None:
            self.concurrent_recognitions = concurrent_recognitions
        self.id = id
        self.endpoint_kind = endpoint_kind
        self.endpoint_urls = endpoint_urls
        self.created_date_time = created_date_time
        self.last_action_date_time = last_action_date_time
        self.status = status
        self.models = models
        if content_logging_enabled is not None:
            self.content_logging_enabled = content_logging_enabled
        self.name = name
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties
        if locale is not None:
            self.locale = locale

    @property
    def concurrent_recognitions(self):
        """Gets the concurrent_recognitions of this Endpoint.  # noqa: E501

        The number of concurrent recognitions the endpoint supports  # noqa: E501

        :return: The concurrent_recognitions of this Endpoint.  # noqa: E501
        :rtype: int
        """
        return self._concurrent_recognitions

    @concurrent_recognitions.setter
    def concurrent_recognitions(self, concurrent_recognitions):
        """Sets the concurrent_recognitions of this Endpoint.

        The number of concurrent recognitions the endpoint supports  # noqa: E501

        :param concurrent_recognitions: The concurrent_recognitions of this Endpoint.  # noqa: E501
        :type: int
        """

        self._concurrent_recognitions = concurrent_recognitions

    @property
    def id(self):
        """Gets the id of this Endpoint.  # noqa: E501

        The identifier of this entity  # noqa: E501

        :return: The id of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Endpoint.

        The identifier of this entity  # noqa: E501

        :param id: The id of this Endpoint.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def endpoint_kind(self):
        """Gets the endpoint_kind of this Endpoint.  # noqa: E501

        The kind of this endpoint (e.g. custom speech, custom voice ...)  # noqa: E501

        :return: The endpoint_kind of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_kind

    @endpoint_kind.setter
    def endpoint_kind(self, endpoint_kind):
        """Sets the endpoint_kind of this Endpoint.

        The kind of this endpoint (e.g. custom speech, custom voice ...)  # noqa: E501

        :param endpoint_kind: The endpoint_kind of this Endpoint.  # noqa: E501
        :type: str
        """
        if endpoint_kind is None:
            raise ValueError("Invalid value for `endpoint_kind`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "SpeechRecognition", "CustomVoice", "LanguageGeneration", "LanguageIdentification"]  # noqa: E501
        if endpoint_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `endpoint_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(endpoint_kind, allowed_values)
            )

        self._endpoint_kind = endpoint_kind

    @property
    def endpoint_urls(self):
        """Gets the endpoint_urls of this Endpoint.  # noqa: E501

        The list of endpoint urls  # noqa: E501

        :return: The endpoint_urls of this Endpoint.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._endpoint_urls

    @endpoint_urls.setter
    def endpoint_urls(self, endpoint_urls):
        """Sets the endpoint_urls of this Endpoint.

        The list of endpoint urls  # noqa: E501

        :param endpoint_urls: The endpoint_urls of this Endpoint.  # noqa: E501
        :type: dict(str, str)
        """
        if endpoint_urls is None:
            raise ValueError("Invalid value for `endpoint_urls`, must not be `None`")  # noqa: E501

        self._endpoint_urls = endpoint_urls

    @property
    def created_date_time(self):
        """Gets the created_date_time of this Endpoint.  # noqa: E501

        The time-stamp when the object was created  # noqa: E501

        :return: The created_date_time of this Endpoint.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this Endpoint.

        The time-stamp when the object was created  # noqa: E501

        :param created_date_time: The created_date_time of this Endpoint.  # noqa: E501
        :type: datetime
        """
        if created_date_time is None:
            raise ValueError("Invalid value for `created_date_time`, must not be `None`")  # noqa: E501

        self._created_date_time = created_date_time

    @property
    def last_action_date_time(self):
        """Gets the last_action_date_time of this Endpoint.  # noqa: E501

        The time-stamp when the current status was entered  # noqa: E501

        :return: The last_action_date_time of this Endpoint.  # noqa: E501
        :rtype: datetime
        """
        return self._last_action_date_time

    @last_action_date_time.setter
    def last_action_date_time(self, last_action_date_time):
        """Sets the last_action_date_time of this Endpoint.

        The time-stamp when the current status was entered  # noqa: E501

        :param last_action_date_time: The last_action_date_time of this Endpoint.  # noqa: E501
        :type: datetime
        """
        if last_action_date_time is None:
            raise ValueError("Invalid value for `last_action_date_time`, must not be `None`")  # noqa: E501

        self._last_action_date_time = last_action_date_time

    @property
    def status(self):
        """Gets the status of this Endpoint.  # noqa: E501

        The status of the object  # noqa: E501

        :return: The status of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Endpoint.

        The status of the object  # noqa: E501

        :param status: The status of this Endpoint.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Succeeded", "Running", "NotStarted", "Failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def models(self):
        """Gets the models of this Endpoint.  # noqa: E501

        Information about the deployed models  # noqa: E501

        :return: The models of this Endpoint.  # noqa: E501
        :rtype: list[Model]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this Endpoint.

        Information about the deployed models  # noqa: E501

        :param models: The models of this Endpoint.  # noqa: E501
        :type: list[Model]
        """
        if models is None:
            raise ValueError("Invalid value for `models`, must not be `None`")  # noqa: E501

        self._models = models

    @property
    def content_logging_enabled(self):
        """Gets the content_logging_enabled of this Endpoint.  # noqa: E501

        A value indicating whether content logging (audio &amp; transcriptions) is being used for a deployment.  Suppressing content logging will result in a higher cost for the deployment.  Free subscriptions can only deploy true  # noqa: E501

        :return: The content_logging_enabled of this Endpoint.  # noqa: E501
        :rtype: bool
        """
        return self._content_logging_enabled

    @content_logging_enabled.setter
    def content_logging_enabled(self, content_logging_enabled):
        """Sets the content_logging_enabled of this Endpoint.

        A value indicating whether content logging (audio &amp; transcriptions) is being used for a deployment.  Suppressing content logging will result in a higher cost for the deployment.  Free subscriptions can only deploy true  # noqa: E501

        :param content_logging_enabled: The content_logging_enabled of this Endpoint.  # noqa: E501
        :type: bool
        """

        self._content_logging_enabled = content_logging_enabled

    @property
    def name(self):
        """Gets the name of this Endpoint.  # noqa: E501

        The name of the object  # noqa: E501

        :return: The name of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Endpoint.

        The name of the object  # noqa: E501

        :param name: The name of this Endpoint.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Endpoint.  # noqa: E501

        The description of the object  # noqa: E501

        :return: The description of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Endpoint.

        The description of the object  # noqa: E501

        :param description: The description of this Endpoint.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def properties(self):
        """Gets the properties of this Endpoint.  # noqa: E501

        The custom properties of this entity  # noqa: E501

        :return: The properties of this Endpoint.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Endpoint.

        The custom properties of this entity  # noqa: E501

        :param properties: The properties of this Endpoint.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def locale(self):
        """Gets the locale of this Endpoint.  # noqa: E501

        The locale of the contained data  # noqa: E501

        :return: The locale of this Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Endpoint.

        The locale of the contained data  # noqa: E501

        :param locale: The locale of this Endpoint.  # noqa: E501
        :type: str
        """

        self._locale = locale

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
        if issubclass(Endpoint, dict):
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
        if not isinstance(other, Endpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
