import hashlib
from django.core.exceptions import ValidationError


class Hasher(object):
    """ handle all hashing """
    def __init__(self, *args, **kwargs):
        self.length = self._get_hash_length()
        self.iterations = 40
        #super(Hasher, self).__init__(*args, **kwargs)

    def new_hasher(self, value=''):
        return hashlib.sha256(value.decode('ascii', 'ignore'))

    def remove_non_ascii(self, s):
        return "".join(i for i in s if ord(i) < 128)

    def _get_hash_length(self):
        return hashlib.sha256(u'Foo').block_size

    def get_hash(self, value, algorithm, mode, salt):
        """ Returns a salted value as an iterated SHA256 hash """
        if not value:
            retval = None
        else:
            if not isinstance(salt, str):
                raise ValidationError('The Encryption keys are not available '
                                      'to this system. Unable to save '
                                      'sensitive data.')
            try:
                digest = self.new_hasher('{0}{1}'.format(salt, value)).digest()
            except:
                value = self.remove_non_ascii(value)
                digest = self.new_hasher('{0}{1}'.format(salt, value)).digest()
            # iterate
            for x in range(0, self.iterations - 1):
                digest = self.new_hasher(digest).digest()
            hash_value = digest.encode("hex")
            retval = hash_value
        return retval
