class ActionNotSupported(Exception):
    """Raised when an action is not supported."""
    pass


class ActionTimedOutError(Exception):
    pass


class ForwardingRuleNotFound(Exception):
    """Raised if a Forwarding Rule for loadbalancers not found."""
    def __init__(self, forwarding_rule_name):
        self.vm_name = forwarding_rule_name


class ImageNotFoundError(Exception):
    pass


class InvalidValueException(Exception):
    """Raises when invalid value provided. E.g. invalid OpenShift project name"""
    pass


class LabelNotFoundException(Exception):
    """Raised when trying to delete a label which doesn't exist"""
    def __init__(self, label_key):
        self._label_key = label_key

    def __str__(self):
        return 'Could not delete label "{}" (label does not exist).'.format(
            self._label_key)


class MultipleImagesError(Exception):
    pass


class NoMoreFloatingIPs(Exception):
    """Raised when provider runs out of FIPs."""


class MultipleInstancesError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class RestClientException(Exception):
    pass


class RequestFailedException(Exception):
    """Raised if some request returned unexpected status code"""
    pass


class NetworkNameNotFound(Exception):
    pass


class VMInstanceNotCloned(Exception):
    """Raised if a VM or instance is not found."""
    def __init__(self, template):
        self.template = template

    def __str__(self):
        return 'Could not clone %s' % self.template


class VMInstanceNotFound(Exception):
    """Raised if a VM or instance is not found."""
    def __init__(self, vm_name):
        self.vm_name = vm_name

    def __str__(self):
        return 'Could not find a VM/instance named %s.' % self.vm_name


class VMInstanceNotSuspended(Exception):
    """Raised if a VM or instance is not able to be suspended."""
    def __init__(self, vm_name):
        self.vm_name = vm_name

    def __str__(self):
        return 'Could not suspend %s because it\'s not running.' % self.vm_name


class VMNotFoundViaIP(Exception):
    """
    Raised if a specific VM cannot be found.
    """
    pass


class HostNotRemoved(Exception):
    """Raised when :py:mod:`utils.mgmt_system` fails to remove host from cluster"""


class VMError(Exception):
    """Raised when a VM goes to the ERROR state."""


class VMCreationDateError(Exception):
    """Raised when we cannot determine a creation date for a VM"""
    pass
