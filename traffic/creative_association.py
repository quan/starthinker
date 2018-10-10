###########################################################################
#
#  Copyright 2017 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################
"""Handles creation and updates of creative asset association.

"""

import json

from traffic.dao import BaseDAO
from traffic.feed import FieldMap
from traffic.campaign import CampaignDAO
from traffic.creative import CreativeDAO


class CreativeAssociationDAO(BaseDAO):
  """Creative Association data access object.

  Inherits from BaseDAO and implements creative association specific logic for
  creating and
  updating creative association.
  """

  def __init__(self, auth, profile_id):
    """Initializes CreativeAssociationDAO with profile id and authentication scheme."""
    super(CreativeAssociationDAO, self).__init__(auth, profile_id)

    self._service = self.service.campaignCreativeAssociations()
    self._id_field = FieldMap.CAMPAIGN_CREATIVE_ASSOCIATION_ID

    self.campaign_dao = CampaignDAO(auth, profile_id)
    self.creative_dao = CreativeDAO(auth, profile_id)

  def get(self, feed_item):
    """It is not possible to retrieve creative associations from DCM,

    and they are read-only, so the get method just returns None,
    it does this to avoid errors when this is invoked polimorfically.

    For more information on the get method, refer to BaseDAO.

    Args:
      feed_item: Feed item representing the creative association from the
        Bulkdozer feed.

    Returns:
      None.
    """
    return None

  def process(self, feed_item):
    """Processes a feed item by creating the creative association in DCM.

    Args:
      feed_item: Feed item representing the creative association from the
        Bulkdozer feed.

    Returns:
      The newly created object from DCM.
    """

    if feed_item.get(FieldMap.CREATIVE_ID, None) and feed_item.get(
        FieldMap.CAMPAIGN_ID, None) and not feed_item.get(
            FieldMap.CAMPAIGN_CREATIVE_ASSOCIATION_ID, None):
      campaign = self.campaign_dao.get(feed_item)
      creative = self.creative_dao.get(feed_item)

      association = {'creativeId': creative['id']}

      result = self._retry(
          self._service.insert(
              profileId=self.profile_id,
              campaignId=campaign['id'],
              body=association))

      feed_item[FieldMap.CAMPAIGN_CREATIVE_ASSOCIATION_ID] = '%s|%s' % (
          campaign['id'], creative['id'])

      return result
