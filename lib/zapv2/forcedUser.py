# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2015 the ZAP development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This file was automatically generated.
"""

class forcedUser(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def is_forced_user_mode_enabled(self):
        return next(self.zap._request(self.zap.base + 'forcedUser/view/isForcedUserModeEnabled/').itervalues())

    def get_forced_user(self, contextid):
        return next(self.zap._request(self.zap.base + 'forcedUser/view/getForcedUser/', {'contextId' : contextid}).itervalues())

    def set_forced_user(self, contextid, userid, apikey=''):
        return next(self.zap._request(self.zap.base + 'forcedUser/action/setForcedUser/', {'contextId' : contextid, 'userId' : userid, 'apikey' : apikey}).itervalues())

    def set_forced_user_mode_enabled(self, boolean, apikey=''):
        return next(self.zap._request(self.zap.base + 'forcedUser/action/setForcedUserModeEnabled/', {'boolean' : boolean, 'apikey' : apikey}).itervalues())


